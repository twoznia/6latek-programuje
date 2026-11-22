# Misje dla dwojga na dużej planszy

30 nowych gier na planszy 7 × 7. Są trochę trudniejsze: dłuższe programy, więcej przeszkód i kilka skarbów. Wciąż wystarczą karty z poziomu 1. Zasady (Programista układa, Robot chodzi) są w pliku „gra dla dwojga”.

Niebieskie kółko to START (trójkąt pokazuje, gdzie Robot patrzy). Gwiazdka to skarb, brązowy kwadrat to klocek, czerwone pole to LAWA, niebieskie to KAŁUŻA.

### 1. Zygzak
Mury z lawy na zmianę z lewej i z prawej.
```plansza
. . . . . . *
. . . . . . .
L L L L L . .
. . . . . . .
. . L L L L L
. . . . . . .
^ . . . . . .
```


### 2. Kałuża za rogiem
Do skarbu da się dojść tylko od dołu.
```plansza
. . . . . . .
. . . . . . .
. . . . . L .
. . . . L * L
. . . . . K .
. . . . . . .
> . . . . . .
```


### 3. Brama
W murze z klocków jest jedna brama. Gdzie?
```plansza
. . . * . . .
. . . . . . .
# # . # # # #
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . ^ .
```


### 4. Dwie rzeki
Dwie rzeki z kałuż, a między nimi lawa.
```plansza
. . . . . . *
K K K K K K K
. . . . . . .
. . . L . . .
. . . . . . .
K K K K K K K
. . . ^ . . .
```


---

# Misje na dużej planszy, ciąg dalszy

### 5. Skarby w rzędzie
Trzy skarby w jednej linii. Ile kart wystarczy?
```plansza
. . . . . . .
. . . . . . .
. * . * . * .
. . . . . . .
. . . . . . .
. . . . . . .
^ . . . . . .
```


### 6. Pokój bez drzwi
Skarb jest w pokoju z lawy. Do środka trzeba wskoczyć przez kałużę.
```plansza
. . . . . . .
. L L L L L .
. L * . . L .
. L . . . L .
. L . . . L .
. L L K L L .
. . . ^ . . .
```


### 7. Dwie kałuże w murach
W każdym murze z lawy jest jedna kałuża.
```plansza
. . . * . . .
. . . . . . .
L L L K L L L
. . . . . . .
L K L L L L L
. . . . . . .
. ^ . . . . .
```


### 8. Na skróty przez kałuże
Droga dookoła jest długa. Czy da się szybciej?
```plansza
* . . . . . .
K . . . . . .
. . . . . . .
K . . . . . .
. . . . . . .
K . . . . . .
^ . . . . . .
```


---

# Misje na dużej planszy, ciąg dalszy

### 9. Cztery rogi
Zbierz skarby we wszystkich rogach. Robot zaczyna w środku.
```plansza
* . . . . . *
. . . . . . .
. . . . . . .
. . . ^ . . .
. . . . . . .
. . . . . . .
* . . . . . *
```


### 10. Powrót przez kałużę
Weź skarb i wróć na START. Kałuży nie wolno dotknąć.
```plansza
. . . * . . .
. . . . . . .
. . . K . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . ^ . . .
```


### 11. Gdzie stanie robot? (1)
Programista kładzie figurkę tam, gdzie stanie robot. Robot sprawdza.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . ^
```
```program
IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ
```


### 12. Znajdź błąd: skręt
Robot wpada do lawy: BZZZT! Która karta jest zła?
```plansza
. . . . . . .
. * . . . . .
. . . . . . .
. . L L L L .
. . . . . . .
. . . . . . .
. . . . . ^ .
```
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×3
```


---

# Misje na dużej planszy, ciąg dalszy

### 13. Labirynt z klocków
Na klocki nie wolno wchodzić. Szukaj najkrótszej drogi.
```plansza
. . . # . . *
. # . # . # .
. # . . . # .
. # # # # # .
. . . . . . .
# # # # # # .
^ . . . . . .
```


