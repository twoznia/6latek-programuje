# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Tam i z powrotem
Bez zmiennej i bez liczenia! Przepis A: jeśli wolne, IDŹ, ZRÓB A (cały przepis jeszcze raz), IDŹ. Jeśli nie, OBRÓĆ SIĘ. Każde IDŹ po ZRÓB A czeka, aż wróci wywołanie, więc robot wraca tyle samo kroków. Wróć na START. Masz tylko 8 kart. Warianty pól ?: 1) S # · · · ·; 2) · S # · · ·; 3) · · S # · ·; 4) · · · · · S. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. L . . . . . . .
. . > ? ? ? ? ? ?
. L . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, ZRÓB A, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

### 2. Wczesny powrót
Przepis zaczyna od strażnika: jeśli przed robotem nie jest wolne, OBRÓĆ SIĘ i META (powrót z tego wywołania). Po każdym powrocie robot robi 2 kroki, więc dochodzi dwa razy dalej, do drugiego skarbu za START. Masz tylko 10 kart. Warianty pól ?: 1) · · · S S # · ·; 2) · · S · · S # ·; 3) · S · · · · S #; 4) S · · · · · · S. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
? ? ? ? > ? ? ? ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI NIE WOLNE?
    OBRÓĆ SIĘ, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ, IDŹ
KONIEC
ZRÓB A
```

### 3. Po skarb i z powrotem
Za skarbem pole jest wolne, więc DOPÓKI WOLNE? tu nie pomoże. Przepis pyta: skarb? Jeśli tak, weź go i zawróć. Jeśli nie, IDŹ, ZRÓB A, IDŹ. Wróć na START. Masz tylko 10 kart. Warianty pól ?: 1) S · · · · ·; 2) · · S · · ·; 3) · · · · S ·. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. > ? ? ? ? ? ? .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A
```

### 4. Dwa korytarze
Skarb jest po prawej i po lewej stronie START. Ten sam przepis co w poprzedniej grze: po pierwszym ZRÓB A robot stoi na START, ale patrzy w drugą stronę. Wróć na START. Masz tylko 10 kart. Warianty pól ?: 1) S · · · · · · S; 2) · S · · · S · ·; 3) · · · S S · · ·. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
L . L . L . L . L
? ? ? ? > ? ? ? ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A ×2
```

---

# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (2/2)

### 5. Kwadraty w kwadratach
Przepis A rysuje kwadrat o boku N, a potem woła sam siebie z N − 1. Kończy się, gdy N = 0. Program to jedno ZRÓB A ×8 (8 to N = 6, potem N + 2, potem ZRÓB A ×N). Masz tylko 12 kart. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . *
. . . . . . . * .
. . . . . . * . .
. . . . . * . . .
. . . . * . . . .
. . . * . . . . .
. . * . . . . . .
. * . . . . . . .
^ . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
N = 6
N + 2
ZRÓB A ×N
```

### 6. Góra z rekurencji
W drodze w górę robot robi schodki przed ZRÓB A, a w drodze w dół te karty, które leżą po ZRÓB A. Szczyt to moment, gdy N = 0. Masz tylko 15 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
L L L * * * L L L
L L * * L * * L L
L * * L L L * * L
* * L L L L L * *
^ L L L L L L L *
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1, ZRÓB A ×N
    SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

### 7. Spirala z rekurencji
Dwa boki po N pól i wywołanie z N − 1. Robot kończy w środku planszy. Masz tylko 12 kart. Przepis A musi wołać sam siebie.
```plansza
* . . . . . . . *
. * . . . . . * .
. . * . . . * . .
. . . * . * . . .
. . . . * * . . .
. . . * . . * . .
. . * . . . . * .
. * . . . . . . *
^ . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×2
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
N = 6
N + 2
ZRÓB A ×N
```

### 8. Drzewo
Pień o długości N, a na jego końcu dwie gałęzie: mniejsze drzewa z N − 1, w lewo i w prawo. Każdy liść to skarb. Robot wraca pod pień. Wróć na START. Masz tylko 14 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L
L L L L L L L L L
* . * L L L * . *
L . L L L L L . L
L . . . . . . . L
L . L L . L L . L
* . * L . L * . *
L L L L . L L L L
L L L L ^ L L L L
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, N − 1, SKRĘĆ W LEWO, ZRÓB A ×N
    OBRÓĆ SIĘ, ZRÓB A ×N
    SKRĘĆ W PRAWO, N + 1, IDŹ ×N, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```
