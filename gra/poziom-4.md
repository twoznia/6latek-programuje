# Gra online, poziom 4 (dla 12-latka)

Źródło gier poziomu 4 w grze online i w druku (`plansze-starsi-poziom-4-*`). Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **zmienna N**. Robot pamięta jedną liczbę N (na starcie N = 0). Karta USTAW N (w rozwiązaniu `N = 3`) wpisuje liczbę, karty `N + 1` i `N − 1` ją zmieniają, a liczba N w okienku karty (`IDŹ ×N`, `POWTÓRZ ×N`) znaczy „tyle, ile teraz jest w N”. Pytania `N > 0?` i `N = 0?` sprawdzają N.

## Plansza 5 × 5

### Zestaw A: Zmienna N
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 1. Spirala rośnie
Każdy bok spirali jest o 1 dłuższy. Na początku N = 1, a po każdym boku N + 1. Zbierz skarby. Masz tylko 6 kart.
```plansza
. . . . .
. L * . *
. . ^ . .
. L . L .
* . . . *
```
```ustawienia
limit: 6
```
```rozwiazanie
N = 1
POWTÓRZ ×4
  IDŹ ×N, SKRĘĆ W PRAWO, N + 1
KONIEC
```

#### 2. Tyle samo w bok
Idź w górę do klocka i licz kroki w N. Potem skręć w prawo i zrób IDŹ ×N. Tam leży skarb. Masz tylko 6 kart.
```plansza
? . . . ?
? . . ? .
? . ? . .
? ? . . .
^ . . . .
```
```ustawienia
limit: 6
warianty: ....#..* ..#..*.. #..*.... .*......
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W PRAWO, IDŹ ×N
```

#### 3. Kwadraty coraz większe
Wszystkie kwadraty zaczynają się w rogu START, a każdy jest o 1 większy. Masz tylko 8 kart.
```plansza
. . . . *
. . . * .
. . * . .
. * . . .
^ . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
N = 1
POWTÓRZ ×4
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N + 1
KONIEC
```

#### 4. Licz i wracaj
Robot nie wie, jak daleko jest skarb. Idź do skarbu i licz kroki w N. Potem obróć się i zrób IDŹ ×N, żeby wrócić na START. Masz tylko 6 kart.
```plansza
. L . L .
. . . . .
. > ? ? ?
. . . . .
. L . L .
```
```ustawienia
limit: 6
warianty: *#. .*# ..*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N
```

### Zestaw B: Licznik
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 5. Lustro
Drugi skarb jest tak samo daleko za robotem, jak pierwszy przed nim. Policz kroki do pierwszego skarbu, a potem przejdź dwa razy tyle w drugą stronę. Masz tylko 7 kart.
```plansza
. . L . .
. . . . .
? ? > ? ?
. . . . .
. . L . .
```
```ustawienia
limit: 7
warianty: .**# *..*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N, IDŹ ×N
```

#### 6. Policz skarby
Idź do końca rzędu i licz skarby w N. Ostatni skarb leży nad końcem rzędu, dokładnie N pól w górę. Masz tylko 9 kart.
```plansza
. . . . .
. . L . ?
. L . . ?
. . . . ?
> ? ? ? ?
```
```ustawienia
limit: 9
warianty: ..*.*.. .*.*..* *..**.*
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

#### 7. Policz kałuże
Przeskocz kałuże do końca rzędu i licz je w N. Skarb leży N pól w górę. Masz tylko 10 kart.
```plansza
. . . . .
. L . . ?
. . L . ?
. . . . ?
> ? ? ? .
```
```ustawienia
limit: 10
warianty: ..*.K. .*.K.K ..*..K
```
```rozwiazanie
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ, N + 1
  NIE
    IDŹ
  KONIEC
KONIEC
SKRĘĆ W LEWO, IDŹ ×N
```

#### 8. Spirala do środka
Dwa boki po N pól, potem N − 1. I tak, dopóki N > 0. Robot kończy w samym środku. Masz tylko 8 kart.
```plansza
. . . . *
. * . . .
. . * . .
. . . . .
^ . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
N = 4
DOPÓKI N > 0?
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N − 1
KONIEC
```

## Plansza 7 × 7

### Zestaw A: Zmienna N
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 1. Spirala rośnie
Każdy bok spirali jest o 1 dłuższy. Na początku N = 1, a po każdym boku N + 1. Zbierz skarby. Masz tylko 6 kart.
```plansza
. * L . L . .
L . . L . L L
. . . * . * L
L . . ^ . . .
. . . L . . .
L * . . . * L
. . L . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
N = 1
POWTÓRZ ×5
  IDŹ ×N, SKRĘĆ W PRAWO, N + 1
