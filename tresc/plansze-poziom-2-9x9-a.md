# Plansze 9 × 9, poziom 2, zestaw A (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Wszystkie gry są z pętlą POWTÓRZ.

### 1. Duży kwadrat
Obejdź całą planszę dookoła, zbierz skarby w rogach i wróć na START.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
Bez pętli to 12 kart, z pętlą tylko 5.

### 2. Ile razy?
W pętli jest IDŹ ×2. Ile razy ją powtórzyć, żeby dojść do skarbu?
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2
KONIEC
```
4 razy po 2 kroki to 8 kroków.

### 3. Długie schody
Robot wchodzi po schodkach. Znajdź kawałek, który się powtarza.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . * . L
. . . . . . . . .
. . . . * . L . .
. . . . . . . . .
. . * . L . . . .
. . . . . . . . .
^ . L . . . . . .
```
```rozwiazanie
POWTÓRZ ×6
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### 4. Dookoła płotu
Obejdź płot z klocków, zbierz skarby i wróć na START.
```plansza
. . . . . . . . .
. . . . * . . . .
. . . # . . . . .
. . . # . . . . .
. . . # . . . . .
. . . # . . . . .
. . . # . . . . .
. . ^ . * . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

---

# Plansze 9 × 9, poziom 2, zestaw A (2/4)

### 5. Gdzie stanie robot? Schodki
Programista kładzie figurkę tam, gdzie stanie robot. Robot liczy powtórzenia.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . . .
```
```program
POWTÓRZ ×3
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 5. polu od lewej. Robot patrzy w górę.

### 6. Znajdź błąd: zły skręt
Robot miał obejść jezioro lawy i zebrać skarby, ale wypadł z planszy: BUM! Co zmienić?
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . L L L . . .
. . . L L L . . .
. . . L L L . . .
. . . . . . . . .
. ^ . . . . . * .
. . . . . . . . .
```
```program
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W LEWO
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
```
W pętli ma być SKRĘĆ W PRAWO. Jedna zmiana poprawia wszystkie 4 powtórzenia.

### 7. Kałuże po schodach
Robot patrzy w prawo. Skacz i wspinaj się do skarbu.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . * . .
. . . . . . K . .
. . . . . K . . .
. . . . K L . . .
. . * K . . . . .
. . K L . . . . .
> K . . L . . . .
```
```rozwiazanie
POWTÓRZ ×3
  SKOCZ, SKRĘĆ W LEWO, SKOCZ, SKRĘĆ W PRAWO
KONIEC
```

### 8. Znajdź błąd: zła liczba
Robot obszedł jezioro, ale ominął jeden skarb. Którą liczbę zmienić?
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . L L L . . .
. . . L L L . . .
. . . L L L . . .
. . . . . . . . .
. ^ . . . . . * .
. . . . . . . . .
```
```program
POWTÓRZ ×4
  IDŹ ×5, SKRĘĆ W PRAWO
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
```
Bok kwadratu ma 6 kroków, a nie 5.

---

# Plansze 9 × 9, poziom 2, zestaw A (3/4)

### 9. Grzebień
Robot zbiera skarby na ząbkach grzebienia. Co się powtarza?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . * . * . * . .
. L . L . L . L .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×3
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 10. Ile razy? Duże schody
W pętli jest duży schodek. Ile razy go powtórzyć?
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . . . L
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . . . L . . . .
. L . . . . . . .
^ . L . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```
4 schodki po 2 pola w górę to 8 pól.

### 11. Gdzie stanie robot? Krok w tył
Robot idzie 2 kroki do przodu i 1 do tyłu. Gdzie skończy?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```program
POWTÓRZ ×3
  IDŹ ×2, OBRÓĆ SIĘ, IDŹ, OBRÓĆ SIĘ
KONIEC
```
**Rozwiązanie:** Robot stanie w 6. rzędzie od góry, na 5. polu od lewej. Robot patrzy w górę. Każde powtórzenie to tylko 1 pole do przodu.

### 12. Gdzie stanie robot? Pętla w pętli
Pętla może być w środku pętli. Robot liczy na głos.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
POWTÓRZ ×2
  POWTÓRZ ×3
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 6. rzędzie od góry, na 4. polu od lewej. Robot patrzy w dół.

---

# Plansze 9 × 9, poziom 2, zestaw A (4/4)

### 13. Trzy kwadraty
Pętla w pętli: mała pętla rysuje kwadrat, a duża powtarza go 3 razy.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . * . * . .
. L . L . L . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×3
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 14. Motylek
Dwa kwadraty jak skrzydła motyla. Zbierz skarby i wróć na START.
```plansza
. . . . . . . . .
. . . . . . . * .
. . . . . L . . .
. . . . . . L . .
. . . . ^ . . . .
. . L . . . . . .
. . . L . . . . .
. * . . . . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```

### 15. Wąż
Robot chodzi jak wąż: w górę i w dół. Zbierz cztery skarby.
```plansza
* . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. L . L . L . L .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . * . . . * . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×4, IDŹ ×4, SKRĘĆ W PRAWO
  IDŹ ×2, SKRĘĆ W PRAWO
  IDŹ ×4, IDŹ ×4, SKRĘĆ W LEWO
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 16. Twoja misja z pętlą
Programista układa pętlę, a Robot zgaduje, gdzie stanie. Potem idzie i sprawdza.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Zacznijcie od POWTÓRZ ×2 i dwóch kart w środku.
