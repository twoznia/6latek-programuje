#!/usr/bin/env python3
"""Gry „Słowa z liter” i „Liczenie na trasie” (poziom 1, plansze 5 × 5 do 13 × 13).

Robi pliki tresc/plansze-poziom-1-<S>x<S>-slowa.md i tresc/plansze-poziom-1-<S>x<S>-liczby.md
(5x5, 7x7 i 9x9 po 16 gier na 4 strony, 11x11 i 13x13 po 8 gier na 2 strony). Plansze 5x5 i 7x7
są wpisane niżej ręcznie, a 9x9, 11x11 i 13x13 losuje funkcja losuj() ze stałym ziarnem (z listy słów
i sum, z lawą i kałużami; zostają plansze z programem o długości z zakresu DLUGOSC). Rozwiązanie (najkrótszy program z kart
poziomu 1) znajduje przeszukiwanie wszerz. Potem: make sprawdz, make online, make druk.

    python3 narzedzia/generatory/slowa_liczby.py

Pola: małe litery (bez v, bo v to robot) to litery do zebrania, cyfry 1-9 to monety.
Ustawienia gry: slowo (litery trzeba zebrać po kolei, inna litera to błąd), ukryte (słowo jest
zagadką, nie ma go w opisie), suma (monety mają dać dokładnie tyle).
"""
import os, random, sys
from collections import deque

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
KIER = "^>v<"
DXY = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
LIMIT = {5: 8, 7: 11, 9: 14, 11: 17, 13: 20}
DLUGOSC = {9: (5, 14), 11: (7, 17), 13: (8, 20)}


def rozwiaz(rows, slowo=None, suma=None, powrot=False, maks=None):
    """Najmniej kart IDŹ/SKRĘĆ/OBRÓĆ/SKOCZ (liczby 1-6). Zwraca (lista kart, droga zebranych pól)."""
    n = len(rows)
    zb = [(y, x) for y in range(n) for x in range(n) if rows[y][x] == "*" or rows[y][x].isdigit()
          or (rows[y][x].isalpha() and rows[y][x].islower() and rows[y][x] != "v")]
    (sy, sx), sd = next(((y, x), rows[y][x]) for y in range(n) for x in range(n) if rows[y][x] in KIER)
    gwiazdy = sum(1 << i for i, p in enumerate(zb) if rows[p[0]][p[1]] == "*")

    def wejdz(y, x, m, lit, s):
        """Robot wchodzi na pole. None = nie wolno."""
        if not (0 <= y < n and 0 <= x < n) or rows[y][x] in ("L", "K", "#"):
            return None
        if (y, x) not in zb:
            return m, lit, s
        i = zb.index((y, x))
        if m >> i & 1:
            return m, lit, s
        t = rows[y][x]
        if t.isdigit():
            if suma is None or s + int(t) > suma:
                return None
            return m | 1 << i, lit, s + int(t)
        if t != "*":
            if slowo is None or lit >= len(slowo) or t.upper() != slowo[lit]:
                return None
            return m | 1 << i, lit + 1, s
        return m | 1 << i, lit, s

    start = (sy, sx, sd, 0, 0, 0)
    prev = {start: None}
    glebokosc = {start: 0}
    q = deque([start])
    while q:
        st = q.popleft()
        y, x, d, m, lit, s = st
        if (m & gwiazdy) == gwiazdy and (slowo is None or lit == len(slowo)) and (suma is None or s == suma) \
                and (not powrot or (y, x) == (sy, sx)):
            prog = []
            while prev[st]:
                st, karta = prev[st]
                prog.append(karta)
            return prog[::-1]
        if maks is not None and glebokosc[st] >= maks:
            continue
        ruchy = []
        dy, dx = DXY[d]
        cy, cx, cm, cl, cs = y, x, m, lit, s
        for k in range(1, 7):
            cy, cx = cy + dy, cx + dx
            w = wejdz(cy, cx, cm, cl, cs)
            if w is None:
                break
            cm, cl, cs = w
            ruchy.append(((cy, cx, d, cm, cl, cs), ("IDŹ", k)))
        for obr, nazwa in ((1, "SKRĘĆ W PRAWO"), (3, "SKRĘĆ W LEWO"), (2, "OBRÓĆ SIĘ")):
            ruchy.append(((y, x, KIER[(KIER.index(d) + obr) % 4], m, lit, s), (nazwa, 1)))
        cy, cx, cm, cl, cs = y, x, m, lit, s
        for k in range(1, 7):
            if not (0 <= cy + dy < n and 0 <= cx + dx < n and rows[cy + dy][cx + dx] == "K"):
                break
            cy, cx = cy + 2 * dy, cx + 2 * dx
            w = wejdz(cy, cx, cm, cl, cs)
            if w is None:
                break
            cm, cl, cs = w
            ruchy.append(((cy, cx, d, cm, cl, cs), ("SKOCZ", k)))
        for s2, karta in ruchy:
            if s2 not in prev:
                prev[s2] = (st, karta)
                glebokosc[s2] = glebokosc[st] + 1
                q.append(s2)
    return None


