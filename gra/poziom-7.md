# Gra online, poziom 7 (trudny)

Źródło gier poziomu 7 w grze online i w druku (`plansze-starsi-poziom-7-*`). Gry generuje `narzedzia/generatory/poziom7.py`. Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **rekurencja** (ustawienie `rekurencja: tak`): karta ZRÓB A może leżeć w samym przepisie A, więc przepis woła sam siebie. Każde wywołanie ma swoje N (z `parametr: tak`), a karty po ZRÓB A wykonują się dopiero po powrocie, w odwrotnej kolejności. **META** w przepisie kończy tylko bieżące wywołanie (wczesny powrót, *return*). Bez warunku stopu robot się „zapętla”: po 40 wywołaniach gra przerywa program.

## Plansza 5 × 5

### Zestaw A: Rekurencja
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 1. Tam i z powrotem
Bez zmiennej i bez liczenia! Przepis A: jeśli wolne, IDŹ, ZRÓB A (cały przepis jeszcze raz), IDŹ. Jeśli nie, OBRÓĆ SIĘ. Każde IDŹ po ZRÓB A czeka, aż wróci wywołanie, więc robot wraca tyle samo kroków. Wróć na START. Masz tylko 8 kart.
```plansza
. . . . .
. L . . .
. . > ? ?
. L . . .
. . . . .
```
```ustawienia
limit: 8
warianty: *# .*
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, ZRÓB A, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 2. Wczesny powrót
Przepis zaczyna od strażnika: jeśli przed robotem nie jest wolne, OBRÓĆ SIĘ i META (powrót z tego wywołania). Po każdym powrocie robot robi 2 kroki, więc dochodzi dwa razy dalej, do drugiego skarbu za START. Masz tylko 10 kart.
```plansza
. . . . .
. . . . .
? ? > ? ?
. . . . .
. . . . .
```
```ustawienia
limit: 10
warianty: .**# *..*
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    OBRÓĆ SIĘ, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ, IDŹ
KONIEC
ZRÓB A
```

#### 3. Po skarb i z powrotem
Za skarbem pole jest wolne, więc DOPÓKI WOLNE? tu nie pomoże. Przepis pyta: skarb? Jeśli tak, weź go i zawróć. Jeśli nie, IDŹ, ZRÓB A, IDŹ. Wróć na START. Masz tylko 10 kart.
```plansza
. . . . .
. . . . .
. > ? ? .
. . . . .
. . . . .
```
```ustawienia
limit: 10
warianty: *. .*
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A
```

#### 4. Dwa korytarze
Skarb jest po prawej i po lewej stronie START. Ten sam przepis co w poprzedniej grze: po pierwszym ZRÓB A robot stoi na START, ale patrzy w drugą stronę. Wróć na START. Masz tylko 10 kart.
```plansza
. . . . .
L . L . L
? ? > ? ?
. . . . .
. . . . .
```
```ustawienia
limit: 10
warianty: *..* .**. .*.*
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A ×2
```

### Zestaw B: Rekurencja z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 5. Kwadraty w kwadratach
Przepis A rysuje kwadrat o boku N, a potem woła sam siebie z N − 1. Kończy się, gdy N = 0. Program to jedno ZRÓB A ×4. Masz tylko 10 kart.
```plansza
. . . . *
. . . * .
. . * . .
. * . . .
^ . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 6. Góra z rekurencji
W drodze w górę robot robi schodki przed ZRÓB A, a w drodze w dół te karty, które leżą po ZRÓB A. Szczyt to moment, gdy N = 0. Masz tylko 15 kart.
```plansza
L L L L L
L L L L L
L * * * L
* * L * *
^ L L L *
```
```ustawienia
limit: 15
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1, ZRÓB A ×N
    SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

#### 7. Spirala z rekurencji
Dwa boki po N pól i wywołanie z N − 1. Robot kończy w środku planszy. Masz tylko 10 kart.
```plansza
* . . . *
. * . * .
. . * * .
. * . . *
^ . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×2
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 8. Drzewo
Pień o długości N, a na jego końcu dwie gałęzie: mniejsze drzewa z N − 1, w lewo i w prawo. Każdy liść to skarb. Robot wraca pod pień. Wróć na START. Masz tylko 14 kart.
```plansza
L L L L L
L L L L L
L * . * L
L L . L L
L L ^ L L
```
```ustawienia
limit: 14
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, N − 1, SKRĘĆ W LEWO, ZRÓB A ×N
    OBRÓĆ SIĘ, ZRÓB A ×N
    SKRĘĆ W PRAWO, N + 1, IDŹ ×N, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

## Plansza 7 × 7

### Zestaw A: Rekurencja
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 1. Tam i z powrotem
Bez zmiennej i bez liczenia! Przepis A: jeśli wolne, IDŹ, ZRÓB A (cały przepis jeszcze raz), IDŹ. Jeśli nie, OBRÓĆ SIĘ. Każde IDŹ po ZRÓB A czeka, aż wróci wywołanie, więc robot wraca tyle samo kroków. Wróć na START. Masz tylko 8 kart.
```plansza
. . . . . . .
. . . . . . .
. L . . . . .
. . > ? ? ? ?
. L . . . . .
. . . . . . .
. . . . . . .
```
```ustawienia
limit: 8
warianty: *#.. .*#. ..*# ...*
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, ZRÓB A, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 2. Wczesny powrót
Przepis zaczyna od strażnika: jeśli przed robotem nie jest wolne, OBRÓĆ SIĘ i META (powrót z tego wywołania). Po każdym powrocie robot robi 2 kroki, więc dochodzi dwa razy dalej, do drugiego skarbu za START. Masz tylko 10 kart.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
? ? ? > ? ? ?
. . . . . . .
. . . . . . .
. . . . . . .
```
```ustawienia
limit: 10
warianty: ..**#. .*..*# *....*
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    OBRÓĆ SIĘ, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ, IDŹ
KONIEC
ZRÓB A
```

#### 3. Po skarb i z powrotem
Za skarbem pole jest wolne, więc DOPÓKI WOLNE? tu nie pomoże. Przepis pyta: skarb? Jeśli tak, weź go i zawróć. Jeśli nie, IDŹ, ZRÓB A, IDŹ. Wróć na START. Masz tylko 10 kart.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
. > ? ? ? ? .
. . . . . . .
. . . . . . .
. . . . . . .
```
```ustawienia
limit: 10
warianty: *... .*.. ..*. ...*
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A
```

