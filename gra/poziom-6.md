# Gra online, poziom 6 (dla średniego programisty)

Źródło gier poziomu 6 w grze online i w druku (`plansze-starsi-poziom-6-*`). Gry generuje `narzedzia/generatory/poziom6.py`. Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **przepis z parametrem** (ustawienie `parametr: tak`). Liczba w okienku karty ZRÓB A nie mówi już „ile razy”, tylko przekazuje wartość: ZRÓB A ×3 robi przepis A raz, a w środku przepisu N = 3. Po powrocie z przepisu N wraca do wartości sprzed wywołania (zmienna lokalna). Liczba N w okienku ZRÓB A przekazuje bieżące N.

## Plansza 5 × 5

### Zestaw A: Przepis z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 1. Kwadraty na zamówienie
Przepis A rysuje kwadrat o boku N. ZRÓB A ×3 to kwadrat o boku 3. Obejdź kwadraty w podanych rozmiarach: każdy skarb to róg innego kwadratu. Masz tylko 8 kart.
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
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×2
ZRÓB A ×4
ZRÓB A ×1
ZRÓB A ×3
```

#### 2. Nierówne schody
Każdy schodek ma inną wysokość, więc pętla nie pomoże. Przepis A to schodek o wysokości i szerokości N. Masz tylko 7 kart.
```plansza
. L . * *
L * . * .
. . L . L
* * . L L
^ . . L L
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×1
ZRÓB A ×2
ZRÓB A ×1
```

#### 3. Wieże
Na szczycie każdej wieży leży skarb. Przepis A wchodzi na wieżę o wysokości N, schodzi i idzie do następnej. Masz tylko 10 kart.
```plansza
# # * # .
* # . # .
. # . * .
. * . . .
> . . . .
```
```ustawienia
limit: 10
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×3
ZRÓB A ×1
ZRÓB A ×4
ZRÓB A ×2
```

#### 4. Diamenty
Przepis A to diament o boku N z poziomu 3. Wszystkie diamenty zaczynają się w START. Zbierz skarby i wróć na START. Masz tylko 11 kart.
```plansza
. . * . .
. * . . .
^ L . . .
. * . . .
L . * . .
```
```ustawienia
limit: 11
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    POWTÓRZ ×N
      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    KONIEC
    SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×2
ZRÓB A ×1
```

### Zestaw B: Parametr i zmienna
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 5. Kwadrat jak odległość
Idź do klocka i licz kroki w N. Potem skręć w lewo i narysuj kwadrat o boku N: ZRÓB A ×N przekazuje N do przepisu. Klocek za każdym razem stoi gdzie indziej. Masz tylko 10 kart.
```plansza
? . . . ?
? . . ? .
? . ? . .
. . . . .
> . . ? ?
```
```ustawienia
limit: 10
warianty: ....**#. ..**...# **......
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W LEWO, ZRÓB A ×N
```

#### 6. Odliczanie w przepisie
Przepis A robi N schodków i odlicza N − 1, dopóki N > 0. Między przepisami robot robi krok w bok. N w przepisie to kopia: zmiana w środku nie psuje liczby w programie. Masz tylko 8 kart.
```plansza
. . . * *
. . * * .
L * * . .
* * . L .
^ L . . L
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
  KONIEC
KONIEC
ZRÓB A ×4
```

#### 7. Spirala dwójkami
Przepis A to dwa boki po N pól. Program woła ZRÓB A ×N i zwiększa N. Każda długość boku pojawia się dwa razy. Masz tylko 9 kart.
```plansza
. . . . *
. . . * .
. . ^ . .
. * . . .
* . . . .
```
```ustawienia
limit: 9
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
N = 1
POWTÓRZ ×4
  ZRÓB A ×N, N + 1
