#!/usr/bin/env python3
"""Symulator robota: sprawdza, czy rozwiązania z plików tresc/*.md dochodzą do skarbów.
Obsługuje poziomy 1-4: polecenia, POWTÓRZ, JEŚLI, STOP, META oraz PRZEPIS X / ZRÓB X (META w przepisie = powrót z przepisu).
Gra online ma też klucze (@), drzwi (D, wejście zabiera jeden klucz) i monety z liczbami 1-6 (suma w info["suma"]).
Litery (małe a-z bez v) robot zbiera po kolei: z ustawieniem slowo każda litera musi być następną literą słowa (info["litery"]).
Użycie: python3 narzedzia/sprawdz.py tresc/plansze-*.md   (albo: make sprawdz)
Pomija gry bez rozwiązania w bloku rozwiazanie i plansze z polami "?" - te sprawdź ręcznie."""
import re, sys

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
ORDER = "^>v<"
COND = {"LAWA?": "L", "KAŁUŻA?": "K", "SKARB?": "*", "ŚCIANA?": "WALL"}

class Fail(Exception): pass
class Stop(Exception): pass
class Meta(Exception): pass

def parse_program(lines):
    """Zwraca listę węzłów: ("cmd", nazwa, n) | ("loop", n, body) | ("if", warunek, tak, nie) | ("def", nazwa, body)."""
    rows = [((len(l) - len(l.lstrip(" "))) // 2, l.strip()) for l in lines if l.strip()]
    pos = 0
    def block(ind):
        nonlocal pos
        out = []
        while pos < len(rows):
            i, t = rows[pos]
            if i < ind or (t == "KONIEC" and i == ind - 1):
                break
            pos += 1
            if t.startswith("POWTÓRZ"):
                n = t.split("×")[1].strip() if "×" in t else "1"
                body = block(i + 1)
                if pos < len(rows) and rows[pos][1] == "KONIEC": pos += 1
                out.append(("loop", None if n == "∞" else int(n), body))
            elif t.startswith("PRZEPIS "):
                body = block(i + 1)
                if pos < len(rows) and rows[pos][1] == "KONIEC": pos += 1
                out.append(("def", t[8:].strip(), body))
            elif t.startswith("JEŚLI "):
                cond, tak, nie = t[6:].strip(), [], []
                while pos < len(rows) and rows[pos][0] > i:
                    branch = rows[pos][1]; pos += 1
                    target = tak if branch.startswith("TAK:") else nie
                    target += cmds(branch[4:])
                if pos < len(rows) and rows[pos][1] == "KONIEC": pos += 1
                out.append(("if", cond, tak, nie))
            elif t == "KONIEC":
                continue
            else:
                out += cmds(t)
        return out
    return block(0)

def cmds(text):
    out = []
    for part in [p.strip() for p in text.split(",") if p.strip()]:
        m = re.match(r"^(.*?)\s*×\s*(\d+)$", part)
        out.append(("cmd", m.group(1), int(m.group(2))) if m else ("cmd", part, 1))
    return out

def run(board, prog, skarby=True, info=None, slowo=None):
    g = [r.split() for r in board]
    keys, suma, litery = 0, 0, ""
    h, w = len(g), len(g[0])
    (r, c), d = next(((y, x), g[y][x]) for y in range(h) for x in range(w) if g[y][x] in DIRS)
    stars = {(y, x) for y in range(h) for x in range(w) if g[y][x] == "*"}
    got = set()
    def cell(y, x):
        return "WALL" if not (0 <= y < h and 0 <= x < w) else g[y][x]
    def step(k):
        nonlocal r, c, keys, suma, litery
        dy, dx = DIRS[d]
        if k == 2:
            mid = cell(r + dy, c + dx)
            if mid != "K": raise Fail(f"skok bez kałuży (nad {'.' if mid in '^>v<*' else mid}) z {(r+1, c+1)}")
        y, x = r + k * dy, c + k * dx
        t = cell(y, x)
        if t in ("L", "K", "#", "WALL"): raise Fail(f"wejście na {t} w {(y+1, x+1)}")
        if t == "D":
            if not keys: raise Fail(f"drzwi bez klucza w {(y+1, x+1)}")
            keys -= 1; g[y][x] = "."
        elif t == "@":
            keys += 1; g[y][x] = "."
        elif len(t) == 1 and t in "123456789":
            suma += int(t); g[y][x] = "."
        elif slowo is not None and len(t) == 1 and "a" <= t <= "z":
            if len(litery) >= len(slowo): raise Fail(f"litera {t.upper()} w {(y+1, x+1)}, a słowo {slowo} jest już gotowe")
            if t.upper() != slowo[len(litery)]: raise Fail(f"litera {t.upper()} w {(y+1, x+1)}, a trzeba {slowo[len(litery)]}")
            litery += t.upper(); g[y][x] = "."
        r, c = y, x
        if (r, c) in stars: got.add((r, c))
    defs = {nd[1]: nd[2] for nd in prog if nd[0] == "def"}
    depth = [0]
    def exe(nodes):
        nonlocal d
        for nd in nodes:
            if nd[0] == "def":
                continue
            if nd[0] == "cmd" and nd[1].startswith("ZRÓB "):
                name = nd[1][5:].strip()
                if name not in defs: raise Fail(f"brak przepisu {name}")
                for _ in range(nd[2]):
                    depth[0] += 1
                    if depth[0] > 20: raise Fail("przepis wywołuje sam siebie bez końca")
                    try:
                        exe(defs[name])
                    except Meta:
                        pass  # META w przepisie = wróć z przepisu (return)
                    depth[0] -= 1
                continue
            if nd[0] == "cmd":
                name, n = nd[1], nd[2]
                for _ in range(n):
                    if name == "IDŹ": step(1)
                    elif name == "SKOCZ": step(2)
                    elif name == "SKRĘĆ W PRAWO": d = ORDER[(ORDER.index(d) + 1) % 4]
                    elif name == "SKRĘĆ W LEWO": d = ORDER[(ORDER.index(d) - 1) % 4]
                    elif name == "OBRÓĆ SIĘ": d = ORDER[(ORDER.index(d) + 2) % 4]
                    elif name == "STOP": raise Stop
                    elif name == "META": raise Meta
                    else: raise Fail(f"nieznane polecenie {name!r}")
            elif nd[0] == "loop":
                i = 0
                try:
                    while nd[1] is None or i < nd[1]:
                        exe(nd[2]); i += 1
                        if i > 200: raise Fail("pętla bez końca")
                except Stop:
                    pass
            else:
                dy, dx = DIRS[d]
                ahead = cell(r + dy, c + dx)
                exe(nd[2] if ahead == COND[nd[1]] else nd[3])
    try:
        exe(prog)
    except Meta:
        pass
    if info is not None:
        info.update(suma=suma, klucze=keys, litery=litery)
    if slowo is not None and litery != slowo:
        raise Fail(f"zebrane litery {litery!r}, a słowo to {slowo}; koniec w {(r+1, c+1)}")
    if skarby and stars - got:
        raise Fail(f"nie zebrano skarbów {sorted((y+1, x+1) for y, x in stars - got)}; koniec w {(r+1, c+1)}")
    return (r + 1, c + 1), d

def games(path):
    text = open(path, encoding="utf-8").read()
    for sec in re.split(r"^### ", text, flags=re.M)[1:]:
        title = sec.splitlines()[0]
        board = re.search(r"```plansza\n(.*?)```", sec, re.S)
        sol = re.search(r"```rozwiazanie[^\n]*\n(.*?)```", sec, re.S)
        yield title, board and board.group(1).splitlines(), sol and sol.group(1).splitlines(), ustawienia(sec)

def ustawienia(sec):
    """Blok ```ustawienia (slowo: KOT, suma: 7) -> słownik."""
    u = re.search(r"```ustawienia\n(.*?)```", sec, re.S)
    if not u:
        return {}
    return {a.strip(): b.strip() for a, b in (l.split(":", 1) for l in u.group(1).splitlines() if ":" in l)}

if __name__ == "__main__":
    bad = 0
    for path in sys.argv[1:]:
        if "starsi" in path:
            print(f"  pomijam   {path}: sprawdza make online (narzedzia/symulator.py)"); continue
        for title, board, sol, ust in games(path):
            if not board or not sol or any("?" in l for l in board):
                print(f"  pomijam   {path}: {title}"); continue
            try:
                info = {}
                end = run([l for l in board if l.strip()], parse_program(sol), info=info, slowo=ust.get("slowo"))
                if "suma" in ust and info["suma"] != int(ust["suma"]):
                    raise Fail(f"suma {info['suma']}, a ma być {ust['suma']}")
                print(f"  OK        {path}: {title} -> koniec {end}")
            except Fail as e:
                bad += 1; print(f"  BŁĄD      {path}: {title}: {e}")
    sys.exit(1 if bad else 0)
