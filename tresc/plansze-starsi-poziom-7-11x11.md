# Plansze 11 × 11 dla starszych, poziom 7 (trudny) (1/2)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie (na dole karty) jest zapisane tekstem: wcięcie to wnętrze pętli, pytania albo przepisu. Pola ? i warianty: S skarb, · puste, # klocek, L lawa, K kałuża, pola ? czytamy od lewej do prawej, z góry na dół. Program ma zadziałać w każdym wariancie.

### 1. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 10 kart. Przepis A musi wołać sam siebie.
```plansza
* . . . . . . . . * .
. . . . . . . . . . .
. . * . . . . * . . .
. . . . . . . . . . .
. . . . * * . . . . .
. . . . . . . . . . .
. . . . * . . * . . .
. . . . . . . . . . .
. . * . . . . . . * .
. . . . . . . . . . .
^ . . . . . . . . . .
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
N = 6
N + 4
ZRÓB A ×N
```

### 2. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L L L
L L L L L * L L L L L
L L L L L . L L L L L
L L L * . * . * L L L
L L L . L . L . L L L
L * . * . ^ . * . * L
L L L . L . L . L L L
L L L * . * . * L L L
L L L L L . L L L L L
L L L L L * L L L L L
L L L L L L L L L L L
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

### 3. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L * L L L L L
L L L L * . L L L L L
L L L * . . L L L L L
L L * . . . L L L L L
L * . . . . L L L L L
* . . . . . L L L L L
> . . . . . . L L L L
```
```kod
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

### 4. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart. Przepis A musi wołać sam siebie.
```plansza
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L L L L L L L
L L L L L L L L L L L
* L L L L L L L L * L
. * L L L L L L * . L
. . * L L L L * . . L
. . . * L L * . . . L
. . . . * * . . . . L
> . . . . . . . . . .
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
ZRÓB A ×5
```

---

# Plansze 11 × 11 dla starszych, poziom 7 (trudny) (2/2)

### 5. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart. Warianty pól ?: 1) · · · · # S; 2) # S · · · ·; 3) · · # S · ·. Przepis A musi wołać sam siebie.
```plansza
? . . . . . . . . . .
. . . . . . . . . ? .
. . . . . . . . . . .
. . . . . . . . . . .
? . . . . . . . . . .
. . . . . ? . . . . .
. . . . . . . . . . .
? . . . . . . . . . .
. . ? . . . . . . . .
. . . . . . . . . . .
^ . . . . . . . . . .
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

### 6. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart. Warianty pól ?: 1) · · # · S ·; 2) · · · # · S; 3) # S · · · ·. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . . . .
. . . . . . . . ? . .
. . . . . . . . ? . .
. . . . . . . . . . .
. . . . . ? . . . . .
. . . . ? ? . . . . .
. . . . ? . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
^ . . . . . . . . . .
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

### 7. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart. Warianty pól ?: 1) · S ·; 2) · · S; 3) S · ·. Przepis A musi wołać sam siebie.
```plansza
. . . . . . . . . L L
. L L L L L L L . L L
. L L L L L L L ? L L
. L . . . L L L . L L
. L . L L L L L . L L
. L ? L L L L L ? L L
. L . L L L L L . L L
. L . . . . . . . L L
. L L L L L L L L L L
. L L L L L L L L L L
^ L L L L L L L L L L
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

### 8. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart. Warianty pól ?: 1) · S ·; 2) S · ·; 3) · · S. Przepis A musi wołać sam siebie.
```plansza
L ? . . . ? . . . . .
L . L L L L L L L L .
L . L L L L L L L L .
L . L L L L L L L L .
L ? L L L . . . L L .
L . L L L L L . L L .
L . L L L L L . L L .
L . L L L L L . L L .
L . . . . . . . L L .
L L L L L L L L L L .
L L L L L L L L L L ^
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
