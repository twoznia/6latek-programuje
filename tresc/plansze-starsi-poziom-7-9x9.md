# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (1/4)

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

# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (2/4)

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

---

# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (3/4)

### 9. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 10 kart. Przepis A musi wołać sam siebie.
```plansza
* . . . . . . * .
. . . . . . . . .
. . * . . * . . .
. . . . . . . . .
. . . . * * . . .
. . . . . . . . .
. . * . . . . * .
. . . . . . . . .
^ . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
N = 6
N + 2
ZRÓB A ×N
```

### 10. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L * L L L L
L L L L . L L L L
L L * . * . * L L
L L . L . L . L L
* . * . ^ . * . *
L L . L . L . L L
L L * . * . * L L
L L L L . L L L L
L L L L * L L L L
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×2, N − 1, ZRÓB A ×N, N + 1, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W LEWO
    KONIEC
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

### 11. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
L L L * L L L L L
L L * . L L L L L
L * . . L L L L L
* . . . L L L L L
> . . . . L L L L
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

### 12. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
L L L L L L L L L
* L L L L L L * L
. * L L L L * . L
. . * L L * . . L
. . . * * . . . L
> . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

---

# Plansze 9 × 9 dla starszych, poziom 7 (trudny) (4/4)

### 13. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart. Warianty pól ?: 1) · · · # · S; 2) · · # · S ·; 3) # S · · · ·. Przepis A musi wołać sam siebie.
```plansza
? . . . . . . . .
. . . . . . . ? .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
? . . . . . . . .
? . ? . . . . . .
. ? . . . . . . .
^ . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

### 14. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart. Warianty pól ?: 1) # · S · · ·; 2) · # · S · ·; 3) · · · · # S. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . ? . . .
. . . . ? ? . . .
. . . . ? . . . .
. . . . . . . . .
. ? . . . . . . .
. ? . . . . . . .
^ . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

### 15. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart. Warianty pól ?: 1) · · S; 2) · S ·; 3) S · ·. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L
. . ? . ? . . L L
. L L L L L . L L
. L L L L L . L L
. L L L L L ? L L
. L L . . . . L L
. L L L L L L L L
. L L L L L L L L
^ L L L L L L L L
```
```kod
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    JEŚLI WOLNE?
      IDŹ, ZRÓB A, IDŹ
    NIE
      SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
ZRÓB A
```

### 16. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart. Warianty pól ?: 1) · · S; 2) · S ·; 3) S · ·. Przepis A musi wołać sam siebie.
```plansza
L . . . . ? . . .
L . L L L L L L .
L . L L L ? L L .
L . L L L . L L .
L . L L L . L L .
L . ? . . . L L .
L L L L L L L L .
L L L L L L L L .
L L L L L L L L ^
```
```kod
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    JEŚLI WOLNE?
      IDŹ, ZRÓB A, IDŹ
    NIE
      SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
ZRÓB A
```
