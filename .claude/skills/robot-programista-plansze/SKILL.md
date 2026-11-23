---
name: robot-programista-plansze
description: Dodawanie lub zmienianie gier, plansz, kart i instrukcji w repo 6latek-programuje (gra Robot i Programista) - format plików .md, sprawdzenie rozwiązań symulatorem, wydruk PDF i merge do main.
---

# Plansze i karty „Robot i Programista” w repo

Repo: `twoznia/6latek-programuje`. Najpierw pobierz aktualny `main`, bo inne wątki też tu pracują.

## Układ repo

- `tresc/*.md` to źródła: `instrukcja.md`, `karty.md` oraz `plansze-poziom-<poziom>-<plansza>[-<zestaw>].md`, np. `plansze-poziom-1-5x5-a.md`, `plansze-poziom-2-3-5x5.md` albo `plansze-poziom-4-9x9.md`. Plansze są 5 × 5, 7 × 7 i 9 × 9.
- `druk/` zawiera wygenerowane PDF i HTML pod tą samą nazwą. Oba commitujemy.
- `narzedzia/drukuj.py` zamienia `.md` na HTML i PDF (sam Python 3; PDF przez Chrome lub Chromium). `narzedzia/styl.css` to wygląd.
- `narzedzia/sprawdz.py` to symulator robota, który sprawdza rozwiązania.
- `Makefile`: `make` tworzy wszystkie wydruki, `make sprawdz` sprawdza rozwiązania.
- README ma tabelę plików. Przy nowym pliku dopisz wiersz.

## Format pliku z planszami

```md
# Plansze 5 × 5, poziom 1, zestaw D (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 49. Tytuł gry
Jedno lub dwa krótkie zdania dla dziecka.
```plansza
. . * . .
. . L . .
. . ^ . .
. . . . .
. . . . .
```
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2
```

---
```

- Tytuł strony zaczyna się od „Plansze”. Wtedy każde `###` jest osobną kartą gry, po 4 na stronę. Plik ma 4 strony oddzielone `---`, czyli 16 gier. Gry są numerowane dalej w obrębie danej planszy i poziomu.
- Symbole planszy: `.` to puste pole, `^ > v <` to robot patrzący w daną stronę, `*` to skarb, `#` to klocek, `L` to lawa, `K` to kałuża, a `?` to pole z niespodzianką.
- Polecenia: IDŹ, SKRĘĆ W PRAWO, SKRĘĆ W LEWO, OBRÓĆ SIĘ, SKOCZ, POWTÓRZ ×n lub ×∞, KONIEC, JEŚLI <LAWA?|KAŁUŻA?|SKARB?|ŚCIANA?>, TAK:, NIE:, STOP, META, PRZEPIS A/B … KONIEC (definicja przepisu, poziom 4) i ZRÓB A/B ×n (wywołanie). META w przepisie kończy tylko przepis. Liczba ×1 się nie pojawia, bo okienko karty ma domyślnie narysowaną kartę liczby 1 („raz”).
- Program z pętlą lub warunkiem zapisuje się w osobnych liniach z wcięciem o 2 spacje:
  ```
  POWTÓRZ ×∞
    JEŚLI SKARB?
      TAK: IDŹ, META
    KONIEC
    IDŹ
  KONIEC
  ```
- Program pokazany dziecku (zadania „gdzie skończy robot?” i „znajdź błąd”) idzie do bloku `program`, a odpowiedź do akapitu `**Rozwiązanie:** …`. Dwa programy do porównania to `program A` i `program B`.
- Karty do wycięcia są w `tresc/karty.md`, w blokach `karty`, np. `IDŹ ×6`, `LICZBY 1-6 ×2`, `LAWA ×4`, `ROBOT ×1`.

## Zasady ruchu (tak działa symulator)

- IDŹ: 1 pole do przodu. SKOCZ: 2 pola do przodu, tylko nad kałużą (pole tuż przed robotem musi być `K`).
- Nie wolno wejść na klocek, lawę, kałużę ani poza planszę. Skok nad pustym polem, skarbem, lawą albo klockiem to błąd. Kałużę można (i trzeba) przeskoczyć.
- SKRĘĆ i OBRÓĆ SIĘ to obrót w miejscu, bez kroku.
- Warunek JEŚLI dotyczy pola tuż przed robotem. ŚCIANA oznacza koniec planszy.
- STOP przerywa najbliższą pętlę (break), a META kończy cały program (return).
- Gra jest rozwiązana, gdy robot zebrał (stanął na) wszystkie skarby.

## Kroki

1. Pobierz `main` i utwórz gałąź.
2. Zaprojektuj gry od najłatwiejszej. Mieszaj rodzaje zadań: dojście, kilka skarbów, lawa, kałuża, robot patrzący w różne strony, „gdzie skończy robot?”, „znajdź błąd”, najkrótszy program i jedna gra do wymyślenia przez dziecko na końcu zestawu. Na planszy 5 × 5 programy mają 1–8 kart, na 7 × 7 do ok. 11 kart, a na 9 × 9 do ok. 14 kart (8 kroków to IDŹ ×6, IDŹ ×2). Liczby w okienkach są od 1 do 6.
3. Uruchom `make sprawdz`. Każde `BŁĄD` popraw. Gry pominięte (`pomijam`: pola `?`, zadania bez bloku `rozwiazanie`) prześledź ręcznie, pole po polu, i zapisz wynik w `**Rozwiązanie:**`.
4. Uruchom `make` i obejrzyj wydruki jako obrazki: `pdftoppm -r 50 -png druk/<plik>.pdf /tmp/podglad`. Sprawdź, czy:
   - każda strona z grami ma 4 gry i nic nie wychodzi poza stronę;
   - nie ma prawie pustych stron;
   - na kartach nie ma szarych podpisów;
   - strony z kartami poleceń są poziome.
5. Uzupełnij tabelę w README, jeśli doszedł plik.
6. Zrób commit (bez plików tymczasowych), push, PR i merge do `main` (merge commit, bez usuwania gałęzi, na której opiera się inny otwarty PR). Na koniec wyślij Tomkowi PDF-y w wątku.
