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

### Zestaw C: Rekurencja rysuje
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 9. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 8 kart.
```plansza
* . . * .
. . . . .
. . * * .
. . . . .
^ . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 10. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart.
```plansza
L L * L L
L * * * L
* * ^ * *
L * * * L
L L * L L
```
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ, N − 1, ZRÓB A ×N, N + 1, OBRÓĆ SIĘ, IDŹ, SKRĘĆ W LEWO
    KONIEC
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

#### 11. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart.
```plansza
L L L L L
L L * L L
L * . L L
* . . L L
> . . . L
```
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×3
```

#### 12. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart.
```plansza
L L L L L
L L L L L
* L L * L
. * * . L
> . . . .
```
```ustawienia
limit: 19
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

### Zestaw D: Powrót po śladach
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 13. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart.
```plansza
? . . . .
? . . ? .
? . ? . .
. ? . . .
^ . . . .
```
```ustawienia
limit: 9
warianty: .#..*. ...#.* #.*...
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

#### 14. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart.
```plansza
. . . ? .
. . ? ? .
. ? ? . .
. ? . . .
^ . . . .
```
```ustawienia
limit: 14
warianty: .#..*. ...#.* #.*...
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 15. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart.
```plansza
. ? ? . L
. L L L L
? L L L L
. L L L L
^ L L L L
```
```ustawienia
limit: 16
warianty: .*. ..* *..
```
```rozwiazanie
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

#### 16. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart.
```plansza
L ? . . .
L . L L ?
L ? L L .
L L L L .
L L L L ^
```
```ustawienia
limit: 16
warianty: .*. ..* *..
```
```rozwiazanie
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

### Zestaw C: Rekurencja rysuje
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 9. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 8 kart.
```plansza
* . . . . * .
. . . . . . .
. . * * . . .
. . . . . . .
. . * . . * .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

#### 10. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart.
```plansza
L L L L L L L
L L L * L L L
L L * * * L L
L * * ^ * * L
L L * * * L L
L L L * L L L
L L L L L L L
```
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ, N − 1, ZRÓB A ×N, N + 1, OBRÓĆ SIĘ, IDŹ, SKRĘĆ W LEWO
    KONIEC
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

#### 11. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart.
```plansza
L L L L L L L
L L L L L L L
L L L L L L L
L L * L L L L
L * . L L L L
* . . L L L L
> . . . L L L
```
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×3
```

#### 12. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart.
```plansza
L L L L L L L
L L L L L L L
L L L L L L L
* L L L L * L
. * L L * . L
. . * * . . L
> . . . . . .
```
```ustawienia
limit: 19
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×3
```

### Zestaw D: Powrót po śladach
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 13. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart.
```plansza
. . . . . . .
? . . . . . .
? . . . ? . .
? . . ? . . .
. . ? . . . .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 9
warianty: ...#.* .#..*. #.*...
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

#### 14. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart.
```plansza
. . . . . ? .
. . . . ? ? .
. . . . ? . .
. . ? . . . .
. . ? . . . .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 14
warianty: .#.*.. ....#* #.*...
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 15. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart.
```plansza
. . . ? . L L
? L L L ? L L
. L L L . L L
. L L L L L L
. L L L L L L
. L L L L L L
^ L L L L L L
```
```ustawienia
limit: 16
warianty: ..* *.. .*.
```
```rozwiazanie
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

#### 16. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart.
```plansza
L L L L L L L
L L L . . . ?
L L L ? L L .
L L L . L L ?
L L L L L L .
L L L L L L .
L L L L L L ^
```
```ustawienia
limit: 16
warianty: ..* .*. *..
```
```rozwiazanie
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

### Zestaw C: Rekurencja rysuje
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 9. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 10 kart.
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
```ustawienia
limit: 10
```
```rozwiazanie
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

#### 10. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart.
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
```ustawienia
limit: 13
```
```rozwiazanie
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

#### 11. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart.
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
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 12. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart.
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
```ustawienia
limit: 19
```
```rozwiazanie
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