def monety_po_drodze(rows, prog):
    """Kolejne monety, na które wchodzi robot (do zapisu „3 + 4 = 7”)."""
    g = [r[:] for r in rows]
    n = len(g)
    (y, x), d = next(((y, x), g[y][x]) for y in range(n) for x in range(n) if g[y][x] in KIER)
    out = []
    for k, ile in prog:
        if k.startswith("SKRĘĆ") or k == "OBRÓĆ SIĘ":
            d = KIER[(KIER.index(d) + {"SKRĘĆ W PRAWO": 1, "SKRĘĆ W LEWO": 3, "OBRÓĆ SIĘ": 2}[k] * ile) % 4]
            continue
        krok = 2 if k == "SKOCZ" else 1
        for _ in range(ile):
            y, x = y + krok * DXY[d][0], x + krok * DXY[d][1]
            if g[y][x].isdigit():
                out.append(g[y][x]); g[y][x] = "."
    return out


def tekst(prog):
    return ", ".join(k if ile == 1 else f"{k} ×{ile}" for k, ile in prog)


# ------------------------------------------------------------------ gry
# (tytuł, opis, plansza, ustawienia). Ustawienia: slowo, ukryte, suma.
# Bez planszy z rozwiązaniem: gra do wymyślenia (tylko w druku), rozwiązanie w "przyklad".

SLOWA_5 = [
    ("Kot na prostej", "Zbierz litery po kolei i ułóż słowo KOT.", """
. . t . .
. . o . .
. . k . .
. . . . .
. . ^ . .""", {"slowo": "KOT"}),
    ("Dom za rogiem", "Ułóż słowo DOM. Najpierw D, potem O, na końcu M.", """
. . . . .
. . . . .
d o m . .
. . . . .
^ . . . .""", {"slowo": "DOM"}),
    ("Las w dół", "Robot patrzy w dół. Ułóż słowo LAS.", """
. . v . .
. . l . .
. . a . .
. . s . .
. . . . .""", {"slowo": "LAS"}),
    ("Oko", "W słowie OKO są dwie litery O. Zbierz O, K i drugie O.", """
. . . . .
o k o . .
. . . . .
. . . . .
> . . . .""", {"slowo": "OKO"}),
    ("Nos i pułapka", "Ułóż słowo NOS. Litera K tu nie pasuje, nie wchodź na nią!", """
. . s . .
. . k . .
. n o . .
. ^ . . .
. . . . .""", {"slowo": "NOS"}),
    ("Sok za lawą", "Ułóż słowo SOK. Obejdź lawę.", """
. . . . .
s L o . .
. L . . .
. . k . .
^ . . . .""", {"slowo": "SOK"}),
    ("Mama", "Ułóż słowo MAMA: M, A, M, A. Uważaj, od której litery zaczynasz!", """
. m a . .
. . . . .
. a m . .
. . . . .
. ^ . . .""", {"slowo": "MAMA"}),
    ("Tata", "Ułóż słowo TATA. Robot patrzy w lewo.", """
t a . . .
. . . . .
. . . . .
. . . . .
a t . . <""", {"slowo": "TATA"}),
    ("Lis za kałużą", "Ułóż słowo LIS. Kałużę trzeba przeskoczyć.", """
. . s . .
. . i . .
. . K . .
. . l . .
. . ^ . .""", {"slowo": "LIS"}),
    ("Mak", "Ułóż słowo MAK. Są tu też litery, które nie pasują.", """
. o . k .
. m . a .
. . . . .
. . t . .
. . ^ . .""", {"slowo": "MAK"}),
    ("Zagadka: miau", "Zagadka! Mruczy, mówi miau i łapie myszy. Zbierz litery tego zwierzęcia po kolei.", """
. . . . .
. o . . .
. . . t .
. k . . .
. ^ . . .""", {"slowo": "KOT", "ukryte": "tak"}),
    ("Zagadka: w wodzie", "Zagadka! Pływa w wodzie i ma płetwy. Zbierz litery po kolei.", """
. . . . a
. y . . b
. . . . .
. r . . .
. ^ . . .""", {"slowo": "RYBA", "ukryte": "tak"}),
    ("Zagadka: bzzz", "Zagadka! Lata, bzyczy i może użądlić. Ma paski. Zbierz litery po kolei.", """
. . . . .
. . a . .
. s L . .
. . . . .
. o < . .""", {"slowo": "OSA", "ukryte": "tak"}),
    ("Ser i powrót", "Ułóż słowo SER i wróć na START.", """
. . . . .
. s . e .
. . . . .
. . . r .
. ^ . . .""", {"slowo": "SER"}),
    ("Lody", "Ułóż słowo LODY. Lawa stoi na drodze.", """
. . . y .
. l o d .
. L . . .
. . . . .
. ^ . . .""", {"slowo": "LODY"}),
    ("Twoje słowo", "Ułóż z tych liter słowo, jakie chcesz: KOT, TOM, SOK albo MAK. Powiedz je Programiście, a on niech ułoży program.", """
. . m . .
. a . s .
. . k . .
. o . t .
. . ^ . .""", {"przyklad": {"slowo": "KOT"}}),
]

