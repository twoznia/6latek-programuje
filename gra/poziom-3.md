# Gra online, poziom 3 (dla 8-latka)

Źródło gier poziomu 3 w grze online (index.html). Po zmianie uruchom `make online`: skrypt sprawdzi każde rozwiązanie symulatorem `narzedzia/symulator.py` (przy polach ? na każdym wariancie) i zapisze `gra/gry.js`.

Nowe na tym poziomie: **pętla w pętli** (POWTÓRZ w środku POWTÓRZ) i karta **DOPÓKI**. DOPÓKI zadaje pytanie o pole przed robotem i powtarza karty aż do KONIEC tak długo, jak odpowiedź to TAK. Gdy odpowiedź to NIE, robot idzie dalej, za KONIEC.

Format jak w `gra/poziom-2.md`, z dwiema zmianami. Rozwiązanie zapisujemy kartami po kolei, z wcięciem tylko dla czytelności (JEŚLI … NIE … KONIEC w osobnych liniach). Linie `pytania:`, `limit:` i inne ustawienia mogą stać pod nagłówkiem zestawu i wtedy dotyczą wszystkich jego gier.

Pytania: `WOLNE?` (przed robotem można zrobić IDŹ), `NIE ŚCIANA?`, `NIE SKARB?`, `KAŁUŻA?`, `LAWA?`, `SKARB?`, `KLOCEK?`, `ŚCIANA?`.

## Plansza 5 × 5

### Zestaw A: Pętla w pętli
karty: POWTÓRZ

#### 1. Diament
Robot chodzi po schodkach dookoła lawy. Jeden schodek to IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO. Zbierz skarby i wróć na START. Masz tylko 9 kart, więc włóż pętlę do pętli.
```plansza
# . * . #
. . . . .
^ . L . *
. . . . .
# . * . #
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×2
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 2. Ósemka
Robot obchodzi dwa kwadraty: jeden w górę, drugi w dół. Zbierz skarby i wróć na START. Masz tylko 7 kart.
```plansza
# # . . *
# L . L .
. . ^ . .
. L . L #
* . . # #
```
```ustawienia
limit: 7
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

#### 3. Góra
Wejdź po schodkach na szczyt i zejdź z drugiej strony. Pod górą jest lawa. Masz tylko 9 kart.
```plansza
. . . . .
. # . # .
# . * . #
. * L * .
^ L L L *
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×2
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### Zestaw B: Pętla DOPÓKI
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, KAŁUŻA?, SKARB?

#### 4. Do ściany
Nowa karta DOPÓKI! Robot pyta: czy przed nami jest wolne pole? Dopóki TAK, robi IDŹ. Klocek za każdym razem stoi gdzie indziej. Masz tylko 3 karty.
```plansza
. . ? . .
. . ? . .
. . ? . .
. . . . .
. . ^ . .
```
```ustawienia
limit: 3
warianty: *.. #*. L.*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

#### 5. Tam i z powrotem
Idź, dopóki przed tobą nie ma skarbu. Weź skarb i wróć na START. Skarb za każdym razem leży gdzie indziej. Masz tylko 8 kart.
```plansza
. . . . .
. L . L .
> ? ? ? ?
. L . L .
. . . . .
```
```ustawienia
limit: 8
warianty: *... .*.. ..*. ...*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
KONIEC
IDŹ, OBRÓĆ SIĘ
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

#### 6. Za róg
Idź w górę aż do przeszkody, skręć w prawo i idź aż do końca. Masz tylko 7 kart.
```plansza
? . . . ?
? . . . ?
? . . . ?
. . . . .
^ . . . .
```
```ustawienia
limit: 7
warianty: .*.... #..*.. #.#..*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ
KONIEC
SKRĘĆ W PRAWO
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

