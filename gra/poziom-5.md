# Gra online, poziom 5 (dla początkującego programisty)

Źródło gier poziomu 5 w grze online i w druku (`plansze-starsi-poziom-5-*`). Format jak w `gra/poziom-3.md`.

Nowe na tym poziomie: **pytania złożone** i **czujniki z boku**. `NIE X` odwraca odpowiedź, `X I Y` to TAK tylko wtedy, gdy oba są TAK, a `X LUB Y` to TAK, gdy choć jedno jest TAK. `WOLNE W LEWO?` i `WOLNE W PRAWO?` pytają o pole obok robota. Do tego labirynty, w których część ścian (pola ?) za każdym razem stoi inaczej: wygrywa ogólny algorytm, a nie wyuczona droga. Gry są generowane skryptem, a rozwiązania sprawdza symulator.

## Plansza 5 × 5

### Zestaw A: Pytania złożone
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 1. Kręta ścieżka nad lawą
Skarb leży raz w połowie ścieżki, a raz na końcu. Po każdym kroku robot pyta: czy przede mną jest zamknięte I w lewo wolne? Wtedy skręca w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
L L . . .
L . ? L .
. . L L ?
. L L L L
^ L L L L
```
```ustawienia
limit: 12
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 2. Ścieżka z kałużami
Kręta ścieżka, a na niej kałuże. Najpierw: kałuża? SKOCZ, a jeśli nie, IDŹ. Potem skręty jak w poprzedniej grze. Masz tylko 16 kart.
```plansza
L . ? . L
. . L . .
K L L L .
. L L L ?
^ L L L L
```
```ustawienia
limit: 16
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 3. Kałuża, lawa albo klocek
Na polach ? za każdym razem stoi coś innego. Kałużę przeskocz. Lawę LUB klocek obejdź górą: to przepis A. Masz tylko 18 kart.
```plansza
. . . . .
. . . . L
. . . . .
> ? ? ? *
L . . . .
```
```ustawienia
limit: 18
warianty: K.# L.K L.L
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

#### 4. Cztery razy inaczej
Ten sam program musi przejść cztery różne rzędy przeszkód. Masz tylko 18 kart.
```plansza
. L . . .
. . . . .
. . . . .
> ? ? ? *
. . L . .
```
```ustawienia
limit: 18
warianty: #.K #.L L.# L.L
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw B: Labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 5. Labirynt prawej ręki
Trzymaj prawą rękę na ścianie: po każdym kroku, jeśli w prawo jest wolne, skręć w prawo. Jeśli nie, kręć się w lewo, dopóki przed tobą nie jest wolne. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
. . . . *
. # # # ?
. . . . .
# # # # .
> . . . .
```
```ustawienia
limit: 11
warianty: # .
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 6. Labirynt lewej ręki
Teraz lewa ręka na ścianie. Przerób program z poprzedniej gry. Masz tylko 11 kart.
```plansza
. . . . *
. # # # #
. . . . .
# # ? # .
> . . . .
```
```ustawienia
limit: 11
warianty: # .
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 7. Labirynt z drzwiami
Na polach ? są drzwi: raz otwarte, raz zamknięte. Program musi znaleźć skarb w każdym z 2 labiryntów. Masz tylko 11 kart.
```plansza
. . . . .
. # # # .
. . . # .
? # . # .
> . . ? *
```
```ustawienia
limit: 11
warianty: ## #.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 8. Wielka zagadka
3 różne labirynty i jeden program. Którą ręką do ściany? Masz tylko 11 kart.
```plansza
. . . . .
. # ? # .
. . * ? .
# # ? # .
> . . . .
```
```ustawienia
limit: 11
warianty: ### ##. #.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### Zestaw C: Ścieżki i przeszkody
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 9. Długa kręta ścieżka
Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
L ? . . .
L L L L .
L L L . ?
L . . . L
> . L L L
```
```ustawienia
limit: 12
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 10. Idź za ścieżką
Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo. Masz tylko 12 kart.
```plansza
L L L L L
L . . ? .
L . L L .
. . L L .
^ L L ? .
```
```ustawienia
limit: 12
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI WOLNE?
    IDŹ
  NIE
    JEŚLI WOLNE W LEWO?
      SKRĘĆ W LEWO
    NIE
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 11. Więcej kałuż
Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty. Masz tylko 16 kart.
```plansza
. K . . L
? L L . ?
L L L L .
L L L . .
> . K . L
```
```ustawienia
limit: 16
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 12. Nowe przeszkody
Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A. Masz tylko 18 kart.
```plansza
. . . L .
. . L L .
. . . . .
> ? ? ? *
L . . . .
```
```ustawienia
limit: 18
warianty: #.K K.# K.K L.K
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw D: Nowe labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 13. Nowy labirynt
Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
. . . . .
# # . # .
. . . ? .
. # # # .
^ ? * . .
```
```ustawienia
limit: 11
warianty: ## .#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 14. Labirynt w lewo
Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania. Masz tylko 11 kart.
```plansza
. . . . .
. # ? # .
* # . . .
# # . # .
> . . ? .
```
```ustawienia
limit: 11
warianty: ## .#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 15. Więcej drzwi
Więcej pól ? i 2 różne labirynty. Program ten sam. Masz tylko 11 kart.
```plansza
. . . . .
. # ? # .
. # * ? .
. # . # .
^ ? . . .
```
```ustawienia
limit: 11
warianty: ### #.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 16. Największa zagadka
3 labirynty, dużo drzwi i jeden program. Masz tylko 11 kart.
```plansza
. . . . .
. # ? # .
. . * ? .
? # ? # .
> . . . .
```
```ustawienia
limit: 11
warianty: #### ###. #.##
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

