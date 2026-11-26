# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. „Masz tylko N kart” liczy wszystkie karty poleceń, także KONIEC i NIE, ale nie liczby. Pola ?: dorosły przed każdą próbą kładzie na nich to, co podaje jeden z wariantów (pola ? czytamy jak książkę: od lewej do prawej, z góry na dół; S skarb, · puste, # klocek, L lawa, K kałuża). Program ma zadziałać w każdym wariancie.

### 1. Diament
Robot chodzi po schodkach dookoła lawy. Jeden schodek to IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO. Zbierz skarby i wróć na START. Masz tylko 9 kart, więc włóż pętlę do pętli.
```plansza
# . * . #
. . . . .
^ . L . *
. . . . .
# . * . #
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×2
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 2. Ósemka
Robot obchodzi dwa kwadraty: jeden w górę, drugi w dół. Zbierz skarby i wróć na START. Masz tylko 7 kart.
```plansza
# # . . *
# L . L .
. . ^ . .
. L . L #
* . . # #
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

### 3. Góra
Wejdź po schodkach na szczyt i zejdź z drugiej strony. Pod górą jest lawa. Masz tylko 9 kart.
```plansza
. . . . .
. # . # .
# . * . #
. * L * .
^ L L L *
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×2
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 4. Do ściany
Nowa karta DOPÓKI! Robot pyta: czy przed nami jest wolne pole? Dopóki TAK, robi IDŹ. Klocek za każdym razem stoi gdzie indziej. Masz tylko 3 karty. Warianty pól ?: 1) S · ·; 2) # S ·; 3) L · S.
```plansza
. . ? . .
. . ? . .
. . ? . .
. . . . .
. . ^ . .
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ
KONIEC
```

---

# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (2/4)

### 5. Tam i z powrotem
Idź, dopóki przed tobą nie ma skarbu. Weź skarb i wróć na START. Skarb za każdym razem leży gdzie indziej. Masz tylko 8 kart. Warianty pól ?: 1) S · · ·; 2) · S · ·; 3) · · S ·; 4) · · · S.
```plansza
. . . . .
. L . L .
> ? ? ? ?
. L . L .
. . . . .
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

### 6. Za róg
Idź w górę aż do przeszkody, skręć w prawo i idź aż do końca. Masz tylko 7 kart. Warianty pól ?: 1) · S · · · ·; 2) # · · S · ·; 3) # · # · · S.
```plansza
? . . . ?
? . . . ?
? . . . ?
. . . . .
^ . . . .
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

### 7. Pokój
Pokój raz jest duży, a raz mały. Obejdź go dookoła, zbierz skarby w rogach i wróć na START. Masz tylko 6 kart. Warianty pól ?: 1) · S · · · · S; 2) S # # # # S #.
```plansza
* . . ? ?
. . . . ?
. . L . ?
. . . . ?
^ . . ? ?
```
```rozwiazanie
POWTÓRZ ×4
  DOPÓKI WOLNE?
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 8. Kałuże w rzędzie
Kałuże są za każdym razem gdzie indziej. Dopóki nie ma ściany: jeśli przed robotem jest kałuża, SKOCZ, a jeśli nie, IDŹ. Masz tylko 7 kart. Warianty pól ?: 1) K · ·; 2) · K ·; 3) · · K; 4) K · K.
```plansza
. L . L .
. . . . .
> ? ? ? *
. . . . .
. L . L .
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

---

# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (3/4)

### 9. Plus
Cztery ramiona po 2 pola. Na końcu każdego ramienia obróć się i wróć do środka. Masz tylko 6 kart.
```plansza
L L * L L
L L . L L
* . ^ . *
L L . L L
L L * L L
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 10. Grzebień
Robot idzie w prawo i co drugie pole robi ząb grzebienia: 3 w górę i z powrotem. Masz tylko 8 kart.
```plansza
L L L L L
L L * L *
L L . L .
L L . L .
> . * . *
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×3, SKRĘĆ W LEWO
KONIEC
```

### 11. Okno
Cztery kwadraty wokół START, jak szybki w oknie. Po każdym kwadracie robot skręca w prawo. Masz tylko 7 kart.
```plansza
* . * . *
. L . L .
* . ^ . *
. L . L .
* . * . *
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 12. Schody w górę i w dół
4 schodków w górę, obrót i te same karty jeszcze raz. Robot schodzi inną drogą! Wróć na START. Masz tylko 9 kart.
```plansza
L L L * *
L L * * *
L * * * L
* * * L L
^ * L L L
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

---

# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (4/4)

### 13. Do klocka i w prawo
Idź, dopóki jest wolne, skręć w prawo i znowu idź, dopóki jest wolne. Klocki za każdym razem stoją gdzie indziej. Masz tylko 7 kart. Warianty pól ?: 1) # · · S # · · ·; 2) · # · · · # · S; 3) · · # · # · S ·.
```plansza
? . . . ?
? . ? ? .
? . . . ?
. . . . ?
^ . . . .
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
Przejdź dolny rząd do ściany, wejdź piętro wyżej i wróć górnym rzędem. Kałuże przeskakuj. Masz tylko 12 kart. Warianty pól ?: 1) · K · · ·; 2) · K · K ·; 3) K · · · ·; 4) · · K · K.
```plansza
. . . . .
. . . . .
. . . . .
* ? ? ? .
> ? ? . *
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
Trzy razy: idź, dopóki jest wolne, i skręć w prawo. Skarb leży tam, gdzie robot stanie. Masz tylko 6 kart. Warianty pól ?: 1) · · # # · · S; 2) · # · · # · S; 3) # · # · · S ·.
```plansza
. . . . ?
? . ? ? .
. . . . .
. ? . . .
^ . . ? ?
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
Idź do skarbu, weź go, obróć się i idź do ściany. Wróć na START. Masz tylko 8 kart. Warianty pól ?: 1) · S ·; 2) · · S; 3) S · ·.
```plansza
. . . . .
L . L . L
> ? . ? ?
. . . . .
. . . . .
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
