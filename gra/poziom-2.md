# Gra online, poziom 2

Źródło gier poziomu 2 w grze online (index.html). Po zmianie uruchom `make online`: skrypt sprawdzi każde rozwiązanie symulatorem i zapisze `gra/gry.js`.

Format: `## Plansza N × N`, potem `### Zestaw X: nazwa` z linią `karty:` (karty dodane do IDŹ, SKRĘĆ, OBRÓĆ SIĘ i SKOCZ), a w nim gry `#### nr. tytuł`. Gra ma opis, blok `plansza`, opcjonalny blok `ustawienia` i blok `rozwiazanie`.

Pola: `.` puste, `^ > v <` robot, `*` skarb, `#` klocek, `L` lawa, `K` kałuża, `@` klucz, `D` drzwi (wejście zabiera jeden klucz), `1`–`6` moneta z liczbą, `?` niespodzianka.

Ustawienia: `limit: N` (najwięcej kart w programie i przepisie razem, liczby się nie liczą), `suma: N` (zebrane monety mają dać dokładnie tyle), `warianty: K .` (co pojawi się na polach `?`, po kolei od lewej do prawej i z góry na dół; program musi zadziałać w każdym wariancie), `pytania: KAŁUŻA?, LAWA?` (karty pytań do JEŚLI, pierwsza jest domyślna). Słowa „wróć na START” w opisie znaczą, że robot musi skończyć na starcie.

## Plansza 5 × 5

### Zestaw A: Pętla POWTÓRZ
karty: POWTÓRZ

#### 1. Kwadrat dookoła klocka
Nowa karta POWTÓRZ! Karty między POWTÓRZ a KONIEC robot robi tyle razy, ile mówi liczba. Zbierz skarby i wróć na START. Masz tylko 4 karty.
```plansza
. . . . .
. * . * .
. . # . .
. ^ . * .
. . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

#### 2. Kwadrat z kałużami
Skacz dookoła lawy, zbierz skarby i wróć na START. Masz tylko 4 karty.
```plansza
. . . . .
. * K * .
. K L K .
. ^ K * .
. . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ, SKRĘĆ W PRAWO
KONIEC
```

#### 3. Spacer po brzegu
Zbierz skarby w rogach i wróć na START. Masz tylko 4 karty.
```plansza
* . . . *
. . . . .
. . # . .
. . . . .
^ . . . *
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

#### 4. Schodki
Znajdź kawałek, który się powtarza. Masz tylko 6 kart.
```plansza
L . . . *
. . . . .
. . . L .
. . L . .
^ . . . L
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

#### 5. Kałuże po schodach
Robot patrzy w prawo. Skacz i wspinaj się. Masz tylko 6 kart.
```plansza
. . . . .
. . . . .
. . . . *
L . . K .
> K . L .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×2
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

#### 6. Schody w dół
Robot schodzi po schodach i zbiera skarby. Masz tylko 6 kart.
```plansza
> . * . .
. . * . .
. . * . *
. . . . *
. . . . *
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### Zestaw B: Klucz i drzwi
karty: POWTÓRZ

#### 7. Pierwszy klucz
Drzwi otwiera tylko klucz. Robot bierze klucz, gdy na nim stanie, i dopiero wtedy przejdzie przez drzwi.
```plansza
. . * . .
# # D # #
. . . . .
. . @ . .
. . ^ . .
```
```rozwiazanie
IDŹ ×4
```

#### 8. Klucz za plecami
Klucz leży za robotem. Co trzeba zrobić najpierw?
```plansza
. . * . .
# # D # #
. . . . .
. . ^ . .
. . @ . .
```
```rozwiazanie
OBRÓĆ SIĘ, IDŹ, OBRÓĆ SIĘ, IDŹ ×4
```

#### 9. Klucz z boku
Najpierw klucz, potem drzwi, a na końcu skarb.
```plansza
. . . * .
# # # D #
. . . . .
@ . ^ . .
. . . . .
```
```rozwiazanie
SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2
```

#### 10. Dwa klucze, dwoje drzwi
Każdy klucz otwiera jedne drzwi. Ile kluczy trzeba zebrać?
```plansza
# # # . .
* D D @ @
# # # . .
. . . . .
. . . . ^
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×4
```

#### 11. Klucz w kwadracie
Zbierz skarby i wróć na START. Masz tylko 4 karty, więc przyda się POWTÓRZ.
```plansza
. . . . .
. . D * .
. @ # . .
. ^ . * .
. . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

