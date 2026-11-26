# Plansze 7 × 7 dla starszych, poziom 3 (dla 8-latka) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. „Masz tylko N kart” liczy wszystkie karty poleceń, także KONIEC i NIE, ale nie liczby. Pola ?: dorosły przed każdą próbą kładzie na nich to, co podaje jeden z wariantów (pola ? czytamy jak książkę: od lewej do prawej, z góry na dół; S skarb, · puste, # klocek, L lawa, K kałuża). Program ma zadziałać w każdym wariancie.

### 1. Duży diament
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
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×3
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 2. Duża ósemka
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
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

### 3. Schody z kwadratów
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
```rozwiazanie
POWTÓRZ ×3
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 4. Wysoka góra
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
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×3
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

---

# Plansze 7 × 7 dla starszych, poziom 3 (dla 8-latka) (2/2)

### 5. Dwa skarby
Pierwszy skarb leży w kolumnie robota, a drugi na końcu tego samego rzędu. Za każdym razem są gdzie indziej. Masz tylko 8 kart. Warianty pól ?: 1) S S · · · · · ·; 2) · · S S · · · ·; 3) · · · · S S · ·; 4) · · · · · · S S.
```plansza
. . . . . . .
? . . . . . ?
? . . . . . ?
? . . . . . ?
? . . . . . ?
. . . . . . .
^ . . . . . .
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

### 6. Spirala
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
```rozwiazanie
POWTÓRZ ×6
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 7. Duży pokój
Pokój raz jest szeroki, a raz wąski. Obejdź go dookoła, zbierz skarby i wróć na START. Masz tylko 6 kart. Warianty pól ?: 1) · · S · · · · · · · S; 2) S # · # # # # # S # ·.
```plansza
* . . . ? ? ?
. . . . . ? .
. . L . . ? .
. . . . . ? .
. . L . . ? .
. . . . . ? .
^ . . . ? ? ?
```
```rozwiazanie
POWTÓRZ ×4
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 8. Kałuże tam i z powrotem
Przejdź przez kałuże do ściany, zejdź rząd niżej i wróć przez kałuże. Zbierz skarby i wróć na START. Masz tylko 12 kart. Warianty pól ?: 1) K · K · · · K · K ·; 2) · K · · K K · · K ·; 3) · · K · K · · K · ·.
```plansza
L L L L L L L
L L L L L L L
> ? ? ? ? ? *
* ? ? ? ? ? .
L L L L L L L
L L L L L L L
. . . . . . .
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