KONIEC
```

#### 8. Kwadraty w rzędzie
Przepis A obchodzi trzy boki kwadratu o boku N i staje w jego prawym dolnym rogu, gotowy do następnego. Każdy skarb to prawy górny róg innego kwadratu. Masz tylko 8 kart.
```plansza
L L L L L
L L L L L
L . . * L
. * L . *
^ . L . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×3
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×1
ZRÓB A ×2
ZRÓB A ×1
```

## Plansza 7 × 7

### Zestaw A: Przepis z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 1. Kwadraty na zamówienie
Przepis A rysuje kwadrat o boku N. ZRÓB A ×3 to kwadrat o boku 3. Obejdź kwadraty w podanych rozmiarach: każdy skarb to róg innego kwadratu. Masz tylko 8 kart.
```plansza
. . . . . . *
. . . . . . .
. . . . * . .
. . . * . . .
. . . . . . .
. * . . . . .
^ . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×3
ZRÓB A ×6
ZRÓB A ×1
ZRÓB A ×4
```

#### 2. Nierówne schody
Każdy schodek ma inną wysokość, więc pętla nie pomoże. Przepis A to schodek o wysokości i szerokości N. Masz tylko 7 kart.
```plansza
. . L . * . *
L . . L . . .
L * . . * . .
. . . L L L .
. . . . . . L
* * L . . . L
^ L L L . L .
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×1
ZRÓB A ×3
ZRÓB A ×2
```

#### 3. Wieże
Na szczycie każdej wieży leży skarb. Przepis A wchodzi na wieżę o wysokości N, schodzi i idzie do następnej. Masz tylko 12 kart.
```plansza
# # * # # # .
# # . # * # .
* # . # . # .
. # . # . * .
. * . # . . .
. . . * . . .
> . . . . . .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×4
ZRÓB A ×2
ZRÓB A ×6
ZRÓB A ×1
ZRÓB A ×5
ZRÓB A ×3
```

#### 4. Diamenty
Przepis A to diament o boku N z poziomu 3. Wszystkie diamenty zaczynają się w START. Zbierz skarby i wróć na START. Masz tylko 12 kart.
```plansza
. . . * . . .
. . * . . . .
. * . . . . .
^ L . . . . .
. * . . . . .
. . * . . . L
. L . * . . .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    POWTÓRZ ×N
      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    KONIEC
    SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×3
ZRÓB A ×1
ZRÓB A ×2
```

### Zestaw B: Parametr i zmienna
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 5. Kwadrat jak odległość
Idź do klocka i licz kroki w N. Potem skręć w lewo i narysuj kwadrat o boku N: ZRÓB A ×N przekazuje N do przepisu. Klocek za każdym razem stoi gdzie indziej. Masz tylko 10 kart.
```plansza
? . . . . . ?
. . . . . . .
? . . . ? . .
. . . . . . .
? . ? . . . .
. . . . . . .
> . . ? . ? .
```
```ustawienia
limit: 10
warianty: ....**#. ..**...# **......
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W LEWO, ZRÓB A ×N
```

#### 6. Odliczanie w przepisie
Przepis A robi N schodków i odlicza N − 1, dopóki N > 0. Między przepisami robot robi krok w bok. N w przepisie to kopia: zmiana w środku nie psuje liczby w programie. Masz tylko 12 kart.
```plansza
L . . . L L L
L . L . L * *
L . . . * * L
L L * * * . .
. * * . . . .
* * L . . . .
^ . . . . L .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
  KONIEC
KONIEC
ZRÓB A ×3
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
ZRÓB A ×2
```

#### 7. Spirala dwójkami
Przepis A to dwa boki po N pól. Program woła ZRÓB A ×N i zwiększa N. Każda długość boku pojawia się dwa razy. Masz tylko 9 kart.
```plansza
. . . . . . *
. . . . . * .
. . . . * . .
. . . ^ . . .
. . * . . . .
. * . . . . .
* . . . . . .
```
```ustawienia
limit: 9
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
N = 1
POWTÓRZ ×6
  ZRÓB A ×N, N + 1
KONIEC
```

#### 8. Kwadraty w rzędzie
Przepis A obchodzi trzy boki kwadratu o boku N i staje w jego prawym dolnym rogu, gotowy do następnego. Każdy skarb to prawy górny róg innego kwadratu. Masz tylko 8 kart.
```plansza
. L . L . L .
. . . L . . .
. L . . . L .
. L . . . . *
. . * . . L .
. . . * . . .
^ . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×3
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
ZRÓB A ×1
ZRÓB A ×3
```

## Plansza 9 × 9

### Zestaw A: Przepis z parametrem
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 1. Kwadraty na zamówienie
Przepis A rysuje kwadrat o boku N. ZRÓB A ×3 to kwadrat o boku 3. Obejdź kwadraty w podanych rozmiarach: każdy skarb to róg innego kwadratu. Masz tylko 12 kart.
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . * . .
. . . . . * . . .
. . . . * . . . .
. . . * . . . . .
. . * . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×5
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×2
ZRÓB A ×6
ZRÓB A ×3
ZRÓB A ×4
```

#### 2. Nierówne schody
Każdy schodek ma inną wysokość, więc pętla nie pomoże. Przepis A to schodek o wysokości i szerokości N. Masz tylko 8 kart.
```plansza
. . . . . . * . *
L . . . L . . L .
. L . * . . * . .
. L L . . L L L L
. . . . . . . . .
L . * * . . . . L
* . * L L . . . .
. . . L L . . . .
^ L . . L L . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  IDŹ ×N, SKRĘĆ W PRAWO, IDŹ ×N, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2
ZRÓB A ×1
ZRÓB A ×3
ZRÓB A ×2
```

