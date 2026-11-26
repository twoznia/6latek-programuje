import os
import random, sys
from labirynt import *
from budowa import sledz
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import eksport_gry as E

PRAWA = """DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ"""
LEWA = PRAWA.replace("PRAWO", "XX").replace("LEWO", "PRAWO").replace("XX", "LEWO")
KRETY = """DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ"""
KRETY_K = """DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ"""
PRZESZKODY = """PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC"""
PYT = "pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?"
DIRS = {(-1, 0): "^", (1, 0): "v", (0, 1): ">", (0, -1): "<"}

def ile(prog):
    p, q = S.czytaj_program(prog.strip().splitlines()); return len(p) + len(q)

def blok(nr, tytul, opis, g, prog, war=None, limit=None):
    lim = limit or ile(prog)
    u = f"limit: {lim}" + (f"\nwarianty: {' '.join(war)}" if war else "")
    pl = "\n".join(" ".join(r) for r in g)
    return f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} kart.\n```plansza\n{pl}\n```\n```ustawienia\n{u}\n```\n```rozwiazanie\n{prog.strip()}\n```\n"

def dziala(g, prog):
    try:
        r = uruchom([row[:] for row in g], prog)
    except S.Blad:
        return None
    if r.gwiazdy - r.zebrane: return None
    return r