## Plansza 7 × 7

### Zestaw A: Pytania złożone
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 1. Kręta ścieżka nad lawą
Skarb leży raz w połowie ścieżki, a raz na końcu. Po każdym kroku robot pyta: czy przede mną jest zamknięte I w lewo wolne? Wtedy skręca w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
L L L . . . .
L ? . . L L .
L L L L L L .
L L L L L . ?
L L L . . . L
. . . . L L L
^ L L L L L L
```
```ustawienia
limit: 12
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 2. Ścieżka z kałużami
Kręta ścieżka, a na niej kałuże. Najpierw: kałuża? SKOCZ, a jeśli nie, IDŹ. Potem skręty jak w poprzedniej grze. Masz tylko 16 kart.
```plansza
L L L L L L L
L L L L L L L
. . . . L L L
. L L . K ? .
. ? L L L L .
L L L L L . .
> . . K . . L
```
```ustawienia
limit: 16
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 3. Kałuża, lawa albo klocek
Na polach ? za każdym razem stoi coś innego. Kałużę przeskocz. Lawę LUB klocek obejdź górą: to przepis A. Masz tylko 18 kart.
```plansza
. . . . . . .
L L . . L . .
. . . . . L .
. . . . . L L
. . . . . . .
> ? ? ? ? ? *
. . . L . L L
```
```ustawienia
limit: 18
warianty: .#.K. .L.L. K.L..
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