### Zestaw C: Monety i liczenie
karty: POWTÓRZ

#### 12. Razem 5
Monety mają liczby. Zbierz monety, które dają razem 5. Ani mniej, ani więcej!
```plansza
. . . . .
. 2 . 4 .
. . . . .
. 3 . 1 .
. . ^ . .
```
```ustawienia
suma: 5
```
```rozwiazanie
SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×3
```
Druga droga: 4 + 1 po prawej.

#### 13. Razem 7
Zbierz monety, które dają razem 7. Prosto do góry wyjdzie 6, więc trzeba inaczej.
```plansza
. . 2 . .
. . . . .
1 . 4 . 3
. . . . .
. . ^ . .
```
```ustawienia
suma: 7
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```

#### 14. Cztery jedynki
Zbierz wszystkie jedynki. Ile to razem? Masz tylko 6 kart.
```plansza
. . . . 1
. . . 1 .
. . 1 . .
. 1 . . .
^ . . . .
```
```ustawienia
suma: 4
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

#### 15. Trzy trójki
Zbierz monety i wróć na START. Ile to razem? Masz tylko 4 karty.
```plansza
. . . . .
. 3 . 3 .
. . # . .
. ^ . 3 .
. . . . .
```
```ustawienia
suma: 9
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

#### 16. Razem 10
Zbierz monety, które dają razem 10. Jest kilka dróg!
```plansza
3 . . . 2
. . . . .
. . 4 . .
. . . . .
1 . ^ . 6
```
```ustawienia
suma: 10
```
```rozwiazanie
IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2
```
4 + 6 = 10. Można też 4 + 2 + 3 + 1.

### Zestaw D: Pytanie JEŚLI
karty: POWTÓRZ, JEŚLI

#### 17. Kałuża czy nie?
Pole ? za każdym razem jest inne: raz kałuża, raz nic. Karta JEŚLI pyta o pole przed robotem. Ułóż jeden program na oba razy.
```plansza
. . * . .
. . ? . .
. . ^ . .
. . . . .
. . . . .
```
```ustawienia
warianty: K .
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
JEŚLI KAŁUŻA?
  TAK: SKOCZ
  NIE: IDŹ ×2
KONIEC
```

#### 18. Gdzie jest skarb?
Skarb raz jest przed robotem, a raz z prawej. Zapytaj: JEŚLI SKARB?
```plansza
. . . . .
. . . . .
. . ? . .
. . ^ ? .
. . . . .
```
```ustawienia
warianty: *. .*
pytania: SKARB?, LAWA?, KAŁUŻA?
```
```rozwiazanie
JEŚLI SKARB?
  TAK: IDŹ
  NIE: SKRĘĆ W PRAWO, IDŹ
KONIEC
```

#### 19. Lawa czy nie?
Na polu ? raz jest lawa, a raz nic. Podejdź, zapytaj, a jeśli lawa, obejdź ją.
```plansza
. . . . .
. . . . .
. . ? * .
. . . . .
. . ^ . .
```
```ustawienia
warianty: L .
pytania: LAWA?, KAŁUŻA?
```
```rozwiazanie
IDŹ
JEŚLI LAWA?
  TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ
  NIE: IDŹ, SKRĘĆ W PRAWO, IDŹ
KONIEC
```

#### 20. Kałuże w pętli
Dwa pola ?. Robot pyta dwa razy, więc włóż JEŚLI do POWTÓRZ.
```plansza
. . * . .
. . ? . .
. . . . .
. . ? . .
. . ^ . .
```
```ustawienia
warianty: KK K. .K
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
POWTÓRZ ×2
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```

#### 21. Lawa czy kałuża?
Na polu ? raz jest lawa, a raz kałuża. Kałużę przeskocz, a lawę obejdź.
```plansza
. . . * .
. . . . .
. . ? . .
. . ^ . .
. . . . .
```
```ustawienia
warianty: L K
pytania: LAWA?, KAŁUŻA?
```
```rozwiazanie
JEŚLI LAWA?
  TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3
  NIE: SKOCZ, IDŹ, SKRĘĆ W PRAWO, IDŹ
KONIEC
```