SLOWA_7 = [
    ("Auto", "Ułóż słowo AUTO.", """
. . . o . . .
. . . t . . .
. . . u . . .
. . . a . . .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"slowo": "AUTO"}),
    ("Sowa", "Ułóż słowo SOWA. Robot patrzy w prawo.", """
. . . . . . .
. . . . . . .
. s o w a . .
. . . . . . .
. . . . . . .
> . . . . . .
. . . . . . .""", {"slowo": "SOWA"}),
    ("Nogi do góry", "Ułóż słowo NOGA. Litery idą zakrętem.", """
. . . . . . .
. . a g . . .
. . . o . . .
. . . n . . .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"slowo": "NOGA"}),
    ("Tort", "Ułóż słowo TORT. Są w nim dwie litery T.", """
. . . . . . .
. t . . . r .
. . . . . . .
. . . . . . .
. o . . . t .
. . . . . . .
^ . . . . . .""", {"slowo": "TORT"}),
    ("Robot", "Ułóż słowo ROBOT. Litera K tu nie pasuje.", """
. . . . . . .
. r o b . . .
. . k o . . .
. . . t . . .
. . . . . . .
. ^ . . . . .
. . . . . . .""", {"slowo": "ROBOT"}),
    ("Kotek", "Ułóż słowo KOTEK. Obejdź lawę.", """
. . . . . . .
. k o t e k .
. L L L L . .
. . . . . . .
. . . . . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "KOTEK"}),
    ("Domek", "Ułóż słowo DOMEK. Przeskocz kałuże.", """
. . . . . . .
. . . k . . .
. . . e . . .
. . . K . . .
. . . m . . .
. d o . . . .
. ^ . . . . .""", {"slowo": "DOMEK"}),
    ("Lampa", "Ułóż słowo LAMPA. Zacznij od L, a nie od A!", """
. . . . . . .
. l a m p a .
. . . . . . .
. a . . . . .
. . . . . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "LAMPA"}),
    ("Motyl", "Ułóż słowo MOTYL. Robot patrzy w dół.", """
. . . v . . .
. . . m o . .
. . . . t . .
. . L . y . .
. . L l . . .
. . . . . . .
. . . . . . .""", {"slowo": "MOTYL"}),
    ("Lalka", "Ułóż słowo LALKA. Litery L są aż dwie.", """
. . . . . . .
. . a . l . .
. . . . . . .
. l . . . k .
. . . . . . .
. . . a . . .
. . . ^ . . .""", {"slowo": "LALKA"}),
    ("Zagadka: hau", "Zagadka! Mówi hau, merda ogonem i pilnuje domu. Zbierz litery po kolei.", """
. . . . . . .
. . i . . e .
. . . . . . .
. p . . . . s
. . . . . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "PIES", "ukryte": "tak"}),
    ("Zagadka: tik-tak", "Zagadka! Robi tik-tak i pokazuje, która godzina. Zbierz litery po kolei.", """
. . . . . . .
. z . e . g .
. . . . . . .
. . . . . a .
. . . . . . .
. . . r . . .
. ^ . . . . .""", {"slowo": "ZEGAR", "ukryte": "tak"}),
    ("Zagadka: huu-huu", "Zagadka! W nocy mówi huu-huu i ma duże oczy. Zbierz litery po kolei.", """
. . . . . . .
. . . . . . .
. a L w . . .
. . L . . . .
. s . o . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "SOWA", "ukryte": "tak"}),
    ("Balon i powrót", "Ułóż słowo BALON i wróć na START.", """
. . . . . . .
. b a . . . .
. . l . . . .
. . o n . . .
. . . . . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "BALON"}),
    ("Rakieta", "Ułóż długie słowo RAKIETA. Uważaj na lawę i kałużę.", """
. . . . . . .
. r a k i e .
. . . L . t .
. . . . . a .
. . . K . . .
. . . . . . .
. ^ . . . . .""", {"slowo": "RAKIETA"}),
    ("Twoje słowo", "Ułóż z tych liter słowo, jakie chcesz: LATO, TATA, MAK albo KOT. Powiedz je Programiście, a on niech ułoży program.", """
. . . . . . .
. l . a . t .
. . . . . . .
. k . o . e .
. . . . . . .
. m . a . t .
. . . ^ . . .""", {"przyklad": {"slowo": "LATO"}}),
]

LICZBY_5 = [
    ("Dwie monety", "Zbierz monety. Ile razem? Ma być 5.", """
. . . . .
. . 3 . .
. . 2 . .
. . . . .
. . ^ . .""", {"suma": 5}),
    ("Trzy monety", "Zbierz trzy monety. Razem ma być 6.", """
. . . . .
. . . . .
> 1 2 3 .
. . . . .
. . . . .""", {"suma": 6}),
    ("Która droga?", "Lewa czy prawa droga? Razem ma być dokładnie 7.", """
. . * . .
. 4 . 3 .
. 4 . 4 .
. . . . .
. . ^ . .""", {"suma": 7}),
    ("Wszystkie monety", "Zbierz wszystkie monety. Razem jest 8.", """
. . . . .
. 2 . . .
. 2 . 2 .
. . . . .
. 2 ^ . .""", {"suma": 8}),
    ("Do dziesięciu", "Zbierz monety, które dają razem 10. Obejdź lawę.", """
. . . . .
. 5 L 5 .
. . L . .
. . L . .
. . ^ . .""", {"suma": 10}),
    ("Za dużo!", "Razem ma być 4. Jedna moneta da za dużo. Omiń ją.", """
. . . . .
. . 6 . .
. 3 . . .
. 1 . . .
. ^ . . .""", {"suma": 4}),
    ("Trzy do dziesięciu", "Razem ma być 10. Wystarczą trzy monety.", """
. . . . .
. 5 . . .
. . 1 . .
. 3 . 2 .
. ^ . . .""", {"suma": 10}),
    ("Monety za kałużą", "Przeskocz kałużę. Razem ma być 6.", """
. . 4 . .
. . . . .
. . 2 . .
. . K . .
. . ^ . .""", {"suma": 6}),
    ("Monety i skarb", "Najpierw zbierz 7, potem idź po skarb.", """
. . . . *
. . . . .
. 3 . 4 .
. . . . .
^ . . . .""", {"suma": 7}),
    ("Dziewięć i powrót", "Razem ma być 9. Potem wróć na START.", """
. . . . .
. 4 . 5 .
. . . . .
. . . . .
. ^ . . .""", {"suma": 9}),
    ("Małe monety", "Razem ma być 4. Duże monety omijaj.", """
. 1 . 6 .
. . . . .
. 1 5 . .
. 2 . . .
. ^ . . .""", {"suma": 4}),
    ("Cztery monety", "Zbierz cztery monety. Razem ma być 10.", """
. . . . .
. 1 2 . .
. . 3 . .
. . 4 . .
. . ^ . .""", {"suma": 10}),
    ("W dół po monety", "Robot patrzy w dół. Razem ma być 8.", """
. . v . .
. . 2 . .
. 3 3 . .
. . 6 . .
. . . . .""", {"suma": 8}),
    ("Labirynt z lawą", "Razem ma być 10. Obejdź lawę.", """
. . . . .
. 4 L . .
. . L 3 .
. 3 L . .
^ . . . .""", {"suma": 10}),
    ("Sześć dwiema drogami", "Razem ma być 6. Są dwie dobre drogi. Którą wybierzesz?", """
. . . . .
. 2 . 1 .
. 4 . 5 .
. . . . .
. . ^ . .""", {"suma": 6}),
    ("Twoja suma", "Wymyśl liczbę od 3 do 10 i powiedz ją Programiście. On ułoży program, który zbierze dokładnie tyle.", """
. 1 . 2 .
. . . . .
. 3 . 4 .
. . . . .
. . ^ . .""", {"przyklad": {"suma": 5}}),
]

LICZBY_7 = [
    ("Prosto po dziesięć", "Zbierz monety. Razem ma być 10.", """
. . . . . . .
. . . 4 . . .
. . . . . . .
. . . 3 . . .
. . . 3 . . .
. . . . . . .
. . . ^ . . .""", {"suma": 10}),
    ("Rząd monet", "Razem ma być 9.", """
. . . . . . .
. . . . . . .
. . . . . . .
> 2 . 3 . 4 .
. . . . . . .
. . . . . . .
. . . . . . .""", {"suma": 9}),
    ("Która kolumna?", "Razem ma być 8. Wybierz dobrą kolumnę.", """
. . . . . . .
. 5 . 2 . 3 .
. . . . . . .
. 4 . 6 . 6 .
. . . . . . .
. . . . . . .
^ . . . . . .""", {"suma": 8}),
    ("Za lawą", "Razem ma być 10. Obejdź lawę.", """
. . . . . . .
. . . 6 . . .
. . L L L . .
. . . . . . .
. . . 4 . . .
. . . . . . .
. . . ^ . . .""", {"suma": 10}),
    ("Skoki po monety", "Przeskocz kałuże. Razem ma być 7.", """
. . . 4 . . .
. . . K . . .
. . . 2 . . .
. . . K . . .
. . . 1 . . .
. . . . . . .
. . . ^ . . .""", {"suma": 7}),
    ("Omiń dużą", "Razem ma być 6. Jedna moneta da za dużo.", """
. . . . . . .
. . . 4 . . .
. . . . . . .
. . . 5 . . .
. . . 2 . . .
. . . . . . .
. . . ^ . . .""", {"suma": 6}),
    ("Monety i skarb", "Zbierz 10, a potem idź po skarb.", """
. . . . . . *
. . . . . . .
. 5 . . . 5 .
. . . . . . .
. . . . . . .
. . . . . . .
^ . . . . . .""", {"suma": 10}),
    ("Dziesięć i powrót", "Razem ma być 10. Potem wróć na START.", """
. . . . . . .
. . . . . . .
. . 4 . 6 . .
. . . . . . .
. . . . . . .
. . . . . . .
. . ^ . . . .""", {"suma": 10}),
    ("Ponad dziesięć", "Dla starszych: razem ma być 12.", """
. . . . . . .
. . . 6 . . .
. . . . . . .
. . . 6 . . .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"suma": 12}),
    ("Piętnaście", "Razem ma być 15. Trzy monety.", """
. . . . . . .
. 5 . . . . .
. 5 . . . . .
. 5 . . . . .
. . . . . . .
. . . . . . .
. ^ . . . . .""", {"suma": 15}),
    ("Czternaście w rzędzie", "Robot patrzy w lewo. Razem ma być 14.", """
. . . . . . .
. . . . . . .
. . . . . . .
. 3 9 . 2 . <
. . . . . . .
. . . . . . .
. . . . . . .""", {"suma": 14}),
    ("Jedenaście", "Razem ma być 11. Nie wszystkie monety pasują.", """
. . . . . . .
. 9 . . . 8 .
. . . . . . .
. 2 . . . 4 .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"suma": 11}),
    ("Dwadzieścia", "Razem ma być 20. Zbierz wszystkie monety.", """
. . . . . . .
. 5 . . . 5 .
. . . . . . .
. 5 . . . 5 .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"suma": 20}),
    ("Szesnaście za lawą", "Razem ma być 16. Obejdź lawę.", """
. . . . . . .
. 8 . . . . .
. L L L . . .
. . . 8 . . .
. . L L L . .
. . . . . . .
. ^ . . . . .""", {"suma": 16}),
    ("Trzynaście i kałuża", "Razem ma być 13. Przeskocz kałużę.", """
. . . . . . .
. . 6 . 7 . .
. . K . . . .
. . 7 . . . .
. . . . . . .
. . . . . . .
. . ^ . . . .""", {"suma": 13}),
    ("Twoja suma", "Wymyśl liczbę od 5 do 20 i powiedz ją Programiście. On ułoży program, który zbierze dokładnie tyle.", """
. . . . . . .
. 2 . 5 . 3 .
. . . . . . .
. 6 . 1 . 4 .
. . . . . . .
. . . . . . .
. . . ^ . . .""", {"przyklad": {"suma": 7}}),
]