#### 7. Pokój
Pokój raz jest duży, a raz mały. Obejdź go dookoła, zbierz skarby w rogach i wróć na START. Masz tylko 6 kart.
```plansza
* . . ? ?
. . . . ?
. . L . ?
. . . . ?
^ . . ? ?
```
```ustawienia
limit: 6
warianty: .*....* *####*#
```
```rozwiazanie
POWTÓRZ ×4
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 8. Kałuże w rzędzie
Kałuże są za każdym razem gdzie indziej. Dopóki nie ma ściany: jeśli przed robotem jest kałuża, SKOCZ, a jeśli nie, IDŹ. Masz tylko 7 kart.
```plansza
. L . L .
. . . . .
> ? ? ? *
. . . . .
. L . L .
```
```ustawienia
limit: 7
warianty: K.. .K. ..K K.K
```
```rozwiazanie
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
KONIEC
```

## Plansza 7 × 7

### Zestaw A: Pętla w pętli
karty: POWTÓRZ

#### 1. Duży diament
Trzy schodki w górę, trzy w prawo w dół i tak dookoła lawy. Zbierz skarby i wróć na START. Masz tylko 9 kart.
```plansza
# . . * . . #
. . . . . . .
. . . L . . .
^ . L L L . *
. . . L . . .
. . . . . . .
# . . * . . #
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×3
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 2. Duża ósemka
Dwa kwadraty: jeden w prawo do góry, drugi w lewo w dół. Zbierz skarby i wróć na START. Masz tylko 7 kart.
```plansza
# # # . . . *
# # # . L L .
# # # . L L .
. . . ^ . . .
. L L . # # #
. L L . # # #
* . . . # # #
```
```ustawienia
limit: 7
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

#### 3. Schody z kwadratów
Trzy kwadraty po skosie. Po każdym kwadracie robot idzie 2 pola w górę i 2 w prawo. Masz tylko 10 kart.
```plansza
# # # # * . *
# # # # . L .
# # * . . . .
# # . L . # #
* . . . . # #
. L . # # # #
^ . . # # # #
```
```ustawienia
limit: 10
```
```rozwiazanie
POWTÓRZ ×3
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

#### 4. Wysoka góra
Trzy schodki w górę na szczyt i trzy w dół. Pod górą jest lawa. Masz tylko 9 kart.
```plansza
. . . . . . .
. . . . . . .
. . # . # . .
. . . * . . .
. . * L * . .
. * L L L * .
^ L L L L L *
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×3
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### Zestaw B: Pętla DOPÓKI
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, KAŁUŻA?, SKARB?

#### 5. Dwa skarby
Pierwszy skarb leży w kolumnie robota, a drugi na końcu tego samego rzędu. Za każdym razem są gdzie indziej. Masz tylko 8 kart.
```plansza
. . . . . . .
? . . . . . ?
? . . . . . ?
? . . . . . ?
? . . . . . ?
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 8
warianty: **...... ..**.... ....**.. ......**
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
KONIEC
IDŹ, SKRĘĆ W PRAWO
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

#### 6. Spirala
Korytarz kręci się jak ślimak. Idź, dopóki jest wolne, potem skręć w prawo. I tak 6 razy. Masz tylko 6 kart.
```plansza
> . . . . . .
# # # # # # .
. . . . . # .
. # # # . # .
. # # # * # .
. # # # # # .
* . . . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×6
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 7. Duży pokój
Pokój raz jest szeroki, a raz wąski. Obejdź go dookoła, zbierz skarby i wróć na START. Masz tylko 6 kart.
```plansza
* . . . ? ? ?
. . . . . ? .
. . L . . ? .
. . . . . ? .
. . L . . ? .
. . . . . ? .
^ . . . ? ? ?
```
```ustawienia
limit: 6
warianty: ..*.......* *#.#####*#.
```
```rozwiazanie
POWTÓRZ ×4
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 8. Kałuże tam i z powrotem
Przejdź przez kałuże do ściany, zejdź rząd niżej i wróć przez kałuże. Zbierz skarby i wróć na START. Masz tylko 12 kart.
```plansza
L L L L L L L
L L L L L L L
> ? ? ? ? ? *
* ? ? ? ? ? .
L L L L L L L
L L L L L L L
. . . . . . .
```
```ustawienia
limit: 12
warianty: K.K...K.K. .K..KK..K. ..K.K..K..
```
```rozwiazanie
POWTÓRZ ×2
  DOPÓKI NIE ŚCIANA?
    JEŚLI KAŁUŻA?
      SKOCZ
    NIE
      IDŹ
    KONIEC
  KONIEC
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

## Plansza 9 × 9

### Zestaw A: Pętla w pętli
karty: POWTÓRZ

#### 1. Wielki diament
Cztery schodki w każdą stronę. Zbierz skarby i wróć na START. Masz tylko 9 kart.
```plansza
# # . . * . . # #
# . . . . . . . #
. . . . L . . . .
. . . L L L . . .
^ . L L L L L . *
. . . L L L . . .
. . . . L . . . .
# . . . . . . . #
# # . . * . . # #
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 2. Wiatraczek
Cztery kwadraty dookoła START. Po każdym kwadracie robot skręca w prawo. Zbierz skarby i wróć na START. Masz tylko 7 kart.
```plansza
. . . . . . . . .
. * . . . . . * .
. . L . . . L . .
. . . . . . . . .
. . . . ^ . . . .
. . . . . . . . .
. . L . . . L . .
. * . . . . . * .
. . . . . . . . .
```
```ustawienia
limit: 7
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 3. Wielka góra
Cztery schodki w górę i cztery w dół. Pod górą jest lawa. Masz tylko 9 kart.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . # . # . . .
. . . . * . . . .
. . . * L * . . .
. . * L L L * . .
. * L L L L L * .
^ L L L L L L L *
```
```ustawienia
limit: 9
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

#### 4. Długie schody z kwadratów
Cztery kwadraty po skosie, aż do górnego rogu. Masz tylko 10 kart.
```plansza
# # # # # # * . *
# # # # # # . L .
# # # # * . . . .
# # # # . L . # #
# # * . . . . # #
# # . L . # # # #
* . . . . # # # #
. L . # # # # # #
^ . . # # # # # #
```
```ustawienia
limit: 10
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### Zestaw B: Pętla DOPÓKI
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, KAŁUŻA?, SKARB?

