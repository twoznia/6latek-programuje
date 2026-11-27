"""Duże plansze 11 × 11 i 13 × 13 w poziomach 5, 6 i 7 gry online (po 8 gier na planszę).

Gry robią te same funkcje co zestawy C i D w druga.py, tylko na większej planszy.
Tu dostają numery 1-8 i nazwy zestawów A i B. W grze online te plansze są tylko na komputerze.
Uruchamiaj PO druga.py (kolejność: poziom5.py ... poziom7.py, druga.py, duze.py), potem make online:
    python3 narzedzia/generatory/duze.py && make online
Skrypt można uruchamiać wiele razy: najpierw usuwa stare sekcje 11 × 11 i 13 × 13.
"""
import os, re, sys
import druga

ROOT = druga.ROOT
DUZE = (11, 13)


def sekcja(nr, n):
    tekst = "\n".join(druga.POZIOMY[nr](n))
    tekst = tekst.replace("### Zestaw C:", "### Zestaw A:").replace("### Zestaw D:", "### Zestaw B:")
    tekst = re.sub(r"^#### (\d+)\.", lambda m: f"#### {int(m.group(1)) - 8}.", tekst, flags=re.M)
    return f"## Plansza {n} × {n}\n\n{tekst}\n"


def wstaw(nr):
    path = os.path.join(ROOT, "gra", f"poziom-{nr}.md")
    text = open(path, encoding="utf-8").read()
    czesci = re.split(r"^(?=## Plansza)", text, flags=re.M)
    zostaw = [c for c in czesci if not re.match(r"## Plansza (\d+)", c) or int(re.match(r"## Plansza (\d+)", c).group(1)) not in DUZE]
    zostaw[-1] = zostaw[-1].rstrip("\n") + "\n\n"
    open(path, "w", encoding="utf-8").write("".join(zostaw) + "\n".join(sekcja(nr, n) for n in DUZE))
    print("zapisano", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    for nr in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else (5, 6, 7)):
        wstaw(nr)