### Zestaw E: Przepis A
karty: POWTÓRZ, ZRÓB A

#### 22. Pierwszy przepis
Nowa karta ZRÓB A! W górnym rzędzie ułóż przepis A. Robot zrobi cały przepis przy każdej karcie ZRÓB A, a ZRÓB A ×2 to przepis dwa razy.
```plansza
. . . . .
. * . * .
. . . . .
. ^ . . .
. . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```

#### 23. Przepis na skok
Ułóż przepis na jeden schodek z kałużą i zrób go dwa razy.
```plansza
. . . . .
. . . . .
. . . . *
. . . K .
> K . . .
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```

#### 24. Krok i skok
Przepis A to IDŹ i SKOCZ. Między przepisami robot skręca.
```plansza
. . . . .
* . K * .
K . . . .
. . . K .
^ . . * .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKOCZ
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

#### 25. Dwa małe kwadraty
Przepis A to mały kwadrat. Zrób go dwa razy w dwóch miejscach. Masz tylko 7 kart.
```plansza
. * . . .
. * . . .
. . . . .
. * . . .
^ * . . .
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A, IDŹ ×3, ZRÓB A
```

#### 26. Schodki w dwie strony
Przepis A to jeden schodek. Robot idzie po schodkach w prawo, a potem w lewo. Masz tylko 7 kart.
```plansza
* . . . .
. . . . .
. . * . .
. * . . .
^ . . . .
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2, SKRĘĆ W LEWO, ZRÓB A ×2
```

## Plansza 7 × 7

### Zestaw A: Pętla POWTÓRZ
karty: POWTÓRZ

#### 1. Duży kwadrat
Nowa karta POWTÓRZ! Karty między POWTÓRZ a KONIEC robot robi tyle razy, ile mówi liczba. Zbierz skarby i wróć na START. Masz tylko 4 karty.
```plansza
. . . . . . .
. * . . . * .
. . . . . . .
. . . # . . .
. . . . . . .
. ^ . . . * .
. . . . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

#### 2. Kwadrat z kałużami
Na każdym boku jest kałuża. Zbierz skarby i wróć na START. Masz tylko 5 kart.
```plansza
. . . . . . .
. . . . . . .
. * . K * . .
. K L L . . .
. . L L K . .
. ^ K . * . .
. . . . . . .
```
```ustawienia
limit: 5
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKOCZ, SKRĘĆ W PRAWO
KONIEC
```

#### 3. Wysokie schodki
Znajdź kawałek, który się powtarza. Lawy nie wolno dotknąć! Masz tylko 6 kart.
```plansza
. . . . L . *
. . . L . . .
. . L . . . .
. L . * . . .
L . . . . . .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×6
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

#### 4. Schody w dół
Robot schodzi po dużych schodach. Masz tylko 6 kart.
```plansza
> . * . . . .
. . . . . . .
. . . . * . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . *
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×3
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

#### 5. Kałuże po schodach
Robot patrzy w prawo. Skok, schodek, skok, schodek… Masz tylko 6 kart.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . *
. . . L . K .
. L . K . . .
> K . . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×3
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

#### 6. Wąż
Robot chodzi jak wąż: w górę, w dół, w górę, w dół. Masz tylko 10 kart.
```plansza
* . * . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
^ * . * * . .
```
```ustawienia
limit: 10
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### Zestaw B: Klucz i drzwi
karty: POWTÓRZ

#### 7. Klucz na drodze
Drzwi otwiera tylko klucz. Robot bierze klucz, gdy na nim stanie, i dopiero wtedy przejdzie przez drzwi.
```plansza
. . . * . . .
. . . . . . .
# # # D # # #
. . . . . . .
. . . @ . . .
. . . . . . .
. . . ^ . . .
```
```rozwiazanie
IDŹ ×6
```

#### 8. Klucz z boku
Klucz leży daleko od drzwi. Najpierw klucz, potem drzwi.
```plansza
. . . . . * .
. . . . . . .
# # # # # D #
. . . . . . .
@ . . . . . .
. . . . . . .
. . . ^ . . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×4
```

#### 9. Pokój ze skarbami
Skarby są w zamkniętym pokoju. Gdzie jest klucz?
```plansza
. . . . . . .
. # # # # # .
. # * . * # .
. # # D # # .
. . . . . . .
. . . ^ . . .
. . . @ . . .
```
```rozwiazanie
OBRÓĆ SIĘ, IDŹ, OBRÓĆ SIĘ, IDŹ ×4, SKRĘĆ W LEWO, IDŹ, OBRÓĆ SIĘ, IDŹ ×2
```

#### 10. Dwa klucze, dwoje drzwi
Każdy klucz otwiera jedne drzwi. Robot musi mieć dwa klucze.
```plansza
# # # # # . .
* D . D @ . .
# # # # # . .
. . . . . @ .
. . . . . . .
. . . . . . .
. . . . . ^ .
```
```rozwiazanie
IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×5
```

#### 11. Klucze w kwadracie
Dwa klucze, dwoje drzwi i dwa skarby. Wróć na START. Masz tylko 4 karty.
```plansza
. . . . . . .
. . @ . D * .
. . . . . . .
. @ . # . . .
. . . . . D .
. ^ . * . . .
. . . . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

