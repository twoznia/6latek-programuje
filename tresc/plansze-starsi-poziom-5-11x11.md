# Plansze 11 × 11 dla starszych, poziom 5 (dla początkującego programisty) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Długa kręta ścieżka
Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo. Masz tylko 12 kart. Warianty pól ?: 1) S ·; 2) · S.
```plansza
L . . . . L L L L L L
. . L L . L L . . . L
. L L L . . L . L . ?
. L L L L . . . L L .
. . ? L L L L L L L .
L L L L L L L L L L .
L L L L L L . . . L .
L L L L L L . L . . .
L L . . . L . L L L L
. . . L . . . L L L L
^ L L L L L L L L L L
```
```kod
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

### 2. Idź za ścieżką
Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo. Masz tylko 12 kart. Warianty pól ?: 1) S ·; 2) · S.
```plansza
. . . . L L L L . . ?
. L L . . L L L . L .
. . L L . . . L . L .
L . L L L L . . . L .
L . ? L L L L L L . .
L L L L L . . . . . L
L L L L L . L L L L L
. . . . L . L L L L L
. L L . . . L L L L L
. L L L L L L L L L L
^ L L L L L L L L L L
```
```kod
DOPÓKI NIE SKARB?
  JEŚLI WOLNE?
    IDŹ
  NIE
    JEŚLI WOLNE W LEWO?
      SKRĘĆ W LEWO
    NIE
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### 3. Więcej kałuż
Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty. Masz tylko 16 kart. Warianty pól ?: 1) · S; 2) S ·.
```plansza
L L L . . . . L L L L
L . . . L L . L L L L
. . L L L L . . L L L
. L L L L L L . L L L
. L L L L L ? . L L L
. . . . L L L L L L L
L L L . . L L L . . .
L L L L ? . K . . L .
L L L L L L L L L L .
L L L . . . . K . L .
> . K . L L L L . . .
```
```kod
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

### 4. Nowe przeszkody
Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A. Masz tylko 18 kart. Warianty pól ?: 1) · · L · # · # · ·; 2) · · L · # · · · L; 3) K · L · · L · · ·; 4) L · K · L · · · K.
```plansza
L . . . . L . L . L .
. L . . . . L L . . .
L . . . . . . L . . L
. L . L L . L . L L .
. . . . L . . . . . .
. . L L . . L . . . .
. . . . L . . . . L L
. L . . . L . . . . .
. . . . . . . . . . .
> ? ? ? ? ? ? ? ? ? *
. . . . . . L . . . .
```
```kod
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

---

# Plansze 11 × 11 dla starszych, poziom 5 (dla początkującego programisty) (2/2)

### 5. Nowy labirynt
Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart. Warianty pól ?: 1) # # # # #; 2) # # # # ·.
```plansza
. . . . . . . # . . .
. # . # # # . # . # .
. # . # . # . . . # .
. # . # . # ? # ? # .
. # . ? . . . . . . .
. # . # . # # # # # #
. # . # . . . # * . .
# # . # ? # . # # # .
. . . # . # . . . # .
. # # # . # ? # . # .
^ # . . . . . . . . .
```
```kod
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### 6. Labirynt w lewo
Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania. Masz tylko 11 kart. Warianty pól ?: 1) # # # # #; 2) # # # # ·.
```plansza
. . . . . . . . . . .
. # # # . # # # # # .
. . . ? . # . . . # .
. # . # # # . # . # .
. # . # . . . # . # .
. # . # . # ? # . # .
. ? . . . ? . . . # .
# # # # . # . # # # .
. . . # . ? . . . # .
. # . # # # # # . # .
^ # . . . . . . . # *
```
```kod
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### 7. Więcej drzwi
Więcej pól ? i 3 różne labirynty. Program ten sam. Masz tylko 11 kart. Warianty pól ?: 1) # # # # # #; 2) # # # # # ·; 3) # # # # · #.
```plansza
. . . . . # . . . . .
? # . # . # . # # # .
. . . # . ? . ? * # .
. # # # . # . # . # .
. # . . . # . . . # .
. # # # . # # # ? # .
. . . # . # . . . # .
. # . # . # . # . # .
. # . ? . # . # . . .
# # . # . # . # # # .
> . . ? . . . # . . .
```
```kod
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### 8. Największa zagadka
4 labirynty, dużo drzwi i jeden program. Masz tylko 11 kart. Warianty pól ?: 1) # # # # # · #; 2) # # # # · # #; 3) # # · # · # #; 4) · # # # # # ·.
```plansza
. . . . . . . . . . .
# # # # . # ? # # # .
. . . # . . . # . . .
. # . # # # . # # # .
. ? . . . ? . . . # .
. # ? # . # . # . # .
. . . # . ? . # . # .
. # . # . # . # . # .
. # . # . # . # . # .
# # . # . # ? # . # .
> . . # . . . . . ? *
```
```kod
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```
