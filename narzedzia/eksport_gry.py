#!/usr/bin/env python3
"""Eksportuje gry poziomu 1 z tresc/plansze-poziom-1-*.md do gra/gry.js (dla wersji online, index.html).

Użycie: python3 narzedzia/eksport_gry.py   (albo: make online)
Bierze tylko gry, które da się zagrać na ekranie: z robotem, skarbem i rozwiązaniem w bloku
rozwiazanie, bez pól "?" i bez programu podanego z góry. Każde rozwiązanie sprawdza symulatorem.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "narzedzia"))
import sprawdz  # noqa: E402

def main():
    games, skipped = [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, "tresc", "plansze-poziom-1-*.md"))):
        m = re.search(r"plansze-poziom-1-(\d)x\d-([a-z])\.md$", path)
        size, zestaw = int(m.group(1)), m.group(2).upper()
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
            sol_lines = [l for l in sol.group(1).splitlines() if l.strip()]
            prog = sprawdz.parse_program(sol_lines)
            if any(n[0] != "cmd" for n in prog):
                skipped += 1; continue
            end, _ = sprawdz.run([" ".join(r) for r in rows], prog)
            start = next((y + 1, x + 1) for y, r in enumerate(rows) for x, t in enumerate(r) if t in "^>v<")
            if back and end != start:
                sys.exit(f"{path}: {head}: rozwiązanie nie wraca na START")
            games.append({
                "id": f"{size}-{int(num)}", "size": size, "zestaw": zestaw, "nr": int(num),
                "tytul": title, "opis": desc, "plansza": [" ".join(r) for r in rows],
                "powrot": back,
                "rozwiazanie": [[name, n] for _, name, n in prog],
            })
    games.sort(key=lambda g: (g["size"], g["nr"]))
    out = os.path.join(ROOT, "gra", "gry.js")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Plik generowany przez narzedzia/eksport_gry.py z tresc/plansze-poziom-1-*.md. Nie edytuj ręcznie.\n")
        f.write("window.GRY = ")
        json.dump(games, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(f"Zapisano {len(games)} gier do gra/gry.js (pominięto {skipped}).")

if __name__ == "__main__":
    main()
