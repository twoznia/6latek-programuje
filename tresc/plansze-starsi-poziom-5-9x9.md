# Plansze 9 × 9 dla starszych, poziom 5 (dla początkującego programisty) (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Kręta ścieżka nad lawą
Skarb leży raz w połowie ścieżki, a raz na końcu. Po każdym kroku robot pyta: czy przede mną jest zamknięte I w lewo wolne? Wtedy skręca w lewo. Tak samo w prawo. Masz tylko 12 kart. Warianty pól ?: 1) · S; 2) S ·.
```plansza
? L L L L L L L L
. L L L L L L L L
. . L L L L L L L
L . . . . L L L L
L L L L . . . . L
. . . . L L L . L
. L L . . . L . .
. L L L L . L L ?
^ L L L L . . . .
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

### 2. Ścieżka z kałużami
Kręta ścieżka, a na niej kałuże. Najpierw: kałuża? SKOCZ, a jeśli nie, IDŹ. Potem skręty jak w poprzedniej grze. Masz tylko 16 kart. Warianty pól ?: 1) S ·; 2) · S.
```plansza
L L L L L L . . ?
L L L L L . . L .
L L L L . . L L .
L L L L K L . . .
L L L L . L . L L
L L L L . L . . .
. . K . . L L L .
. L L L L L L . .
^ L L L L ? . . L
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

### 3. Kałuża, lawa albo klocek
Na polach ? za każdym razem stoi coś innego. Kałużę przeskocz. Lawę LUB klocek obejdź górą: to przepis A. Masz tylko 18 kart. Warianty pól ?: 1) · K · K · # ·; 2) L · · K · K ·; 3) L · K · · · ·.
```plansza
. . . . L . L L L
L . L . . . . . .
. . . L . . L . .
L L . L L . . L .
L . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> ? ? ? ? ? ? ? *
. . . L . . . L .
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

### 4. Cztery razy inaczej
Ten sam program musi przejść cztery różne rzędy przeszkód. Masz tylko 18 kart. Warianty pól ?: 1) # · # · # · L; 2) # · K · K · ·; 3) L · # · · · ·; 4) L · K · · # ·.
```plansza
. L . . L . . . .
. L L . . . . . L
. . L L . . . . L
. . . . . . . L .
L L . L . . . . L
. . . L . . . . L
. . . . . . . . .
> ? ? ? ? ? ? ? *
. . L . L . . . L
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

# Plansze 9 × 9 dla starszych, poziom 5 (dla początkującego programisty) (2/4)

### 5. Labirynt prawej ręki
Trzymaj prawą rękę na ścianie: po każdym kroku, jeśli w prawo jest wolne, skręć w prawo. Jeśli nie, kręć się w lewo, dopóki przed tobą nie jest wolne. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart. Warianty pól ?: 1) # # #; 2) # · #.
```plansza
* # . . . . . . .
. # . # # # . # .
. # . # . . . # .
. # . # . # ? # .
. # . # . . . # .
. # . # # # . # .
. . . . . # . ? .
# # ? # # # . # .
> . . . . . . # .
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

### 6. Labirynt lewej ręki
Teraz lewa ręka na ścianie. Przerób program z poprzedniej gry. Masz tylko 11 kart. Warianty pól ?: 1) # # #; 2) # # ·.
```plansza
. . . . . ? * . .
. # # # . # # # .
. . . # . . . . .
. # . # ? # # # .
. # . . . . . # .
# # ? # # # . # #
. . . . . # . . .
. # # # . # # # .
^ # . . . . . . .
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

### 7. Labirynt z drzwiami
Na polach ? są drzwi: raz otwarte, raz zamknięte. Program musi znaleźć skarb w każdym z 3 labiryntów. Masz tylko 11 kart. Warianty pól ?: 1) # # # #; 2) # # # ·; 3) # · # #.
```plansza
. . . # . . . # *
. # . # . # . # .
. # . . . # . # .
. # ? # ? # . # .
. . . # . # . # .
. # . # . # . # .
. # . # . . . # .
# # . # . # ? # .
> . . ? . . . . .
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

### 8. Wielka zagadka
4 różne labirynty i jeden program. Którą ręką do ściany? Masz tylko 11 kart. Warianty pól ?: 1) # # # # #; 2) # # # · #; 3) · # # # ·; 4) · # # · #.
```plansza
. . . . . . . ? *
. # ? # ? # . # .
. . . # . # . # .
. # . # . # . # .
. ? . # . # . # .
# # . # . # . # .
. . . # . . . # .
. # ? # . # # # .
^ # . . . . . . .
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

