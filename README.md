# 6latek programuje

**Robot i Programista** to zabawa ruchowa na podłodze, bez komputera, dla dwóch osób. Jedna osoba (**Programista**) układa program z wydrukowanych kart, a druga (**Robot**) chodzi po planszy z taśmy malarskiej i wykonuje polecenia. Potem zamiana ról. Gra uczy 6-latka myślenia jak programista: sekwencji, pętli, warunków (if / then / else), przerywania (break / return) i funkcji (przepisy). Przy okazji dziecko czyta krótkie słowa i liczy.

## Gra online

Otwórz [`index.html`](index.html) w przeglądarce (wystarczy podwójne kliknięcie, internet nie jest potrzebny). To strona startowa gry na ekranie: wybór planszy 5 × 5, 7 × 7 albo 9 × 9, lista gier poziomu 1 i gra. Dziecko dotyka kart IDŹ, SKRĘĆ W PRAWO, SKRĘĆ W LEWO, OBRÓĆ SIĘ i SKOCZ, dokłada liczbę „ile razy” i naciska START. Program można poprawiać: dotknięcie karty w programie ją zaznacza, nowa karta wstawia się za zaznaczoną (▶ to początek), liczba zmienia się w zaznaczonej karcie, a ✕ ją usuwa. Robot idzie po planszy, a przy błędzie mówi, co się stało (lawa, kałuża, klocek, koniec planszy, skok bez kałuży). Za każdą rozwiązaną grę jest gwiazdka, zapamiętywana w przeglądarce. Karty można też czytać na głos.

Gry pochodzą z plików `tresc/plansze-poziom-1-*.md`. Po zmianie plansz uruchom `make online` (albo `python3 narzedzia/eksport_gry.py`), żeby odświeżyć `gra/gry.js`. Skrypt pomija gry, których nie da się zagrać na ekranie (pola „?”, program podany z góry), a każde rozwiązanie sprawdza symulatorem.

## Pliki

Każdy plik ma źródło w Markdown w katalogu [`tresc/`](tresc/) i gotowy wydruk (PDF i HTML) w katalogu [`druk/`](druk/), pod tą samą nazwą.

