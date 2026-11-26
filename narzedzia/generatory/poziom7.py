import os
from budowa import auto, pusta, S, sledz
"""Generator gier poziomu 7 (rekurencja i META). Uruchom: python3 narzedzia/generatory/poziom7.py, potem make online."""

KA = "karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META\npytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?\nrekurencja: tak\nwymagaj: rekurencja\n"
KB = "karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META\npytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?\nrekurencja: tak\nparametr: tak\nwymagaj: rekurencja\n"

TAM = """PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, ZRÓB A, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A"""
DWA = """PRZEPIS A
  JEŚLI NIE WOLNE?
    OBRÓĆ SIĘ, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ, IDŹ
KONIEC
ZRÓB A"""
PO = """PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A"""
KWADRATY = """PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
"""
GORA = """PRZEPIS A
  JEŚLI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1, ZRÓB A ×N
    SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
"""
SPIRALA = """PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×2
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
"""
DRZEWO = """PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, N − 1, SKRĘĆ W LEWO, ZRÓB A ×N
    OBRÓĆ SIĘ, ZRÓB A ×N
    SKRĘĆ W PRAWO, N + 1, IDŹ ×N, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
"""

def liscie_drzewa(n, c, prog):
    """liść = pole, na którym robot robi 3 obroty pod rząd bez kroku"""
    b = pusta(n, n - 1, c, "^")
    pr, przepis = S.czytaj_program(prog.strip().splitlines())
    r = S.Robot(b, przepis, True, True)
    seq = []
    orig = r.krok
    def krok(k):
        orig(k); seq.append((k, (r.y, r.x)))
    r.krok = krok
    r.uruchom(pr)
    out, run = set(), 0
    for k, pos in seq:
        if k in ("IDŹ", "SKOCZ"): run = 0
        else:
            run += 1
            if run == 3: out.add(pos)
    return sorted(out)

def wywolanie(k):
    return f"ZRÓB A ×{k}" if k <= 6 else f"N = 6\nN + {k - 6}\nZRÓB A ×N"

def ile(prog):
    p, q = S.czytaj_program(prog.strip().splitlines()); return len(p) + len(q)

def blok(nr, tytul, opis, plansza, war, prog, extra=""):
    lim = ile(prog)
    return (f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} kart.\n```plansza\n{plansza.strip()}\n```\n"
            f"```ustawienia\nlimit: {lim}\nwarianty: {' '.join(war)}{extra}\n```\n```rozwiazanie\n{prog.strip()}\n```\n")

def rzad(n, y, x0, d, cells, inne=None):
    """plansza z robotem w (y, x0) i polami ? w podanym rzędzie"""
    b = pusta(n, y, x0, d)
    for x in cells: b[y][x] = "?"
    for (yy, xx), t in (inne or {}).items(): b[yy][xx] = t
    return "\n".join(" ".join(r) for r in b)