### Zestaw C: Monety i liczenie
karty: POWTÓRZ

#### 12. Razem 6
Monety mają liczby. Zbierz monety, które dają razem 6. Ani mniej, ani więcej!
```plansza
. . . 3 . . .
. . . . . . .
. 4 . 5 . . .
. . . . . . .
. 2 . 1 . . .
. . . . . . .
. . . ^ . . .
```
```ustawienia
suma: 6
```
```rozwiazanie
IDŹ ×4
```
1 + 5 = 6. Można też 2 + 4 po lewej.

#### 13. Razem 10
Zbierz monety, które dają razem 10.
```plansza
6 . . . . . 3
. . . . . . .
. . . 2 . . .
. . . . . . .
4 . . . . . 5
. . . . . . .
. . . ^ . . .
```
```ustawienia
suma: 10
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×4
```
4 + 6 = 10. Można też 2 + 3 + 5.

#### 14. Cztery dwójki
Zbierz wszystkie dwójki. Ile to razem? Masz tylko 6 kart.
```plansza
. . . . . . .
. . . . . . .
. . . . 2 . .
. . . 2 . . .
. . 2 . . . .
. 2 . . . . .
^ . . . 1 . .
```
```ustawienia
suma: 8
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

#### 15. Trzy trójki
Zbierz monety i wróć na START. Ile to razem? Masz tylko 4 karty.
```plansza
. . . . . . .
. 3 . . . 3 .
. . . . . . .
. . . # . . .
. . . . . . .
. ^ . . . 3 .
. . . . . . .
```
```ustawienia
suma: 9
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

#### 16. Razem 12
Zbierz monety, które dają razem 12.
```plansza
3 . . 6 . . 2
. . . . . . .
. . . . . . .
4 . . . . . 1
. . . . . . .
. . . . . . .
> . . 6 . 5 .
```
```ustawienia
suma: 12
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×6
```
6 + 6 = 12.

### Zestaw D: Pytanie JEŚLI
karty: POWTÓRZ, JEŚLI

#### 17. Kałuża czy nie?
Pole ? za każdym razem jest inne: raz kałuża, raz nic. Karta JEŚLI pyta o pole przed robotem. Ułóż jeden program na oba razy.
```plansza
. . . * . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . ? . . .
. . . . . . .
. . . ^ . . .
```
```ustawienia
warianty: K .
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
IDŹ
JEŚLI KAŁUŻA?
  TAK: SKOCZ
  NIE: IDŹ ×2
KONIEC
IDŹ ×3
```

#### 18. Gdzie jest skarb?
Skarb raz jest przed robotem, a raz z prawej. Najpierw podejdź, potem zapytaj.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
. . . ? . . .
. . . . ? . .
. . . . . . .
. . . ^ . . .
```
```ustawienia
warianty: *. .*
pytania: SKARB?, LAWA?, KAŁUŻA?
```
```rozwiazanie
IDŹ ×2
JEŚLI SKARB?
  TAK: IDŹ
  NIE: SKRĘĆ W PRAWO, IDŹ