# ------------------------------------------------------------------ duże plansze (losowane)
# słowo albo (słowo, zagadka); zagadka = słowo ukryte, bez liter-pułapek
SLOWA_9 = ["ROBOT", "BALON", "ZEGAR", ("ZEBRA", "Koń w czarno-białe paski.", "paski"), "BANAN", "PIRAT",
           ("PAPUGA", "Kolorowy ptak, który powtarza słowa.", "gadający ptak"), "KAKTUS", "TULIPAN",
           ("MARCHEW", "Pomarańczowa, rośnie w ziemi i lubi ją królik.", "obiad królika"), "POMIDOR", "TRAKTOR",
           ("PINGWIN", "Czarno-biały ptak. Nie lata, ale świetnie pływa.", "ptak na lodzie"), "SAMOLOT",
           ("KROKODYL", "Jest zielony, ma dużo zębów i pływa w rzece.", "zęby w rzece")]
SLOWA_11 = ["KANAPKA", "DINOZAUR", ("PARASOL", "Chroni przed deszczem.", "deszcz"), "MOTOCYKL",
            ("BIEDRONKA", "Czerwona z czarnymi kropkami. Siada na listkach.", "kropki"), "HELIKOPTER",
            ("TRUSKAWKA", "Czerwony owoc z pestkami na zewnątrz.", "czerwony owoc")]
