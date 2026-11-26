#!/usr/bin/env python3
"""Symulator gry online dla poziomów 3 i wyżej. Działa na płaskiej liście kart, tak jak gra/gra.js.

Karty (token [nazwa, argument]):
  IDŹ, SKRĘĆ W PRAWO, SKRĘĆ W LEWO, OBRÓĆ SIĘ, SKOCZ  - argument: liczba albo "N"
  POWTÓRZ n|N … KONIEC, DOPÓKI pytanie … KONIEC, JEŚLI pytanie … [NIE …] KONIEC
  N = liczba, N + liczba, N − liczba                   - zmienna N (poziom 4+)
  ZRÓB A [×n]                                          - przepis A (z "parametr": ZRÓB A ×n daje N = n w przepisie)
  META                                                 - w przepisie: wróć z przepisu, w programie: koniec
Pytania: LAWA?, KAŁUŻA?, SKARB?, ŚCIANA?, KLOCEK?, WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, N > 0?, N = 0?
oraz złożone: "NIE X", "X I Y", "X LUB Y" (LUB łączy słabiej niż I).
"""
import re

KIER = "^>v<"
DXY = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
MAX_KROKOW = 600
ODPOWIEDZ = {"LAWA?": "L", "KAŁUŻA?": "K", "SKARB?": "*", "ŚCIANA?": "SCIANA", "KLOCEK?": "#"}
OTWIERA = ("POWTÓRZ", "DOPÓKI", "JEŚLI")
RUCH = ("IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ")


class Blad(Exception):
    pass


class _Meta(Exception):
    pass


def czytaj_program(lines):
    """Tekst rozwiązania (wcięcia tylko dla czytelności) -> (program, przepis) jako płaskie listy kart."""
    prog, przepis, cel, w_przepisie = [], [], None, False
    cel = prog
    for raw in lines:
        if not raw.strip():
            continue
        ind = len(raw) - len(raw.lstrip(" "))
        t = raw.strip()
        if ind == 0 and t == "PRZEPIS A":
            cel, w_przepisie = przepis, True; continue
        if w_przepisie and ind == 0:
            if t == "KONIEC":
                cel, w_przepisie = prog, False; continue
            cel, w_przepisie = prog, False
        cel.extend(karty_z_linii(t))
    return prog, przepis


def _liczba(s):
    s = s.strip()
    return "N" if s == "N" else int(s)


def karty_z_linii(t):
    for k in ("POWTÓRZ", "DOPÓKI", "JEŚLI"):
        if t.startswith(k + " ") or t == k:
            reszta = t[len(k):].strip()
            if k == "POWTÓRZ":
                return [[k, _liczba(reszta.lstrip("×"))]]
            return [[k, reszta]]
    if t in ("NIE", "KONIEC"):
        return [[t, 1]]
    out = []
    for part in [p.strip() for p in t.split(",") if p.strip()]:
        m = re.match(r"^N\s*([=+−-])\s*(\d+)$", part)
        if m:
            op = {"=": "N =", "+": "N +", "-": "N −", "−": "N −"}[m.group(1)]
            out.append([op, int(m.group(2))]); continue
        m = re.match(r"^(.*?)\s*×\s*(\d+|N)$", part)
        if m:
            out.append([m.group(1), _liczba(m.group(2))])
        else:
            out.append([part, 1])
    return out


def drzewo(lista):
    korzen = []
    stos = [{"w": None, "cel": korzen}]
    for c in lista:
        top = stos[-1]
        k = c[0]
        if k in ("POWTÓRZ", "DOPÓKI"):
            w = {"t": "petla" if k == "POWTÓRZ" else "dopoki", "c": c, "cialo": []}
            top["cel"].append(w); stos.append({"w": w, "cel": w["cialo"]})
        elif k == "JEŚLI":
            w = {"t": "jesli", "c": c, "tak": [], "nie": []}
            top["cel"].append(w); stos.append({"w": w, "cel": w["tak"]})
        elif k == "NIE":
            if top["w"] and top["w"]["t"] == "jesli":
                top["cel"] = top["w"]["nie"]
        elif k == "KONIEC":
            if len(stos) > 1:
                stos.pop()
        else:
            top["cel"].append({"t": "karta", "c": c})
    if len(stos) > 1:
        raise Blad("brak karty KONIEC")
    return korzen


