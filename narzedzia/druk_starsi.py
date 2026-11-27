#!/usr/bin/env python3
"""Robi wersję do druku poziomów 3-7 gry online: z gra/poziom-<N>.md powstają
tresc/plansze-starsi-poziom-<N>-<S>x<S>.md (po 4 gry na stronę). Potem `python3 narzedzia/drukuj.py`
zamienia je na PDF i HTML w druk/. Pliki w tresc/ są generowane: zmieniaj gra/poziom-<N>.md.

Użycie: python3 narzedzia/druk_starsi.py   (robi to też `make druk`)
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DLA = {3: "dla 8-latka", 4: "dla 12-latka", 5: "dla początkującego programisty",
       6: "dla średniego programisty", 7: "trudny"}
SLOWO = {"*": "S", ".": "·", "#": "#", "L": "L", "K": "K"}
WSTEP = ("Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. "
         "„Masz tylko N kart” liczy wszystkie karty poleceń, także KONIEC i NIE, ale nie liczby. "
         "Pola ?: dorosły przed każdą próbą kładzie na nich to, co podaje jeden z wariantów "
         "(pola ? czytamy jak książkę: od lewej do prawej, z góry na dół; S skarb, · puste, # klocek, L lawa, K kałuża). "
         "Program ma zadziałać w każdym wariancie.")
WSTEP_KOD = ("Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: "
             "wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, "
             "pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.")


def gry(path):
    text = open(path, encoding="utf-8").read()
    size, zest = None, {}
    for blok in re.split(r"^(?=#{2,4} )", text, flags=re.M):
        head = blok.splitlines()[0] if blok.strip() else ""
        if head.startswith("## "):
            size = int(re.search(r"(\d+)", head).group(1))
        elif head.startswith("### "):
            zest = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in blok.splitlines()[1:] if ":" in l)}
        elif head.startswith("#### "):
            num, title = re.match(r"^#### (\d+)\.\s*(.*)$", head).groups()
            desc = " ".join(l.strip() for l in blok.split("```")[0].splitlines()[1:] if l.strip())
            board = re.search(r"```plansza\n(.*?)```", blok, re.S).group(1)
            sol = re.search(r"```rozwiazanie\n(.*?)```", blok, re.S).group(1)
            u = re.search(r"```ustawienia\n(.*?)```", blok, re.S)
            ust = dict(l.split(":", 1) for l in u.group(1).splitlines() if ":" in l) if u else {}
            ust = {**zest, **{k.strip(): v.strip() for k, v in ust.items()}}
            # ustawienia zestawu (np. warianty nie, ale parametr tak) - tylko te, które wpływają na opis
            yield size, int(num), title, desc, board, sol, ust


def main():
    for path in sorted(glob.glob(os.path.join(ROOT, "gra", "poziom-*.md"))):
        nr = int(re.search(r"poziom-(\d+)\.md$", path).group(1))
        if nr < 3:
            continue
        po_rozm = {}
        for g in gry(path):
            po_rozm.setdefault(g[0], []).append(g)
        for size, lista in sorted(po_rozm.items()):
            stron = (len(lista) + 3) // 4
            out = []
            for s in range(stron):
                out.append(f"# Plansze {size} × {size} dla starszych, poziom {nr} ({DLA.get(nr, '')}) ({s + 1}/{stron})\n")
                if s == 0:
                    out.append((WSTEP_KOD if nr >= 5 else WSTEP) + "\n")
                for _, num, title, desc, board, sol, ust in lista[s * 4:(s + 1) * 4]:
                    out.append(f"### {num}. {title}")
                    opis = desc
                    if "warianty" in ust:
                        w = [" ".join(SLOWO.get(c, c) for c in x) for x in ust["warianty"].split()]
                        opis += " Warianty pól ?: " + "; ".join(f"{i + 1}) {x}" for i, x in enumerate(w)) + "."
                    if ust.get("wymagaj") == "rekurencja":
                        opis += " Przepis A musi wołać sam siebie."
                    out.append(opis)
                    out.append("```plansza\n" + board + "```")
                    out.append(("```kod\n" if nr >= 5 else "```rozwiazanie\n") + sol + "```\n")
                if s < stron - 1:
                    out.append("---\n")
            dst = os.path.join(ROOT, "tresc", f"plansze-starsi-poziom-{nr}-{size}x{size}.md")
            with open(dst, "w", encoding="utf-8") as f:
                f.write("\n".join(out))
            print("zapisano", os.path.relpath(dst, ROOT))


if __name__ == "__main__":
    main()
