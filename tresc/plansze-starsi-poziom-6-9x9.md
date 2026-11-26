# Plansze 9 × 9 dla starszych, poziom 6 (dla średniego programisty) (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Kwadraty na zamówienie
Przepis A rysuje kwadrat o boku N. ZRÓB A ×3 to kwadrat o boku 3. Obejdź kwadraty w podanych rozmiarach: każdy skarb to róg innego kwadratu. Masz tylko 12 kart.
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . * . .
. . . . . * . . .
. . . . * . . . .
. . . * . . . . .
. . * . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×5
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×2
ZRÓB A ×6
ZRÓB A ×3
ZRÓB A ×4
```

### 2. Nierówne schody
Każdy schodek ma inną wysokość, więc pętla nie pomoże. Przepis A to schodek o wysokości i szerokości N. Masz tylko 8 kart.
```plansza
. . . . . . * . *
L . . . L . . L .
. L . * . . * . .
. L L . . L L L L
. . . . . . . . .
L . * * . . . . L
* . * L L . . . .
. . . L L . . . .
^ L . . L L . . .
```
```kod
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2
ZRÓB A ×1
ZRÓB A ×3
ZRÓB A ×2
```

### 3. Wieże
Na szczycie każdej wieży leży skarb. Przepis A wchodzi na wieżę o wysokości N, schodzi i idzie do następnej. Masz tylko 18 kart.
```plansza
# # # # * # # # .
# # * # . # # # .
# # . # . # * # .
* # . # . # . # .
. # . # . # . * .
. # . * . # . . .
. * . . . # . . .
. . . . . * . . .
> . . . . . . . .
```
```kod
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×5
ZRÓB A ×2
N = 6
N + 1
ZRÓB A ×N
ZRÓB A ×3
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×1
ZRÓB A ×6
ZRÓB A ×4
```

### 4. Diamenty
Przepis A to diament o boku N z poziomu 3. Wszystkie diamenty zaczynają się w START. Zbierz skarby i wróć na START. Masz tylko 12 kart.
```plansza
. . . . * . . L .
L . . * . . . . L
. . * . . . . . .
. . . . . . . . .
^ . . . . L . . .
. . L . . . . . .
. . * . . . . . .
. . . * . . . . .
. . . . * . . . .
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    POWTÓRZ ×N
      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    KONIEC
    SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×4
ZRÓB A ×2
ZRÓB A ×3
```

---

# Plansze 9 × 9 dla starszych, poziom 6 (dla średniego programisty) (2/4)

### 5. Kwadrat jak odległość
Idź do klocka i licz kroki w N. Potem skręć w lewo i narysuj kwadrat o boku N: ZRÓB A ×N przekazuje N do przepisu. Klocek za każdym razem stoi gdzie indziej. Masz tylko 10 kart. Warianty pól ?: 1) · · · · S S # ·; 2) · · S S · · · #; 3) S S · · · · · ·.
```plansza
? . . . . . . . ?
. . . . . . . . .
. . . . . . . . .
? . . . . ? . . .
. . . . . . . . .
? . . ? . . . . .
. . . . . . . . .
. . . . . . . . .
> . . . ? . ? . .
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W LEWO, ZRÓB A ×N
```

### 6. Odliczanie w przepisie
Przepis A robi N schodków i odlicza N − 1, dopóki N > 0. Między przepisami robot robi krok w bok. N w przepisie to kopia: zmiana w środku nie psuje liczby w programie. Masz tylko 12 kart.
```plansza
. L . L . L . . .
. L . . L L L * *
. . . L . . * * L
. . L . . * * . .
. . . * * * . . .
L L * * L . . . L
. * * . L L L . .
* * . . . L . . L
^ . . . . . . L .
```
```kod
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
  KONIEC
KONIEC
ZRÓB A ×4
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
ZRÓB A ×3
```

### 7. Spirala dwójkami
Przepis A to dwa boki po N pól. Program woła ZRÓB A ×N i zwiększa N. Każda długość boku pojawia się dwa razy. Masz tylko 11 kart.
```plansza
. . . . . . . . *
. . . . . . . * .
. . . . . . * . .
. . . . . * . . .
. . . . ^ . . . .
. . . * . . . . .
. . * . . . . . .
. * . . . . . . .
* . . . . . . . .
```
```kod
PRZEPIS A
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
N = 1
POWTÓRZ ×2
  POWTÓRZ ×4
    ZRÓB A ×N, N + 1
  KONIEC