### Zestaw D: Powrót po śladach
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 13. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart.
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
```ustawienia
limit: 9
warianty: ...#.* ..#.*. #*....
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

#### 14. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart.
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
```ustawienia
limit: 14
warianty: #.*... .#.*.. ....#*
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 15. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart.
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
```ustawienia
limit: 16
warianty: ..* .*. *..
```
```rozwiazanie
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

#### 16. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart.
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
```ustawienia
limit: 16
warianty: ..* .*. *..
```
```rozwiazanie
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

## Plansza 11 × 11

### Zestaw A: Rekurencja rysuje
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 1. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 10 kart.
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
```ustawienia
limit: 10
```
```rozwiazanie
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

#### 2. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart.
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
```ustawienia
limit: 13
```
```rozwiazanie
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

#### 3. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 13 kart.
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
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

#### 4. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart.
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
```ustawienia
limit: 19
```
```rozwiazanie
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

### Zestaw B: Powrót po śladach
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 5. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart.
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
```ustawienia
limit: 9
warianty: ....#* #*.... ..#*..
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

#### 6. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart.
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
```ustawienia
limit: 14
warianty: ..#.*. ...#.* #*....
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 7. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart.
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
```ustawienia
limit: 16
warianty: .*. ..* *..
```
```rozwiazanie
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

#### 8. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart.
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
```ustawienia
limit: 16
warianty: .*. *.. ..*
```
```rozwiazanie
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


## Plansza 13 × 13

### Zestaw A: Rekurencja rysuje
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A, META
pytania: N > 0?, N = 0?, WOLNE?, NIE WOLNE?
rekurencja: tak
parametr: tak
wymagaj: rekurencja

#### 1. Ślimak z rekurencji
Bok o długości N, skręt i wywołanie z N − 1. Kończy się, gdy N = 0. Masz tylko 10 kart.
```plansza
* . . . . . . . . . . * .
. . . . . . . . . . . . .
. . * . . . . . . * . . .
. . . . . . . . . . . . .
. . . . * . . * . . . . .
. . . . . . . . . . . . .
. . . . . . * * . . . . .
. . . . . . . . . . . . .
. . . . * . . . . * . . .
. . . . . . . . . . . . .
. . * . . . . . . . . * .
. . . . . . . . . . . . .
^ . . . . . . . . . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    IDŹ ×N, SKRĘĆ W PRAWO, N − 1, ZRÓB A ×N
  NIE
  KONIEC
KONIEC
N = 6
N + 6
ZRÓB A ×N
```

#### 2. Płatek śniegu
Plus, a na końcu każdego ramienia mniejszy plus. Robot wraca do środka. Wróć na START. Masz tylko 13 kart.
```plansza
L L L L L L * L L L L L L
L L L L L L . L L L L L L
L L L L L L . L L L L L L
L L L * . . * . . * L L L
L L L . L L . L L . L L L
L L L . L L . L L . L L L
* . . * . . ^ . . * . . *
L L L . L L . L L . L L L
L L L . L L . L L . L L L
L L L * . . * . . * L L L
L L L L L L . L L L L L L
L L L L L L . L L L L L L
L L L L L L * L L L L L L
```
```ustawienia
limit: 13
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    POWTÓRZ ×4
      IDŹ ×3, N − 1, ZRÓB A ×N, N + 1, OBRÓĆ SIĘ, IDŹ ×3, SKRĘĆ W LEWO
    KONIEC
  NIE
  KONIEC
KONIEC
ZRÓB A ×2
```

#### 3. Słupki rosną
Przepis najpierw woła sam siebie z N − 1, a dopiero potem stawia słupek o wysokości N. Dlatego słupki rosną: 1, 2, 3… Masz tylko 15 kart.
```plansza
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L * L L L L L
L L L L L L * . L L L L L
L L L L L * . . L L L L L
L L L L * . . . L L L L L
L L L * . . . . L L L L L
L L * . . . . . L L L L L
L * . . . . . . L L L L L
* . . . . . . . L L L L L
> . . . . . . . . L L L L
```
```ustawienia
limit: 15
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
N = 6
N + 2
ZRÓB A ×N
```

#### 4. Dolina
Te same karty przed wywołaniem i po nim: słupki maleją w drodze w dół rekurencji i rosną w drodze powrotnej. Masz tylko 19 kart.
```plansza
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
L L L L L L L L L L L L L
* L L L L L L L L L L * L
. * L L L L L L L L * . L
. . * L L L L L L * . . L
. . . * L L L L * . . . L
. . . . * L L * . . . . L
. . . . . * * . . . . . L
> . . . . . . . . . . . .
```
```ustawienia
limit: 19
```
```rozwiazanie
PRZEPIS A
  JEŚLI N > 0?
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
    N − 1, ZRÓB A ×N, N + 1
    SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
  NIE
  KONIEC
