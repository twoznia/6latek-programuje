# Plansze 5 × 5, poziom 2, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Wszystkie gry są z pętlą POWTÓRZ.

### 33. Cztery skarby w rzędzie
W pętli jest tylko jedna karta. Ile razy ją powtórzyć?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
> * * * *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ
KONIEC
```

### 34. Najpierw obrót
Robot patrzy w dół. Jedna karta przed pętlą, a potem pętla.
```plansza
. . * . .
. . . . .
. . . . .
. . . . .
. . v . .
```
```rozwiazanie
OBRÓĆ SIĘ
POWTÓRZ ×2
  IDŹ ×2
KONIEC
```

### 35. Wielki kwadrat w lewo
Zbierz skarby w rogach i wróć na START. Robot skręca w lewo.
```plansza
* . . . *
. . . . .
. . L . .
. . . . .
* . . . ^
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W LEWO
KONIEC
```

### 36. Zygzak w dół
Robot patrzy w prawo i schodzi po schodkach.
```plansza
> . L . .
. . . L .
. . * . L
. . . . .
. . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

---

# Plansze 5 × 5, poziom 2, zestaw C (2/4)

### 37. Wąski prostokąt
Zbierz skarby i wróć na START. Prostokąt ma tylko 2 pola szerokości.
```plansza
. . . * *
. . . . .
. L L . .
. . . . .
. . . * ^
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×4, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### 38. Schodki nad lawą
Robot wchodzi po schodkach. Pod schodkami jest lawa.
```plansza
. . . . *
. . . . L
. . . L .
. * L . .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### 39. Gdzie stanie robot? Schodki w lewo
Robot liczy powtórzenia. Połóż skarb tam, gdzie robot stanie.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . ^
```
```program
POWTÓRZ ×3
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 2. rzędzie od góry, na 2. polu od lewej. Robot patrzy w górę.

### 40. Znajdź błąd: za duża liczba
Robot zebrał skarb i wyszedł poza planszę. Którą liczbę zmienić?
```plansza
. . * . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×4
  IDŹ ×2
KONIEC
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2
KONIEC
```
2 razy po 2 kroki to 4 kroki. 4 razy po 2 to już 8 kroków.

---

# Plansze 5 × 5, poziom 2, zestaw C (3/4)

### 41. Skok i schodek
W pętli jest skok i schodek. Ile razy ją powtórzyć?
```plansza
. . * . .
. K . . .
. . . . .
K . . . .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×2
  SKOCZ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```

### 42. Gdzie stanie robot? Pętla z dwoma skrętami
Robot liczy na głos. Czy wróci na START?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×2
  IDŹ ×3, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 1. polu od lewej. Robot patrzy w górę. Tak, to jest START.

### 43. Duże schodki w lewo
Każdy schodek ma 2 pola. Zbierz oba skarby.
```plansza
* . . . .
. L . . .
. . * . .
. . L . .
. . . . ^
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

### 44. Znajdź błąd: zły skręt w pętli
Robot miał obejść lawę dookoła, a wyszedł poza planszę. Którą kartę wymienić?
```plansza
. . . . .
. * . * .
. . L . .
. ^ . * .
. . . . .
```
```program
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
Skarby są po prawej, więc w pętli ma być SKRĘĆ W PRAWO.

---

# Plansze 5 × 5, poziom 2, zestaw C (4/4)

### 45. Kałuże na każdym boku
Na każdym boku jest kałuża. Zbierz skarby i wróć na START.
```plansza
* . K . *
. . . . .
K . L . K
. . . . .
^ . K . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKOCZ, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

### 46. Gdzie stanie robot? Skoki tam i z powrotem
Robot skacze i się obraca. Gdzie stanie po 3 powtórzeniach?
```plansza
. . . . .
. . . . .
. . . . .
. . K . .
. . ^ . .
```
```program
POWTÓRZ ×3
  SKOCZ, OBRÓĆ SIĘ
KONIEC
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 3. polu od lewej. Robot patrzy w dół.

### 47. Tam i z powrotem dwa razy
Zbierz skarb i wróć na START. Masz tylko 3 karty.
```plansza
. * . . .
. . . . .
. . . L .
. . . . .
. ^ . . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×4, OBRÓĆ SIĘ
KONIEC
```

### 48. Twoja misja z pętlą
Dziecko kładzie skarby w kwadrat albo schodki. Dorosły układa program z POWTÓRZ. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry program ma pętlę, a nie wiele takich samych kart.