def korytarz(n, seed, dl, sciana="L", kaluze=0):
    rnd = random.Random(seed)
    for _ in range(4000):
        path = [(n - 1, 0)]
        while len(path) < dl:
            y, x = path[-1]
            opts = []
            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < n and 0 <= nx < n) or (ny, nx) in path: continue
                if any((ny + a, nx + b) in path[:-1] for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1))): continue
                opts.append((ny, nx))
            if not opts: break
            path.append(rnd.choice(opts))
        if len(path) < dl: continue
        turns = sum(1 for i in range(1, len(path) - 1) if (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]) != (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1]))
        if turns < 5: continue
        g = [[sciana] * n for _ in range(n)]
        for c in path: g[c[0]][c[1]] = "."
        d = (path[1][0] - path[0][0], path[1][1] - path[0][1])
        g[path[0][0]][path[0][1]] = DIRS[d]
        g[path[-1][0]][path[-1][1]] = "*"
        if kaluze:
            proste = [i for i in range(2, len(path) - 2)
                      if (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]) == (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])]
            rnd.shuffle(proste); wz = []
            for i in proste:
                if all(abs(i - j) > 2 for j in wz): wz.append(i)
                if len(wz) == kaluze: break
            if len(wz) < kaluze: continue
            for i in wz: g[path[i][0]][path[i][1]] = "K"
        prog = KRETY_K if kaluze else KRETY
        if not dziala(g, prog): continue
        # skarb raz w połowie ścieżki, raz na końcu: robot nie zna długości
        k = next((i for i in range(len(path) // 2, len(path) - 2) if g[path[i][0]][path[i][1]] == "."), None)
        if k is None: continue
        h = [r[:] for r in g]; h[path[k][0]][path[k][1]] = "*"; h[path[-1][0]][path[-1][1]] = "."
        if not dziala(h, prog): continue
        g[path[k][0]][path[k][1]] = "?"; g[path[-1][0]][path[-1][1]] = "?"
        w = "*." if path[k] < path[-1] else ".*"
        w2 = w[::-1]
        return g, [w, w2]
    raise SystemExit("korytarz: nie znalazłem")

def labirynt(n, seed, prog, ile_drzwi, ile_war):
    rnd = random.Random(seed)
    for s in range(seed, seed + 500):
        g = perfekcyjny(n, s)
        # najdalszy ślepy zaułek
        from collections import deque
        dist = {(n - 1, 0): 0}; q = deque([(n - 1, 0)])
        while q:
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and g[ny][nx] == "." and (ny, nx) not in dist:
                    dist[(ny, nx)] = dist[(y, x)] + 1; q.append((ny, nx))
        cel = max(dist, key=dist.get)
        g[cel[0]][cel[1]] = "*"
        g[n - 1][0] = "^" if g[n - 2][0] == "." else ">"
        if not dziala(g, prog): continue
        sciany = [(y, x) for y in range(n) for x in range(n) if g[y][x] == "#" and (y % 2) != (x % 2)]
        for _ in range(200):
            drzwi = sorted(rnd.sample(sciany, ile_drzwi))
            kombi = set()
            for _ in range(60):
                kombi.add("".join(rnd.choice("#.") for _ in drzwi))
            ok = []
            sciezki = set()
            for w in sorted(kombi):
                h = [r[:] for r in g]
                for (y, x), t in zip(drzwi, w): h[y][x] = t
                rr = dziala(h, prog)
                if rr:
                    _, vis, _, _ = sledz(h, prog)
                    key = tuple(vis)
                    if key not in sciezki:
                        sciezki.add(key); ok.append(w)
            if len(ok) >= ile_war:
                h = [r[:] for r in g]
                for (y, x) in drzwi: h[y][x] = "?"
                return h, ok[:ile_war]
    raise SystemExit("labirynt: nie znalazłem")

def przeszkody(n, seed, ile_war):
    rnd = random.Random(seed)
    y = n - 2
    g = [["." for _ in range(n)] for _ in range(n)]
    g[y][0] = ">"; g[y][n - 1] = "*"
    for x in range(1, n - 1): g[y][x] = "?"
    for yy in range(n):
        for xx in range(n):
            if yy not in (y, y - 1) and rnd.random() < 0.25: g[yy][xx] = "L"
    war = set()
    while len(war) < ile_war:
        w = ""
        x = 1
        cells = ["."] * (n - 2)
        i = 0
        while i < n - 2:
            if rnd.random() < 0.5 and i < n - 2:
                cells[i] = rnd.choice("KL#"); i += 2
            else: i += 1
        w = "".join(cells)
        h = [r[:] for r in g]
        for (xx, t) in zip(range(1, n - 1), w): h[y][xx] = t
        if dziala(h, PRZESZKODY) and sum(c != "." for c in w) >= 2: war.add(w)
    return g, sorted(war)

def main():
    out = ["""# Gra online, poziom 5 (dla początkującego programisty)

Źródło gier poziomu 5 w grze online i w druku (`plansze-starsi-poziom-5-*`). Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **pytania złożone** i **czujniki z boku**. `NIE X` odwraca odpowiedź, `X I Y` to TAK tylko wtedy, gdy oba są TAK, a `X LUB Y` to TAK, gdy choć jedno jest TAK. `WOLNE W LEWO?` i `WOLNE W PRAWO?` pytają o pole obok robota. Do tego labirynty, w których część ścian (pola ?) za każdym razem stoi inaczej: wygrywa ogólny algorytm, a nie wyuczona droga. Gry są generowane skryptem, a rozwiązania sprawdza symulator.
"""]
    cfg = {5: dict(dl=11, war=2, drzwi=2), 7: dict(dl=19, war=3, drzwi=3), 9: dict(dl=31, war=3, drzwi=4)}
    for n in (5, 7, 9):
        c = cfg[n]
        out.append(f"## Plansza {n} × {n}\n\n### Zestaw A: Pytania złożone\nkarty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A\n{PYT}\n")
        g, w = korytarz(n, n * 10 + 1, c["dl"])
        out.append(blok(1, "Kręta ścieżka nad lawą", "Skarb leży raz w połowie ścieżki, a raz na końcu. Po każdym kroku robot pyta: czy przede mną jest zamknięte I w lewo wolne? Wtedy skręca w lewo. Tak samo w prawo.", g, KRETY, w))
        g, w = korytarz(n, n * 10 + 2, c["dl"] + 1, kaluze=1 if n == 5 else 2)
        out.append(blok(2, "Ścieżka z kałużami", "Kręta ścieżka, a na niej kałuże. Najpierw: kałuża? SKOCZ, a jeśli nie, IDŹ. Potem skręty jak w poprzedniej grze.", g, KRETY_K, w))
        g, w = przeszkody(n, n * 10 + 3, 3)
        out.append(blok(3, "Kałuża, lawa albo klocek", "Na polach ? za każdym razem stoi coś innego. Kałużę przeskocz. Lawę LUB klocek obejdź górą: to przepis A.", g, PRZESZKODY, w))
        g, w = przeszkody(n, n * 10 + 4, 4)
        out.append(blok(4, "Cztery razy inaczej", "Ten sam program musi przejść cztery różne rzędy przeszkód.", g, PRZESZKODY, w))
        out.append(f"### Zestaw B: Labirynty\nkarty: POWTÓRZ, DOPÓKI, JEŚLI\n{PYT}\n")
        g, w = labirynt(n, n * 100 + 5, PRAWA, c["drzwi"] - 1, 2)
        out.append(blok(5, "Labirynt prawej ręki", "Trzymaj prawą rękę na ścianie: po każdym kroku, jeśli w prawo jest wolne, skręć w prawo. Jeśli nie, kręć się w lewo, dopóki przed tobą nie jest wolne. Część ścian (pola ?) za każdym razem stoi inaczej.", g, PRAWA, w))
        g, w = labirynt(n, n * 100 + 6, LEWA, c["drzwi"] - 1, 2)
        out.append(blok(6, "Labirynt lewej ręki", "Teraz lewa ręka na ścianie. Przerób program z poprzedniej gry.", g, LEWA, w))
        g, w = labirynt(n, n * 100 + 7, PRAWA, c["drzwi"], c["war"])
        out.append(blok(7, "Labirynt z drzwiami", f"Na polach ? są drzwi: raz otwarte, raz zamknięte. Program musi znaleźć skarb w każdym z {c['war']} labiryntów.", g, PRAWA, w))
        g, w = labirynt(n, n * 100 + 8, LEWA, c["drzwi"] + 1, c["war"] + 1)
        out.append(blok(8, "Wielka zagadka", f"{c['war'] + 1} różne labirynty i jeden program. Którą ręką do ściany?", g, LEWA, w))
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gra", "poziom-5.md"), "w", encoding="utf-8").write("\n".join(out))
main()
