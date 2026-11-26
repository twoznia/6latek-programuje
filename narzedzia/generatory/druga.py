"""Druga ósemka gier (9-16) na każdą planszę w poziomach 3-7 gry online.

Dopisuje zestawy C i D na końcu każdej sekcji „## Plansza S × S” w gra/poziom-<N>.md.
Uruchamiaj PO generatorach poziomów (poziom4.py ... poziom7.py nadpisują swoje pliki):
    python3 narzedzia/generatory/druga.py && make online
Skrypt można uruchamiać wiele razy: najpierw usuwa stare zestawy C i D.
Gry z polami ? mają warianty losowane tak, żeby każdy dawał inną drogę robota.
"""
import os, random, re
from budowa import auto, pusta, sledz, S

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")


def ile(prog):
    p, q = S.czytaj_program(prog.strip().splitlines())
    return len(p) + len(q)


def liczba(k):
    """karta ×k albo N = 6, N + ... dla k > 6 (liczby na kartach tylko 0-6)"""
    return f"ZRÓB A ×{k}" if k <= 6 else f"N = 6\nN + {k - 6}\nZRÓB A ×N"


def stala(nr, tytul, opis, n, y, x, d, prog, **kw):
    md, _ = auto(nr, tytul, opis, n, y, x, d, prog, **kw)
    return md


def losowa(nr, tytul, opis, n, y, x, d, prog, kand=(), sym="#", ile_p=0, gw_kand=(), gw_ile=0,
           koniec=True, ile_war=3, seed=1, param=False, rek=False, tlo=None, gw_fn=None, min_kroki=2):
    """Gra z polami ?: losuje przeszkody (ile_p z kand) i skarby (gw_ile z gw_kand), symuluje program,
    a gdy koniec=True kładzie skarb tam, gdzie robot staje. Pola, które różnią się w wariantach, to ?."""
    rnd = random.Random(seed * 7919 + nr * 31 + n)
    powrot = "wróć na start" in opis.lower()
    warianty, drogi = [], set()
    for _ in range(6000):
        b = pusta(n, y, x, d)
        for (yy, xx), t in (tlo or {}).items():
            b[yy][xx] = t
        ip = rnd.choice(ile_p) if isinstance(ile_p, tuple) else ile_p
        ig = rnd.choice(gw_ile) if isinstance(gw_ile, tuple) else gw_ile
        wolne = [c for c in kand if b[c[0]][c[1]] == "."]
        if len(wolne) < ip: continue
        for (yy, xx) in rnd.sample(wolne, ip):
            b[yy][xx] = rnd.choice(sym) if len(sym) > 1 else sym
        wolne = [c for c in gw_kand if b[c[0]][c[1]] == "."]
        if len(wolne) < ig: continue
        for (yy, xx) in rnd.sample(wolne, ig):
            b[yy][xx] = "*"
        try:
            r, vis, turns, _ = sledz(b, prog, param, rek)
        except S.Blad:
            continue
        if len(vis) < min_kroki: continue
        dodaj = []
        if koniec:
            if (r.y, r.x) == (y, x) or b[r.y][r.x] != ".": continue
            dodaj.append((r.y, r.x))
        if gw_fn:
            dodaj += gw_fn(r, vis, turns)
        for (yy, xx) in dodaj:
            if b[yy][xx] not in ".*": break
            b[yy][xx] = "*"
        else:
            try:
                r, vis, turns, _ = sledz(b, prog, param, rek)
            except S.Blad:
                continue
            if r.gwiazdy - r.zebrane or not r.gwiazdy: continue
            if powrot and (r.y, r.x) != (y, x): continue
            key = tuple(vis)
            if key in drogi: continue
            drogi.add(key)
            warianty.append(b)
            if len(warianty) == ile_war: break
    if len(warianty) < ile_war:
        raise SystemExit(f"{n}x{n} {nr}. {tytul}: znalazłem tylko {len(warianty)} wariantów")
    pyt = [(yy, xx) for yy in range(n) for xx in range(n) if len({w[yy][xx] for w in warianty}) > 1]
    plansza = [r[:] for r in warianty[0]]
    for (yy, xx) in pyt:
        plansza[yy][xx] = "?"
    war = ["".join(w[yy][xx] for (yy, xx) in pyt) for w in warianty]
    lim = ile(prog)
    ust = f"limit: {lim}\nwarianty: {' '.join(war)}"
    pl = "\n".join(" ".join(r) for r in plansza)
    return (f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} kart.\n```plansza\n{pl}\n```\n"
            f"```ustawienia\n{ust}\n```\n```rozwiazanie\n{prog.strip()}\n```\n")


