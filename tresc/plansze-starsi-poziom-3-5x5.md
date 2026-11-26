# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (1/2)

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

# Plansze 5 × 5 dla starszych, poziom 3 (dla 8-latka) (2/2)

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