class Robot:
    def __init__(self, plansza, przepis=None, parametr=False, rekurencja=False):
        self.g = [r.split() if isinstance(r, str) else list(r) for r in plansza]
        self.n = len(self.g)
        (self.y, self.x), self.d = next(((y, x), t) for y, r in enumerate(self.g) for x, t in enumerate(r) if t in KIER)
        self.start = (self.y, self.x)
        self.gwiazdy = {(y, x) for y, r in enumerate(self.g) for x, t in enumerate(r) if t == "*"}
        self.zebrane = set()
        self.klucze = self.suma = self.kroki = 0
        self.N = 0
        self.przepis = drzewo(przepis or [])
        self.parametr, self.rekurencja = parametr, rekurencja
        self.glebokosc = 0

    def pole(self, y, x):
        if not (0 <= y < self.n and 0 <= x < self.n):
            return "SCIANA"
        return self.g[y][x]

    def przed(self, obrot=0):
        d = KIER[(KIER.index(self.d) + obrot) % 4]
        dy, dx = DXY[d]
        return self.pole(self.y + dy, self.x + dx)

    def atom(self, q):
        q = q.strip()
        if q.startswith("NIE "):
            return not self.atom(q[4:])
        if q in ODPOWIEDZ:
            return self.przed() == ODPOWIEDZ[q]
        if q == "WOLNE?":
            return self.przed() not in ("L", "K", "#", "SCIANA", "D")
        if q == "WOLNE W LEWO?":
            return self.przed(3) not in ("L", "K", "#", "SCIANA", "D")
        if q == "WOLNE W PRAWO?":
            return self.przed(1) not in ("L", "K", "#", "SCIANA", "D")
        if q == "N > 0?":
            return self.N > 0
        if q == "N = 0?":
            return self.N == 0
        raise Blad(f"nieznane pytanie {q!r}")

    def pytaj(self, q):
        return any(all(self.atom(a) for a in czesc.split(" I ")) for czesc in q.split(" LUB "))

    def ile(self, arg):
        return self.N if arg == "N" else arg

    def tik(self):
        self.kroki += 1
        if self.kroki > MAX_KROKOW:
            raise Blad("robot jest zmęczony (za dużo kroków)")

    def krok(self, k):
        if k == "SKRĘĆ W PRAWO":
            self.d = KIER[(KIER.index(self.d) + 1) % 4]; return
        if k == "SKRĘĆ W LEWO":
            self.d = KIER[(KIER.index(self.d) + 3) % 4]; return
        if k == "OBRÓĆ SIĘ":
            self.d = KIER[(KIER.index(self.d) + 2) % 4]; return
        dy, dx = DXY[self.d]
        ile = 2 if k == "SKOCZ" else 1
        if ile == 2 and self.pole(self.y + dy, self.x + dx) != "K":
            raise Blad(f"skok bez kałuży z {(self.y + 1, self.x + 1)}")
        y, x = self.y + ile * dy, self.x + ile * dx
        t = self.pole(y, x)
        if t in ("L", "K", "#", "SCIANA"):
            raise Blad(f"wejście na {t} w {(y + 1, x + 1)}")
        if t == "D":
            if not self.klucze:
                raise Blad(f"drzwi bez klucza w {(y + 1, x + 1)}")
            self.klucze -= 1; self.g[y][x] = "o"
        self.y, self.x = y, x
        if t == "*":
            self.zebrane.add((y, x))
        elif t == "@":
            self.klucze += 1; self.g[y][x] = "."
        elif t in "123456789":
            self.suma += int(t); self.g[y][x] = "."

    def wykonaj(self, wezly):
        for w in wezly:
            c = w["c"]
            if w["t"] == "petla":
                for _ in range(self.ile(c[1])):
                    self.tik(); self.wykonaj(w["cialo"])
            elif w["t"] == "dopoki":
                while self.pytaj(c[1]):
                    self.tik(); self.wykonaj(w["cialo"])
            elif w["t"] == "jesli":
                self.wykonaj(w["tak"] if self.pytaj(c[1]) else w["nie"])
            else:
                k, arg = c
                if k == "ZRÓB A":
                    n = self.ile(arg)
                    for _ in range(1 if self.parametr else n):
                        self.glebokosc += 1
                        if self.glebokosc > 40:
                            raise Blad("przepis woła sam siebie bez końca")
                        stare = self.N
                        if self.parametr:
                            self.N = n
                        try:
                            self.wykonaj(self.przepis)
                        except _Meta:
                            pass
                        if self.parametr:
                            self.N = stare
                        self.glebokosc -= 1
                elif k == "META":
                    raise _Meta
                elif k == "N =":
                    self.tik(); self.N = arg
                elif k == "N +":
                    self.tik(); self.N += arg
                elif k == "N −":
                    self.tik(); self.N -= arg
                elif k in RUCH:
                    for _ in range(self.ile(arg)):
                        self.tik(); self.krok(k)
                else:
                    raise Blad(f"nieznana karta {k!r}")

    def uruchom(self, program):
        try:
            self.wykonaj(drzewo(program))
        except _Meta:
            pass
        return self


def ile_kart(program, przepis):
    return len(program) + len(przepis)
