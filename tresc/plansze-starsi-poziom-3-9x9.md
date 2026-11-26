# Plansze 9 × 9 dla starszych, poziom 3 (dla 8-latka) (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. „Masz tylko N kart” liczy wszystkie karty poleceń, także KONIEC i NIE, ale nie liczby. Pola ?: dorosły przed każdą próbą kładzie na nich to, co podaje jeden z wariantów (pola ? czytamy jak książkę: od lewej do prawej, z góry na dół; S skarb, · puste, # klocek, L lawa, K kałuża). Program ma zadziałać w każdym wariancie.

### 1. Wielki diament
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
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 2. Wiatraczek
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
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 3. Wielka góra
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
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 4. Długie schody z kwadratów
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
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

---

# Plansze 9 × 9 dla starszych, poziom 3 (dla 8-latka) (2/4)

### 5. Dwa skarby w korytarzu
Zbierz dwa skarby i wróć na START. Za każdym razem leżą gdzie indziej. Masz tylko 10 kart. Warianty pól ?: 1) · S · · · S · ·; 2) S · · · · · · S; 3) · · · S S · · ·; 4) · · S · · · S ·.
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

### 6. Wielka spirala
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

### 7. Wąż
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

### 8. Kałuże w długim korytarzu
Przejdź przez kałuże do ściany, zejdź rząd niżej i wróć. Zbierz skarby i wróć na START. Masz tylko 12 kart. Warianty pól ?: 1) K · K · K · · · K · K · K ·; 2) · K · · K · · K · · K · · ·; 3) · · K · K · K · · K · K · ·.
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

---

# Plansze 9 × 9 dla starszych, poziom 3 (dla 8-latka) (3/4)

### 9. Plus
Cztery ramiona po 4 pola. Na końcu każdego ramienia obróć się i wróć do środka. Masz tylko 6 kart.
```plansza
L L L L * L L L L
L L L L . L L L L
L L L L . L L L L
L L L L . L L L L
* . . . ^ . . . *
L L L L . L L L L
L L L L . L L L L
L L L L . L L L L
L L L L * L L L L
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×4, SKRĘĆ W LEWO
KONIEC
```

### 10. Grzebień
Robot idzie w prawo i co drugie pole robi ząb grzebienia: 7 w górę i z powrotem. Masz tylko 8 kart.
```plansza
L L L L L L L L L
L L * L * L * L *
L L . L . L . L .
L L . L . L . L .
L L . L . L . L .
L L . L . L . L .
L L . L . L . L .
L L . L . L . L .
> . * . * . * . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×7, OBRÓĆ SIĘ, IDŹ ×7, SKRĘĆ W LEWO
KONIEC
```

### 11. Okno
Cztery kwadraty wokół START, jak szybki w oknie. Po każdym kwadracie robot skręca w prawo. Masz tylko 7 kart.
```plansza
* . . . * . . . *
. L L L . L L L .
. L L L . L L L .
. L L L . L L L .
* . . . ^ . . . *
. L L L . L L L .
. L L L . L L L .
. L L L . L L L .
* . . . * . . . *
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×4, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 12. Schody w górę i w dół
8 schodków w górę, obrót i te same karty jeszcze raz. Robot schodzi inną drogą! Wróć na START. Masz tylko 11 kart.
```plansza
L L L L L L L * *
L L L L L L * * *
L L L L L * * * L
L L L L * * * L L
L L L * * * L L L
L L * * * L L L L
L * * * L L L L L
* * * L L L L L L
^ * L L L L L L L
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×2
    POWTÓRZ ×4
      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    KONIEC
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

---

# Plansze 9 × 9 dla starszych, poziom 3 (dla 8-latka) (4/4)

### 13. Do klocka i w prawo
Idź, dopóki jest wolne, skręć w prawo i znowu idź, dopóki jest wolne. Klocki za każdym razem stoją gdzie indziej. Masz tylko 7 kart. Warianty pól ?: 1) · # · # · S · · ·; 2) · · # · · · · # S; 3) # · · · # · S · ·.
```plansza
. . . ? . . . . .
? . . ? . . . . .
. . . . . . . . .
? . . . . . . . .
? . . . . . . . ?
. . . . . . . . ?
? . . . . . . . .
. . . . . . . . ?
^ . . . . . . . .
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

### 14. Dwa rzędy kałuż
Przejdź dolny rząd do ściany, wejdź piętro wyżej i wróć górnym rzędem. Kałuże przeskakuj. Masz tylko 12 kart. Warianty pól ?: 1) · · K · K K; 2) · K · K · ·; 3) K · · K · ·; 4) K · · · · K.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . ? ? . ? . . .
> . ? . ? . ? . *
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
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### 15. Trzy razy do klocka
Trzy razy: idź, dopóki jest wolne, i skręć w prawo. Skarb leży tam, gdzie robot stanie. Masz tylko 6 kart. Warianty pól ?: 1) · · · # · # · S; 2) · # # · · · · S; 3) # · · · # · S ·.
```plansza
. . . . . ? . . .
. . . . . . . . .
. . . ? . . . . .
? . . . . . . . .
. . . . ? . . . .
. . . . . . . ? .
. . . . ? . . . .
. . . . . . . . .
^ . . . ? . . . ?
```
```rozwiazanie
POWTÓRZ ×3
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 16. Skarb i z powrotem
Idź do skarbu, weź go, obróć się i idź do ściany. Wróć na START. Masz tylko 8 kart. Warianty pól ?: 1) · · S; 2) · S ·; 3) S · ·.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
L . L . L . L . L
> . . ? . ? ? . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
KONIEC
IDŹ, OBRÓĆ SIĘ
DOPÓKI NIE ŚCIANA?
  IDŹ
KONIEC
```