KONIEC
```

#### 19. Lawa czy nie?
Na polu ? raz jest lawa, a raz nic. Podejdź, zapytaj, a jeśli lawa, obejdź ją.
```plansza
. . . . . . .
. . . . . . .
. . . . * . .
. . . . . . .
. . . ? . . .
. . . . . . .
. . . ^ . . .
```
```ustawienia
warianty: L .
pytania: LAWA?, KAŁUŻA?
```
```rozwiazanie
IDŹ
JEŚLI LAWA?
  TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3
  NIE: IDŹ ×3, SKRĘĆ W PRAWO, IDŹ
KONIEC
```

#### 20. Kałuże w pętli
Trzy pola ?. Robot pyta trzy razy, więc włóż JEŚLI do POWTÓRZ.
```plansza
. . . * . . .
. . . ? . . .
. . . . . . .
. . . ? . . .
. . . . . . .
. . . ? . . .
. . . ^ . . .
```
```ustawienia
warianty: KKK .K. K..
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
POWTÓRZ ×3
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```

#### 21. Skarb czy kałuża?
Na polach ? jest skarb albo kałuża. Zbierz wszystkie skarby.
```plansza
. . . * . . .
. . . ? . . .
. . . . . . .
. . . ? . . .
. . . . . . .
. . . ? . . .
. . . ^ . . .
```
```ustawienia
warianty: K*K *K* KK*
pytania: KAŁUŻA?, SKARB?, LAWA?
```
```rozwiazanie
POWTÓRZ ×3
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```

### Zestaw E: Przepis A
karty: POWTÓRZ, ZRÓB A

#### 22. Pierwszy przepis
Nowa karta ZRÓB A! W górnym rzędzie ułóż przepis A. Robot zrobi cały przepis przy każdej karcie ZRÓB A, a ZRÓB A ×3 to przepis trzy razy.
```plansza
. . . . . . .
. . . . . . .
. * . . * . .
. . . . . . .
. . . . . . .
. ^ . . * . .
. . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×3, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
```

#### 23. Krok i skok
Przepis A to IDŹ i SKOCZ. Między przepisami robot skręca raz w prawo, raz w lewo.
```plansza
. . . . . K *
. . . K . . .
. . . . . . .
. . K * . . .
K . . . . . .
. . . . . . .
^ . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKOCZ
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

#### 24. Trzy małe kwadraty
Przepis A to mały kwadrat. Zrób go trzy razy w trzech miejscach.
```plansza
. . . . . . .
. * . . . . .
. . . . . . .
. * . . . . .
. . . . . . .
. * . . . . .
^ . . . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A, IDŹ ×2, ZRÓB A, IDŹ ×2, ZRÓB A
```

#### 25. Schodki w dwie strony
Przepis A to jeden schodek. Robot idzie po schodkach w prawo, a potem w lewo. Masz tylko 7 kart.
```plansza
* . . . . . .
. . . . . . .
. . . . . . .
. . . * . . .
. . * . . . .
. . . . . . .
^ . . . . . .
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3, SKRĘĆ W LEWO, ZRÓB A ×3
```

#### 26. Przepis z kluczami
Przepis A to duży schodek. Po drodze są klucze i drzwi. Masz tylko 5 kart.
```plansza
. . . . . . *
. . . . . . .
. . . . . . *
. . . . D . .
. . . . @ . .
. . D . . . .
> @ . . . . .
```
```ustawienia
limit: 5
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
```

## Plansza 9 × 9

### Zestaw A: Pętla POWTÓRZ
karty: POWTÓRZ

#### 1. Wielki kwadrat
Nowa karta POWTÓRZ! Karty między POWTÓRZ a KONIEC robot robi tyle razy, ile mówi liczba. Zbierz skarby i wróć na START. Masz tylko 4 karty.
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . . . . . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . * .
. . . . . . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
```

#### 2. Kwadrat z kałużami
Na każdym boku jest kałuża. Zbierz skarby i wróć na START. Masz tylko 5 kart.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. * . . K * . . .
. K . . . . . . .
. . . L . . . . .
. . . . . K . . .
. ^ K . . * . . .
. . . . . . . . .
```
```ustawienia
limit: 5
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKOCZ, SKRĘĆ W PRAWO
KONIEC
```