#### 4. Dwa korytarze
Skarb jest po prawej i po lewej stronie START. Ten sam przepis co w poprzedniej grze: po pierwszym ZRÓB A robot stoi na START, ale patrzy w drugą stronę. Wróć na START. Masz tylko 10 kart.
```plansza
. . . . . . .
. . . . . . .
L . L . L . L
? ? ? > ? ? ?
. . . . . . .
. . . . . . .
. . . . . . .
```
```ustawienia
limit: 10
warianty: *....* .*..*. ..**..
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A ×2
```

### Zestaw B: Rekurencja z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 5. Kwadraty w kwadratach
Przepis A rysuje kwadrat o boku N, a potem woła sam siebie z N − 1. Kończy się, gdy N = 0. Program to jedno ZRÓB A ×6. Masz tylko 10 kart.
```plansza
. . . . . . *
. . . . . * .
. . . . * . .
. . . * . . .
. . * . . . .
. * . . . . .
^ . . . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

#### 6. Góra z rekurencji
W drodze w górę robot robi schodki przed ZRÓB A, a w drodze w dół te karty, które leżą po ZRÓB A. Szczyt to moment, gdy N = 0. Masz tylko 15 kart.
```plansza
L L L L L L L
L L L L L L L
L L L L L L L
L L * * * L L
L * * L * * L
* * L L L * *
^ L L L L L *
```
```ustawienia
limit: 15
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1, ZRÓB A ×N
    SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×3
```

#### 7. Spirala z rekurencji
Dwa boki po N pól i wywołanie z N − 1. Robot kończy w środku planszy. Masz tylko 10 kart.
```plansza
* . . . . . *
. * . . . * .
. . * . * . .
. . . * * . .
. . * . . * .
. * . . . . *
^ . . . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×2
      IDŹ ×N, SKRĘĆ W PRAWO
    KONIEC
    N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

