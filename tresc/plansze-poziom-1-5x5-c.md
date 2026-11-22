# Plansze 5 × 5, poziom 1, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 33. Gdzie skończy robot?
Przeczytaj program i połóż skarb tam, gdzie robot się zatrzyma.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
```
**Rozwiązanie:** W drugim rzędzie od góry, na czwartym polu od lewej.

### 34. Literka U
Przejdź dookoła ściany z klocków.
```plansza
. . . . .
. # . . .
. # . . .
. # . . .
^ # * . .
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4
```

### 35. Trzy skarby
Robot patrzy w prawo. Zbierz wszystkie skarby.
```plansza
. . . . .
. . . . .
. . * . *
. . . L .
> . * . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```

### 36. Trzy skarby w rogach
Robot musi stanąć na wszystkich trzech skarbach.
```plansza
* . . . *
. . . . .
. . . . .
. . . . .
^ . . . *
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4
```

---

# Plansze 5 × 5, poziom 1, zestaw C (2/4)

### 37. Gdzie stanie robot? Zakręty
Programista kładzie figurkę Lego tam, gdzie według niego stanie robot. Potem Robot idzie i sprawdza.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. ^ . . .
```
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ
```
**Rozwiązanie:** W 3. rzędzie od góry, na 4. polu od lewej. Robot patrzy w dół.

### 38. Gdzie stanie robot? Skok
Programista kładzie figurkę tam, gdzie stanie robot. Robot sprawdza.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
IDŹ, SKRĘĆ W PRAWO, SKOCZ, SKRĘĆ W LEWO, IDŹ ×2
```
**Rozwiązanie:** W 2. rzędzie od góry, na 3. polu od lewej. Robot patrzy w górę.

### 39. Dwa skarby po drodze
Robot musi stanąć na obu skarbach, w dowolnej kolejności.
```plansza
* . . . .
. . . . .
. . K . .
. . . . .
. . ^ . *
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×4
```

### 40. Mur z klocków
W murze jest jedna dziura.
```plansza
. . * . .
. . . . .
# # # . #
. . . . .
. ^ . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ
```

---

# Plansze 5 × 5, poziom 1, zestaw C (3/4)

### 41. Lawa!
Lawę trzeba obejść dookoła.
```plansza
. . * . .
. . . . .
. . L . .
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
```

### 42. Kałuża i lawa
Kałużę można przeskoczyć, lawy nie.
```plansza
. . * . .
. . L . .
. . . . .
. . K . .
. . ^ . .
```
```rozwiazanie
SKOCZ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ
```

### 43. Korytarz z lawy
Robot idzie korytarzem. Lawa po obu stronach!
```plansza
L . * L .
L . L L .
L . . . L
L L L . L
. . . ^ .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ
```

### 44. Znajdź błąd: zły skręt
Program już leży, ale jest w nim jedna zła karta. Robot idzie, a Programista szuka błędu.
```plansza
. . . . *
. . . . .
L L L . .
. . . . .
^ . . . .
```
```program
IDŹ, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×3
```
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ
```
Druga karta SKRĘĆ powinna być W LEWO. Po poprawce robot dochodzi do prawego brzegu i trzeba jeszcze dołożyć SKRĘĆ W PRAWO i IDŹ.

---

# Plansze 5 × 5, poziom 1, zestaw C (4/4)

### 45. Kałuża i powrót
Weź skarb i wróć na START. Kałuży nie wolno dotknąć.
```plansza
. . * . .
. . . . .
. . K . .
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ, SKOCZ, IDŹ, OBRÓĆ SIĘ, IDŹ, SKOCZ, IDŹ
```

### 46. Cztery rogi
Robot zaczyna w środku. Zbierz skarby we wszystkich rogach.
```plansza
* . . . *
. . . . .
. . ^ . .
. . . . .
* . . . *
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4
```

### 47. Dwa skarby i klocki
Zbierz oba skarby. Na klocki nie wolno wchodzić.
```plansza
* . # . *
. . # . .
. . . . .
. # # # .
. . ^ . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×2
```

### 48. Pułapka dla dorosłego
Dziecko rozkłada 3 lawy, 1 kałużę i skarb. Dorosły jest Programistą, a dziecko sprawdza jego program jako Robot.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dziecko sprawdza program dorosłego, chodząc jako Robot.
