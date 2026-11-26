import os
"""Pomocnik do projektowania gier: auto(size, start, dir, prog, ...) -> blok markdown gry."""
import sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import symulator as S

def sledz(board, prog_text, param=False, rek=False):
    prog, przepis = S.czytaj_program(prog_text.strip("\n").splitlines())
    r = S.Robot(board, przepis, param, rek)
    visited, turns = [], []
    orig = r.krok
    def krok(k):
        orig(k)
        if k in ("IDŹ", "SKOCZ"): visited.append((r.y, r.x))
        else: turns.append((r.y, r.x))
    r.krok = krok
    r.uruchom(prog)
    return r, visited, turns, len(prog) + len(przepis)

def pusta(n, y, x, d):
    b = [["."] * n for _ in range(n)]
    b[y][x] = d
    return b

def auto(nr, tytul, opis, n, y, x, d, prog, gwiazdy="zakrety", lawa=0.0, klocki=0.0, seed=1, limit=None,
         extra=None, powrot=False, ustaw=None, param=False, rek=False, zostaw=()):
    b = pusta(n, y, x, d)
    for (yy, xx), t in (extra or {}).items():
        b[yy][xx] = t
    r, vis, turns, ile = sledz(b, prog, param, rek)
    path = set(vis) | {(y, x)}
    if gwiazdy == "zakrety":
        st = set(turns) - {(y, x)}
        st.add((r.y, r.x)) if (r.y, r.x) != (y, x) else None
    elif gwiazdy == "koniec":
        st = {(r.y, r.x)}
    else:
        st = set(gwiazdy)
    st -= set(zostaw)
    rnd = random.Random(seed)
    for yy in range(n):
        for xx in range(n):
            if (yy, xx) in path or b[yy][xx] != ".":
                continue
            v = rnd.random()
            if v < lawa: b[yy][xx] = "L"
            elif v < lawa + klocki: b[yy][xx] = "#"
    for (yy, xx) in st:
        if b[yy][xx] == ".": b[yy][xx] = "*"
    lim = limit if limit is not None else ile
    u = [f"limit: {lim}"] + ([ustaw] if ustaw else [])
    if powrot and "wróć na START" not in opis:
        opis += " Wróć na START."
    md = f"#### {nr}. {tytul}\n{opis} Masz tylko {lim} {'karty' if lim in (2,3,4) else 'kart'}.\n```plansza\n" + \
         "\n".join(" ".join(row) for row in b) + "\n```\n```ustawienia\n" + "\n".join(u) + "\n```\n```rozwiazanie\n" + prog.strip("\n") + "\n```\n"
    return md, ile
