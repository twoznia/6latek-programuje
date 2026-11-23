# Plansze 5 × 5, poziom 2, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Wszystkie gry są z pętlą POWTÓRZ. Gry 1–11 poziomu 2 są w pliku z poziomami 2 i 3.

### 17. Dwa razy po dwa
W pętli jest IDŹ ×2. Ile razy ją powtórzyć?
```plansza
. . * . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2
KONIEC
```
2 razy po 2 kroki to 4 kroki.

### 18. Skok, skok
Robot patrzy w prawo. W pętli jest tylko jedna karta.
```plansza
. . . . .
. . . . .
> K . K *
. . . . .
. . . . .
```
```rozwiazanie
POWTÓRZ ×2
  SKOCZ
KONIEC
```

### 19. Kwadrat w lewo
Zbierz skarby i wróć na START. Tym razem robot skręca w lewo.
```plansza
. . . . .
. * . * .
. . L . .
. * . ^ .
. . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 20. Ile razy? Dookoła
Zbierz trzy skarby. Ile razy trzeba powtórzyć pętlę?
```plansza
* . . . *
. . . . .
. . L . .
. . . . .
^ . . . *
```
```rozwiazanie
POWTÓRZ ×3
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```
Wystarczą 3 razy, bo robot nie musi wracać na START.

---

# Plansze 5 × 5, poziom 2, zestaw B (2/4)

### 21. Prostokąt
Zbierz skarby i wróć na START. Prostokąt ma dwa długie i dwa krótkie boki.
```plansza
* . * . .
. . . . .
. L . . .
. . . . .
^ . * . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

### 22. Gdzie stanie robot? Zygzak
Robot liczy powtórzenia. Połóż skarb tam, gdzie robot stanie.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×2
  IDŹ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 5. polu od lewej. Robot patrzy w górę.

### 23. Zjeżdżalnia
Robot patrzy w lewo i schodzi po schodkach w dół.
```plansza
. . . . <
. L . . .
. . * L .
. . . . L
* . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
Gdy robot patrzy w lewo, SKRĘĆ W LEWO obraca go w dół.

### 24. Schodki i prosto
Po pętli robot robi jeszcze jedną kartę. Zbierz oba skarby.
```plansza
* . . . .
. . . . .
. . L . .
. * . . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
IDŹ ×2
```

---

# Plansze 5 × 5, poziom 2, zestaw B (3/4)

### 25. Znajdź błąd: karta za pętlą
Robot miał wejść po schodkach do skarbów, a zszedł na dół. Którą kartę przełożyć?
```plansza
. . . . *
. . . . .
. . * . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×2
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
KONIEC
SKRĘĆ W LEWO
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```
SKRĘĆ W LEWO musi być w środku pętli, przed kartą KONIEC. Wtedy robot skręca w każdym powtórzeniu.

### 26. Trzy skoki dookoła
W pętli jest skok i skręt. Ile razy ją powtórzyć?
```plansza
. . . . .
. . . . .
. K . . .
K . K . .
^ . * . .
```
```rozwiazanie
POWTÓRZ ×3
  SKOCZ, SKRĘĆ W PRAWO
KONIEC
```

### 27. Gdzie stanie robot? Obrót w pętli
Robot idzie i się obraca. Gdzie stanie po 3 powtórzeniach?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×3
  IDŹ ×2, OBRÓĆ SIĘ
KONIEC
```
**Rozwiązanie:** Robot chodzi tam i z powrotem. Stanie w 3. rzędzie od góry, na 3. polu od lewej. Robot patrzy w dół.


### 28. Mała gwiazda
Robot stoi w środku. Zbierz skarby na końcach i wróć na START.
```plansza
. . * . .
. L . L .
* . ^ . *
. L . L .
. . * . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
Po powrocie do środka robot patrzy w dół, więc SKRĘĆ W PRAWO obraca go w lewo.
---

# Plansze 5 × 5, poziom 2, zestaw B (4/4)

### 29. Znajdź błąd: zamienione karty w pętli
Robot miał obejść kwadrat, a wypadł z planszy: BUM! Co zamienić?
```plansza
. . . . .
. . . . .
* . * . .
. L . . .
^ . * . .
```
```program
POWTÓRZ ×4
  SKRĘĆ W PRAWO, IDŹ ×2
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
Robot najpierw skręca, a powinien najpierw iść. Karty w pętli są zamienione.

### 30. Pierwsza pętla w pętli
Mała pętla robi kroki, a duża dodaje skręt. Dojdź do skarbu.
```plansza
. . . . .
. . . . .
. . * . .
. . . . .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×2
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 31. Mały grzebień
Robot zbiera skarby na ząbkach grzebienia. Co się powtarza?
```plansza
. . . . .
. . . . .
* . * . .
. . . . .
^ . . . *
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 32. Twoja misja z pętlą
Dziecko kładzie skarby i lawę, a dorosły układa program z POWTÓRZ. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Najłatwiej ułożyć skarby w kwadrat albo w schodki.