KONIEC
```

### 8. Kwadraty w rzędzie
Przepis A obchodzi trzy boki kwadratu o boku N i staje w jego prawym dolnym rogu, gotowy do następnego. Każdy skarb to prawy górny róg innego kwadratu. Masz tylko 8 kart.
```plansza
. . . . . . . L L
. . . . . . . . .
L . . L . . . L .
. . . L . . . L .
. . L . . . . . *
. . . * . L . . .
. . . . . . . L .
. . . . * . . . .
^ . L . . . . . .
```
```kod
PRZEPIS A
  POWTÓRZ ×3
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
ZRÓB A ×1
ZRÓB A ×4
```

---

# Plansze 9 × 9 dla starszych, poziom 6 (dla średniego programisty) (3/4)

### 9. Cztery kwadraty
Przepis A to kwadrat o boku N i skręt w prawo. Cztery kwadraty różnej wielkości wokół START, jak w oknie z poziomu 3. Wróć na START. Masz tylko 9 kart.
```plansza
L L L L * . . . *
L L L L . L L L .
L L L L . L L L .
L L L * * L L L .
L * . * ^ . * . *
L . L L . L . L L
L . L L * . * L L
L * . . * L L L L
L L L L L L L L L
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
ZRÓB A ×2
ZRÓB A ×3
ZRÓB A ×1
```

### 10. Wykres słupkowy
Przepis A to słupek o wysokości N i krok w prawo. Na szczycie każdego słupka leży skarb. Masz tylko 14 kart.
```plansza
L L L L L L L L L
L L L L L L L L L
L * L L L * L L L
L . L * L . L L L
* . L . L . L * L
. . L . * . L . L
. . * . . . L . L
. . . . . . * . L
> . . . . . . . .
```
```kod
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×4
ZRÓB A ×6
ZRÓB A ×2
ZRÓB A ×5
ZRÓB A ×3
ZRÓB A ×6
ZRÓB A ×1
ZRÓB A ×4
```

### 11. Grzebień z zębami
Przepis A to ząb o wysokości N: w górę, krok w prawo, w dół i krok w prawo. Skarby na czubkach zębów. Masz tylko 14 kart.
```plansza
L L L L * * L L L
L L L L . . L L L
* * L L . . L L L
. . L L . . * * L
. . L L . . . . L
. . * * . . . . L
. . . . . . . . L
. . . . . . . . L
^ . . . . . . . .
```
```kod
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×6
ZRÓB A ×3
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×5
```

### 12. Ramki
Przepis A rysuje ramkę o boku N i robi krok po skosie do środka. Każda następna ramka jest o 2 mniejsza. Masz tylko 14 kart.
```plansza
* . . . . . . . *
. * . . . . . * .
. . * . . . * . .
. . . * . * . . .
. . . * * . . . .
. . * * . * . . .
. * * . . . * . .
* * . . . . . * .
^ . . . . . . . *
```
```kod
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×6
ZRÓB A ×4
ZRÓB A ×2
```

---

# Plansze 9 × 9 dla starszych, poziom 6 (dla średniego programisty) (4/4)

### 13. Róg jak odległość
Zmierz drogę do klocka. Obróć się i przekaż N do przepisu A: dwa boki po N pól. Masz tylko 10 kart. Warianty pól ?: 1) # · · · · S; 2) · · # S · ·; 3) · # · · S ·.
```plansza
? . . . . . . . .
? . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
? . . . . . . . .
. . . . . . . . .
^ ? . . . . ? ? .
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

### 14. Schody jak odległość
Idź do klocka i licz. Potem skręć w lewo i zrób tyle schodków, ile było kroków. Masz tylko 13 kart. Warianty pól ?: 1) · S · · # ·; 2) S · · · · #; 3) · · S # · ·.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ?
. . . . . . ? . .
. . . . ? . . . .
. . . . . . . . .
> . . ? ? ? . . .
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

### 15. Ile skarbów, taki kwadrat
Policz skarby w dolnym rzędzie. Potem obejdź kwadrat o boku N w lewo do góry. Ostatni skarb leży w lewym górnym rogu kwadratu. Masz tylko 13 kart. Warianty pól ?: 1) · S ·; 2) S S S; 3) · · ·.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . ? ? . ? . * .
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

### 16. Ślimak jak odległość
Zmierz drogę do klocka. Przepis A to ślimak: bok N, potem N − 1 i tak do zera. Masz tylko 11 kart. Warianty pól ?: 1) · · # · · S; 2) # · · S · ·; 3) · # · · S ·.
```plansza
. . . . . . . . .
? . . . . . . . .
. . . . . . . . .
? . . . . . . . .
? . . . . . . . .
. . . . ? . . . .
. . ? . . . . . .
. . ? . . . . . .
^ . . . . . . . .
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