#### 4. Cztery razy inaczej
Ten sam program musi przejść cztery różne rzędy przeszkód. Masz tylko 18 kart.
```plansza
. . L L . . .
. . . . . . .
L . L . . . .
. . . L . . .
. . . . . . .
> ? ? ? ? ? *
. . . . L . .
```
```ustawienia
limit: 18
warianty: #...K ..L.K K.L.K L..#.
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw B: Labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 5. Labirynt prawej ręki
Trzymaj prawą rękę na ścianie: po każdym kroku, jeśli w prawo jest wolne, skręć w prawo. Jeśli nie, kręć się w lewo, dopóki przed tobą nie jest wolne. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
* . . . . . .
? # # # # # .
. . . . . # .
. # ? # . # .
. . . # . # .
# # . # . # .
> . . # . . .
```
```ustawienia
limit: 11
warianty: ## #.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 6. Labirynt lewej ręki
Teraz lewa ręka na ścianie. Przerób program z poprzedniej gry. Masz tylko 11 kart.
```plansza
. . . . . . *
. # # # # # #
. # . . . . .
. # . # ? # .
. . . # . . .
# # ? # . # .
> . . . . # .
```
```ustawienia
limit: 11
warianty: ## #.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 7. Labirynt z drzwiami
Na polach ? są drzwi: raz otwarte, raz zamknięte. Program musi znaleźć skarb w każdym z 3 labiryntów. Masz tylko 11 kart.
```plansza
. . . . . . *
. # . # ? # #
. # . . . . .
# # # # # # .
. . . . . . .
. # ? # ? # .
^ # . . . . .
```
```ustawienia
limit: 11
warianty: ### ##. #.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 8. Wielka zagadka
4 różne labirynty i jeden program. Którą ręką do ściany? Masz tylko 11 kart.
```plansza
* # . . . . .
. # . # ? # .
. . . ? . . .
# # # # . # #
. . . ? . . .
. # . # ? # .
^ # . . . . .
```
```ustawienia
limit: 11
warianty: #### ###. ##.# #.##
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### Zestaw C: Ścieżki i przeszkody
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 9. Długa kręta ścieżka
Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
L L L L ? . .
L L L . . L .
L . . . L . .
L . L L . . L
. . L L . L L
. L L L . ? L
^ L L L L L L
```
```ustawienia
limit: 12
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 10. Idź za ścieżką
Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo. Masz tylko 12 kart.
```plansza
L L L L L L L
L L L L L L L
L . . . L L L
L . L . . . .
? . L L L L ?
L L . . . L .
> . . L . . .
```
```ustawienia
limit: 12
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI WOLNE?
    IDŹ
  NIE
    JEŚLI WOLNE W LEWO?
      SKRĘĆ W LEWO
    NIE
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 11. Więcej kałuż
Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty. Masz tylko 16 kart.
```plansza
. . . L L L L
K L . . L L L
. L L ? L L L
. L . . L L L
K L . L L L ?
. L K L L L .
^ L . . . . .
```
```ustawienia
limit: 16
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 12. Nowe przeszkody
Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A. Masz tylko 18 kart.
```plansza
. . L . . . L
L . . L . . L
L . L L . . .
. L . . . . L
. . . . . . .
> ? ? ? ? ? *
. . . . . L .
```
```ustawienia
limit: 18
warianty: ..#.# L..#. L...K L..L.
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw D: Nowe labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 13. Nowy labirynt
Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
. . . . . . .
. # # # # # .
. . . ? * . .
. # . # # # #
. # . . . . .
? # # # ? # .
> . . . . . .
```
```ustawienia
limit: 11
warianty: ### .##
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 14. Labirynt w lewo
Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania. Masz tylko 11 kart.
```plansza
. . . . . . .
. # # # # # .
. # . . . # .
. # . # . # .
. . . ? * # .
# # ? # ? # .
> . . . . . .
```
```ustawienia
limit: 11
warianty: ### ##.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 15. Więcej drzwi
Więcej pól ? i 3 różne labirynty. Program ten sam. Masz tylko 11 kart.
```plansza
* . . . . . .
? # # # # # .
. . . . . # .
. # ? # . # .
. . . ? . # .
# # . # . # .
> . . ? . . .
```
```ustawienia
limit: 11
warianty: #### ###. ##.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 16. Największa zagadka
4 labirynty, dużo drzwi i jeden program. Masz tylko 11 kart.
```plansza
* # . . . . .
. # . # ? # .
. . . . . ? .
. # # # ? # .
. ? . . . . .
? # . # # # .
> . . # . . .
```
```ustawienia
limit: 11
warianty: ##### ###.# ##.## #.###
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

## Plansza 9 × 9

### Zestaw A: Pytania złożone
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 1. Kręta ścieżka nad lawą
Skarb leży raz w połowie ścieżki, a raz na końcu. Po każdym kroku robot pyta: czy przede mną jest zamknięte I w lewo wolne? Wtedy skręca w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
? L L L L L L L L
. L L L L L L L L
. . L L L L L L L
L . . . . L L L L
L L L L . . . . L
. . . . L L L . L
. L L . . . L . .
. L L L L . L L ?
^ L L L L . . . .
```
```ustawienia
limit: 12
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 2. Ścieżka z kałużami
Kręta ścieżka, a na niej kałuże. Najpierw: kałuża? SKOCZ, a jeśli nie, IDŹ. Potem skręty jak w poprzedniej grze. Masz tylko 16 kart.
```plansza
L L L L L L . . ?
L L L L L . . L .
L L L L . . L L .
L L L L K L . . .
L L L L . L . L L
L L L L . L . . .
. . K . . L L L .
. L L L L L L . .
^ L L L L ? . . L
```
```ustawienia
limit: 16
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 3. Kałuża, lawa albo klocek
Na polach ? za każdym razem stoi coś innego. Kałużę przeskocz. Lawę LUB klocek obejdź górą: to przepis A. Masz tylko 18 kart.
```plansza
. . . . L . L L L
L . L . . . . . .
. . . L . . L . .
L L . L L . . L .
L . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> ? ? ? ? ? ? ? *
. . . L . . . L .
```
```ustawienia
limit: 18
warianty: .K.K.#. L..K.K. L.K....
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