---

# Plansze 9 × 9 dla starszych, poziom 5 (dla początkującego programisty) (3/4)

### 9. Długa kręta ścieżka
Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo. Masz tylko 12 kart. Warianty pól ?: 1) S ·; 2) · S.
```plansza
. . ? . L L L L L
. L L . . L L L L
. L L L . L L L L
. . L L . . . . L
L . . L L L L . L
L L . L L L L . .
L L . . L L L L .
L L L . L L L L .
> . . . L L ? . .
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

### 10. Idź za ścieżką
Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo. Masz tylko 12 kart. Warianty pól ?: 1) · S; 2) S ·.
```plansza
. . . L L L L L L
. L . L L L . . .
? L . . . . . L .
L L L L L L L ? .
L L L L L L L . L
L L L L L L L . .
L L L L L L L L .
L L . . . L . . .
> . . L . . . L L
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

### 11. Więcej kałuż
Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty. Masz tylko 16 kart. Warianty pól ?: 1) · S; 2) S ·.
```plansza
L L L . . K . . .
L L . . L L L L .
? . . L L L L L .
L L L L L L L L K
L . . . . . . L .
L . L L L L . L .
L . L L L L . L K
. . L L L L . L ?
^ L L L L L . . .
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

### 12. Nowe przeszkody
Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A. Masz tylko 18 kart. Warianty pól ?: 1) · · · L · K ·; 2) · K · · · · K; 3) K · · # · · ·; 4) L · K · L · ·.
```plansza
. . . . . L . . .
L . . . . . . . .
L . . . . . . . L
L . . . . . L . .
L L . . . . L . .
. L . L L . . . .
. . . . . . . . .
> ? ? ? ? ? ? ? *
. L . . L . . . L
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

# Plansze 9 × 9 dla starszych, poziom 5 (dla początkującego programisty) (4/4)

### 13. Nowy labirynt
Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart. Warianty pól ?: 1) # # # #; 2) # # · #.
```plansza
. . . . . . . . .
. # # # # # # # .
. . . . . . . # .
? # . # # # # # .
. . . ? . . . . .
. # # # . # ? # #
. . * # . . . . .
# # ? # # # # # .
> . . . . . . . .
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

### 14. Labirynt w lewo
Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania. Masz tylko 11 kart. Warianty pól ?: 1) # # # #; 2) · # # #.
```plansza
* . . . . # . . .
# # ? # . # . # .
. . . # . . . # .
. # . # # # . # .
. ? . . . # . # .
. # # # . # # # .
. . . ? . . . . .
? # . # # # # # .
> . . # . . . . .
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

### 15. Więcej drzwi
Więcej pól ? i 3 różne labirynty. Program ten sam. Masz tylko 11 kart. Warianty pól ?: 1) # # # # #; 2) # # # · ·; 3) # · # # ·.
```plansza
. . . . . ? . . .
. # # # . # . # .
. # . . . # * # .
. # ? # . # ? # .
. . . ? . . . ? .
. # . # # # . # .
. # . # . . . # .
# # . # . # # # .
> . . # . . . . .
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

### 16. Największa zagadka
4 labirynty, dużo drzwi i jeden program. Masz tylko 11 kart. Warianty pól ?: 1) # # # # # ·; 2) # # # · # #; 3) # # # · # ·; 4) # # · # # #.
```plansza
. . . . . # . . .
. # ? # . # ? # .
. # . # . . . . .
. # . # # # # # .
. # . . . . . . .
. # # # ? # . # ?
. . . . . # . . .
? # ? # . # # # .
> . . . . # * . .
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
