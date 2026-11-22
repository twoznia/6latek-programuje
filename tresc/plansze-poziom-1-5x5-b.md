# Plansze 5 × 5, poziom 1, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 17. Skrót przez kałużę
Najkrótszy program ma tylko 3 karty.
```plansza
* . L . .
. . L . .
K . . . .
. . L . .
^ . L . .
```
```rozwiazanie
IDŹ, SKOCZ, IDŹ
```

### 18. W lewo!
Robot czyta głośno każdą kartę. Uwaga na lewo i prawo.
```plansza
. . . . .
* . . . .
. . . . .
. . . . .
. . . ^ .
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×3
```

### 19. Znajdź błąd: kałuża
W programie brakuje jednej karty. Robot wpada do kałuży: PLUSK! Którą kartę dołożyć?
```plansza
. . * . .
. . . . .
. . K . .
. . . . .
. . ^ . .
```
```program
IDŹ, IDŹ ×2
```
```rozwiazanie
IDŹ, SKOCZ, IDŹ
```
Zamiast IDŹ ×2 robot musi skoczyć: IDŹ, SKOCZ, IDŹ.

### 20. Slalom
Robot omija słupki z lawy.
```plansza
. . . . *
. L . L .
. . . . .
. L . L .
^ . . . .
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4
```

---

# Plansze 5 × 5, poziom 1, zestaw B (2/4)

### 21. Kałuża w rogu
Skarb leży za kałużą w rogu planszy.
```plansza
* K . . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W LEWO, SKOCZ
```

### 22. Robot patrzy w prawo
Gdzie jest jego lewa ręka?
```plansza
. . . . .
. . . * .
. . . . .
. . . . .
> . . . .
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×3
```

### 23. Znajdź błąd: zła liczba
Robot uderza w ścianę: BUM! Którą liczbę zmienić?
```plansza
. . . . .
. . . . *
. . . . .
. . . . .
^ . . . .
```
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×5
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×4
```
Na końcu robot ma iść 4 pola, a nie 5.

### 24. Tylko 3 karty
Programista może położyć najwyżej 3 karty.
```plansza
. . . . .
. * . . .
. . . . .
. . . . .
. . . . <
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×3
```

---

# Plansze 5 × 5, poziom 1, zestaw B (3/4)

### 25. Kałuża i lawa obok siebie
Jedno można przeskoczyć, drugiego nie.
```plansza
. . * . .
. . . . .
. L K . .
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ, SKOCZ, IDŹ
```

### 26. Labirynt
Na klocki nie wolno wchodzić.
```plansza
. . . # *
. # . # .
. # . . .
. # # # .
^ . . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×4
```

### 27. Wyspa
Skarb leży na wyspie w lawie. Jest tylko jedno wejście.
```plansza
. . . . .
. L L L .
. L * L .
. . . L .
^ . . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2
```

### 28. Dyktando
Programista nie układa kart, tylko mówi program na głos. Robot sam układa karty i dopiero potem idzie.
```plansza
. . . . .
. * . . .
. . . . .
. . . . .
. . . . >
```
```rozwiazanie
SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×3
```

---

# Plansze 5 × 5, poziom 1, zestaw B (4/4)

### 29. Skarb w kącie
Lawa pilnuje skarbu z dwóch stron.
```plansza
. . . L *
. . . L .
. . . . .
. . . . .
^ . . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×4
```

### 30. Omiń klocek
Na klocek nie wolno wejść!
```plansza
. . * . .
. . . . .
. # . . .
. . . . .
. ^ . . .
```
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3
```

### 31. Wyzwanie
Ułóż program z jak najmniejszej liczby kart.
```plansza
# . . . *
. . . . .
. . . . .
. . . . .
^ . . . #
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×2
```

### 32. Lawa i kałuża
Robot patrzy w prawo.
```plansza
. . . . .
. . . . .
. . . . *
. . . . .
> K . L .
```
```rozwiazanie
SKOCZ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```