#### 3. Wysokie schodki
Znajdź kawałek, który się powtarza. Lawy nie wolno dotknąć! Masz tylko 6 kart.
```plansza
. . . . . . . . *
. . . . L . . . .
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
L . . . . . . . .
. . . . . . . . .
. . L . . . . . .
^ . . . . . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

#### 4. Kałuże po schodach
Robot patrzy w prawo. Skok, schodek, skok, schodek… Masz tylko 6 kart.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . *
. . . . . . . K .
. . . . . K . . .
. . . K . . . . .
> K . . . . . . .
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

#### 5. Schody w dół
Robot schodzi po dużych schodach i omija lawę. Masz tylko 6 kart.
```plansza
> . . L . . . . .
. . . . . . . . .
. . * . . L . . .
. . . . . . . . .
. . . . . . . L .
. . . . . . . . .
. . . . . . * . .
. . . . . . . . .
. . . . . . . . *
```
```ustawienia
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

#### 6. Wąż
Robot chodzi jak wąż: w górę, w dół, w górę, w dół. 8 kroków to IDŹ ×6 i IDŹ ×2. Masz tylko 12 kart.
```plansza
* . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ * . * * . . . .
```
```ustawienia
limit: 12
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×6, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### Zestaw B: Klucz i drzwi
karty: POWTÓRZ

#### 7. Klucz na drodze
Drzwi otwiera tylko klucz. Robot bierze klucz, gdy na nim stanie, i dopiero wtedy przejdzie przez drzwi. 8 kroków to IDŹ ×6 i IDŹ ×2.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
# # # # D # # # #
. . . . . . . . .
. . . . @ . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×6, IDŹ ×2
```

#### 8. Klucz z boku
Klucz leży daleko od drzwi. Najpierw klucz, potem drzwi.
```plansza
. . . . . . . * .
. . . . . . . . .
# # # # # # # D #
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
@ . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×6, IDŹ, SKRĘĆ W LEWO, IDŹ ×6
```

#### 9. Pokój ze skarbami
Skarby są w zamkniętym pokoju. Gdzie jest klucz?
```plansza
. . . . . . . . .
. # # # # # # # .
. # . * . . . * .
. # # # D # # # .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
. . . . . . . . .
. . . . @ . . . .
```
```rozwiazanie
OBRÓĆ SIĘ, IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×6, SKRĘĆ W LEWO, IDŹ, OBRÓĆ SIĘ, IDŹ ×4
```

#### 10. Trzy klucze, troje drzwi
Każdy klucz otwiera jedne drzwi. Ile kluczy zbierze robot po drodze?
```plansza
# # # # # # # . .
* D . D . D @ @ .
# # # # # # # . .
. . . . . . . . .
. . . . . . . @ .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . ^ .
```
```rozwiazanie
IDŹ ×6, IDŹ, SKRĘĆ W LEWO, IDŹ ×6, IDŹ
```

#### 11. Klucze w kwadracie
Dwa klucze, dwoje drzwi i dwa skarby. Wróć na START. Masz tylko 4 karty.
```plansza
. . . . . . . . .
. . . @ . . D . .
. . . . . . . . .
. . . . . . . . .
. . . . # . . D .
. @ . . . . . . .
. . . . . . . . .
. ^ . . * . . * .
. . . . . . . . .
```
```ustawienia
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
```

### Zestaw C: Monety i liczenie
karty: POWTÓRZ

#### 12. Razem 8
Monety mają liczby. Zbierz monety, które dają razem 8. Ani mniej, ani więcej!
```plansza
. . . . 2 . . . .
. . . . . . . . .
. . . . . . . . .
. . . . 5 . . . .
. . . . . . . . .
. . 6 . . . . . .
. . . . 3 . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```ustawienia
suma: 8
```
```rozwiazanie
IDŹ ×5
```
3 + 5 = 8.

#### 13. Razem 10
Zbierz monety, które dają razem 10.
```plansza
. . . . 3 . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
5 . . . 6 . . . 4
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . 2
```
```ustawienia
suma: 10
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4
```
6 + 4 = 10.

#### 14. Cztery dwójki
Zbierz wszystkie dwójki. Ile to razem? Masz tylko 6 kart.
```plansza
. . . . . . . . 2
. . . . . . . . .
. . . . . . 2 . .
. . . . . . . . .
. . . . 2 . . . .
. . . . . . . . .
. . 2 . . . . . .
. . . . . . . . .
^ . . . . 1 . . .
```
```ustawienia
suma: 8
limit: 6
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

