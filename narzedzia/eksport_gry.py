#!/usr/bin/env python3
"""Eksportuje gry do gra/gry.js (dla wersji online, index.html).

Użycie: python3 narzedzia/eksport_gry.py   (albo: make online)

Poziom 1: gry z tresc/plansze-poziom-1-*.md, które da się zagrać na ekranie: z robotem, skarbem
i rozwiązaniem w bloku rozwiazanie, bez pól "?" i bez programu podanego z góry.
Poziom 2: gry z gra/poziom-2.md (POWTÓRZ, klucze i drzwi, monety i limit kart, JEŚLI z polem ?,
przepis A). Każde rozwiązanie jest sprawdzane symulatorem, a przy polach "?" na każdym wariancie.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "narzedzia"))
import sprawdz  # noqa: E402

PODSTAWOWE = ["IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ"]
PYTANIA = ["LAWA?", "KAŁUŻA?", "SKARB?", "ŚCIANA?"]


def tokeny(nodes):
    """Drzewo z sprawdz.parse_program -> płaska lista kart, tak jak leżą na stole."""
    out = []
    for nd in nodes:
        if nd[0] == "cmd":
            out.append([nd[1], nd[2]])
        elif nd[0] == "loop":
            out += [["POWTÓRZ", nd[1]]] + tokeny(nd[2]) + [["KONIEC", 1]]
        elif nd[0] == "if":
            out += [["JEŚLI", nd[1]]] + tokeny(nd[2]) + [["NIE", 1]] + tokeny(nd[3]) + [["KONIEC", 1]]
        elif nd[0] == "def":
            pass
        else:
            sys.exit(f"nieobsługiwany węzeł {nd!r}")
    return out


class Blad(Exception):
    pass


BLEDY = []


def sprawdz_gre(where, plansza, prog, warianty, suma, powrot):
    """Uruchamia rozwiązanie na każdym wariancie planszy. Kończy skrypt przy błędzie."""
    pyt = [(y, x) for y, r in enumerate(plansza) for x, t in enumerate(r.split()) if t == "?"]
    if pyt and not warianty:
        raise Blad(f"{where}: pola ? bez wariantów")
    for w in (warianty or [""]):
        if len(w) != len(pyt):
            raise Blad(f"{where}: wariant {w!r} ma inną liczbę pól niż plansza ({len(pyt)})")
        rows = [r.split() for r in plansza]
        for (y, x), t in zip(pyt, w):
            rows[y][x] = t
        board = [" ".join(r) for r in rows]
        info = {}
        try:
            end, _ = sprawdz.run(board, prog, info=info)
        except sprawdz.Fail as e:
            raise Blad(f"{where}: wariant {w!r}: {e}")
        if suma is not None and info["suma"] != suma:
            raise Blad(f"{where}: wariant {w!r}: suma {info['suma']}, a ma być {suma}")
        start = next((y + 1, x + 1) for y, r in enumerate(rows) for x, t in enumerate(r) if t in "^>v<")
        if powrot and end != start:
            raise Blad(f"{where}: rozwiązanie nie wraca na START")


def poziom1():
    games, skipped = [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, "tresc", "plansze-poziom-1-*.md"))):
        m = re.search(r"plansze-poziom-1-(\d)x\d(?:-([a-z]))?\.md$", path)
        size, zestaw = int(m.group(1)), (m.group(2) or "").upper()
        text = open(path, encoding="utf-8").read()
        for sec in re.split(r"^### ", text, flags=re.M)[1:]:
            head = sec.splitlines()[0].strip()
            num, title = re.match(r"^(\d+)\.\s*(.*)$", head).groups()
            board = re.search(r"```plansza\n(.*?)```", sec, re.S)
            sol = re.search(r"```rozwiazanie\n(.*?)```", sec, re.S)
            if not board or not sol or "```program" in sec:
                skipped += 1; continue
            rows = [l.split() for l in board.group(1).splitlines() if l.strip()]
            flat = [t for r in rows for t in r]
            if "?" in flat or "*" not in flat or not any(t in "^>v<" for t in flat):
                skipped += 1; continue
            desc = " ".join(l.strip() for l in sec.split("```plansza")[0].splitlines()[1:] if l.strip())
            back = "wróć na start" in desc.lower()
            prog = sprawdz.parse_program([l for l in sol.group(1).splitlines() if l.strip()])
            if any(n[0] != "cmd" for n in prog):
                skipped += 1; continue
            plansza = [" ".join(r) for r in rows]
            try:
                sprawdz_gre(f"{path}: {head}", plansza, prog, None, None, back)
            except Blad as e:
                BLEDY.append(str(e))
            games.append({
                "id": f"{size}-{int(num)}", "poziom": 1, "size": size, "zestaw": zestaw, "nr": int(num),
                "tytul": title, "opis": desc, "plansza": plansza, "powrot": back,
                "karty": PODSTAWOWE,
                "rozwiazanie": {"program": tokeny(prog)},
            })
    return games, skipped


def poziom2():
    path = os.path.join(ROOT, "gra", "poziom-2.md")
    text = open(path, encoding="utf-8").read()
    games = []
    size = zestaw = nazwa = None
    karty_zestawu = []
    for blok in re.split(r"^(?=#{2,4} )", text, flags=re.M):
        head = blok.splitlines()[0] if blok.strip() else ""
        if head.startswith("## "):
            size = int(re.search(r"(\d)", head).group(1))
        elif head.startswith("### "):
            m = re.match(r"### Zestaw ([A-Z]): (.*)$", head)
            zestaw, nazwa = m.group(1), m.group(2).strip()
            k = re.search(r"^karty: (.*)$", blok, re.M)
            karty_zestawu = [x.strip() for x in k.group(1).split(",")] if k else []
        elif head.startswith("#### "):
            num, title = re.match(r"^#### (\d+)\.\s*(.*)$", head).groups()
            where = f"{path}: {size}x{size} {head[5:]}"
            board = re.search(r"```plansza\n(.*?)```", blok, re.S)
            sol = re.search(r"```rozwiazanie\n(.*?)```", blok, re.S)
            if not board or not sol:
                sys.exit(f"{where}: brak planszy albo rozwiązania")
            rows = [l.split() for l in board.group(1).splitlines() if l.strip()]
            if len(rows) != size or any(len(r) != size for r in rows):
                sys.exit(f"{where}: plansza nie ma rozmiaru {size} × {size}")
            plansza = [" ".join(r) for r in rows]
            ust = {}
            u = re.search(r"```ustawienia\n(.*?)```", blok, re.S)
            if u:
                for l in u.group(1).splitlines():
                    if ":" in l:
                        a, b = l.split(":", 1); ust[a.strip()] = b.strip()
            desc = " ".join(l.strip() for l in blok.split("```")[0].splitlines()[1:] if l.strip())
            back = "wróć na start" in desc.lower()
            sol_lines = [l for l in sol.group(1).splitlines() if l.strip()]
            prog = sprawdz.parse_program(sol_lines)
            warianty = ust["warianty"].split() if "warianty" in ust else None
            suma = int(ust["suma"]) if "suma" in ust else None
            limit = int(ust["limit"]) if "limit" in ust else None
            try:
                sprawdz_gre(where, plansza, prog, warianty, suma, back)
            except Blad as e:
                BLEDY.append(str(e))
            przepis = next((nd[2] for nd in prog if nd[0] == "def"), None)
            rozw = {"program": tokeny(prog)}
            if przepis is not None:
                rozw["przepis"] = tokeny(przepis)
            ile = len(rozw["program"]) + len(rozw.get("przepis", []))
            if limit is not None and ile > limit:
                sys.exit(f"{where}: rozwiązanie ma {ile} kart, a limit to {limit}")
            flat = [t for r in rows for t in r]
            if "*" not in flat and suma is None and not (warianty and any("*" in w for w in warianty)):
                sys.exit(f"{where}: nie ma skarbu ani sumy do zebrania")
            karty = PODSTAWOWE + [k for k in karty_zestawu if k]
            if "pytania" in ust:
                pyt = ust["pytania"].split(",")
            else:
                pyt = PYTANIA
            g = {
                "id": f"2-{size}-{int(num)}", "poziom": 2, "size": size, "zestaw": zestaw, "zestawNazwa": nazwa,
                "nr": int(num), "tytul": title, "opis": desc, "plansza": plansza, "powrot": back,
                "karty": karty, "rozwiazanie": rozw,
            }
            if warianty: g["warianty"] = warianty
            if suma is not None: g["suma"] = suma
            if limit is not None: g["limit"] = limit
            if "JEŚLI" in karty: g["pytania"] = [p.strip() for p in pyt]
            games.append(g)
    return games


def main():
    g1, skipped = poziom1()
    g2 = poziom2()
    if BLEDY:
        sys.exit("BŁĘDY:\n" + "\n".join(BLEDY))
    games = g1 + g2
    games.sort(key=lambda g: (g["poziom"], g["size"], g["nr"]))
    ids = [g["id"] for g in games]
    if len(ids) != len(set(ids)):
        sys.exit("powtórzone numery gier: " + ", ".join(sorted({i for i in ids if ids.count(i) > 1})))
    out = os.path.join(ROOT, "gra", "gry.js")
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Plik generowany przez narzedzia/eksport_gry.py z tresc/plansze-poziom-1-*.md i gra/poziom-2.md. Nie edytuj ręcznie.\n")
        f.write("window.GRY = ")
        json.dump(games, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(f"Zapisano {len(games)} gier do gra/gry.js: poziom 1 {len(g1)} (pominięto {skipped}), poziom 2 {len(g2)}.")
    for s in (5, 7, 9):
        print(f"  {s}x{s}: poziom 1 {sum(1 for g in g1 if g['size'] == s)}, poziom 2 {sum(1 for g in g2 if g['size'] == s)}")


if __name__ == "__main__":
    main()