#### 3. Wieże
Na szczycie każdej wieży leży skarb. Przepis A wchodzi na wieżę o wysokości N, schodzi i idzie do następnej. Masz tylko 18 kart.
```plansza
# # # # * # # # .
# # * # . # # # .
# # . # . # * # .
* # . # . # . # .
. # . # . # . * .
. # . * . # . . .
. * . . . # . . .
. . . . . * . . .
> . . . . . . . .
```
```ustawienia
limit: 18
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ ×N, OBRÓĆ SIĘ, IDŹ ×N, SKRĘĆ W LEWO, IDŹ
KONIEC
ZRÓB A ×5
ZRÓB A ×2
N = 6
N + 1
ZRÓB A ×N
ZRÓB A ×3
N = 6
N + 2
ZRÓB A ×N
ZRÓB A ×1
ZRÓB A ×6
ZRÓB A ×4
```

#### 4. Diamenty
Przepis A to diament o boku N z poziomu 3. Wszystkie diamenty zaczynają się w START. Zbierz skarby i wróć na START. Masz tylko 12 kart.
```plansza
. . . . * . . L .
L . . * . . . . L
. . * . . . . . .
. . . . . . . . .
^ . . . . L . . .
. . L . . . . . .
. . * . . . . . .
. . . * . . . . .
. . . . * . . . .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    POWTÓRZ ×N
      IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    KONIEC
    SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A ×4
ZRÓB A ×2
ZRÓB A ×3
```

### Zestaw B: Parametr i zmienna
karty: POWTÓRZ, DOPÓKI, JEŚLI, N =, N +, N −, ZRÓB A
pytania: WOLNE?, NIE ŚCIANA?, NIE SKARB?, SKARB?, N > 0?, N = 0?
parametr: tak

#### 5. Kwadrat jak odległość
Idź do klocka i licz kroki w N. Potem skręć w lewo i narysuj kwadrat o boku N: ZRÓB A ×N przekazuje N do przepisu. Klocek za każdym razem stoi gdzie indziej. Masz tylko 10 kart.
```plansza
? . . . . . . . ?
. . . . . . . . .
. . . . . . . . .
? . . . . ? . . .
. . . . . . . . .
? . . ? . . . . .
. . . . . . . . .
. . . . . . . . .
> . . . ? . ? . .
```
```ustawienia
limit: 10
warianty: ....**#. ..**...# **......
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×N, SKRĘĆ W LEWO
  KONIEC
KONIEC
DOPÓKI WOLNE?
  IDŹ, N + 1
KONIEC
SKRĘĆ W LEWO, ZRÓB A ×N
```

#### 6. Odliczanie w przepisie
Przepis A robi N schodków i odlicza N − 1, dopóki N > 0. Między przepisami robot robi krok w bok. N w przepisie to kopia: zmiana w środku nie psuje liczby w programie. Masz tylko 12 kart.
```plansza
. L . L . L . . .
. L . . L L L * *
. . . L . . * * L
. . L . . * * . .
. . . * * * . . .
L L * * L . . . L
. * * . L L L . .
* * . . . L . . L
^ . . . . . . L .
```
```ustawienia
limit: 12
```
```rozwiazanie
PRZEPIS A
  DOPÓKI N > 0?
    IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, N − 1
  KONIEC
KONIEC
ZRÓB A ×4
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
ZRÓB A ×3
```

#### 7. Spirala dwójkami
Przepis A to dwa boki po N pól. Program woła ZRÓB A ×N i zwiększa N. Każda długość boku pojawia się dwa razy. Masz tylko 11 kart.
```plansza
. . . . . . . . *
. . . . . . . * .
. . . . . . * . .
. . . . . * . . .
. . . . ^ . . . .
. . . * . . . . .
. . * . . . . . .
. * . . . . . . .
* . . . . . . . .
```
```ustawienia
limit: 11
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×2
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
KONIEC
N = 1
POWTÓRZ ×2
  POWTÓRZ ×4
    ZRÓB A ×N, N + 1
  KONIEC
KONIEC
```

#### 8. Kwadraty w rzędzie
Przepis A obchodzi trzy boki kwadratu o boku N i staje w jego prawym dolnym rogu, gotowy do następnego. Każdy skarb to prawy górny róg innego kwadratu. Masz tylko 8 kart.
```plansza
. . . . . . . L L
. . . . . . . . .
L . . L . . . L .
. . . L . . . L .
. . L . . . . . *
. . . * . L . . .
. . . . . . . L .
. . . . * . . . .
^ . L . . . . . .
```
```ustawienia
limit: 8
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×3
    IDŹ ×N, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
ZRÓB A ×1
ZRÓB A ×4
```
