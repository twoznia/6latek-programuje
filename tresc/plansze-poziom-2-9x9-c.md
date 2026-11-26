# Plansze 9 × 9, poziom 2, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Wszystkie gry są z pętlą POWTÓRZ.

### 33. Skarby co dwa pola
W pętli jest jedna karta. Zbierz cztery skarby.
```plansza
. . * . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . ^ . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2
KONIEC
```

### 34. Skok i dwa kroki
Robot patrzy w prawo. W pętli jest skok i dwa kroki.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> K . . * K . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  SKOCZ, IDŹ ×2
KONIEC
```

### 35. Wielki kwadrat
Zbierz skarby w rogach i wróć na START.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
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

### 36. Wielki prostokąt
Zbierz skarby i wróć na START. Prostokąt jest wysoki i wąski.
```plansza
* . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . * . . . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

---

# Plansze 9 × 9, poziom 2, zestaw C (2/4)

### 37. Zygzak w dół
Robot patrzy w prawo i schodzi po dużych schodach.
```plansza
> . . . L . . . .
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . . . * . . . L
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 38. Gdzie stanie robot? Pięć razy za róg
Robot chodzi w kółko. Ile razy minie START?
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
POWTÓRZ ×5
  IDŹ ×3, SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 6. rzędzie od góry, na 1. polu od lewej. Robot patrzy w prawo. Po 4 powtórzeniach robot jest na START, a potem idzie jeszcze raz.

### 39. Duże schody w lewo
Robot wchodzi po schodach w lewo. Pod schodami jest lawa.
```plansza
* . . . . . . . .
. L . . . . . . .
. . . . . . . . .
. . . L . . . . .
. . . . * . . . .
. . . . . L . . .
. . . . . . . . .
. . . . . . . L .
. . . . . . . . ^
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```

### 40. Znajdź błąd: KONIEC za wcześnie
Robot miał chodzić po kwadracie, a wyszedł poza planszę. Którą kartę przełożyć?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . . . * . . . .
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
^ . . . * . . . .
```
```program
POWTÓRZ ×4
  IDŹ ×4
KONIEC
SKRĘĆ W PRAWO
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```
SKRĘĆ W PRAWO musi być w pętli, przed kartą KONIEC. Wtedy robot skręca na każdym rogu.

---

# Plansze 9 × 9, poziom 2, zestaw C (3/4)

### 41. Skoki za rogiem
Mała pętla skacze, a duża ją powtarza i skręca.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. K . K * . . . .
K . . . . . . . .
. . . . . . . . .
K . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×2
    SKOCZ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 42. Gdzie stanie robot? Pętla w pętli
Mała pętla robi kroki, a duża skręca. Robot liczy na głos.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ^
```
```program
POWTÓRZ ×2
  POWTÓRZ ×3
    IDŹ
  KONIEC
  SKRĘĆ W LEWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 6. rzędzie od góry, na 6. polu od lewej. Robot patrzy w dół.

### 43. Schody w dół w lewo
Robot patrzy w dół. Jego prawa ręka jest po lewej stronie planszy.
```plansza
. . . . . . . . v
. . . . . . . L .
. . . . . . . . .
. . . . . L . . .
. . . . * . . . .
. . . L . . . . .
. . . . . . . . .
. L . . . . . . .
* . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 44. Znajdź błąd: krok przed skokiem
Robot wszedł do kałuży. Którą kartę wymienić?
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```program
POWTÓRZ ×2
  IDŹ ×2, SKOCZ
KONIEC
IDŹ ×2
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ, SKOCZ
KONIEC
IDŹ ×2
```
Przed kałużą jest tylko 1 pole, więc w pętli ma być IDŹ, a nie IDŹ ×2.

---

# Plansze 9 × 9, poziom 2, zestaw C (4/4)

### 45. Wieża z kwadratów
Mała pętla robi kwadrat, a duża stawia drugi kwadrat nad pierwszym.
```plansza
* . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. L . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. L . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×4
KONIEC
```

### 46. Gdzie stanie robot? Po skosie
W pętli są 2 kroki w górę i 1 w lewo. Gdzie stanie robot?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ^
```
```program
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Robot stanie w 1. rzędzie od góry, na 5. polu od lewej. Robot patrzy w górę.

### 47. Wąż przez labirynt
Wąż idzie w górę i w dół między klockami. Zbierz cztery skarby.
```plansza
. . * # . . * # .
. # . # . # . # .
. # . # . # . # .
. # . # . # . # .
. # . # . # . # .
. # . # . # . # .
. # . # . # . # .
. # . # . # . # .
^ # . . * # . . *
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO
  IDŹ ×6, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 48. Twoja misja z pętlą
Dziecko kładzie skarby na dużej planszy, a dorosły układa program z POWTÓRZ. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Na dużej planszy pętla oszczędza dużo kart.
