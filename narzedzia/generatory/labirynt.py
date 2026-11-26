import os
import random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import symulator as S

def perfekcyjny(n, seed):
    """n nieparzyste; komórki na parzystych współrzędnych, ściany '#'."""
    rnd = random.Random(seed)
    g = [["#"] * n for _ in range(n)]
    cells = [(y, x) for y in range(0, n, 2) for x in range(0, n, 2)]
    start = (n - 1, 0)
    g[start[0]][start[1]] = "."
    stos, seen = [start], {start}
    while stos:
        y, x = stos[-1]
        nb = [(y + dy, x + dx, dy, dx) for dy, dx in ((-2, 0), (2, 0), (0, -2), (0, 2))
              if 0 <= y + dy < n and 0 <= x + dx < n and (y + dy, x + dx) not in seen]
        if not nb:
            stos.pop(); continue
        ny, nx, dy, dx = rnd.choice(nb)
        g[y + dy // 2][x + dx // 2] = "."; g[ny][nx] = "."
        seen.add((ny, nx)); stos.append((ny, nx))
    return g

def uruchom(g, prog_text, przepis=None):
    prog, prz = S.czytaj_program(prog_text.strip().splitlines())
    r = S.Robot(g, prz)
    r.uruchom(prog)
    return r
