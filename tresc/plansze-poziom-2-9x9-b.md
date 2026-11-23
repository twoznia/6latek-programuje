# Plansze 9 × 9, poziom 2, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Wszystkie gry są z pętlą POWTÓRZ.

### 17. Kałuża co drugie pole
W pętli jest tylko jedna karta. Ile razy skoczyć?
```plansza
. . . . * . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ
KONIEC
```

### 18. Dwie pętle
Jedna pętla w górę, druga w prawo. Zbierz trzy skarby.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2
KONIEC
SKRĘĆ W PRAWO
POWTÓRZ ×4
  IDŹ ×2
KONIEC
```
Można też krócej: IDŹ ×6, IDŹ ×2 zamiast pętli. Obie drogi są dobre.

### 19. Wielki kwadrat w lewo
Zbierz skarby i wróć na START. Robot skręca w lewo.
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . . L . . . .
. . . L L L . . .
. . . . L . . . .
. . . . . . . . .
. * . . . . . ^ .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×6, SKRĘĆ W LEWO
KONIEC
```

### 20. Gdzie stanie robot? 6 razy w kółko
Robot chodzi w kółko. Ile razy wróci na START?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . ^ . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```program
POWTÓRZ ×6
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
**Rozwiązanie:** Po 4 powtórzeniach robot jest znowu na START. Potem idzie jeszcze 2 razy i stanie w 5. rzędzie od góry, na 5. polu od lewej. Robot patrzy w dół.

---

# Plansze 9 × 9, poziom 2, zestaw B (2/4)

### 21. Duże schody w dół
Robot patrzy w prawo i schodzi po dużych schodach.
```plansza
> . . . . . . . .
. L . . . . . . .
. . . . . . . . .
. . . L . . . . .
. . . . * . . . .
. . . . . L . . .
. . . . . . . . .
. . . . . . . L .
. . . . . . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```

### 22. Znajdź błąd: kałuża na schodach
Robot miał wejść po schodach, ale wszedł do kałuży. Którą kartę wymienić?
```plansza
. . . . * . . . .
. . . K . . . . .
. . . . . . . . .
. . K . . . . . .
. . . . . . . . .
. K . . . . . . .
. . . . . . . . .
K . . . . . . . .
^ . . . . . . . .
```
```program
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
Zamiast IDŹ ×2 ma być SKOCZ. Robot też przesunie się o 2 pola, ale nad kałużą.

### 23. Wielki spacer z kałużami
Na każdym boku planszy jest kałuża. Zbierz skarby i wróć na START.
```plansza
* . . . K . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K . . . L . . . K
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . K . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×3, SKOCZ, IDŹ ×3, SKRĘĆ W PRAWO
KONIEC
```

### 24. Gwiazda
Robot stoi w środku. Zbierz skarby na końcach i wróć na START.
```plansza
. . . . * . . . .
. . . . . . . . .
. . L . . . L . .
. . . . . . . . .
* . . . ^ . . . *
. . . . . . . . .
. . L . . . L . .
. . . . . . . . .
. . . . * . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```
Po powrocie do środka robot patrzy w dół, więc SKRĘĆ W PRAWO obraca go w lewo.

---

# Plansze 9 × 9, poziom 2, zestaw B (3/4)

### 25. Korona
Robot rysuje ząbki korony: w górę, w bok, w dół. Na każdym ząbku jest skarb.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. * . * . * . * .
. . . . . . . . .
> . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×4
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ
  SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ
KONIEC
```

### 26. Skoki w pętli w pętli
Mała pętla skacze, a duża ją powtarza. Dojdź do skarbu.
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

### 27. Prostokąt dookoła lawy
Zbierz skarby i wróć na START. Prostokąt ma długie i krótkie boki.
```plansza
. . . . . . . . .
. * . . . * . . .
. . . . . . . . .
. . . L L . . . .
. . . L L . . . .
. . . L L . . . .
. . . . . . . . .
. ^ . . . * . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```

### 28. Gdzie stanie robot? Schody w lewo
Robot liczy powtórzenia. Połóż skarb tam, gdzie robot stanie.
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

---

# Plansze 9 × 9, poziom 2, zestaw B (4/4)

### 29. Znajdź błąd: BUM o ścianę
Robot doszedł do skarbu, ale szedł dalej i uderzył w ścianę. Którą liczbę zmienić?
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
```program
POWTÓRZ ×5
  IDŹ ×2
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2
KONIEC
```
Do skarbu jest 8 kroków, czyli 4 razy po 2. Piąte powtórzenie wyprowadza robota poza planszę.

### 30. Wieża z kwadratów
Mała pętla rysuje kwadrat, a duża stawia dwa kwadraty jeden na drugim.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . * . . . . .
. . . . . . . . .
. L . . . . . . .
. . . * . . . . .
. . . . . . . . .
. L . . . . . . .
^ . . * . . . . .
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×4
    IDŹ ×3, SKRĘĆ W PRAWO
  KONIEC
  IDŹ ×3
KONIEC
```

### 31. Kałuże na zjeżdżalni
Robot patrzy w dół. Skacz i schodź w prawo.
```plansza
v . . . . . . . .
K . . . . . . . .
. . . . . . . . .
. K . . . . . . .
. . . . . . . . .
. . K . . . . . .
. . . . . . . . .
. . . K . . . . .
. . . . * . . . .
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```
Gdy robot patrzy w dół, SKRĘĆ W LEWO obraca go w prawą stronę planszy.

### 32. Wielka górka
Jedna pętla wchodzi pod górę, a druga schodzi w dół. Zbierz skarby.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . * . . . .
. . . L . L . . .
. . . . . . . . .
. L . . . . . L .
> . . . . . . . *
```
```rozwiazanie
POWTÓRZ ×2
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
KONIEC
POWTÓRZ ×2
  SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2
KONIEC
```