### 14. Skok i zakręt
Kałuże stoją na drodze. Obejść czy skoczyć?
```plansza
. . . . . . .
. . . . . K *
. . . . . . .
. . . . . . .
. K . . . . .
. . . . . . .
. ^ . . . . .
```


### 15. Tylko 5 kart
Programista ma najwyżej 5 kart. Robot pilnuje, czy nie ma ich za dużo.
```plansza
. . . . . . *
. . . . . . .
L L L L L L .
. . . . . . .
. . . . . . .
. . . . . . .
^ . . . . . L
```


### 16. Dwa skarby, dwie kałuże
Zbierz oba skarby. Kałuże przeskakujemy.
```plansza
* . . . . . .
. . . . . . .
K . . . . . .
. . . . . . .
. . . . . . *
. . . . . . K
. . . ^ . . .
```


---

# Misje na dużej planszy, ciąg dalszy

### 17. Pół na pół: wyspy
Pierwszy gracz prowadzi robota na pierwszą wyspę, drugi na drugą.
```plansza
. . . . . . .
. L L L . . .
. L * L . . .
. . . . . L .
. . . . L * L
. . . . . . .
^ . . . . . .
```


### 18. Most
Przez rzekę lawy prowadzi most z jednego pola.
```plansza
. . . . . * .
. . . . . . .
L L L L . L L
L L L L . L L
. . . . . . .
. . . . . . .
^ . . . . . .
```


### 19. Gdzie stanie robot? (2)
Program ma skoki. Robot liczy na głos.
```plansza
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . K . . .
. . . . . . .
. ^ . . . . .
```
```program
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, SKOCZ ×2, SKRĘĆ W PRAWO, IDŹ ×3
```


### 20. Znajdź błąd: brakuje karty
W programie brakuje jednej karty. Robot wchodzi w kałużę: PLUSK!
```plansza
. . . . . . .
. . . . * . .
. . . . . . .
. . . . K . .
. . . . . . .
. . . . . . .
^ . . . . . .
```
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×3
```


---

# Misje na dużej planszy, ciąg dalszy

### 21. Klocki i lawa
Na klocki i lawę nie wolno wchodzić.
```plansza
* . # . . . .
. . # . L . .
. . # . L . .
. . . . L . .
. # # # L . .
. . . . . . .
. . . . . . ^
```


### 22. Tam i z powrotem przez bramę
Weź skarb i wróć na START.
```plansza
. . . . . * .
. . . . . . .
L L . L L L L
. . . . . . .
. . . . . . .
. . . . . . .
. . ^ . . . .
```


### 23. Wyścig na liczby
Każdy układa swój program. Wygrywa ten, kto ma mniej kart. Remis? Liczymy kroki.
```plansza
. . . * . . .
. . . . . . .
. L . K . L .
. L . . . L .
. L . K . L .
. L . . . L .
. L . ^ . L .
```


### 24. Spirala z kałużą
Skarb jest w środku spirali. Jest skrót przez kałużę!
```plansza
. . . . . . .
. L L L L L .
. L . . . L .
. L . * . L .
. L K L L L .
. . . . . . .
. ^ . . . . .
```


---

# Misje na dużej planszy, ciąg dalszy

### 25. Trzy skarby i powrót
Zbierz trzy skarby i wróć na START.
```plansza
. . . * . . .
. . . . . . .
. . . . . . .
* . . . . . *
. . . . . . .
. . . . . . .
. . . ^ . . .
```


### 26. Na zmianę
Gracze kładą po jednej karcie na zmianę. Robot rusza dopiero, gdy program jest gotowy.
```plansza
. . . . . . *
. L L L L L L
. . . . . . .
L L L L L . .
. . . . . . .
. . . . . . .
^ . . . . . .
```


### 27. Robot z zamkniętymi oczami
Robotem jest dorosły z zamkniętymi oczami. Programista czyta mu karty.
```plansza
. . . . . . .
. * . . . . .
. . . . . L .
. . . . . L .
. L L L . L .
. . . . . . .
. . . . . ^ .
```


### 28. Znajdź błąd: zła liczba
Robot uderza w ścianę: BUM! Która liczba jest zła?
```plansza
* . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . ^
```
```program
SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6, IDŹ
```


---

# Misje na dużej planszy, ciąg dalszy

### 29. Wielka pętla
Robot obchodzi lawę dookoła i zbiera wszystkie skarby.
```plansza
. . * . . . .
. . . . . . .
* . L L L . *
. . L L L . .
. . L L L . .
. . . . . . .
. . . . ^ . .
```


### 30. Super finał
Lawa, kałuże, klocki i dwa skarby. Kto ułoży program z najmniejszej liczby kart?
```plansza
. . . # . . *
. . . # . . .
* . . K . . .
L L . . . L L
. . . L . . .
. . . . . . .
. . . ^ . . .
```

---

# Rozwiązania dla dorosłego

To rozwiązania z najmniejszą liczbą kart. Każdy program, który dochodzi do skarbu bez wchodzenia na klocek, lawę ani kałużę, też jest dobry.

### 1. Zygzak
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×3
```