SLOWA_13 = ["KOMPUTER", ("KANGUR", "Skacze i nosi dziecko w torbie.", "torba"), "KALKULATOR",
            ("TELEFON", "Dzwoni, a przez niego można rozmawiać z babcią.", "dzwoni"), "ASTRONAUTA",
            ("BIBLIOTEKA", "Tu pożycza się książki.", "książki"), "PROGRAMISTA"]
SUMY_9 = [9, 10, 12, 11, 13, 14, 15, 12, 16, 17, 18, 15, 19, 20, 20]
SUMY_11 = [14, 16, 18, 20, 22, 25, 30]
SUMY_13 = [18, 20, 24, 26, 30, 35, 40]
INNE = "abdeiklmnoprstuyz"


def sciezka(rnd, g, znaki, size):
    """Kładzie znaki po kolei, każdy 1-3 pola od poprzedniego (prosto w jedną stronę), żeby droga nie była za długa."""
    for _ in range(50):
        zajete = []
        y, x = rnd.randrange(size - 2), rnd.randrange(size)
        if g[y][x] != ".":
            continue
        zajete.append((y, x))
        ok = True
        for _ in znaki[1:]:
            for _ in range(30):
                dy, dx = rnd.choice(list(DXY.values()))
                k = rnd.randint(1, 3)
                ny, nx = y + dy * k, x + dx * k
                if 0 <= ny < size - 1 and 0 <= nx < size and g[ny][nx] == "." and (ny, nx) not in zajete:
                    y, x = ny, nx; zajete.append((y, x)); break
            else:
                ok = False; break
        if ok:
            for (y, x), z in zip(zajete, znaki):
                g[y][x] = z
            return True
    return False