| Plik | Co zawiera | Strony | Źródło | Do druku |
|---|---|---|---|---|
| instrukcja | zasady gry dla dwojga, poziomy 1–4, rodzaje gier, zabawy bez przygotowania, matematyka | 8 | [instrukcja.md](tresc/instrukcja.md) | [PDF](druk/instrukcja.pdf) · [HTML](druk/instrukcja.html) |
| karty | wszystkie karty: polecenia, liczby, pola na podłogę, plakietki ról, karty poziomów 2, 3 i 4 | 19 | [karty.md](tresc/karty.md) | [PDF](druk/karty.pdf) · [HTML](druk/karty.html) |
| plansze-poziom-1-5x5-a | gry 1–16, poziom 1, plansza 5 × 5 | 4 | [md](tresc/plansze-poziom-1-5x5-a.md) | [PDF](druk/plansze-poziom-1-5x5-a.pdf) · [HTML](druk/plansze-poziom-1-5x5-a.html) |
| plansze-poziom-1-5x5-b | gry 17–32, poziom 1, plansza 5 × 5 | 4 | [md](tresc/plansze-poziom-1-5x5-b.md) | [PDF](druk/plansze-poziom-1-5x5-b.pdf) · [HTML](druk/plansze-poziom-1-5x5-b.html) |
| plansze-poziom-1-5x5-c | gry 33–48, poziom 1, plansza 5 × 5 | 4 | [md](tresc/plansze-poziom-1-5x5-c.md) | [PDF](druk/plansze-poziom-1-5x5-c.pdf) · [HTML](druk/plansze-poziom-1-5x5-c.html) |
| plansze-poziom-1-5x5-d | gry 49–58, poziom 1, plansza 5 × 5 | 3 | [md](tresc/plansze-poziom-1-5x5-d.md) | [PDF](druk/plansze-poziom-1-5x5-d.pdf) · [HTML](druk/plansze-poziom-1-5x5-d.html) |
| plansze-poziom-1-7x7-a | gry 1–16, poziom 1, plansza 7 × 7 | 4 | [md](tresc/plansze-poziom-1-7x7-a.md) | [PDF](druk/plansze-poziom-1-7x7-a.pdf) · [HTML](druk/plansze-poziom-1-7x7-a.html) |
| plansze-poziom-1-7x7-b | gry 17–32, poziom 1, plansza 7 × 7 | 4 | [md](tresc/plansze-poziom-1-7x7-b.md) | [PDF](druk/plansze-poziom-1-7x7-b.pdf) · [HTML](druk/plansze-poziom-1-7x7-b.html) |
| plansze-poziom-1-7x7-c | gry 33–48, poziom 1, plansza 7 × 7 | 4 | [md](tresc/plansze-poziom-1-7x7-c.md) | [PDF](druk/plansze-poziom-1-7x7-c.pdf) · [HTML](druk/plansze-poziom-1-7x7-c.html) |
| plansze-poziom-1-7x7-d | gry 49–58, poziom 1, plansza 7 × 7 | 3 | [md](tresc/plansze-poziom-1-7x7-d.md) | [PDF](druk/plansze-poziom-1-7x7-d.pdf) · [HTML](druk/plansze-poziom-1-7x7-d.html) |
| plansze-poziom-1-9x9-a | gry 1–16, poziom 1, plansza 9 × 9 | 4 | [md](tresc/plansze-poziom-1-9x9-a.md) | [PDF](druk/plansze-poziom-1-9x9-a.pdf) · [HTML](druk/plansze-poziom-1-9x9-a.html) |
| plansze-poziom-1-9x9-b | gry 17–26, poziom 1, plansza 9 × 9 | 3 | [md](tresc/plansze-poziom-1-9x9-b.md) | [PDF](druk/plansze-poziom-1-9x9-b.pdf) · [HTML](druk/plansze-poziom-1-9x9-b.html) |
| plansze-poziom-2-3-5x5 | gry 1–11 z pętlą POWTÓRZ, gry 12–15 z JEŚLI, STOP i META, gra 16 do wymyślenia | 4 | [md](tresc/plansze-poziom-2-3-5x5.md) | [PDF](druk/plansze-poziom-2-3-5x5.pdf) · [HTML](druk/plansze-poziom-2-3-5x5.html) |
| plansze-poziom-2-5x5-b | gry 17–26, poziom 2 (POWTÓRZ), plansza 5 × 5 | 3 | [md](tresc/plansze-poziom-2-5x5-b.md) | [PDF](druk/plansze-poziom-2-5x5-b.pdf) · [HTML](druk/plansze-poziom-2-5x5-b.html) |
| plansze-poziom-2-9x9-a | gry 1–16, poziom 2 (POWTÓRZ, pętla w pętli), plansza 9 × 9 | 4 | [md](tresc/plansze-poziom-2-9x9-a.md) | [PDF](druk/plansze-poziom-2-9x9-a.pdf) · [HTML](druk/plansze-poziom-2-9x9-a.html) |
| plansze-poziom-2-9x9-b | gry 17–26, poziom 2, plansza 9 × 9 | 3 | [md](tresc/plansze-poziom-2-9x9-b.md) | [PDF](druk/plansze-poziom-2-9x9-b.pdf) · [HTML](druk/plansze-poziom-2-9x9-b.html) |
| plansze-poziom-3-5x5-a | gry 1–16, poziom 3 (JEŚLI, STOP, META, pola ?), plansza 5 × 5 | 4 | [md](tresc/plansze-poziom-3-5x5-a.md) | [PDF](druk/plansze-poziom-3-5x5-a.pdf) · [HTML](druk/plansze-poziom-3-5x5-a.html) |
| plansze-poziom-3-5x5-b | gry 17–26, poziom 3, plansza 5 × 5 | 3 | [md](tresc/plansze-poziom-3-5x5-b.md) | [PDF](druk/plansze-poziom-3-5x5-b.pdf) · [HTML](druk/plansze-poziom-3-5x5-b.html) |
| plansze-poziom-3-9x9-a | gry 1–16, poziom 3, plansza 9 × 9 | 4 | [md](tresc/plansze-poziom-3-9x9-a.md) | [PDF](druk/plansze-poziom-3-9x9-a.pdf) · [HTML](druk/plansze-poziom-3-9x9-a.html) |
| plansze-poziom-3-9x9-b | gry 17–26, poziom 3, plansza 9 × 9 | 3 | [md](tresc/plansze-poziom-3-9x9-b.md) | [PDF](druk/plansze-poziom-3-9x9-b.pdf) · [HTML](druk/plansze-poziom-3-9x9-b.html) |
| plansze-poziom-4-5x5-a | gry 1–16, poziom 4 (PRZEPIS i ZRÓB), plansza 5 × 5 | 4 | [md](tresc/plansze-poziom-4-5x5-a.md) | [PDF](druk/plansze-poziom-4-5x5-a.pdf) · [HTML](druk/plansze-poziom-4-5x5-a.html) |
| plansze-poziom-4-5x5-b | gry 17–26, poziom 4, plansza 5 × 5 | 3 | [md](tresc/plansze-poziom-4-5x5-b.md) | [PDF](druk/plansze-poziom-4-5x5-b.pdf) · [HTML](druk/plansze-poziom-4-5x5-b.html) |
| plansze-poziom-4-9x9-a | gry 1–16, poziom 4, plansza 9 × 9 | 4 | [md](tresc/plansze-poziom-4-9x9-a.md) | [PDF](druk/plansze-poziom-4-9x9-a.pdf) · [HTML](druk/plansze-poziom-4-9x9-a.html) |
| plansze-poziom-4-9x9-b | gry 17–26, poziom 4, plansza 9 × 9 | 3 | [md](tresc/plansze-poziom-4-9x9-b.md) | [PDF](druk/plansze-poziom-4-9x9-b.pdf) · [HTML](druk/plansze-poziom-4-9x9-b.html) |