def main():
    out = ["""# Gra online, poziom 7 (trudny)

Źródło gier poziomu 7 w grze online i w druku (`plansze-starsi-poziom-7-*`). Gry generuje `narzedzia/generatory/poziom7.py`. Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **rekurencja** (ustawienie `rekurencja: tak`): karta ZRÓB A może leżeć w samym przepisie A, więc przepis woła sam siebie. Każde wywołanie ma swoje N (z `parametr: tak`), a karty po ZRÓB A wykonują się dopiero po powrocie, w odwrotnej kolejności. **META** w przepisie kończy tylko bieżące wywołanie (wczesny powrót, *return*). Bez warunku stopu robot się „zapętla”: po 40 wywołaniach gra przerywa program.
"""]
    for n in (5, 7, 9):
        c = n // 2
        out.append(f"## Plansza {n} × {n}\n\n### Zestaw A: Rekurencja\n{KA}")
        # 1 tam i z powrotem: robot w kolumnie 2, ? od kolumny 3
        cells = list(range(3, n))
        war = []
        for d in range(1, len(cells) + 1):
            if len(war) >= 3 and d < len(cells): continue
            w = ["."] * len(cells); w[d - 1] = "*"
            if d < len(cells): w[d] = "#"
            war.append("".join(w))
        war = sorted(set(war))[:4]
        pl = rzad(n, c, 2, ">", cells, {(c - 1, 1): "L", (c + 1, 1): "L"})
        out.append(blok(1, "Tam i z powrotem", "Bez zmiennej i bez liczenia! Przepis A: jeśli wolne, IDŹ, ZRÓB A (cały przepis jeszcze raz), IDŹ. Jeśli nie, OBRÓĆ SIĘ. Każde IDŹ po ZRÓB A czeka, aż wróci wywołanie, więc robot wraca tyle samo kroków. Wróć na START.", pl, war, TAM))
        # 2 dwa razy dalej z META
        if n == 5: pl = rzad(n, 2, 2, ">", [0, 1, 3, 4]); war = [".**#", "*..*"]
        elif n == 7: pl = rzad(n, 3, 3, ">", [0, 1, 2, 4, 5, 6]); war = ["..**#.", ".*..*#", "*....*"]
        else: pl = rzad(n, 4, 4, ">", [0, 1, 2, 3, 5, 6, 7, 8]); war = ["...**#..", "..*..*#.", ".*....*#", "*......*"]
        out.append(blok(2, "Wczesny powrót", "Przepis zaczyna od strażnika: jeśli przed robotem nie jest wolne, OBRÓĆ SIĘ i META (powrót z tego wywołania). Po każdym powrocie robot robi 2 kroki, więc dochodzi dwa razy dalej, do drugiego skarbu za START.", pl, war, DWA))
        # 3 po skarb i z powrotem (za skarbem wolne pola)
        cells = list(range(2, n - 1))
        war = []
        for i in range(len(cells)):
            w = ["."] * len(cells); w[i] = "*"; war.append("".join(w))
        war = war[::max(1, len(war) // 3)][:4]
        pl = rzad(n, c, 1, ">", cells, {(c, n - 1): "."})
        out.append(blok(3, "Po skarb i z powrotem", "Za skarbem pole jest wolne, więc DOPÓKI WOLNE? tu nie pomoże. Przepis pyta: skarb? Jeśli tak, weź go i zawróć. Jeśli nie, IDŹ, ZRÓB A, IDŹ. Wróć na START.", pl, war, PO))
        # 4 dwa korytarze: start w środku, skarby po obu stronach
        lewo = list(range(0, c)); prawo = list(range(c + 1, n))
        war = []
        for i, j in ((0, len(prawo) - 1), (len(lewo) - 1, 0), (1 % len(lewo), (1 % len(prawo)))):
            wl = ["."] * len(lewo); wl[i] = "*"; wp = ["."] * len(prawo); wp[j] = "*"
            war.append("".join(wl) + "".join(wp))
        war = sorted(set(war))
        pl = rzad(n, c, c, ">", lewo + prawo, {(c - 1, x): "L" for x in range(0, n, 2)})
        out.append(blok(4, "Dwa korytarze", "Skarb jest po prawej i po lewej stronie START. Ten sam przepis co w poprzedniej grze: po pierwszym ZRÓB A robot stoi na START, ale patrzy w drugą stronę. Wróć na START.", pl, war, PO.replace("\nZRÓB A", "\nZRÓB A ×2")))
        out.append(f"### Zestaw B: Rekurencja z parametrem\n{KB}")
        # 5 kwadraty w kwadratach
        k = n - 1
        p = KWADRATY + wywolanie(k)
        md, _ = auto(5, "Kwadraty w kwadratach", f"Przepis A rysuje kwadrat o boku N, a potem woła sam siebie z N − 1. Kończy się, gdy N = 0. Program to jedno ZRÓB A ×{k}" + (" (8 to N = 6, potem N + 2, potem ZRÓB A ×N)." if k > 6 else "."), n, n - 1, 0, "^", p,
                     gwiazdy=[(n - 1 - s, s) for s in range(1, k + 1)], param=True, rek=True, lawa=1.0)
        out.append(md)
        # 6 góra
        k = c
        p = GORA + wywolanie(k)
        md, _ = auto(6, "Góra z rekurencji", "W drodze w górę robot robi schodki przed ZRÓB A, a w drodze w dół te karty, które leżą po ZRÓB A. Szczyt to moment, gdy N = 0.", n, n - 1, 0, "^", p, lawa=1.0, seed=n + 6, param=True, rek=True)
        out.append(md)
        # 7 spirala
        k = n - 1
        p = SPIRALA + wywolanie(k)
        md, _ = auto(7, "Spirala z rekurencji", "Dwa boki po N pól i wywołanie z N − 1. Robot kończy w środku planszy.", n, n - 1, 0, "^", p, gwiazdy="zakrety", param=True, rek=True)
        out.append(md)
        # 8 drzewo
        k = {5: 2, 7: 3, 9: 4}[n]
        p = DRZEWO + wywolanie(k)
        liscie = liscie_drzewa(n, c, p)
        md, _ = auto(8, "Drzewo", "Pień o długości N, a na jego końcu dwie gałęzie: mniejsze drzewa z N − 1, w lewo i w prawo. Każdy liść to skarb. Robot wraca pod pień. Wróć na START.", n, n - 1, c, "^", p, gwiazdy=liscie, param=True, rek=True, lawa=1.0)
        out.append(md)
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gra", "poziom-7.md"), "w", encoding="utf-8").write("\n".join(out))

main()
