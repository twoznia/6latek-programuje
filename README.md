# 6latek programuje

**Robot i Programista** to zabawa ruchowa na podłodze, bez komputera. Uczy 6-latka myślenia jak programista: najpierw sekwencji poleceń, potem pętli, warunków (if / then / else) oraz przerywania (break / return). Przy okazji dziecko ćwiczy czytanie krótkich słów i liczenie.

Dziecko jest robotem albo programistą. Program układa się z wydrukowanych kart na podłodze, na siatce 5 × 5 pól zrobionej z taśmy malarskiej.

## Poziomy

| Poziom | Czego uczy | Treść | Do druku |
|---|---|---|---|
| 1 | sekwencja, kierunki, „ile razy”, lawa i kałuża | [poziom-1.md](poziomy/poziom-1.md) | [poziom-1.pdf](druk/poziom-1.pdf) |
| 1+ | duża plansza 7 × 7: dłuższe programy, większe liczby, labirynty | [poziom-1-plus.md](poziomy/poziom-1-plus.md) | [poziom-1-plus.pdf](druk/poziom-1-plus.pdf) |
| 2 | pętla POWTÓRZ … KONIEC, czytanie kodu, szukanie błędu | [poziom-2.md](poziomy/poziom-2.md) | [poziom-2.pdf](druk/poziom-2.pdf) |
| 3 | JEŚLI / TAK / NIE, pętla ∞, STOP (break) i META (return) | [poziom-3.md](poziomy/poziom-3.md) | [poziom-3.pdf](druk/poziom-3.pdf) |

Każdy poziom zawiera instrukcję dla dorosłego, karty do wycięcia, misje z planszami, rozwiązania oraz zabawy, które nie wymagają przygotowania.

## Drukowanie

Gotowe pliki PDF leżą w katalogu [`druk/`](druk/). Strony z kartami poleceń są poziome. W oknie drukowania wybierz „dopasuj automatycznie” albo „orientacja automatyczna”.

## Zmiana treści i ponowne wygenerowanie

Treść każdego poziomu jest w zwykłym pliku Markdown w katalogu `poziomy/`. Po zmianie uruchom:

```sh
python3 narzedzia/drukuj.py              # wszystkie poziomy
python3 narzedzia/drukuj.py poziomy/poziom-2.md
python3 narzedzia/drukuj.py --bez-pdf    # tylko HTML
```

albo po prostu `make`.

Wystarczy Python 3, bez żadnych dodatkowych pakietów. Jeśli na komputerze jest Chrome, Chromium albo Edge, skrypt od razu zrobi PDF. Jeśli nie, otwórz plik `druk/poziom-N.html` w przeglądarce i wydrukuj go (Ctrl+P, marginesy: brak).

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

- **karty**: lista kart do wycięcia. Dostępne są polecenia (IDŹ, SKRĘĆ W PRAWO, SKRĘĆ W LEWO, OBRÓĆ SIĘ, SKOCZ, POWTÓRZ, KONIEC, JEŚLI, STOP, META), karty liczb `LICZBY a-b`, pytania (LAWA?, KAŁUŻA?, SKARB?, ŚCIANA?), TAK, NIE i ZAWSZE oraz pola na podłogę (START, SKARB, LAWA, KAŁUŻA).
- **plansza**: `.` to puste pole, `^ > v <` to robot patrzący w daną stronę, `*` to skarb, `#` to klocek, `L` to lawa, `K` to kałuża, a `?` to pole z niespodzianką.
- **program**: wcięcie o 2 spacje oznacza wnętrze POWTÓRZ albo JEŚLI. Linie `TAK: …` i `NIE: …` to rzędy pod JEŚLI. Kilka kart w jednej linii oddziela się przecinkami. Po słowie `program` można dodać podpis, np. `program A`.
- **legenda**: linie `NAZWA: opis` dają legendę z ikonami.
- Linia `---` zaczyna nową stronę. Na stronie, której tytuł zaczyna się od „Misje”, każda sekcja `###` staje się osobną ramką misji.