Pliki z planszami mają 4 strony po 4 gry (nowe zestawy z 10 grami mają 3 strony). W każdym zestawie gry idą od najłatwiejszej. Na dole każdej karty gry jest rozwiązanie dla dorosłego (przed grą można je zagiąć). Rozwiązania gier poziomu 1 zostały sprawdzone programem, który symuluje robota.

Konwencja nazw: `instrukcja`, `karty` i `plansze-poziom-<poziom>-<plansza>[-<zestaw>]`, małymi literami, bez polskich znaków.

W katalogu [`archiwum/`](archiwum/) leżą pierwsze wersje kart.

## Drukowanie

Otwórz PDF albo HTML z katalogu `druk/` i wydrukuj (w HTML: Ctrl+P, marginesy: brak). Strony z kartami poleceń są poziome. W oknie drukowania wybierz „dopasuj automatycznie” albo „orientacja automatyczna”.

## Zmiana treści i ponowne wygenerowanie

Po zmianie pliku w `tresc/` uruchom:

```sh
python3 narzedzia/drukuj.py                       # wszystkie pliki
python3 narzedzia/drukuj.py tresc/instrukcja.md   # jeden plik
python3 narzedzia/drukuj.py --bez-pdf             # tylko HTML
```

albo po prostu `make`.

Wystarczy Python 3, bez żadnych dodatkowych pakietów. Jeśli na komputerze jest Chrome, Chromium albo Edge, skrypt od razu zrobi PDF. Jeśli nie, zrobi tylko HTML.

### Sprawdzanie rozwiązań

`make sprawdz` (albo `python3 narzedzia/sprawdz.py tresc/plansze-*.md`) przepuszcza każde rozwiązanie z bloku `rozwiazanie` przez symulator robota. Symulator zgłasza wejście na lawę, kałużę, klocek albo poza planszę, skok bez kałuży pod spodem (skakać można tylko przez kałużę) i niezebrane skarby. Gry z polami `?` i zadania bez bloku `rozwiazanie` trzeba sprawdzić ręcznie.

### Skille do tworzenia kolejnych gier

W katalogu `.claude/skills/` są dwa skille dla Claude: `nowa-gra-offline` (jak projektować nowe gry i poziomy) oraz `robot-programista-plansze` (jak dodać plansze i karty do repo, sprawdzić je i wydrukować).

### Specjalne bloki w plikach .md

W blokach kodu z odpowiednią nazwą można opisać karty, plansze i programy. Skrypt narysuje je jako obrazki.

````md
```karty
IDŹ ×6
LICZBY 1-6 ×2
LAWA ×4
```

```plansza
. . * . .
. . L . .
. . ^ . .
```

```program
POWTÓRZ ×3
  IDŹ
  SKRĘĆ W PRAWO
KONIEC
```
````

- **karty**: lista kart do wycięcia. Dostępne są polecenia (IDŹ, SKRĘĆ W PRAWO, SKRĘĆ W LEWO, OBRÓĆ SIĘ, SKOCZ, POWTÓRZ, KONIEC, JEŚLI, STOP, META, PRZEPIS A/B, ZRÓB A/B), karty liczb `LICZBY a-b`, pytania (LAWA?, KAŁUŻA?, SKARB?, ŚCIANA?), TAK, NIE i ZAWSZE oraz pola na podłogę (START, SKARB, LAWA, KAŁUŻA) i plakietki ról (ROBOT, PROGRAMISTA).
- **plansza**: `.` to puste pole, `^ > v <` to robot patrzący w daną stronę, `*` to skarb, `#` to klocek, `L` to lawa, `K` to kałuża, a `?` to pole z niespodzianką.
- **program**: wcięcie o 2 spacje oznacza wnętrze POWTÓRZ, JEŚLI albo PRZEPIS. `PRZEPIS A` … `KONIEC` definiuje przepis, a `ZRÓB A ×2` go uruchamia (META w przepisie kończy tylko przepis). Kilka rzędów `TAK:` pod jednym JEŚLI robot wykonuje po kolei. Linie `TAK: …` i `NIE: …` to rzędy pod JEŚLI. Kilka kart w jednej linii oddziela się przecinkami. Po słowie `program` można dodać podpis, np. `program A`.
- **legenda**: linie `NAZWA: opis` dają legendę z ikonami.
- **rozwiazanie**: tak samo jak `program`, ale rysuje się na dole karty gry jako rozwiązanie dla dorosłego. Rozwiązanie bez programu zapisuje się akapitem `**Rozwiązanie:** …`.
- Linia `---` zaczyna nową stronę. Na stronie, której tytuł zaczyna się od „Plansze”, każda sekcja `###` staje się osobną kartą gry (4 karty na stronę).