KONIEC
```

#### 2. Schody coraz wyższe
Każdy schodek jest o 1 wyższy i o 1 szerszy od poprzedniego. Masz tylko 8 kart.
```plansza
L . L * . . *
. L L . . L .
. . . . L . L
L * . * L L .
. . . L L . L
* * . . . . .
^ . . . . L L
```
```ustawienia
limit: 8
```
```rozwiazanie
N = 1
POWTÓRZ ×3
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N + 1
KONIEC
```

#### 3. Kwadraty coraz większe
Wszystkie kwadraty zaczynają się w rogu START, a każdy jest o 1 większy. Masz tylko 8 kart.
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
limit: 8
```
```rozwiazanie
N = 1
POWTÓRZ ×6
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N + 1
KONIEC
```

#### 4. Licz i wracaj
Robot nie wie, jak daleko jest skarb. Idź do skarbu i licz kroki w N. Potem obróć się i zrób IDŹ ×N, żeby wrócić na START. Masz tylko 6 kart.
```plansza
. L . . . L .
. . . . . . .
. . . . . . .
. . > ? ? ? ?
. . . . . . .
. . . . . . .
. L . . . L .
```
```ustawienia
limit: 6
warianty: *#.. .*#. ..*# ...*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N
```

### Zestaw B: Licznik
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 5. Lustro
Drugi skarb jest tak samo daleko za robotem, jak pierwszy przed nim. Policz kroki do pierwszego skarbu, a potem przejdź dwa razy tyle w drugą stronę. Masz tylko 7 kart.
```plansza
. . . L . . .
. . . . . . .
. . . . . . .
? ? ? > ? ? ?
. . . . . . .
. . . . . . .
. . . L . . .
```
```ustawienia
limit: 7
warianty: ..**#. .*..*# *....*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N, IDŹ ×N
```

#### 6. Policz skarby
Idź do końca rzędu i licz skarby w N. Ostatni skarb leży nad końcem rzędu, dokładnie N pól w górę. Masz tylko 9 kart.
```plansza
. . . . . . .
. . L . . . ?
. L . . L . ?
. . . L . . ?
. . L . . . ?
. . . . . . ?
> ? ? ? ? ? ?
```
```ustawienia
limit: 9
warianty: ....*..*... ...*..*..*. ..*..*.*..* *....**.***
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

#### 7. Schody coraz niższe
Pierwszy schodek jest najwyższy, a każdy następny o 1 niższy. Pętla DOPÓKI N > 0? kończy się sama, gdy N spadnie do zera. Masz tylko 8 kart.
```plansza
L . * * . . L
L * * . . . .
. . . L L . .
* * L . . L .
. . L . L . L
. L . . . . .
^ . . L . . L
```
```ustawienia
limit: 8
```
```rozwiazanie
N = 3
DOPÓKI N > 0?
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
KONIEC
```

#### 8. Spirala do środka
Dwa boki po N pól, potem N − 1. I tak, dopóki N > 0. Robot kończy w samym środku. Masz tylko 8 kart.
```plansza
. . . . . . *
. * . . . . .
. . . . . . .
. . . * * . .
. . * . . . .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
N = 6
DOPÓKI N > 0?
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  N − 1
KONIEC
```

## Plansza 9 × 9

### Zestaw A: Zmienna N
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 1. Spirala rośnie
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
```ustawienia
limit: 8
```
```rozwiazanie
N = 1
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO, N + 1
  KONIEC
KONIEC
```

#### 2. Schody coraz wyższe
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
```ustawienia
limit: 8
```
```rozwiazanie
N = 1
POWTÓRZ ×3
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N + 1
KONIEC
```

#### 3. Kwadraty coraz większe
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
```ustawienia
limit: 8
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

#### 4. Licz i wracaj
Robot nie wie, jak daleko jest skarb. Idź do skarbu i licz kroki w N. Potem obróć się i zrób IDŹ ×N, żeby wrócić na START. Masz tylko 6 kart.
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
```ustawienia
limit: 6
warianty: ...#* .#*.. *....
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N
```

### Zestaw B: Licznik
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, KAŁUŻA?, N > 0?, N = 0?

#### 5. Lustro
Drugi skarb jest tak samo daleko za robotem, jak pierwszy przed nim. Policz kroki do pierwszego skarbu, a potem przejdź dwa razy tyle w drugą stronę. Masz tylko 7 kart.
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
```ustawienia
limit: 7
warianty: ..#**... .#*..*.. #*....*. *......*
```
```rozwiazanie
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
OBRÓĆ SIĘ, IDŹ ×N, IDŹ ×N
```

#### 6. Policz skarby
Idź do końca rzędu i licz skarby w N. Ostatni skarb leży nad końcem rzędu, dokładnie N pól w górę. Masz tylko 9 kart.
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
```ustawienia
limit: 9
warianty: ......*...*.... ....*...*...*.* ...*...*.*.*.*. *......***.****
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

#### 7. Schody coraz niższe
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
```ustawienia
limit: 8
```
```rozwiazanie
N = 3
DOPÓKI N > 0?
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO, N − 1
KONIEC
```

#### 8. Spirala do środka
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
```ustawienia
limit: 9
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
