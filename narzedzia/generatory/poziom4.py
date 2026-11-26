import os
from budowa import *
def blok(nr, tytul, opis, plansza, ustaw, prog):
    lim = [l for l in ustaw.splitlines() if l.startswith("limit")][0].split(":")[1].strip()
    return f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} {'karty' if lim in ('2','3','4') else 'kart'}.\n```plansza\n{plansza.strip()}\n```\n```ustawienia\n{ustaw.strip()}\n```\n```rozwiazanie\n{prog.strip()}\n```\n"

def ile(prog):
    p, q = S.czytaj_program(prog.strip().splitlines()); return len(p) + len(q)

LICZ = """DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N"""
LUSTRO = """DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N, IDŹ ×N"""
POLICZ = """DOPÓKI WOLNE?
  JEŚLI SKARB?
    N + 1
  NIE
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO, IDŹ ×N"""

out = ["""# Gra online, poziom 4 (dla 12-latka)

Źródło gier poziomu 4 w grze online i w druku (`plansze-starsi-poziom-4-*`). Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **zmienna N**. Robot pamięta jedną liczbę N (na starcie N = 0). Karta USTAW N (w rozwiązaniu `N = 3`) wpisuje liczbę, karty `N + 1` i `N − 1` ją zmieniają, a liczba N w okienku karty (`IDŹ ×N`, `POWTÓRZ ×N`) znaczy „tyle, ile teraz jest w N”. Pytania `N > 0?` i `N = 0?` sprawdzają N.
"""]
SZ = {5: {}, 7: {}, 9: {}}
for n in (5, 7, 9):
    out.append(f"## Plansza {n} × {n}\n\n### Zestaw A: Zmienna N\nkarty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?\n")
    c = n // 2
    # 1 spirala na zewnątrz
    if n == 5:
        p = "N = 1\nPOWTÓRZ ×4\n  IDŹ ×N, SKRĘĆ W PRAWO, N + 1\nKONIEC"
    elif n == 7:
        p = "N = 1\nPOWTÓRZ ×5\n  IDŹ ×N, SKRĘĆ W PRAWO, N + 1\nKONIEC"
    else:
        p = "N = 1\nPOWTÓRZ ×2\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO, N + 1\n  KONIEC\nKONIEC"
    md, k = auto(1, "Spirala rośnie", "Każdy bok spirali jest o 1 dłuższy. Na początku N = 1, a po każdym boku N + 1. Zbierz skarby.", n, c, c, "^", p, lawa=0.25, seed=n)
    out.append(md)
    # 2 schody coraz wyższe
    k3 = 2 if n == 5 else 3
    p = f"N = 1\nPOWTÓRZ ×{k3}\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N + 1\nKONIEC"
    if n == 5:
        out.append(blok(2, "Tyle samo w bok", "Idź w górę do klocka i licz kroki w N. Potem skręć w prawo i zrób IDŹ ×N. Tam leży skarb.",
            "? . . . ?\n? . . ? .\n? . ? . .\n? ? . . .\n^ . . . .", "limit: 6\nwarianty: ....#..* ..#..*.. #..*.... .*......",
            "DOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W PRAWO, IDŹ ×N"))
    else:
      md, k = auto(2, "Schody coraz wyższe", "Każdy schodek jest o 1 wyższy i o 1 szerszy od poprzedniego.", n, n - 1, 0, "^", p, lawa=0.3, seed=n + 1)
      out.append(md)
    # 3 kwadraty coraz większe
    if n == 9:
        p = "N = 3\nPOWTÓRZ ×6\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  N + 1\nKONIEC"; sizes = range(3, 9)
    else:
        p = f"N = 1\nPOWTÓRZ ×{n - 1}\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  N + 1\nKONIEC"; sizes = range(1, n)
    md, k = auto(3, "Kwadraty coraz większe", "Wszystkie kwadraty zaczynają się w rogu START, a każdy jest o 1 większy.", n, n - 1, 0, "^", p,
                 gwiazdy=[(n - 1 - s, s) for s in sizes], lawa=0.0, seed=n + 2)
    out.append(md)
    # 4 licz i wracaj (warianty)
    if n == 5:
        pl = ". L . L .\n. . . . .\n. > ? ? ?\n. . . . .\n. L . L ."; w = "*#. .*# ..*"
    elif n == 7:
        pl = ". L . . . L .\n. . . . . . .\n. . . . . . .\n. . > ? ? ? ?\n. . . . . . .\n. . . . . . .\n. L . . . L ."; w = "*#.. .*#. ..*# ...*"
    else:
        pl = "\n".join(" ".join("?" if (y <= 4 and x == 4) else "^" if (y, x) == (5, 4) else ("L" if (y in (2, 6) and x in (2, 6)) else ".") for x in range(9)) for y in range(9))
        w = "...#* .#*.. *...."
    out.append(blok(4, "Licz i wracaj", "Robot nie wie, jak daleko jest skarb. Idź do skarbu i licz kroki w N. Potem obróć się i zrób IDŹ ×N, żeby wrócić na START.", pl, f"limit: 6\nwarianty: {w}", LICZ))
    out.append("### Zestaw B: Licznik\nkarty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?\n")
    # 5 lustro
    if n == 5:
        pl = ". . L . .\n. . . . .\n? ? > ? ?\n. . . . .\n. . L . ."; w = ".**# *..*"
    elif n == 7:
        pl = ". . . L . . .\n. . . . . . .\n. . . . . . .\n? ? ? > ? ? ?\n. . . . . . .\n. . . . . . .\n. . . L . . ."; w = "..**#. .*..*# *....*"
    else:
        pl = "\n".join(" ".join("^" if (y, x) == (4, 4) else "?" if x == 4 else ("L" if (y == 4 and x in (1, 7)) else ".") for x in range(9)) for y in range(9))
        w = "..#**... .#*..*.. #*....*. *......*"
    out.append(blok(5, "Lustro", "Drugi skarb jest tak samo daleko za robotem, jak pierwszy przed nim. Policz kroki do pierwszego skarbu, a potem przejdź dwa razy tyle w drugą stronę.", pl, f"limit: 7\nwarianty: {w}", LUSTRO))
    # 6 policz skarby
    rows = [["." for _ in range(n)] for _ in range(n)]
    rows[n - 1][0] = ">"
    for x in range(1, n): rows[n - 1][x] = "?"
    for y in range(1, n - 1): rows[y][n - 1] = "?"
    for y in range(1, n - 2):
        for x in range(1, n - 2):
            if (x + y) % 3 == 0: rows[y][x] = "L"
    pl = "\n".join(" ".join(r) for r in rows)
    col = n - 2  # pola kolumny: wiersze 1..n-2 (z góry na dół), N = n-1-y
    rowc = n - 1  # pola rzędu: kolumny 1..n-1
    def war(gw_row, N):
        cc = ["." for _ in range(col)]; cc[(n - 1 - N) - 1] = "*"
        rr = ["." for _ in range(rowc)]
        for x in gw_row: rr[x - 1] = "*"
        return "".join(cc) + "".join(rr)
    if n == 5: ws = [war([2], 1), war([1, n - 1], 2), war([1, 2, 4], 3)]
    elif n == 7: ws = [war([3], 1), war([2, 5], 2), war([1, 3, 6], 3), war([1, 2, 4, 5, 6], 5)]
    else: ws = [war([4], 1), war([2, 6, 8], 3), war([1, 3, 5, 7], 4), war([1, 2, 3, 5, 6, 7, 8], 7)]
    out.append(blok(6, "Policz skarby", "Idź do końca rzędu i licz skarby w N. Ostatni skarb leży nad końcem rzędu, dokładnie N pól w górę.", pl, f"limit: 9\nwarianty: {' '.join(ws)}", POLICZ))
    # 7 schody coraz niższe
    if n == 5: p = "N = 2\nDOPÓKI N > 0?\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N − 1\nKONIEC"; st = (n - 1, 0)
    elif n == 7: p = "N = 3\nDOPÓKI N > 0?\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1\nKONIEC"; st = (n - 1, 0)
    else: p = "N = 3\nDOPÓKI N > 0?\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N − 1\nKONIEC"; st = (n - 1, 0)
    if n == 5:
        out.append(blok(7, "Policz kałuże", "Przeskocz kałuże do końca rzędu i licz je w N. Skarb leży N pól w górę.",
            ". . . . .\n. L . . ?\n. . L . ?\n. . . . ?\n> ? ? ? .", "limit: 10\nwarianty: ..*.K. .*.K.K ..*..K",
            "DOPÓKI NIE ŚCIANA?\n  JEŚLI KAŁUŻA?\n    SKOCZ, N + 1\n  NIE\n    IDŹ\n  KONIEC\nKONIEC\nSKRĘĆ W LEWO, IDŹ ×N"))
    else:
      md, k = auto(7, "Schody coraz niższe", "Pierwszy schodek jest najwyższy, a każdy następny o 1 niższy. Pętla DOPÓKI N > 0? kończy się sama, gdy N spadnie do zera.", n, st[0], st[1], "^", p, lawa=0.3, seed=n + 7)
      out.append(md)
    # 8 spirala do środka
    if n == 9: p = "N = 6\nN + 2\nDOPÓKI N > 0?\n  POWTÓRZ ×2\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  N − 1\nKONIEC"
    else: p = f"N = {n - 1}\nDOPÓKI N > 0?\n  POWTÓRZ ×2\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  N − 1\nKONIEC"
    b = pusta(n, n - 1, 0, "^"); r, vis, turns, k = sledz(b, p)
    gw = turns[1::3] + [(r.y, r.x)]
    md, k = auto(8, "Spirala do środka", "Dwa boki po N pól, potem N − 1. I tak, dopóki N > 0. Robot kończy w samym środku." + (" Najwyższa karta liczby to 6, więc N = 8 trzeba zrobić z dwóch kart." if n == 9 else ""), n, n - 1, 0, "^", p, gwiazdy=gw)
    out.append(md)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gra", "poziom-4.md"), "w", encoding="utf-8").write("\n".join(out))
