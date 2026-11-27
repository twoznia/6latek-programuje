# Plansze 13 × 13 dla starszych, poziom 6 (dla średniego programisty) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Cztery kwadraty
Przepis A to kwadrat o boku N i skręt w prawo. Cztery kwadraty różnej wielkości wokół START, jak w oknie z poziomu 3. Wróć na START. Masz tylko 9 kart.
```plansza
L L L L L L * . . . . . *
L L L L L L . L L L L L .
L L L L L L . L L L L L .
L L L L L L . L L L L L .
L L L L * . * L L L L L .
L L L L . L . L L L L L .
L * . . * . ^ . . * . . *
L . L L L L . L L . L L L
L . L L L L . L L . L L L
L . L L L L * . . * L L L
L . L L L L . L L L L L L
L * . . . . * L L L L L L
L L L L L L L L L L L L L
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×6
ZRÓB A ×3
ZRÓB A ×5
ZRÓB A ×2
```

### 2. Wykres słupkowy
Przepis A to słupek o wysokości N i krok w prawo. Na szczycie każdego słupka leży skarb. Masz tylko 22 kart.
```plansza
L L L L L L L L L L L L L
L L L * L L L L L L L L L
L L L . L * L L L L L L L
L * L . L . L L L L L L L
L . L . L . L L L L L L L
L . L . L . L * L L L L L
L . L . * . L . L L L L L
L . L . . . L . L L L L L
* . L . . . L . L L L L L
. . L . . . * . L L L L L
. . * . . . . . L L L L L
. . . . . . . . L L L L L
> . . . . . . . . L L L L
```
```kod
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×4
N = 6
N + 3
ZRÓB A ×N
ZRÓB A ×2
N = 6
N + 5
ZRÓB A ×N
ZRÓB A ×6
N = 6
N + 4
ZRÓB A ×N
ZRÓB A ×3
N = 6
N + 1
ZRÓB A ×N
```

### 3. Grzebień z zębami
Przepis A to ząb o wysokości N: w górę, krok w prawo, w dół i krok w prawo. Skarby na czubkach zębów. Masz tylko 20 kart.
```plansza
L L L L L L L L L L L L L
L L L L * * L L L L L L L
L L L L . . L L * * L L L
L L L L . . L L . . L L L
* * L L . . L L . . L L L
. . L L . . L L . . L L L
. . L L . . L L . . * * L
. . * * . . L L . . . . L
. . . . . . L L . . . . L
. . . . . . * * . . . . L
. . . . . . . . . . . . L
. . . . . . . . . . . . L
^ . . . . . . . . . . . .
```
```kod
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×5
N = 6
N + 5
ZRÓB A ×N
ZRÓB A ×3
N = 6
N + 4
ZRÓB A ×N
ZRÓB A ×6
```

### 4. Ramki
Przepis A rysuje ramkę o boku N i robi krok po skosie do środka. Każda następna ramka jest o 2 mniejsza. Masz tylko 20 kart.
```plansza
* . . . . . . . . . . . *
. * . . . . . . . . . * .
. . * . . . . . . . * . .
. . . * . . . . . * . . .
. . . . * . . . * . . . .
. . . . . * . * . . . . .
. . . . . * * . . . . . .
. . . . * * . * . . . . .
. . . * * . . . * . . . .
. . * * . . . . . * . . .
. * * . . . . . . . * . .
* * . . . . . . . . . * .
^ . . . . . . . . . . . *
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
N = 6
N + 6
ZRÓB A ×N
N = 6
N + 4
ZRÓB A ×N
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×6
ZRÓB A ×4
ZRÓB A ×2
```

---

# Plansze 13 × 13 dla starszych, poziom 6 (dla średniego programisty) (2/2)

### 5. Róg jak odległość
Zmierz drogę do klocka. Obróć się i przekaż N do przepisu A: dwa boki po N pól. Masz tylko 10 kart. Warianty pól ?: 1) · # · · S ·; 2) # · · · · S; 3) · · # S · ·.
```plansza
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . . . . . . .
^ ? . . . ? . . ? . . . .
```
```kod
PRZEPIS A
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ
ZRÓB A ×N
```

### 6. Schody jak odległość
Idź do klocka i licz. Potem skręć w lewo i zrób tyle schodków, ile było kroków. Masz tylko 13 kart. Warianty pól ?: 1) · · S # · ·; 2) S · · · · #; 3) · S · · # ·.
```plansza
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . ? . .
. . . . . . . . ? . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . ? . . . . . . . . . .
> . ? . . ? ? . . . . . .
```
```kod
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W LEWO
ZRÓB A ×N
```

### 7. Ile skarbów, taki kwadrat
Policz skarby w dolnym rzędzie. Potem obejdź kwadrat o boku N w lewo do góry. Ostatni skarb leży w lewym górnym rogu kwadratu. Masz tylko 13 kart. Warianty pól ?: 1) · S S S S · ·; 2) · · · · · S S; 3) S S · · S · ·.
```plansza
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
> . . . ? ? . ? ? ? ? ? .
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI SKARB?
    N + 1
  NIE
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO
ZRÓB A ×N
```

### 8. Ślimak jak odległość
Zmierz drogę do klocka. Przepis A to ślimak: bok N, potem N − 1 i tak do zera. Masz tylko 11 kart. Warianty pól ?: 1) · · # · S; 2) # · · S ·; 3) · # · S ·.
```plansza
? . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . ? . . . . . .
. . . . ? . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
^ . . . . . . . . . . . .
```
```kod
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W PRAWO
ZRÓB A ×N
```
