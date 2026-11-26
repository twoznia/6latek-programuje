import os, sys
from budowa import auto, sledz, pusta, S
"""Generator gier poziomu 6 (przepis z parametrem). Uruchom: python3 narzedzia/generatory/poziom6.py, potem make online."""

KART = "karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?\nparametr: tak\n"

def blok(nr, tytul, opis, plansza, ustaw, prog):
    lim = [l for l in ustaw.splitlines() if l.startswith("limit")][0].split(":")[1].strip()
    return f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} kart.\n```plansza\n{plansza.strip()}\n```\n```ustawienia\n{ustaw.strip()}\n```\n```rozwiazanie\n{prog.strip()}\n```\n"

def zrob(lista):
    return ", ".join(f"ZRÓB A ×{k}" for k in lista)

def main():
    out = ["""# Gra online, poziom 6 (dla średniego programisty)

Źródło gier poziomu 6 w grze online i w druku (`plansze-starsi-poziom-6-*`). Gry generuje `narzedzia/generatory/poziom6.py`. Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **przepis z parametrem** (ustawienie `parametr: tak`). Liczba w okienku karty ZRÓB A nie mówi już „ile razy”, tylko przekazuje wartość: ZRÓB A ×3 robi przepis A raz, a w środku przepisu N = 3. Po powrocie z przepisu N wraca do wartości sprzed wywołania (zmienna lokalna). Liczba N w okienku ZRÓB A przekazuje bieżące N.
"""]
    for n in (5, 7, 9):
        out.append(f"## Plansza {n} × {n}\n\n### Zestaw A: Przepis z parametrem\n{KART}")
        # 1 kwadraty różnej wielkości
        rozm = {5: [2, 4, 1, 3], 7: [3, 6, 1, 4], 9: [5, 8, 2, 6, 3, 4]}[n]
        p = "PRZEPIS A\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\nKONIEC\n" + "\n".join(f"ZRÓB A ×{k}" if k <= 6 else f"N = 6\nN + {k - 6}\nZRÓB A ×N" for k in rozm)
        gw = [(n - 1 - k, k) for k in rozm]
        md, _ = auto(1, "Kwadraty na zamówienie", "Przepis A rysuje kwadrat o boku N. ZRÓB A ×3 to kwadrat o boku 3. Obejdź kwadraty w podanych rozmiarach: każdy skarb to róg innego kwadratu.", n, n - 1, 0, "^", p, gwiazdy=gw, param=True)
        out.append(md)
        # 2 nierówne schody
        st = {5: [1, 2, 1], 7: [1, 3, 2], 9: [2, 1, 3, 2]}[n]
        p = "PRZEPIS A\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO\nKONIEC\n" + "\n".join(f"ZRÓB A ×{k}" for k in st)
        md, _ = auto(2, "Nierówne schody", "Każdy schodek ma inną wysokość, więc pętla nie pomoże. Przepis A to schodek o wysokości i szerokości N.", n, n - 1, 0, "^", p, lawa=0.3, seed=n + 2, param=True)
        out.append(md)
        # 3 wieże
        wys = {5: [3, 1, 4, 2], 7: [4, 2, 6, 1, 5, 3], 9: [5, 2, 7, 3, 8, 1, 6, 4]}[n]
        p = "PRZEPIS A\n  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ\nKONIEC\n" + \
            "\n".join(f"ZRÓB A ×{k}" if k <= 6 else f"N = 6\nN + {k - 6}\nZRÓB A ×N" for k in wys)
        gw = [(n - 1 - h, i) for i, h in enumerate(wys)]
        ex = {(y, i): "#" for i, h in enumerate(wys) for y in range(0, n - 1 - h)}
        md, _ = auto(3, "Wieże", "Na szczycie każdej wieży leży skarb. Przepis A wchodzi na wieżę o wysokości N, schodzi i idzie do następnej.", n, n - 1, 0, ">", p, gwiazdy=gw, extra=ex, param=True)
        out.append(md)
        # 4 diamenty (wspólny lewy róg)
        dm = {5: [2, 1], 7: [3, 1, 2], 9: [4, 2, 3]}[n]
        p = "PRZEPIS A\n  POWTÓRZ ×4\n    POWTÓRZ ×N\n      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\n    KONIEC\n    SKRĘĆ W PRAWO\n  KONIEC\nKONIEC\n" + "\n".join(f"ZRÓB A ×{k}" for k in dm)
        c = n // 2
        gw = [(c - k, k) for k in dm] + [(c + k, k) for k in dm]
        md, _ = auto(4, "Diamenty", "Przepis A to diament o boku N z poziomu 3. Wszystkie diamenty zaczynają się w START. Zbierz skarby i wróć na START.", n, c, 0, "^", p, gwiazdy=gw, lawa=0.2, seed=n + 4, param=True)
        out.append(md)
        out.append(f"### Zestaw B: Parametr i zmienna\n{KART}")
        # 5 kopiuj odległość: policz, a potem kwadrat o boku N w lewo
        prog = "PRZEPIS A\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W LEWO\n  KONIEC\nKONIEC\nDOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W LEWO, ZRÓB A ×N"
        # robot (n-1,0) w prawo; klocek na (n-1, d+1); gwiazdy w (n-1-d, d) i (n-1-d, 0)
        ds = {5: [2, 3, 4], 7: [2, 4, 6], 9: [3, 5, 8]}[n]
        q = sorted({(n - 1 - d, d) for d in ds} | {(n - 1 - d, 0) for d in ds} | {(n - 1, d + 1) for d in ds if d + 1 < n})
        war = []
        for d in ds:
            v = ""
            for (y, x) in q:
                if (y, x) in ((n - 1 - d, d), (n - 1 - d, 0)): v += "*"
                elif (y, x) == (n - 1, d + 1): v += "#"
                else: v += "."
            war.append(v)
        b = pusta(n, n - 1, 0, ">")
        for (y, x) in q: b[y][x] = "?"
        pl = "\n".join(" ".join(r) for r in b)
        lim = len(S.czytaj_program(prog.splitlines())[0]) + len(S.czytaj_program(prog.splitlines())[1])
        out.append(blok(5, "Kwadrat jak odległość", "Idź do klocka i licz kroki w N. Potem skręć w lewo i narysuj kwadrat o boku N: ZRÓB A ×N przekazuje N do przepisu. Klocek za każdym razem stoi gdzie indziej.", pl, f"limit: {lim}\nwarianty: {' '.join(war)}", prog))
        # 6 odliczanie w przepisie
        od = {5: [4], 7: [3, 2], 9: [4, 3]}[n]
        p = "PRZEPIS A\n  DOPÓKI N > 0?\n    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1\n  KONIEC\nKONIEC\n" + "\nSKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\n".join(f"ZRÓB A ×{k}" for k in od)
        st = (n - 1, 0)
        md, _ = auto(6, "Odliczanie w przepisie", "Przepis A robi N schodków i odlicza N − 1, dopóki N > 0. Między przepisami robot robi krok w bok. N w przepisie to kopia: zmiana w środku nie psuje liczby w programie.", n, st[0], st[1], "^", p, lawa=0.3, seed=n + 6, param=True)
        out.append(md)
        # 7 spirala z przepisu
        k7 = {5: 4, 7: 6, 9: 4}[n]
        if n == 9:
            p = "PRZEPIS A\n  POWTÓRZ ×2\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\nKONIEC\nN = 1\nPOWTÓRZ ×2\n  POWTÓRZ ×4\n    ZRÓB A ×N, N + 1\n  KONIEC\nKONIEC"
        else:
            p = f"PRZEPIS A\n  POWTÓRZ ×2\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\nKONIEC\nN = 1\nPOWTÓRZ ×{k7}\n  ZRÓB A ×N, N + 1\nKONIEC"
        c = n // 2
        b = pusta(n, c, c, "^"); r, vis, turns, _ = sledz(b, p, True)
        md, _ = auto(7, "Spirala dwójkami", "Przepis A to dwa boki po N pól. Program woła ZRÓB A ×N i zwiększa N. Każda długość boku pojawia się dwa razy.", n, c, c, "^", p, gwiazdy=turns[1::2] + [(r.y, r.x)], param=True)
        out.append(md)
        # 8 kwadraty obok siebie
        kw = {5: [1, 2, 1], 7: [2, 1, 3], 9: [3, 1, 4]}[n]
        p = "PRZEPIS A\n  POWTÓRZ ×3\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  SKRĘĆ W PRAWO\nKONIEC\n" + "\n".join(f"ZRÓB A ×{k}" for k in kw)
        x = 0; gw = []
        for k in kw:
            gw.append((n - 1 - k, x + k)); x += k
        md, _ = auto(8, "Kwadraty w rzędzie", "Przepis A obchodzi trzy boki kwadratu o boku N i staje w jego prawym dolnym rogu, gotowy do następnego. Każdy skarb to prawy górny róg innego kwadratu.", n, n - 1, 0, "^", p, gwiazdy=gw, lawa=1.0 if n == 5 else 0.25, seed=n + 8, param=True)
        out.append(md)
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gra", "poziom-6.md"), "w", encoding="utf-8").write("\n".join(out))

main()