def kolumna(n, x, od, do):
    return [(yy, x) for yy in range(od, do)]


def rzad(n, y, od, do):
    return [(y, xx) for xx in range(od, do)]


def wszystkie(n, bez=()):
    return [(yy, xx) for yy in range(n) for xx in range(n) if (yy, xx) not in bez]


# ---------------------------------------------------------------- poziom 3
def poziom3(n):
    c = n // 2
    out = ["### Zestaw C: Wzory z pętli\nkarty: POWTÓRZ\n"]
    p = f"POWTÓRZ ×4\n  IDŹ ×{c}, OBRÓĆ SIĘ, IDŹ ×{c}, SKRĘĆ W LEWO\nKONIEC"
    out.append(stala(9, "Plus", f"Cztery ramiona po {c} pola. Na końcu każdego ramienia obróć się i wróć do środka.", n, c, c, "^", p, lawa=1.0))
    h = c
    h = n - 2
    p = f"POWTÓRZ ×{(n - 1) // 2}\n  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×{h}, OBRÓĆ SIĘ, IDŹ ×{h}, SKRĘĆ W LEWO\nKONIEC"
    out.append(stala(10, "Grzebień", f"Robot idzie w prawo i co drugie pole robi ząb grzebienia: {h} w górę i z powrotem.", n, n - 1, 0, ">", p, lawa=1.0, seed=n))
    p = f"POWTÓRZ ×4\n  POWTÓRZ ×4\n    IDŹ ×{c}, SKRĘĆ W PRAWO\n  KONIEC\n  SKRĘĆ W PRAWO\nKONIEC"
    out.append(stala(11, "Okno", "Cztery kwadraty wokół START, jak szybki w oknie. Po każdym kwadracie robot skręca w prawo.", n, c, c, "^", p, lawa=1.0))
    k = n - 1
    p = f"POWTÓRZ ×2\n  POWTÓRZ ×{k}\n    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\n  KONIEC\n  OBRÓĆ SIĘ\nKONIEC" if k <= 6 else \
        f"POWTÓRZ ×2\n  POWTÓRZ ×2\n    POWTÓRZ ×4\n      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\n    KONIEC\n  KONIEC\n  OBRÓĆ SIĘ\nKONIEC"
    out.append(stala(12, "Schody w górę i w dół", f"{k} schodków w górę, obrót i te same karty jeszcze raz. Robot schodzi inną drogą! Wróć na START.", n, n - 1, 0, "^", p, lawa=1.0, seed=n + 12))
    out.append("### Zestaw D: DOPÓKI w nowych miejscach\nkarty: POWTÓRZ, DOPÓKI, JEŚLI\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, KAŁUŻA?, SKARB?\n")
    p = "DOPÓKI WOLNE?\n  IDŹ\nKONIEC\nSKRĘĆ W PRAWO\nDOPÓKI WOLNE?\n  IDŹ\nKONIEC"
    out.append(losowa(13, "Do klocka i w prawo", "Idź, dopóki jest wolne, skręć w prawo i znowu idź, dopóki jest wolne. Klocki za każdym razem stoją gdzie indziej.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 1, n - 2) + wszystkie(n, bez=[(n - 1, 0)])[: n * 2], ile_p=2, seed=3))
    p = "POWTÓRZ ×2\n  DOPÓKI NIE ŚCIANA?\n    JEŚLI KAŁUŻA?\n      SKOCZ\n    NIE\n      IDŹ\n    KONIEC\n  KONIEC\n  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO\nKONIEC"
    out.append(losowa(14, "Dwa rzędy kałuż", "Przejdź dolny rząd do ściany, wejdź piętro wyżej i wróć górnym rzędem. Kałuże przeskakuj.", n, n - 1, 0, ">", p,
                      kand=rzad(n, n - 1, 1, n - 1) + rzad(n, n - 2, 1, n - 1), sym="K", ile_p=(2, 3) if n > 5 else (1, 2), koniec=False,
                      tlo={(n - 1, n - 1): "*", (n - 2, 0): "*"}, ile_war=4, seed=4))
    p = "POWTÓRZ ×3\n  DOPÓKI WOLNE?\n    IDŹ\n  KONIEC\n  SKRĘĆ W PRAWO\nKONIEC"
    out.append(losowa(15, "Trzy razy do klocka", "Trzy razy: idź, dopóki jest wolne, i skręć w prawo. Skarb leży tam, gdzie robot stanie.", n, n - 1, 0, "^", p,
                      kand=wszystkie(n, bez=[(n - 1, 0)]), ile_p=2, seed=5, min_kroki=n))
    p = "DOPÓKI NIE SKARB?\n  IDŹ\nKONIEC\nIDŹ, OBRÓĆ SIĘ\nDOPÓKI NIE ŚCIANA?\n  IDŹ\nKONIEC"
    out.append(losowa(16, "Skarb i z powrotem", "Idź do skarbu, weź go, obróć się i idź do ściany. Wróć na START.", n, c, 0, ">", p,
                      gw_kand=rzad(n, c, 1, n), gw_ile=1, koniec=False, ile_war=3, seed=6,
                      tlo={(c - 1, xx): "L" for xx in range(0, n, 2)}))
    return out


# ---------------------------------------------------------------- poziom 4
KART4 = "karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?\n"


def ustaw(k):
    return f"N = {k}" if k <= 6 else f"N = 6\nN + {k - 6}"


def poziom4(n):
    c = n // 2
    out = [f"### Zestaw C: Liczby rosną i maleją\n{KART4}"]
    m = (n - 1) // 2
    p = f"N = 1\nPOWTÓRZ ×{m}\n  SKRĘĆ W LEWO, IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, IDŹ, N + 1\nKONIEC"
    if n == 5:  # na małej planszy stała droga jest za łatwa bez zmiennej, więc klocek raz jest, raz nie
        p = "DOPÓKI WOLNE?\n  IDŹ, N + 1, SKRĘĆ W LEWO, IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO\nKONIEC"
        out.append(losowa(9, "Fale do klocka", "Krok w prawo, N + 1 i fala o wysokości N. Tak, dopóki przed robotem jest wolne. Skarb jest tam, gdzie robot stanie.", n, n - 1, 0, ">", p,
                          kand=[(n - 1, 3)], ile_p=(0, 1), ile_war=2, seed=9))
    else:
        out.append(stala(9, "Fale", "Każda fala jest o 1 wyższa od poprzedniej. Wysokość fali to N.", n, n - 1, 0, ">", p, lawa=1.0, seed=n + 9))
    p = f"{ustaw(n - 1)}\nDOPÓKI N > 0?\n  IDŹ ×N, SKRĘĆ W PRAWO, N − 1\nKONIEC"
    out.append(stala(10, "Ślimak", f"Pierwszy bok ma {n - 1} pól, a każdy następny o 1 mniej. Pętla kończy się sama, gdy N = 0.", n, n - 1, 0, "^", p))
    p = f"N = 1\nPOWTÓRZ ×{m}\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, N + 1\n  IDŹ ×N, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO, N + 1\nKONIEC"
    out.append(stala(11, "Choinka", "Robot idzie w dół zygzakiem, a każdy rząd jest o 1 dłuższy. Wychodzi choinka.", n, 0, c, ">", p, lawa=1.0, seed=n + 11))
    p = f"{ustaw(n - 1)}\nDOPÓKI N > 0?\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 2\nKONIEC"
    out.append(stala(12, "Kwadrat w kwadracie", "Kwadrat o boku N, krok w środek po skosie i kwadrat o 2 mniejszy.", n, n - 1, 0, "^", p))
    out.append(f"### Zestaw D: Zmierz i użyj\n{KART4}")
    p = "DOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W PRAWO\nIDŹ ×N"
    out.append(losowa(13, "Zmierz i skręć", "Idź do klocka i licz kroki w N. Potem skręć w prawo i zrób IDŹ ×N.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 0, n - 2), ile_p=1, ile_war=3, seed=13))
    p = "DOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W PRAWO\nDOPÓKI N > 0?\n  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1\nKONIEC"
    out.append(losowa(14, "Zejdź po schodach", "Wejdź na górę do klocka i licz piętra. Potem zejdź po tylu schodkach, ile było pięter.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 0, n - 2), ile_p=1, ile_war=3, seed=14))
    p = "DOPÓKI NIE SKARB?\n  IDŹ, N + 1\nKONIEC\nIDŹ, SKRĘĆ W LEWO\nIDŹ ×N"
    out.append(losowa(15, "Skarb i wieża", "Licz kroki do pierwszego skarbu. Drugi skarb leży nad nim, tyle pól w górę, ile było kroków.", n, n - 1, 0, ">", p,
                      gw_kand=rzad(n, n - 1, 2, n), gw_ile=1, ile_war=3, seed=15))
    p = "DOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nOBRÓĆ SIĘ\nDOPÓKI N > 0?\n  IDŹ, N − 2\nKONIEC"
    out.append(losowa(16, "Połowa drogi", "Idź do klocka i licz kroki. Wróć, ale tylko w połowę drogi: za każdy krok odejmij 2.", n, c, 0, ">", p,
                      kand=rzad(n, c, 3, n), ile_p=1, ile_war=3 if n > 5 else 2, seed=16, tlo={(c + 1, xx): "L" for xx in range(1, n, 2)}))
    return out


# ---------------------------------------------------------------- poziom 5
import poziom5 as P5

IDZ_ZA = """DOPÓKI NIE SKARB?
  JEŚLI WOLNE?
    IDŹ
  NIE
    JEŚLI WOLNE W LEWO?
      SKRĘĆ W LEWO
    NIE
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ"""


def poziom5(n):
    cfg = {5: dict(dl=12, war=2, drzwi=2), 7: dict(dl=21, war=3, drzwi=3), 9: dict(dl=33, war=3, drzwi=4)}[n]
    out = [f"### Zestaw C: Ścieżki i przeszkody\nkarty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A\n{P5.PYT}\n"]
    g, w = P5.korytarz(n, n * 10 + 51, cfg["dl"])
    out.append(P5.blok(9, "Długa kręta ścieżka", "Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo.", g, P5.KRETY, w))
    g, w = korytarz_za(n, n * 10 + 52, cfg["dl"])
    out.append(P5.blok(10, "Idź za ścieżką", "Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo.", g, IDZ_ZA, w))
    g, w = P5.korytarz(n, n * 10 + 53, cfg["dl"] + 2, kaluze=2 if n == 5 else 3)
    out.append(P5.blok(11, "Więcej kałuż", "Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty.", g, P5.KRETY_K, w))
    g, w = P5.przeszkody(n, n * 10 + 54, 4)
    out.append(P5.blok(12, "Nowe przeszkody", "Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A.", g, P5.PRZESZKODY, w))
    out.append(f"### Zestaw D: Nowe labirynty\nkarty: POWTÓRZ, DOPÓKI, JEŚLI\n{P5.PYT}\n")
    g, w = P5.labirynt(n, n * 100 + 55, P5.PRAWA, cfg["drzwi"], 2)
    out.append(P5.blok(13, "Nowy labirynt", "Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej.", g, P5.PRAWA, w))
    g, w = P5.labirynt(n, n * 100 + 56, P5.LEWA, cfg["drzwi"], 2)
    out.append(P5.blok(14, "Labirynt w lewo", "Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania.", g, P5.LEWA, w))
    g, w = P5.labirynt(n, n * 100 + 57, P5.PRAWA, cfg["drzwi"] + 1, cfg["war"])
    out.append(P5.blok(15, "Więcej drzwi", f"Więcej pól ? i {cfg['war']} różne labirynty. Program ten sam.", g, P5.PRAWA, w))
    g, w = P5.labirynt(n, n * 100 + 58, P5.LEWA, cfg["drzwi"] + 2, cfg["war"] + 1)
    out.append(P5.blok(16, "Największa zagadka", f"{cfg['war'] + 1} labirynty, dużo drzwi i jeden program.", g, P5.LEWA, w))
    return out


def korytarz_za(n, seed, dl):
    """kręta ścieżka dla programu IDZ_ZA (skarb raz w połowie, raz na końcu)"""
    stary = P5.KRETY
    P5.KRETY = IDZ_ZA
    try:
        return P5.korytarz(n, seed, dl)
    finally:
        P5.KRETY = stary


# ---------------------------------------------------------------- poziom 6
KART6 = "karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A\npytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?\nparametr: tak\n"


def poziom6(n):
    c = n // 2
    out = [f"### Zestaw C: Kształty na zamówienie\n{KART6}"]
    boki = {5: [2, 1, 1, 2], 7: [3, 2, 1, 3], 9: [4, 2, 3, 1]}[n]
    p = "PRZEPIS A\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  SKRĘĆ W PRAWO\nKONIEC\n" + "\n".join(liczba(k) for k in boki)
    out.append(stala(9, "Cztery kwadraty", "Przepis A to kwadrat o boku N i skręt w prawo. Cztery kwadraty różnej wielkości wokół START, jak w oknie z poziomu 3. Wróć na START.", n, c, c, "^", p,
                     lawa=1.0, param=True))
    slupki = {5: [2, 4, 1, 3], 7: [3, 5, 2, 6, 1, 4], 9: [4, 6, 2, 5, 3, 6, 1, 4]}[n]
    p = "PRZEPIS A\n  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ\nKONIEC\n" + "\n".join(liczba(k) for k in slupki)
    out.append(stala(10, "Wykres słupkowy", "Przepis A to słupek o wysokości N i krok w prawo. Na szczycie każdego słupka leży skarb.", n, n - 1, 0, ">", p,
                     gwiazdy=[(n - 1 - h, i) for i, h in enumerate(slupki)], lawa=1.0, param=True))
    zeby = {5: [3, 1], 7: [2, 5, 3], 9: [6, 3, 8, 5]}[n]
    p = "PRZEPIS A\n  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO\nKONIEC\n" + "\n".join(liczba(k) for k in zeby)
    out.append(stala(11, "Grzebień z zębami", "Przepis A to ząb o wysokości N: w górę, krok w prawo, w dół i krok w prawo. Skarby na czubkach zębów.", n, n - 1, 0, "^", p,
                     gwiazdy=sledz(pusta(n, n - 1, 0, "^"), p, True)[1] if n < 9 else [(n - 1 - h, 2 * i) for i, h in enumerate(zeby)] + [(n - 1 - h, 2 * i + 1) for i, h in enumerate(zeby)], lawa=1.0, seed=n, param=True))
    p = "PRZEPIS A\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W PRAWO\n  KONIEC\n  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\nKONIEC\n" + "\n".join(liczba(k) for k in range(n - 1, 0, -2))
    out.append(stala(12, "Ramki", "Przepis A rysuje ramkę o boku N i robi krok po skosie do środka. Każda następna ramka jest o 2 mniejsza.", n, n - 1, 0, "^", p, param=True))
    out.append(f"### Zestaw D: Zmierz i przekaż\n{KART6}")
    p = "PRZEPIS A\n  POWTÓRZ ×2\n    IDŹ ×N, SKRĘĆ W LEWO\n  KONIEC\nKONIEC\nDOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nOBRÓĆ SIĘ\nZRÓB A ×N"
    out.append(losowa(13, "Róg jak odległość", "Zmierz drogę do klocka. Obróć się i przekaż N do przepisu A: dwa boki po N pól.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 0, n - 2), ile_p=1, ile_war=3, seed=61, param=True))
    p = "PRZEPIS A\n  DOPÓKI N > 0?\n    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1\n  KONIEC\nKONIEC\nDOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W LEWO\nZRÓB A ×N"
    out.append(losowa(14, "Schody jak odległość", "Idź do klocka i licz. Potem skręć w lewo i zrób tyle schodków, ile było kroków.", n, n - 1, 0, ">", p,
                      kand=rzad(n, n - 1, 1, n), ile_p=1, ile_war=3 if n > 5 else 2, seed=62, param=True))
    p = ("PRZEPIS A\n  POWTÓRZ ×4\n    IDŹ ×N, SKRĘĆ W LEWO\n  KONIEC\nKONIEC\nDOPÓKI NIE ŚCIANA?\n  JEŚLI SKARB?\n    N + 1\n  NIE\n  KONIEC\n  IDŹ\nKONIEC\n"
         "SKRĘĆ W LEWO\nZRÓB A ×N")
    def rog(r, vis, turns):
        return [turns[-2]] if len(turns) >= 3 else []
    out.append(losowa(15, "Ile skarbów, taki kwadrat", "Policz skarby w dolnym rzędzie. Potem obejdź kwadrat o boku N w lewo do góry. Ostatni skarb leży w lewym górnym rogu kwadratu.", n, n - 1, 0, ">", p,
                      gw_kand=rzad(n, n - 1, 1, n - 1), gw_ile=(1, 2, 3), koniec=False, gw_fn=rog, ile_war=3, seed=63, param=True))
    p = "PRZEPIS A\n  DOPÓKI N > 0?\n    IDŹ ×N, SKRĘĆ W PRAWO, N − 1\n  KONIEC\nKONIEC\nDOPÓKI WOLNE?\n  IDŹ, N + 1\nKONIEC\nSKRĘĆ W PRAWO\nZRÓB A ×N"
    out.append(losowa(16, "Ślimak jak odległość", "Zmierz drogę do klocka. Przepis A to ślimak: bok N, potem N − 1 i tak do zera.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 0, n - 3), ile_p=1, ile_war=3 if n > 5 else 2, seed=64, param=True))
    return out


# ---------------------------------------------------------------- poziom 7
KC = "karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META\npytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?\nrekurencja: tak\nparametr: tak\nwymagaj: rekurencja\n"
KD = "karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META\npytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?\nrekurencja: tak\nwymagaj: rekurencja\n"

SLAD = """PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    JEŚLI WOLNE?
      IDŹ, ZRÓB A, IDŹ
    NIE
      SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
ZRÓB A"""


def korytarz_prawy(n, seed, prawo=True):
    """ścieżka w lawie, która skręca tylko w prawo (albo tylko w lewo): spirala do środka"""
    rnd = random.Random(seed)
    for _ in range(2000):
        g = [["L"] * n for _ in range(n)]
        y, x, d = n - 1, 0 if prawo else n - 1, 0
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] if prawo else [(-1, 0), (0, -1), (1, 0), (0, 1)]
        path = [(y, x)]
        ok = True
        dl = n - 1 - rnd.randint(0, 1)
        while dl >= 2:
            dy, dx = dirs[d % 4]
            for _ in range(dl):
                y, x = y + dy, x + dx
                if not (0 <= y < n and 0 <= x < n) or (y, x) in path: ok = False; break
                path.append((y, x))
            if not ok: break
            d += 1
            dl -= rnd.choice((1, 2))
        if not ok or len(path) < n + 3: continue
        # ścieżka nie może dotykać sama siebie bokiem (poza sąsiadami na ścieżce)
        idx = {c: i for i, c in enumerate(path)}
        if any(abs(idx.get((cy + a, cx + b), i) - i) > 1 for i, (cy, cx) in enumerate(path) for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1))):
            continue
        for (cy, cx) in path: g[cy][cx] = "."
        return g, path
    raise SystemExit("korytarz_prawy: nie znalazłem")


def slad(nr, tytul, opis, n, seed, prawo=True, ile_war=3):
    g, path = korytarz_prawy(n, seed, prawo)
    prog = SLAD if prawo else SLAD.replace("PRAWO", "XX").replace("LEWO", "PRAWO").replace("XX", "LEWO")
    sy, sx = path[0]
    tlo = {(yy, xx): g[yy][xx] for yy in range(n) for xx in range(n) if (yy, xx) != (sy, sx)}
    kand = path[len(path) // 3:]
    return losowa(nr, tytul, opis, n, sy, sx, "^", prog, gw_kand=kand, gw_ile=1, koniec=False, ile_war=ile_war, seed=seed, tlo=tlo, rek=True)


def poziom7(n):
    c = n // 2
    out = [f"### Zestaw C: Rekurencja rysuje\n{KC}"]
    p = "PRZEPIS A\n  JEŚLI N > 0?\n    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N\n  NIE\n  KONIEC\nKONIEC\n" + liczba(n - 1)
    out.append(stala(9, "Ślimak z rekurencji", "Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0.", n, n - 1, 0, "^", p, param=True, rek=True))
    ramie = "IDŹ" if n < 9 else "IDŹ ×2"
    p = ("PRZEPIS A\n  JEŚLI N > 0?\n    POWTÓRZ ×4\n      " + ramie + ", N − 1, ZRÓB A ×N, N + 1, OBRÓĆ SIĘ, " + ramie + ", SKRĘĆ W LEWO\n    KONIEC\n  NIE\n  KONIEC\nKONIEC\nZRÓB A ×2")
    out.append(stala(10, "Płatek śniegu", "Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START.", n, c, c, "^", p, gwiazdy="zakrety", lawa=1.0, param=True, rek=True))
    k = {5: 3, 7: 3, 9: 4}[n]
    p = ("PRZEPIS A\n  JEŚLI N > 0?\n    N − 1, ZRÓB A ×N, N + 1\n    IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO\n  NIE\n  KONIEC\nKONIEC\n"
         "SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO\n" + liczba(k)) if False else \
        ("PRZEPIS A\n  JEŚLI N > 0?\n    N − 1, ZRÓB A ×N, N + 1\n    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ\n  NIE\n  KONIEC\nKONIEC\n" + liczba(k))
    out.append(stala(11, "Słupki rosną", "Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3…", n, n - 1, 0, ">", p,
                     gwiazdy=[(n - 1 - h, h - 1) for h in range(1, k + 1)], lawa=1.0, seed=n, param=True, rek=True))
    p = ("PRZEPIS A\n  JEŚLI N > 0?\n    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ\n    N − 1, ZRÓB A ×N, N + 1\n"
         "    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ\n  NIE\n  KONIEC\nKONIEC\n" + liczba(c))
    hs = list(range(c, 0, -1)) + list(range(1, c + 1))
    out.append(stala(12, "Dolina", "Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej.", n, n - 1, 0, ">", p,
                     gwiazdy=[(n - 1 - h, i) for i, h in enumerate(hs)], lawa=1.0, seed=n + 12, param=True, rek=True))
    out.append(f"### Zestaw D: Powrót po śladach\n{KD}")
    p = "PRZEPIS A\n  JEŚLI NIE WOLNE?\n    SKRĘĆ W PRAWO, META\n  NIE\n  KONIEC\n  IDŹ, ZRÓB A, IDŹ\nKONIEC\nZRÓB A"
    out.append(losowa(13, "Za róg tyle samo", "Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę.", n, n - 1, 0, "^", p,
                      kand=kolumna(n, 0, 0, n - 2), ile_p=1, ile_war=3, seed=71))
    p = ("PRZEPIS A\n  JEŚLI WOLNE?\n    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ\n  NIE\n    OBRÓĆ SIĘ\n  KONIEC\nKONIEC\nZRÓB A")
    def szczyt(r, vis, turns):
        return [max(vis, key=lambda c: (n - 1 - c[0]) + c[1])]
    out.append(losowa(14, "Schody i z powrotem", "Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START.", n, n - 1, 0, "^", p,
                      kand=[(n - 2 - i, i) for i in range(n - 1)], ile_p=1, koniec=False, gw_fn=szczyt, ile_war=3, seed=72))
    out.append(slad(15, "Powrót po śladach", "Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START.", n, 75 + n))
    out.append(slad(16, "Ślady w lewo", "Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START.", n, 76 + n, prawo=False))
    return out


POZIOMY = {3: poziom3, 4: poziom4, 5: poziom5, 6: poziom6, 7: poziom7}


def wstaw(nr):
    path = os.path.join(ROOT, "gra", f"poziom-{nr}.md")
    text = open(path, encoding="utf-8").read()
    czesci = re.split(r"^(?=## Plansza)", text, flags=re.M)
    nowe = [czesci[0]]
    for cz in czesci[1:]:
        n = int(re.match(r"## Plansza (\d)", cz).group(1))
        cz = re.split(r"^### Zestaw C:", cz, flags=re.M)[0].rstrip("\n") + "\n\n"
        nowe.append(cz + "\n".join(POZIOMY[nr](n)) + "\n")
    open(path, "w", encoding="utf-8").write("".join(nowe))
    print("zapisano", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    import sys
    for nr in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else POZIOMY):
        wstaw(nr)