### 2. Kałuża za rogiem
```program
IDŹ ×5, SKRĘĆ W LEWO, IDŹ, SKOCZ
```


### 3. Brama
```program
SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ
```


### 4. Dwie rzeki
```program
SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, SKOCZ ×3
```


### 5. Skarby w rzędzie
```program
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×5
```


### 6. Pokój bez drzwi
```program
SKOCZ ×2, SKRĘĆ W LEWO, IDŹ
```


### 7. Dwie kałuże w murach
```program
IDŹ, SKOCZ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, SKOCZ, IDŹ
```


### 8. Na skróty przez kałuże
```program
SKOCZ ×3
```


---

# Rozwiązania, ciąg dalszy

### 9. Cztery rogi
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6
```


### 10. Powrót przez kałużę
```program
IDŹ, SKOCZ ×2, IDŹ, OBRÓĆ SIĘ, IDŹ, SKOCZ, IDŹ ×3
```


### 11. Gdzie stanie robot? (1)
W 4. rzędzie od góry, na 3. polu od lewej. Robot patrzy w lewo.


### 12. Znajdź błąd: skręt
```program
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×3
```
Pierwszy skręt ma być W LEWO, a nie W PRAWO.


### 13. Labirynt z klocków
```program
SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6
```


### 14. Skok i zakręt
```program
SKRĘĆ W PRAWO, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×5
```


### 15. Tylko 5 kart
```program
IDŹ, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×5
```


### 16. Dwa skarby, dwie kałuże
```program
SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, SKOCZ ×3, SKRĘĆ W LEWO, IDŹ ×6
```


---

# Rozwiązania, ciąg dalszy

### 17. Pół na pół: wyspy
```program
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
```


### 18. Most
```program
SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ
```


### 19. Gdzie stanie robot? (2)
W 2. rzędzie od góry, na 6. polu od lewej. Robot patrzy w prawo.


### 20. Znajdź błąd: brakuje karty
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, SKOCZ, IDŹ
```
Zamiast IDŹ ×3 na końcu robot musi przeskoczyć kałużę: SKOCZ, IDŹ.


### 21. Klocki i lawa
```program
SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6
```


### 22. Tam i z powrotem przez bramę
```program
IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×6
```


### 23. Wyścig na liczby
```program
IDŹ, SKOCZ ×2, IDŹ
```


### 24. Spirala z kałużą
```program
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ, SKOCZ, SKRĘĆ W PRAWO, IDŹ
```


---

# Rozwiązania, ciąg dalszy

### 25. Trzy skarby i powrót
```program
SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×3
```


### 26. Na zmianę
```program
SKRĘĆ W PRAWO, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×5, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×6
```


### 27. Robot z zamkniętymi oczami
```program
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×5
```


### 28. Znajdź błąd: zła liczba
```program
SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6
```
Ostatnia karta IDŹ jest zbędna: robot doszedł już do skarbu i uderzyłby w ścianę. Trzeba ją zabrać.


### 29. Wielka pętla
```program
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×2
```


### 30. Super finał
```program
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W LEWO, SKOCZ ×2, OBRÓĆ SIĘ, SKOCZ ×3, SKRĘĆ W LEWO, IDŹ ×2
```