KONIEC
ZRÓB A ×6
```

### Zestaw B: Powrót po śladach
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A, META
pytania: WOLNE?, NIE WOLNE?, SKARB?, NIE SKARB?, NIE ŚCIANA?
rekurencja: tak
wymagaj: rekurencja

#### 5. Za róg tyle samo
Idź do klocka. Tam strażnik skręca w prawo i robi META. Każde IDŹ po ZRÓB A czeka na powrót, więc robot idzie w prawo tyle pól, ile przeszedł w górę. Masz tylko 9 kart.
```plansza
? . . . . . . . . . . . .
. . . . . . . . . . . ? .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . . . . . ? . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
? . . . . . . . . . . . .
. . . ? . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
^ . . . . . . . . . . . .
```
```ustawienia
limit: 9
warianty: ..#*.. #*.... ....#*
```
```rozwiazanie
PRZEPIS A
  JEŚLI NIE WOLNE?
    SKRĘĆ W PRAWO, META
  NIE
  KONIEC
  IDŹ, ZRÓB A, IDŹ
KONIEC
ZRÓB A
```

#### 6. Schody i z powrotem
Schodkami w górę, aż nad robotem stanie klocek. Karty po ZRÓB A sprowadzają robota tą samą drogą. Wróć na START. Masz tylko 14 kart.
```plansza
. . . . . . . . . . . . .
. . . . . . . . . . ? . .
. . . . . . . . . . ? . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . ? . . . . . .
. . . . . . ? . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. ? . . . . . . . . . . .
. ? . . . . . . . . . . .
^ . . . . . . . . . . . .
```
```ustawienia
limit: 14
warianty: ....#* ..#*.. #*....
```
```rozwiazanie
PRZEPIS A
  JEŚLI WOLNE?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE
    OBRÓĆ SIĘ
  KONIEC
KONIEC
ZRÓB A
```

#### 7. Powrót po śladach
Przepis zapamiętuje drogę: każde IDŹ i każdy skręt czeka na powrót. Za skarbem robot zawraca i idzie tą samą drogą. Wróć na START. Masz tylko 16 kart.
```plansza
L L L L L L L L L L L L L
. . . . . . . . . . ? L L
. L L L L L L L L L . L L
. L L . . . . . . L . L L
. L L . L L L L . L . L L
. L L . L L L L . L . L L
. L L . L L L L . L ? L L
. L L . L L L L L L . L L
. L L . L L L L L L . L L
. L L . . . . . . ? . L L
. L L L L L L L L L L L L
. L L L L L L L L L L L L
^ L L L L L L L L L L L L
```
```ustawienia
limit: 16
warianty: .*. *.. ..*
```
```rozwiazanie
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

#### 8. Ślady w lewo
Ta sama sztuczka, ale ścieżka skręca w lewo. Zmień w przepisie strony skrętów. Wróć na START. Masz tylko 16 kart.
```plansza
L L . . . . . . . . . . .
L L . L L L L L L L L L .
L L ? L L L L L L L L L .
L L ? L . . . . . . L L .
L L ? L . L L L L . L L .
L L . L . L L L L . L L .
L L . L . L L L L . L L .
L L . L L L L L L . L L .
L L . L L L L L L . L L .
L L . . . . . . . . L L .
L L L L L L L L L L L L .
L L L L L L L L L L L L .
L L L L L L L L L L L L ^
```
```ustawienia
limit: 16
warianty: *.. .*. ..*
```
```rozwiazanie
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