#### 15. Dookoła po monety
Zbierz monety i wróć na START. Ile to razem? Masz tylko 4 karty.
```plansza
. . . . . . . . .
. 2 . . . . . 3 .
. . . . . . . . .
. . . . . . . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . 4 .
. . . . . . . . .
```
```ustawienia
suma: 9
limit: 4
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
```

#### 16. Dwie szóstki
Zbierz monety, które dają razem 12.
```plansza
3 . . . 6 . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
5 . . . ^ . . . 4
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . 6 . . . .
```
```ustawienia
suma: 12
```
```rozwiazanie
IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×6, IDŹ ×2
```
6 + 6 = 12.

### Zestaw D: Pytanie JEŚLI
karty: POWTÓRZ, JEŚLI

#### 17. Kałuża czy nie?
Pole ? za każdym razem jest inne: raz kałuża, raz nic. Karta JEŚLI pyta o pole przed robotem. Ułóż jeden program na oba razy.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```ustawienia
warianty: K .
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
IDŹ ×3
JEŚLI KAŁUŻA?
  TAK: SKOCZ
  NIE: IDŹ ×2
KONIEC
IDŹ ×3
```

#### 18. Gdzie jest skarb?
Skarb raz jest przed robotem, a raz z prawej. Najpierw podejdź, potem zapytaj.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . ? . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```ustawienia
warianty: *. .*
pytania: SKARB?, LAWA?, KAŁUŻA?
```
```rozwiazanie
IDŹ ×4
JEŚLI SKARB?
  TAK: IDŹ
  NIE: SKRĘĆ W PRAWO, IDŹ
KONIEC
```

#### 19. Kałuże w pętli
Cztery pola ?. Robot pyta cztery razy, więc włóż JEŚLI do POWTÓRZ.
```plansza
. . . . * . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . ^ . . . .
```
```ustawienia
warianty: K.K. .K.K KK..
pytania: KAŁUŻA?, LAWA?
```
```rozwiazanie
POWTÓRZ ×4
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```

#### 20. Lawa w pętli
Na polach ? może być lawa. Jeśli lawa, obejdź ją z prawej. Robot pyta cztery razy.
```plansza
. . . . * . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . ^ . . . .
```
```ustawienia
warianty: L.L. .L.L LL..
pytania: LAWA?, KAŁUŻA?
```
```rozwiazanie
POWTÓRZ ×4
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
    NIE: IDŹ ×2
  KONIEC
KONIEC
```

#### 21. Lawa czy kałuża?
Na polach ? jest lawa albo kałuża. Kałużę przeskocz, a lawę obejdź z prawej.
```plansza
. . . . * . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . ^ . . . .
```
```ustawienia
warianty: LKLK KLKL KKLL
pytania: LAWA?, KAŁUŻA?
```
```rozwiazanie
POWTÓRZ ×4
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
    NIE: SKOCZ
  KONIEC
KONIEC
```

### Zestaw E: Przepis A
karty: POWTÓRZ, ZRÓB A

#### 22. Pierwszy przepis
Nowa karta ZRÓB A! W górnym rzędzie ułóż przepis A. Robot zrobi cały przepis przy każdej karcie ZRÓB A, a ZRÓB A ×3 to przepis trzy razy.
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . * .
. . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
```

#### 23. Krok i skok
Przepis A to IDŹ i SKOCZ. Między przepisami robot skręca raz w prawo, raz w lewo.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . K * . .
. . . K . . . . .
. . . . . . . . .
. . K * . . . . .
K . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKOCZ
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

#### 24. Trzy kwadraty
Przepis A to kwadrat. Zrób go trzy razy w trzech miejscach.
```plansza
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A, IDŹ ×3, ZRÓB A, IDŹ ×3, ZRÓB A
```

#### 25. Schodki w dwie strony
Przepis A to jeden schodek. Robot idzie po schodkach w prawo, a potem w lewo. Masz tylko 7 kart.
```plansza
* . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```ustawienia
limit: 7
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4, SKRĘĆ W LEWO, ZRÓB A ×4
```

#### 26. Przepis z kluczami
Przepis A to duży schodek. Po drodze są klucze i drzwi. Masz tylko 5 kart.
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . . . *
. . . . . . D . .
. . . . . . @ . .
. . . . D . . . .
. . . . @ . . . .
. . D . . . . . .
> @ . . . . . . .
```
```ustawienia
limit: 5
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