def losuj(size, rodzaj, lista):
    """Losowe plansze z listy słów albo sum. Ostatnia gra to gra do wymyślenia."""
    rnd = random.Random(f"{size}-{rodzaj}")
    lo, hi = DLUGOSC[size]
    gry = []
    for nr, co in enumerate(lista):
        trudnosc = nr / max(1, len(lista) - 1)  # od 0 (łatwa) do 1 (trudna)
        for proba in range(150):
            g = [["."] * size for _ in range(size)]
            sx = rnd.randrange(size)
            sd = "^" if trudnosc < 0.3 or rnd.random() < 0.6 else rnd.choice("><")
            g[size - 1][sx] = sd
            wolne = [(y, x) for y in range(size) for x in range(size) if g[y][x] == "."]
            rnd.shuffle(wolne)
            lawa = int(size * size * (0.04 + 0.08 * trudnosc))
            kaluze = rnd.randint(0, 1 + int(3 * trudnosc))
            for _ in range(lawa):
                y, x = wolne.pop(); g[y][x] = "L"
            for _ in range(kaluze):
                y, x = wolne.pop(); g[y][x] = "K"
            ust = {}
            if rodzaj == "slowa":
                slowo, zagadka = (co, None) if isinstance(co, str) else co[:2]
                if not sciezka(rnd, g, slowo.lower(), size):
                    continue
                wolne = [p for p in wolne if g[p[0]][p[1]] == "."]
                pulapki = 0 if zagadka else rnd.randint(1, 2 + int(2 * trudnosc))
                for _ in range(pulapki):
                    y, x = wolne.pop(); g[y][x] = rnd.choice(INNE if rnd.random() < 0.5 else slowo.lower())
                ust = {"slowo": slowo, "ukryte": "tak"} if zagadka else {"slowo": slowo}
            else:
                cel = co
                ile = rnd.randint(2, 3) if cel <= 12 else rnd.randint(3, 5)
                ile = max(ile, -(-cel // 7))  # średnio najwyżej 7 na monetę, żeby dało się dobrać
                while True:
                    wybrane = [rnd.randint(1, 9) for _ in range(ile - 1)]
                    reszta = cel - sum(wybrane)
                    if 1 <= reszta <= 9:
                        wybrane.append(reszta); break
                dodatkowe = [rnd.randint(1, 9) for _ in range(rnd.randint(2, 3))]
                if not sciezka(rnd, g, "".join(map(str, wybrane)), size):
                    continue
                wolne = [p for p in wolne if g[p[0]][p[1]] == "."]
                for v in dodatkowe:
                    y, x = wolne.pop(); g[y][x] = str(v)
                ust = {"suma": cel}
            rows = [r[:] for r in g]
            prog = rozwiaz(rows, ust.get("slowo"), ust.get("suma"), maks=hi)
            if prog is None or not (lo + int((hi - lo) * 0.4 * trudnosc) <= len(prog) <= hi):
                continue
            break
        else:
            sys.exit(f"{size}x{size} {rodzaj} {co}: nie udało się wylosować planszy")
        print(f"  losuję {size}x{size} {co}: próba {proba + 1}, {len(prog)} kart", flush=True)
        plansza = "\n".join(" ".join(r) for r in rows)
        przeszkody = []
        if any("L" in r for r in rows): przeszkody.append("Obejdź lawę")
        if any("K" in r for r in rows): przeszkody.append("przeskocz kałuże" if przeszkody else "Przeskocz kałuże")
        p = (" i ".join(przeszkody) + ".") if przeszkody else ""
        if rodzaj == "slowa":
            if "ukryte" in ust:
                gry.append((f"Zagadka: {co[2]}", f"Zagadka! {co[1]} Zbierz litery po kolei. {p}".strip(), plansza, ust))
            else:
                gry.append((co.capitalize(), f"Ułóż słowo {co}. Nie każda litera pasuje. {p}".strip(), plansza, ust))
        else:
            gry.append((f"Razem {co}", f"Razem ma być {co}. Nie wszystkie monety pasują. {p}".strip(), plansza, ust))
    # gra do wymyślenia: litery albo monety bez przeszkód
    g = [["."] * size for _ in range(size)]
    g[size - 1][size // 2] = "^"
    miejsca = [(y, x) for y in range(1, size - 1, 2) for x in range(1, size, 2)]
    rnd.shuffle(miejsca)
    if rodzaj == "slowa":
        for (y, x), l in zip(miejsca, "kotdomlasmapa"):
            g[y][x] = l
        gry.append(("Twoje słowo", "Ułóż z tych liter słowo, jakie chcesz: KOT, DOM, LAS, MAPA, LAMPA albo SOK. Powiedz je Programiście, a on niech ułoży program.",
                    "\n".join(" ".join(r) for r in g), {"przyklad": {"slowo": "LAMPA"}}))
    else:
        for (y, x), v in zip(miejsca, "253948176"):
            g[y][x] = v
        cel = {9: 15, 11: 20, 13: 25}[size]
        gry.append(("Twoja suma", f"Wymyśl liczbę od 10 do {cel + 10} i powiedz ją Programiście. On ułoży program, który zbierze dokładnie tyle.",
                    "\n".join(" ".join(r) for r in g), {"przyklad": {"suma": cel}}))
    return gry


WSTEP_SLOWA = ("Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Robot zbiera literę, gdy na niej stanie. "
               "Litery trzeba zbierać po kolei, tak jak w słowie. Na literę, która teraz nie pasuje, nie wolno wejść. "
               "Rozwiązanie na dole karty można przed grą zagiąć.")
WSTEP_LICZBY = ("Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Robot zbiera monetę, gdy na niej stanie. "
                "Dodaj liczby z zebranych monet. Razem ma być dokładnie tyle, ile mówi zadanie. "
                "Rozwiązanie na dole karty można przed grą zagiąć.")


def plik(size, rodzaj, gry, pierwszy):
    nazwa = {"slowa": "słowa", "liczby": "liczby"}[rodzaj]
    out, bledy = [], []
    stron = len(gry) // 4
    for s in range(stron):
        out.append(f"# Plansze {size} × {size}, poziom 1: {nazwa} ({s + 1}/{stron})\n")
        if s == 0:
            out.append((WSTEP_SLOWA if rodzaj == "slowa" else WSTEP_LICZBY) + "\n")
        for i, (tytul, opis, plansza, ust) in enumerate(gry[s * 4:(s + 1) * 4]):
            nr = pierwszy + s * 4 + i
            rows = [l.split() for l in plansza.strip().splitlines()]
            if len(rows) != size or any(len(r) != size for r in rows):
                bledy.append(f"{size}x{size} {nr}: plansza nie ma rozmiaru {size}"); continue
            out.append(f"### {nr}. {tytul}\n{opis}")
            out.append("```plansza\n" + "\n".join(" ".join(r) for r in rows) + "\n```")
            if "przyklad" in ust:
                pr = ust["przyklad"]
                prog = rozwiaz(rows, pr.get("slowo"), pr.get("suma"))
                if prog is None:
                    bledy.append(f"{size}x{size} {nr} {tytul}: przykład się nie da"); continue
                co = pr.get("slowo") or " + ".join(monety_po_drodze(rows, prog)) + f" = {pr['suma']}"
                out.append(f"**Rozwiązanie:** Na przykład {co}: {tekst(prog)}. {'Każde słowo' if 'slowo' in pr else 'Każda liczba'} ma inną drogę.\n")
                continue
            powrot = "wróć na start" in opis.lower()
            prog = rozwiaz(rows, ust.get("slowo"), ust.get("suma"), powrot)
            if prog is None:
                bledy.append(f"{size}x{size} {nr} {tytul}: nie da się rozwiązać"); continue
            if len(prog) > LIMIT[size]:
                bledy.append(f"{size}x{size} {nr} {tytul}: rozwiązanie ma {len(prog)} kart (najwyżej {LIMIT[size]})")
            u = "\n".join(f"{k}: {v}" for k, v in ust.items())
            out.append("```ustawienia\n" + u + "\n```")
            out.append(("```rozwiazanie tekst\n" if size >= 11 else "```rozwiazanie\n") + tekst(prog) + "\n```")
            if "suma" in ust:
                m = monety_po_drodze(rows, prog)
                out.append(f"Monety: {' + '.join(m)} = {ust['suma']}." + "\n")
            elif ust.get("ukryte"):
                out.append(f"Słowo: {ust['slowo']}.\n")
            else:
                out.append("")
            print(f"  {size}x{size} {nr:3d} {tytul:24s} {len(prog):2d} kart: {tekst(prog)}")
        if s < stron - 1:
            out.append("---\n")
    dst = os.path.join(ROOT, "tresc", f"plansze-poziom-1-{size}x{size}-{rodzaj}.md")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")
    return bledy


def main():
    bledy = []
    bledy += plik(5, "slowa", SLOWA_5, 97)
    bledy += plik(5, "liczby", LICZBY_5, 113)
    bledy += plik(7, "slowa", SLOWA_7, 97)
    bledy += plik(7, "liczby", LICZBY_7, 113)
    bledy += plik(9, "slowa", losuj(9, "slowa", SLOWA_9), 65)
    bledy += plik(9, "liczby", losuj(9, "liczby", SUMY_9), 81)
    bledy += plik(11, "slowa", losuj(11, "slowa", SLOWA_11), 1)
    bledy += plik(11, "liczby", losuj(11, "liczby", SUMY_11), 9)
    bledy += plik(13, "slowa", losuj(13, "slowa", SLOWA_13), 1)
    bledy += plik(13, "liczby", losuj(13, "liczby", SUMY_13), 9)
    if bledy:
        sys.exit("BŁĘDY:\n" + "\n".join(bledy))


if __name__ == "__main__":
    main()