#### 5. Dwa skarby w korytarzu
Zbierz dwa skarby i wróć na START. Za każdym razem leżą gdzie indziej. Masz tylko 10 kart.
```plansza
. . . . . . . . .
. L L L L L L L .
. . . . . . . . .
. # # # # # # # .
> ? ? ? ? ? ? ? ?
. # # # # # # # .
. . . . . . . . .
. L L L L L L L .
. . . . . . . . .
```
```ustawienia
limit: 10
warianty: .*...*.. *......* ...**... ..*...*.
```
```rozwiazanie
POWTÓRZ ×2
  DOPÓKI NIE SKARB?
    IDŹ
  KONIEC
  IDŹ
KONIEC
OBRÓĆ SIĘ
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

#### 6. Wielka spirala
Korytarz kręci się jak ślimak aż do skarbu w środku. Robot skręca 9 razy, a liczba może być najwyżej 6. Pomoże pętla w pętli: 3 razy po 3. Masz tylko 8 kart.
```plansza
> . . . . . . . .
# # # # # # # # .
. . . . . . . # .
. # # # # # . # .
. # . . * # . # .
. # . # # # . # .
. # . . . . . # .
. # # # # # # # .
* . . . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
POWTÓRZ ×3
  POWTÓRZ ×3
    DOPÓKI WOLNE?
      IDŹ
    KONIEC
    SKRĘĆ W PRAWO
  KONIEC
KONIEC
```

#### 7. Wąż
Robot idzie wężykiem z dołu do góry. Rzędy mają różną długość. Zbierz wszystkie skarby. Masz tylko 14 kart.
```plansza
* . . . . . . . .
* . . . . . . . .
. . . . . . * # .
. . # * . . . . .
. . . . . . . . *
* . . . . . . . .
. . . . . . . * #
# * . . . . . . .
> . . . . . . * #
```
```ustawienia
limit: 14
```
```rozwiazanie
POWTÓRZ ×4
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

#### 8. Kałuże w długim korytarzu
Przejdź przez kałuże do ściany, zejdź rząd niżej i wróć. Zbierz skarby i wróć na START. Masz tylko 12 kart.
```plansza
L L L L L L L L L
. . . . . . . . .
L L L L L L L L L
> ? ? ? ? ? ? ? *
* ? ? ? ? ? ? ? .
L L L L L L L L L
. . . . . . . . .
L L L L L L L L L
. . . . . . . . .
```
```ustawienia
limit: 12
warianty: K.K.K...K.K.K. .K..K..K..K... ..K.K.K..K.K..
```
```rozwiazanie
POWTÓRZ ×2
  DOPÓKI NIE ŚCIANA?
    JEŚLI KAŁUŻA?
      SKOCZ
    NIE
      IDŹ
    KONIEC
  KONIEC
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