#### 4. Cztery razy inaczej
Ten sam program musi przejść cztery różne rzędy przeszkód. Masz tylko 18 kart.
```plansza
. L . . L . . . .
. L L . . . . . L
. . L L . . . . L
. . . . . . . L .
L L . L . . . . L
. . . L . . . . L
. . . . . . . . .
> ? ? ? ? ? ? ? *
. . L . L . . . L
```
```ustawienia
limit: 18
warianty: #.#.#.L #.K.K.. L.#.... L.K..#.
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw B: Labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 5. Labirynt prawej ręki
Trzymaj prawą rękę na ścianie: po każdym kroku, jeśli w prawo jest wolne, skręć w prawo. Jeśli nie, kręć się w lewo, dopóki przed tobą nie jest wolne. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
* # . . . . . . .
. # . # # # . # .
. # . # . . . # .
. # . # . # ? # .
. # . # . . . # .
. # . # # # . # .
. . . . . # . ? .
# # ? # # # . # .
> . . . . . . # .
```
```ustawienia
limit: 11
warianty: ### #.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 6. Labirynt lewej ręki
Teraz lewa ręka na ścianie. Przerób program z poprzedniej gry. Masz tylko 11 kart.
```plansza
. . . . . ? * . .
. # # # . # # # .
. . . # . . . . .
. # . # ? # # # .
. # . . . . . # .
# # ? # # # . # #
. . . . . # . . .
. # # # . # # # .
^ # . . . . . . .
```
```ustawienia
limit: 11
warianty: ### ##.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 7. Labirynt z drzwiami
Na polach ? są drzwi: raz otwarte, raz zamknięte. Program musi znaleźć skarb w każdym z 3 labiryntów. Masz tylko 11 kart.
```plansza
. . . # . . . # *
. # . # . # . # .
. # . . . # . # .
. # ? # ? # . # .
. . . # . # . # .
. # . # . # . # .
. # . # . . . # .
# # . # . # ? # .
> . . ? . . . . .
```
```ustawienia
limit: 11
warianty: #### ###. #.##
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 8. Wielka zagadka
4 różne labirynty i jeden program. Którą ręką do ściany? Masz tylko 11 kart.
```plansza
. . . . . . . ? *
. # ? # ? # . # .
. . . # . # . # .
. # . # . # . # .
. ? . # . # . # .
# # . # . # . # .
. . . # . . . # .
. # ? # . # # # .
^ # . . . . . . .
```
```ustawienia
limit: 11
warianty: ##### ###.# .###. .##.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

### Zestaw C: Ścieżki i przeszkody
karty: POWTÓRZ, DOPÓKI, JEŚLI, ZRÓB A
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 9. Długa kręta ścieżka
Nowa ścieżka, ten sam pomysł: jeśli przed tobą zamknięte I w lewo wolne, skręć w lewo. Tak samo w prawo. Masz tylko 12 kart.
```plansza
. . ? . L L L L L
. L L . . L L L L
. L L L . L L L L
. . L L . . . . L
L . . L L L L . L
L L . L L L L . .
L L . . L L L L .
L L L . L L L L .
> . . . L L ? . .
```
```ustawienia
limit: 12
warianty: *. .*
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 10. Idź za ścieżką
Krócej: jeśli wolne, IDŹ. Jeśli nie, a w lewo wolne, skręć w lewo. W każdym innym razie skręć w prawo. Masz tylko 12 kart.
```plansza
. . . L L L L L L
. L . L L L . . .
? L . . . . . L .
L L L L L L L ? .
L L L L L L L . L
L L L L L L L . .
L L L L L L L L .
L L . . . L . . .
> . . L . . . L L
```
```ustawienia
limit: 12
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI WOLNE?
    IDŹ
  NIE
    JEŚLI WOLNE W LEWO?
      SKRĘĆ W LEWO
    NIE
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 11. Więcej kałuż
Kręta ścieżka z kałużami. Kałużę przeskocz, a potem pytaj o skręty. Masz tylko 16 kart.
```plansza
L L L . . K . . .
L L . . L L L L .
? . . L L L L L .
L L L L L L L L K
L . . . . . . L .
L . L L L L . L .
L . L L L L . L K
. . L L L L . L ?
^ L L L L L . . .
```
```ustawienia
limit: 16
warianty: .* *.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    IDŹ
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
  KONIEC
  JEŚLI NIE WOLNE? I WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
  KONIEC
KONIEC
IDŹ
```