#### 8. Drzewo
Pień o długości N, a na jego końcu dwie gałęzie: mniejsze drzewa z N − 1, w lewo i w prawo. Każdy liść to skarb. Robot wraca pod pień. Wróć na START. Masz tylko 14 kart.
```plansza
L L L L L L L
L L L L L L L
L * L L L * L
L . . . . . L
L * L . L * L
L L L . L L L
L L L ^ L L L
```
```ustawienia
limit: 14
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, N − 1, SKRĘĆ W LEWO, ZRÓB A ×N
    OBRÓĆ SIĘ, ZRÓB A ×N
    SKRĘĆ W PRAWO, N + 1, IDŹ ×N, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×3
```

## Plansza 9 × 9

### Zestaw A: Rekurencja
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 1. Tam i z powrotem
Bez zmiennej i bez liczenia! Przepis A: jeśli wolne, IDŹ, ZRÓB A (cały przepis jeszcze raz), IDŹ. Jeśli nie, OBRÓĆ SIĘ. Każde IDŹ po ZRÓB A czeka, aż wróci wywołanie, więc robot wraca tyle samo kroków. Wróć na START. Masz tylko 8 kart.
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
```ustawienia
limit: 8
warianty: *#.... .*#... ..*#.. .....*
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, ZRÓB A, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 2. Wczesny powrót
Przepis zaczyna od strażnika: jeśli przed robotem nie jest wolne, OBRÓĆ SIĘ i META (powrót z tego wywołania). Po każdym powrocie robot robi 2 kroki, więc dochodzi dwa razy dalej, do drugiego skarbu za START. Masz tylko 10 kart.
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
```ustawienia
limit: 10
warianty: ...**#.. ..*..*#. .*....*# *......*
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    OBRÓĆ SIĘ, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ, IDŹ
KONIEC
ZRÓB A
```

#### 3. Po skarb i z powrotem
Za skarbem pole jest wolne, więc DOPÓKI WOLNE? tu nie pomoże. Przepis pyta: skarb? Jeśli tak, weź go i zawróć. Jeśli nie, IDŹ, ZRÓB A, IDŹ. Wróć na START. Masz tylko 10 kart.
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
```ustawienia
limit: 10
warianty: *..... ..*... ....*.
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A
```

#### 4. Dwa korytarze
Skarb jest po prawej i po lewej stronie START. Ten sam przepis co w poprzedniej grze: po pierwszym ZRÓB A robot stoi na START, ale patrzy w drugą stronę. Wróć na START. Masz tylko 10 kart.
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
```ustawienia
limit: 10
warianty: *......* .*...*.. ...**...
```
```rozwiazanie
PRZEPIS A
  JEŚLI SKARB?
    IDŹ, OBRÓĆ SIĘ, IDŹ
  NIE
    IDŹ, ZRÓB A, IDŹ
  KONIEC
KONIEC
ZRÓB A ×2
```

### Zestaw B: Rekurencja z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 5. Kwadraty w kwadratach
Przepis A rysuje kwadrat o boku N, a potem woła sam siebie z N − 1. Kończy się, gdy N = 0. Program to jedno ZRÓB A ×8 (8 to N = 6, potem N + 2, potem ZRÓB A ×N). Masz tylko 12 kart.
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
```ustawienia
limit: 12
```
```rozwiazanie
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

#### 6. Góra z rekurencji
W drodze w górę robot robi schodki przed ZRÓB A, a w drodze w dół te karty, które leżą po ZRÓB A. Szczyt to moment, gdy N = 0. Masz tylko 15 kart.
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
```ustawienia
limit: 15
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1, ZRÓB A ×N
    SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ, OBRÓĆ SIĘ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 7. Spirala z rekurencji
Dwa boki po N pól i wywołanie z N − 1. Robot kończy w środku planszy. Masz tylko 12 kart.
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
```ustawienia
limit: 12
```
```rozwiazanie
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

#### 8. Drzewo
Pień o długości N, a na jego końcu dwie gałęzie: mniejsze drzewa z N − 1, w lewo i w prawo. Każdy liść to skarb. Robot wraca pod pień. Wróć na START. Masz tylko 14 kart.
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
```ustawienia
limit: 14
```
```rozwiazanie
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
