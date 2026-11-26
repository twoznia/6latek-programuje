# Plansze 9 × 9 dla starszych, poziom 4 (dla 12-latka) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. „Masz tylko N kart” liczy wszystkie karty poleceń, także KONIEC i NIE, ale nie liczby. Pola ?: dorosły przed każdą próbą kładzie na nich to, co podaje jeden z wariantów (pola ? czytamy jak książkę: od lewej do prawej, z góry na dół; S skarb, · puste, # klocek, L lawa, K kałuża). Program ma zadziałać w każdym wariancie.

### 1. Spirala rośnie
Każdy bok spirali jest o 1 dłuższy. Na początku N = 1, a po każdym boku N + 1. Zbierz skarby. Masz tylko 8 kart.
```plansza
. . L . L . . L .
. L * . . . . . *
. . . . . L L L .
. . . . * . * . .
. . . L ^ . . . .
. . . L . L . . .
. L * . . . * . .
. L . . L . . L .
* . . . . . . . *
```
```rozwiazanie
N = 1
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO, N + 1
  KONIEC
KONIEC
```

### 2. Schody coraz wyższe
Każdy schodek jest o 1 wyższy i o 1 szerszy od poprzedniego. Masz tylko 8 kart.
```plansza
. . . L . . . L .
. L . . L . . . L
. . . * . . * . L
. . . . . L L L .
. . . . . . . L .
. * . * L L . L .
. . . . . L . . .
* * L . L L . . .
^ . L L . L L . L
```
```rozwiazanie
N = 1
POWTÓRZ ×3
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N + 1
KONIEC
```

### 3. Kwadraty coraz większe
Wszystkie kwadraty zaczynają się w rogu START, a każdy jest o 1 większy. Masz tylko 8 kart.
```plansza
. . . . . . . . *
. . . . . . . * .
. . . . . . * . .
. . . . . * . . .
. . . . * . . . .
. . . * . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
N = 3
POWTÓRZ ×6
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N + 1
KONIEC
```

### 4. Licz i wracaj
Robot nie wie, jak daleko jest skarb. Idź do skarbu i licz kroki w N. Potem obróć się i zrób IDŹ ×N, żeby wrócić na START. Masz tylko 6 kart. Warianty pól ?: 1) · · · # S; 2) · # S · ·; 3) S · · · ·.
```plansza
. . . . ? . . . .
. . . . ? . . . .
. . L . ? . L . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ^ . . . .
. . L . . . L . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N
```

---

# Plansze 9 × 9 dla starszych, poziom 4 (dla 12-latka) (2/2)

### 5. Lustro
Drugi skarb jest tak samo daleko za robotem, jak pierwszy przed nim. Policz kroki do pierwszego skarbu, a potem przejdź dwa razy tyle w drugą stronę. Masz tylko 7 kart. Warianty pól ?: 1) · · # S S · · ·; 2) · # S · · S · ·; 3) # S · · · · S ·; 4) S · · · · · · S.
```plansza
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. L . . ^ . . L .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N, IDŹ ×N
```

### 6. Policz skarby
Idź do końca rzędu i licz skarby w N. Ostatni skarb leży nad końcem rzędu, dokładnie N pól w górę. Masz tylko 9 kart. Warianty pól ?: 1) · · · · · · S · · · S · · · ·; 2) · · · · S · · · S · · · S · S; 3) · · · S · · · S · S · S · S ·; 4) S · · · · · · S S S · S S S S.
```plansza
. . . . . . . . .
. . L . . L . . ?
. L . . L . . . ?
. . . L . . L . ?
. . L . . L . . ?
. L . . L . . . ?
. . . L . . L . ?
. . . . . . . . ?
> ? ? ? ? ? ? ? ?
```
```rozwiazanie
DOPÓKI WOLNE?
  JEŚLI SKARB?
    N + 1
  NIE
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO, IDŹ ×N
```

### 7. Schody coraz niższe
Pierwszy schodek jest najwyższy, a każdy następny o 1 niższy. Pętla DOPÓKI N > 0? kończy się sama, gdy N spadnie do zera. Masz tylko 8 kart.
```plansza
. . . . . . L . L
. . L . . . . L .
. . L . . * * L L
. L . * . * . . .
. L L . . . . . L
* . . * L . . L .
. . L . . . . . .
. . . L L L . . .
^ . . . . . . . .
```
```rozwiazanie
N = 3
DOPÓKI N > 0?
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N − 1
KONIEC
```

### 8. Spirala do środka
Dwa boki po N pól, potem N − 1. I tak, dopóki N > 0. Robot kończy w samym środku. Najwyższa karta liczby to 6, więc N = 8 trzeba zrobić z dwóch kart. Masz tylko 9 kart.
```plansza
. . . . . . . . *
. * . . . . . . .
. . . . . . . . .
. . . . . * . . .
. . . . * . . . .
. . . . . . * . .
. . * . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
N = 6
N + 2
DOPÓKI N > 0?
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N − 1
KONIEC
```