#### 12. Nowe przeszkody
Cztery różne rzędy przeszkód i jeden program. Kałużę przeskocz, lawę LUB klocek obejdź przepisem A. Masz tylko 18 kart.
```plansza
. . . . . L . . .
L . . . . . . . .
L . . . . . . . L
L . . . . . L . .
L L . . . . L . .
. L . L L . . . .
. . . . . . . . .
> ? ? ? ? ? ? ? *
. L . . L . . . L
```
```ustawienia
limit: 18
warianty: ...L.K. .K....K K..#... L.K.L..
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
DOPÓKI NIE ŚCIANA?
  JEŚLI KAŁUŻA?
    SKOCZ
  NIE
    JEŚLI LAWA? LUB KLOCEK?
      ZRÓB A
    NIE
      IDŹ
    KONIEC
  KONIEC
KONIEC
```

### Zestaw D: Nowe labirynty
karty: POWTÓRZ, DOPÓKI, JEŚLI
pytania: WOLNE?, NIE WOLNE?, WOLNE W LEWO?, WOLNE W PRAWO?, NIE WOLNE? I WOLNE W LEWO?, NIE WOLNE? I WOLNE W PRAWO?, NIE SKARB?, NIE ŚCIANA?, KAŁUŻA?, LAWA? LUB KLOCEK?, LAWA?, KLOCEK?

#### 13. Nowy labirynt
Prawa ręka na ścianie. Część ścian (pola ?) za każdym razem stoi inaczej. Masz tylko 11 kart.
```plansza
. . . . . . . . .
. # # # # # # # .
. . . . . . . # .
? # . # # # # # .
. . . ? . . . . .
. # # # . # ? # #
. . * # . . . . .
# # ? # # # # # .
> . . . . . . . .
```
```ustawienia
limit: 11
warianty: #### ##.#
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 14. Labirynt w lewo
Lewa ręka na ścianie. Napisz program sam, zanim zajrzysz do rozwiązania. Masz tylko 11 kart.
```plansza
* . . . . # . . .
# # ? # . # . # .
. . . # . . . # .
. # . # # # . # .
. ? . . . # . # .
. # # # . # # # .
. . . ? . . . . .
? # . # # # # # .
> . . # . . . . .
```
```ustawienia
limit: 11
warianty: #### .###
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 15. Więcej drzwi
Więcej pól ? i 3 różne labirynty. Program ten sam. Masz tylko 11 kart.
```plansza
. . . . . ? . . .
. # # # . # . # .
. # . . . # * # .
. # ? # . # ? # .
. . . ? . . . ? .
. # . # # # . # .
. # . # . . . # .
# # . # . # # # .
> . . # . . . . .
```
```ustawienia
limit: 11
warianty: ##### ###.. #.##.
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W PRAWO?
    SKRĘĆ W PRAWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W LEWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

#### 16. Największa zagadka
4 labirynty, dużo drzwi i jeden program. Masz tylko 11 kart.
```plansza
. . . . . # . . .
. # ? # . # ? # .
. # . # . . . . .
. # . # # # # # .
. # . . . . . . .
. # # # ? # . # ?
. . . . . # . . .
? # ? # . # # # .
> . . . . # * . .
```
```ustawienia
limit: 11
warianty: #####. ###.## ###.#. ##.###
```
```rozwiazanie
DOPÓKI NIE SKARB?
  IDŹ
  JEŚLI WOLNE W LEWO?
    SKRĘĆ W LEWO
  NIE
    DOPÓKI NIE WOLNE?
      SKRĘĆ W PRAWO
    KONIEC
  KONIEC
KONIEC
IDŹ
```

