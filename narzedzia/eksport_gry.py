#!/usr/bin/env python3
"""Eksportuje gry do gra/gry.js (dla wersji online, index.html).

Użycie: python3 narzedzia/eksport_gry.py   (albo: make online)

Poziom 1: gry z tresc/plansze-poziom-1-*.md, które da się zagrać na ekranie: z robotem, skarbem
i rozwiązaniem w bloku rozwiazanie, bez pól "?" i bez programu podanego z góry.
Poziom 2: gry z gra/poziom-2.md (POWTÓRZ, klucze i drzwi, monety i limit kart, JEŚLI z polem ?,
przepis A). Każde rozwiązanie jest sprawdzane symulatorem, a przy polach "?" na każdym wariancie.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "narzedzia"))
import sprawdz  # noqa: E402
import symulator  # noqa: E402

PODSTAWOWE = ["IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ"]
PYTANIA = ["LAWA?", "KAŁUŻA?", "SKARB?", "ŚCIANA?"]


def tokeny(nodes):
    """Drzewo z sprawdz.parse_program -> płaska lista kart, tak jak leżą na stole."""
    out = []
    for nd in nodes:
        if nd[0] == "cmd":
            out.append([nd[1], nd[2]])
        elif nd[0] == "loop":
            out += [["POWTÓRZ", nd[1]]] + tokeny(nd[2]) + [["KONIEC", 1]]
        elif nd[0] == "if":
            out += [["JEŚLI", nd[1]]] + tokeny(nd[2]) + [["NIE", 1]] + tokeny(nd[3]) + [["KONIEC", 1]]
        elif nd[0] == "def":
            pass
        else:
            sys.exit(f"nieobsługiwany węzeł {nd!r}")
    return out


class Blad(Exception):
    pass


BLEDY = []


def sprawdz_gre(where, plansza, prog, warianty, suma, powrot):
    """Uruchamia rozwiązanie na każdym wariancie planszy. Kończy skrypt przy błędzie."""
    pyt = [(y, x) for y, r in enumerate(plansza) for x, t in enumerate(r.split()) if t == "?"]
    if pyt and not warianty:
        raise Blad(f"{where}: pola ? bez wariantów")
    for w in (warianty or [""]):
        if len(w) != len(pyt):
            raise Blad(f"{where}: wariant {w!r} ma inną liczbę pól niż plansza ({len(pyt)})")
        rows = [r.split() for r in plansza]
        for (y, x), t in zip(pyt, w):
            rows[y][x] = t
        board = [" ".join(r) for r in rows]
        info = {}
        try:
            end, _ = sprawdz.run(board, prog, info=info)
        except sprawdz.Fail as e:
            raise Blad(f"{where}: wariant {w!r}: {e}")
        if suma is not None and info["suma"] != suma:
            raise Blad(f"{where}: wariant {w!r}: suma {info['suma']}, a ma być {suma}")
        start = next((y + 1, x + 1) for y, r in enumerate(rows) for x, t in enumerate(r) if t in "^>v<")
        if powrot and end != start:
            raise Blad(f"{where}: rozwiązanie nie wraca na START")


def poziom1():
    games, skipped = [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, "tresc", "plansze-poziom-1-*.md"))):
        m = re.search(r"plansze-poziom-1-(\d)x\d(?:-([a-z]))?\.md$", path)
        size, zestaw = int(m.group(1)), (m.group(2) or "").upper()
        text = open(path, encoding="utf-8").read()
        for sec in re.split(r"^### ", text, flags=re.M)[1:]:
            head = sec.splitlines()[0].strip()
            num, title = re.match(r"^(\d+)\.\s*(.*)$", head).groups()
            board = re.search(r"```plansza\n(.*?)```", sec, re.S)
            sol = re.search(r"```rozwiazanie\n(.*?)```", sec, re.S)
            if not board or not sol or "```program" in sec:
                skipped += 1; continue
            rows = [l.split() for l in board.group(1).splitlines() if l.strip()]
            flat = [t for r in rows for t in r]
            if "?" in flat or "*" not in flat or not any(t in "^>v<" for t in flat):
                skipped += 1; continue
            desc = " ".join(l.strip() for l in sec.split("```plansza")[0].splitlines()[1:] if l.strip())
            back = "wróć na start" in desc.lower()
            prog = sprawdz.parse_program([l for l in sol.group(1).splitlines() if l.strip()])
            if any(n[0] != "cmd" for n in prog):
                skipped += 1; continue
            plansza = [" ".join(r) for r in rows]
            try:
                sprawdz_gre(f"{path}: {head}", plansza, prog, None, None, back)
            except Blad as e:
                BLEDY.append(str(e))
            games.append({
                "id": f"{size}-{int(num)}", "poziom": 1, "size": size, "zestaw": zestaw, "nr": int(num),
                "tytul": title, "opis": desc, "plansza": plansza, "powrot": back,
                "karty": PODSTAWOWE,
                "rozwiazanie": {"program": tokeny(prog)},
            })
    return games, skipped


def poziom2():
    path = os.path.join(ROOT, "gra", "poziom-2.md")
    text = open(path, encoding="utf-8").read()
    games = []
    size = zestaw = nazwa = None
    karty_zestawu = []
    for blok in re.split(r"^(?=#{2,4} )", text, flags=re.M):
        head = blok.splitlines()[0] if blok.strip() else ""
        if head.startswith("## "):
            size = int(re.search(r"(\d)", head).group(1))
        elif head.startswith("### "):
            m = re.match(r"### Zestaw ([A-Z]): (.*)$", head)
            zestaw, nazwa = m.group(1), m.group(2).strip()
            k = re.search(r"^karty: (.*)$", blok, re.M)
            karty_zestawu = [x.strip() for x in k.group(1).split(",")] if k else []
        elif head.startswith("#### "):
            num, title = re.match(r"^#### (\d+)\.\s*(.*)$", head).groups()
            where = f"{path}: {size}x{size} {head[5:]}"
            board = re.search(r"```plansza\n(.*?)```", blok, re.S)
            sol = re.search(r"```rozwiazanie\n(.*?)```", blok, re.S)
            if not board or not sol:
                sys.exit(f"{where}: brak planszy albo rozwiązania")
            rows = [l.split() for l in board.group(1).splitlines() if l.strip()]
            if len(rows) != size or any(len(r) != size for r in rows):
                sys.exit(f"{where}: plansza nie ma rozmiaru {size} × {size}")
            plansza = [" ".join(r) for r in rows]
            ust = {}
            u = re.search(r"```ustawienia\n(.*?)```", blok, re.S)
            if u:
                for l in u.group(1).splitlines():
                    if ":" in l:
                        a, b = l.split(":", 1); ust[a.strip()] = b.strip()
            desc = " ".join(l.strip() for l in blok.split("```")[0].splitlines()[1:] if l.strip())
            back = "wróć na start" in desc.lower()
            sol_lines = [l for l in sol.group(1).splitlines() if l.strip()]
            prog = sprawdz.parse_program(sol_lines)
            warianty = ust["warianty"].split() if "warianty" in ust else None
            suma = int(ust["suma"]) if "suma" in ust else None
            limit = int(ust["limit"]) if "limit" in ust else None
            try:
                sprawdz_gre(where, plansza, prog, warianty, suma, back)
            except Blad as e:
                BLEDY.append(str(e))
            przepis = next((nd[2] for nd in prog if nd[0] == "def"), None)
            rozw = {"program": tokeny(prog)}
            if przepis is not None:
                rozw["przepis"] = tokeny(przepis)
            ile = len(rozw["program"]) + len(rozw.get("przepis", []))
            if limit is not None and ile > limit:
                sys.exit(f"{where}: rozwiązanie ma {ile} kart, a limit to {limit}")
            flat = [t for r in rows for t in r]
            if "*" not in flat and suma is None and not (warianty and any("*" in w for w in warianty)):
                sys.exit(f"{where}: nie ma skarbu ani sumy do zebrania")
            karty = PODSTAWOWE + [k for k in karty_zestawu if k]
            if "pytania" in ust:
                pyt = ust["pytania"].split(",")
            else:
                pyt = PYTANIA
            g = {
                "id": f"2-{size}-{int(num)}", "poziom": 2, "size": size, "zestaw": zestaw, "zestawNazwa": nazwa,
                "nr": int(num), "tytul": title, "opis": desc, "plansza": plansza, "powrot": back,
                "karty": karty, "rozwiazanie": rozw,
            }
            if warianty: g["warianty"] = warianty
            if suma is not None: g["suma"] = suma
            if limit is not None: g["limit"] = limit
            if "JEŚLI" in karty: g["pytania"] = [p.strip() for p in pyt]
            games.append(g)
    return games


def bez_nowych_kart(plansza, powrot):
    """Najmniej kart IDŹ/SKRĘĆ/OBRÓĆ/SKOCZ (z liczbą 1-6), które rozwiązują planszę. None, gdy się nie da."""
    from collections import deque
    rows = [r.split() for r in plansza]
    n = len(rows)
    gw = [(y, x) for y in range(n) for x in range(n) if rows[y][x] == "*"]
    if any(t in "@D123456789?" for r in rows for t in r) or len(gw) > 12:
        return None  # przy wielu skarbach przeszukiwanie trwa za długo, a prosty program i tak jest długi
    (sy, sx), sd = next(((y, x), rows[y][x]) for y in range(n) for x in range(n) if rows[y][x] in "^>v<")
    full = (1 << len(gw)) - 1
    def ok(y, x):
        return 0 <= y < n and 0 <= x < n and rows[y][x] not in "LK#"
    start = (sy, sx, sd, 0)
    dist = {start: 0}
    q = deque([start])
    while q:
        st = q.popleft()
        y, x, d, m = st
        if m == full and (not powrot or (y, x) == (sy, sx)):
            return dist[st]
        nxt = []
        for obr in (1, 3, 2):
            nxt.append((y, x, "^>v<"[("^>v<".index(d) + obr) % 4], m))
        dy, dx = symulator.DXY[d]
        cy, cx, cm = y, x, m
        for k in range(1, 7):
            cy, cx = cy + dy, cx + dx
            if not ok(cy, cx): break
            if (cy, cx) in gw: cm |= 1 << gw.index((cy, cx))
            nxt.append((cy, cx, d, cm))
        cy, cx, cm = y, x, m
        for k in range(1, 7):
            if not (0 <= cy + dy < n and 0 <= cx + dx < n and rows[cy + dy][cx + dx] == "K"): break
            cy, cx = cy + 2 * dy, cx + 2 * dx
            if not ok(cy, cx): break
            if (cy, cx) in gw: cm |= 1 << gw.index((cy, cx))
            nxt.append((cy, cx, d, cm))
        for s2 in nxt:
            if s2 not in dist:
                dist[s2] = dist[st] + 1; q.append(s2)
    return None


OPCJE = ("limit", "suma", "warianty", "pytania", "parametr", "rekurencja", "wymagaj")


def poziom_wyzszy(nr):
    """Gry z gra/poziom-<nr>.md (poziom 3 i wyżej): płaskie karty, sprawdzane symulatorem z narzedzia/symulator.py."""
    path = os.path.join(ROOT, "gra", f"poziom-{nr}.md")
    if not os.path.exists(path):
        return [], []
    text = open(path, encoding="utf-8").read()
    games, uwagi = [], []
    size = zestaw = nazwa = None
    karty_zestawu, ust_zestawu = [], {}
    for blok in re.split(r"^(?=#{2,4} )", text, flags=re.M):
        head = blok.splitlines()[0] if blok.strip() else ""
        if head.startswith("## "):
            size = int(re.search(r"(\d)", head).group(1))
        elif head.startswith("### "):
            m = re.match(r"### Zestaw ([A-Z]): (.*)$", head)
            zestaw, nazwa = m.group(1), m.group(2).strip()
            k = re.search(r"^karty: (.*)$", blok, re.M)
            karty_zestawu = [x.strip() for x in k.group(1).split(",") if x.strip()] if k else []
            ust_zestawu = {}
            for a in OPCJE:
                mm = re.search(rf"^{a}: (.*)$", blok, re.M)
                if mm: ust_zestawu[a] = mm.group(1).strip()
        elif head.startswith("#### "):
            num, title = re.match(r"^#### (\d+)\.\s*(.*)$", head).groups()
            where = f"{path}: {size}x{size} {head[5:]}"
            board = re.search(r"```plansza\n(.*?)```", blok, re.S)
            sol = re.search(r"```rozwiazanie\n(.*?)```", blok, re.S)
            if not board or not sol:
                sys.exit(f"{where}: brak planszy albo rozwiązania")
            rows = [l.split() for l in board.group(1).splitlines() if l.strip()]
            if len(rows) != size or any(len(r) != size for r in rows):
                sys.exit(f"{where}: plansza nie ma rozmiaru {size} × {size}")
            plansza = [" ".join(r) for r in rows]
            ust = dict(ust_zestawu)
            u = re.search(r"```ustawienia\n(.*?)```", blok, re.S)
            if u:
                for l in u.group(1).splitlines():
                    if ":" in l:
                        a, b = l.split(":", 1); ust[a.strip()] = b.strip()
            desc = " ".join(l.strip() for l in blok.split("```")[0].splitlines()[1:] if l.strip())
            back = "wróć na start" in desc.lower()
            prog, przepis = symulator.czytaj_program(sol.group(1).splitlines())
            warianty = ust["warianty"].split() if "warianty" in ust else None
            suma = int(ust["suma"]) if "suma" in ust else None
            limit = int(ust["limit"]) if "limit" in ust else None
            parametr = ust.get("parametr") == "tak"
            rekurencja = ust.get("rekurencja") == "tak"
            karty = PODSTAWOWE + karty_zestawu
            uzyte = {c[0] for c in prog + przepis} - {"NIE", "KONIEC"}
            if uzyte - set(karty):
                sys.exit(f"{where}: rozwiązanie używa kart spoza zestawu: {sorted(uzyte - set(karty))}")
            if any(c[0] == "ZRÓB A" for c in przepis) and not rekurencja:
                sys.exit(f"{where}: ZRÓB A w przepisie bez 'rekurencja: tak'")
            wymagaj = ust.get("wymagaj")
            if wymagaj not in (None, "rekurencja"):
                sys.exit(f"{where}: nieznane 'wymagaj: {wymagaj}'")
            if wymagaj and not any(c[0] == "ZRÓB A" for c in przepis):
                sys.exit(f"{where}: 'wymagaj: rekurencja', a przepis A nie woła sam siebie")
            pytania = [p.strip() for p in ust["pytania"].split(",")] if "pytania" in ust else PYTANIA
            for c in prog + przepis:
                if c[0] in ("JEŚLI", "DOPÓKI") and c[1] not in pytania:
                    sys.exit(f"{where}: pytania {c[1]!r} nie ma na liście pytań gry")
            pyt = [(y, x) for y, r in enumerate(rows) for x, t in enumerate(r) if t == "?"]
            if pyt and not warianty:
                sys.exit(f"{where}: pola ? bez wariantów")
            for w in (warianty or [""]):
                if len(w) != len(pyt):
                    BLEDY.append(f"{where}: wariant {w!r} ma inną liczbę pól niż plansza ({len(pyt)})"); continue
                b = [r[:] for r in rows]
                for (y, x), t in zip(pyt, w):
                    b[y][x] = t
                try:
                    r = symulator.Robot(b, przepis, parametr, rekurencja).uruchom(prog)
                except symulator.Blad as e:
                    BLEDY.append(f"{where}: wariant {w!r}: {e}"); continue
                if r.gwiazdy - r.zebrane:
                    BLEDY.append(f"{where}: wariant {w!r}: nie zebrano skarbów, koniec w {(r.y + 1, r.x + 1)}")
                if not r.gwiazdy and suma is None:
                    BLEDY.append(f"{where}: wariant {w!r}: brak skarbu")
                if suma is not None and r.suma != suma:
                    BLEDY.append(f"{where}: wariant {w!r}: suma {r.suma}, a ma być {suma}")
                if back and (r.y, r.x) != r.start:
                    BLEDY.append(f"{where}: wariant {w!r}: nie wraca na START")
            ile = symulator.ile_kart(prog, przepis)
            if limit is not None and ile > limit:
                BLEDY.append(f"{where}: rozwiązanie ma {ile} kart, a limit to {limit}")
            if limit is not None and not warianty and not wymagaj:
                prosto = bez_nowych_kart(plansza, back)
                if prosto is not None and prosto <= limit:
                    uwagi.append(f"{where}: da się bez nowych kart w {prosto} kartach (limit {limit})")
            rozw = {"program": prog}
            if przepis:
                rozw["przepis"] = przepis
            g = {
                "id": f"{nr}-{size}-{int(num)}", "poziom": nr, "size": size, "zestaw": zestaw, "zestawNazwa": nazwa,
                "nr": int(num), "tytul": title, "opis": desc, "plansza": plansza, "powrot": back,
                "karty": karty, "rozwiazanie": rozw,
            }
            if warianty: g["warianty"] = warianty
            if suma is not None: g["suma"] = suma
            if limit is not None: g["limit"] = limit
            if parametr: g["parametr"] = True
            if rekurencja: g["rekurencja"] = True
            if wymagaj: g["wymagaj"] = wymagaj
            if {"JEŚLI", "DOPÓKI"} & set(karty): g["pytania"] = pytania
            games.append(g)
    return games, uwagi


def main():
    g1, skipped = poziom1()
    g2 = poziom2()
    wyzsze, uwagi = [], []
    for nr in range(3, 10):
        g, u = poziom_wyzszy(nr)
        wyzsze += g; uwagi += u
    for u in uwagi:
        print("UWAGA", u)
    if BLEDY:
        sys.exit("BŁĘDY:\n" + "\n".join(BLEDY))
    games = g1 + g2 + wyzsze
    games.sort(key=lambda g: (g["poziom"], g["size"], g["nr"]))
    ids = [g["id"] for g in games]
    if len(ids) != len(set(ids)):
        sys.exit("powtórzone numery gier: " + ", ".join(sorted({i for i in ids if ids.count(i) > 1})))
    out = os.path.join(ROOT, "gra", "gry.js")
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Plik generowany przez narzedzia/eksport_gry.py z tresc/plansze-poziom-1-*.md i gra/poziom-*.md. Nie edytuj ręcznie.\n")
        f.write("window.GRY = ")
        json.dump(games, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(f"Zapisano {len(games)} gier do gra/gry.js: poziom 1 {len(g1)} (pominięto {skipped}), poziom 2 {len(g2)}.")
    for s in (5, 7, 9):
        print(f"  {s}x{s}: poziom 1 {sum(1 for g in g1 if g['size'] == s)}, poziom 2 {sum(1 for g in g2 if g['size'] == s)}"
              + "".join(f", poziom {p} {sum(1 for g in wyzsze if g['size'] == s and g['poziom'] == p)}" for p in sorted({g['poziom'] for g in wyzsze})))


if __name__ == "__main__":
    main()
