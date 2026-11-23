# Plansze 7 × 7, poziom 1, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 17. Wielka rzeka
Na planszy 7 × 7. Rzeka ma dwa rzędy kałuż. Czy jeden skok wystarczy?
```plansza
. . . . . * .
. . . . . . .
K K K K K K K
. . . . . . .
K K K K K K K
. . . . . . .
. ^ . . . . .
```
```rozwiazanie
IDŹ, SKOCZ ×2, IDŹ, SKRĘĆ W PRAWO, IDŹ ×4
```

### 18. Pół na pół
Pierwszy gracz programuje drogę do pierwszego skarbu. Potem zamiana ról: drugi programuje dalej, od miejsca, gdzie stoi robot.
```plansza
. . . . . . *
. . . . . . .
. # # # # . .
. . . . . . .
. * . . . . .
. . . . . . .
^ . . . . . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×4
```

### 19. Zygzak
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
```rozwiazanie
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×3
```

### 20. Znajdź błąd: skręt
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
```rozwiazanie
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×3
```
Pierwszy skręt ma być W LEWO, a nie W PRAWO.

---

# Plansze 7 × 7, poziom 1, zestaw B (2/4)

### 21. Tylko 5 kart
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
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×5
```

### 22. Tylko 6 kart
Programista może położyć najwyżej 6 kart. Robot sprawdza, czy to się uda.
```plansza
. . . . . . .
. . . . . . *
L L L L . L L
. . . . . . .
. . . . . . .
. . . . . . .
^ . . . . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×5, SKRĘĆ W PRAWO, IDŹ ×2
```

### 23. Brama
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
```rozwiazanie
SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ
```

### 24. Dwa skarby, dwie kałuże
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
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, SKOCZ, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×6
```

---

# Plansze 7 × 7, poziom 1, zestaw B (3/4)

### 25. Most
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
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ
```

### 26. Znajdź błąd: brakuje karty
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
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, SKOCZ, IDŹ
```
Zamiast IDŹ ×3 na końcu robot musi przeskoczyć kałużę: SKOCZ, IDŹ.

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
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×5
```

### 28. Dziura w murze
W murze z lawy jest tylko jedno wolne pole.
```plansza
. * . . . . .
. . . . . . .
. . . . . . .
L L L L L . L
. . . . . . .
. . . . . . .
. ^ . . . . .
```
```rozwiazanie
IDŹ, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×5, SKRĘĆ W LEWO, IDŹ ×4
```

---

# Plansze 7 × 7, poziom 1, zestaw B (4/4)

### 29. Spacer dookoła
Zbierz skarby we wszystkich rogach i wróć na START.
```plansza
* . . . . . *
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
> . . . . . *
```
```rozwiazanie
IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×6
```
Trzy razy powtarza się to samo: IDŹ ×6 i SKRĘĆ W LEWO. Na poziomie 2 da się to skrócić kartą POWTÓRZ.

### 30. Gdzie skończy robot?
Przeczytaj program i połóż skarb tam, gdzie robot się zatrzyma.
```plansza
. . . . . . .
. . . . . . .
. K . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . ^ . . .
```
```program
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, SKOCZ, SKRĘĆ W PRAWO, IDŹ
```
**Rozwiązanie:** W drugim rzędzie od góry, na trzecim polu od lewej. Robot patrzy wtedy w prawo.

### 31. Daleki skarb i powrót
Weź skarb i wróć na START. Robot czyta karty na głos.
```plansza
. . . . . . *
. . . . . . .
. . L L L . .
. . . . . . .
. . . . . . .
. . . . . . .
^ . . . . . .
```
```rozwiazanie
IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×6
```

### 32. Dwie kałuże w murach
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
```rozwiazanie
IDŹ, SKOCZ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, SKOCZ, IDŹ
```
