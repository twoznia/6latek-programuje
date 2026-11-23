# Plansze 9 × 9, poziom 3, zestaw A (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 1. Długi korytarz
Robot idzie do ściany i zbiera skarby po drodze. Ile ich jest?
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . L . . .
. . . . * . . . .
. . . L . . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . L . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```

### 2. Gdzie stanie robot? Lawa i ściana
Robot skręca przy lawie i staje przy ścianie. Gdzie?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
L . . . . . . . .
. . . . . L . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot skręci 2 razy i stanie w 9. rzędzie od góry, na 5. polu od lewej. Robot patrzy w dół.

### 3. Gdzie jest skarb? Długi rząd
Dorosły chowa skarb na jednym z pól ?. Robot ma stanąć na skarbie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> ? ? ? ? ? ? ? ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```

### 4. Cztery monety
Na każdym polu ? może być kałuża. Jeden program na każdy rzut monetą.
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
```rozwiazanie
POWTÓRZ ×4
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```
Ten program działa w 16 różnych ułożeniach kałuż.

---

# Plansze 9 × 9, poziom 3, zestaw A (2/4)

### 5. Do rogu
Dwie pętle do ściany. Zbierz skarby w rogach.
```plansza
* . . . . . . . *
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```

### 6. Gdzie stanie robot? Kałuże
Robot 4 razy pyta o kałużę. Ile razy skoczy?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
POWTÓRZ ×4
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot skoczy 2 razy i stanie w 3. rzędzie od góry, na 1. polu od lewej. Robot patrzy w górę.

### 7. Rzeka niespodzianek
Na polach ? mogą być kałuże, ale nigdy dwie obok siebie. Robot idzie do ściany.
```plansza
. . . . * . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```

### 8. STOP czy META? Długa droga
Gdzie stanie robot w programie A, a gdzie w B?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . ^ . . . . . .
```
```program A
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×4
```
```program B
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×4
```
**Rozwiązanie:** W A robot stanie w 4. rzędzie od góry, na 7. polu od lewej. Robot patrzy w prawo. W B stanie na skarbie, w 4. rzędzie od góry, na 3. polu od lewej. Robot patrzy w górę.

---

# Plansze 9 × 9, poziom 3, zestaw A (3/4)

### 9. Cztery ściany
Pętla do ściany jest w środku pętli ×4. Zbierz skarby.
```plansza
. . . . . . . . *
. . . . . . . . .
. . L . . . L . .
. . . . . . . . .
. . . . ^ . . . .
. . . . . . . . .
. . L . . . L . .
. . . . . . . . .
* . . . . . . . *
```
```rozwiazanie
POWTÓRZ ×4
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: STOP
    KONIEC
    IDŹ
  KONIEC
  SKRĘĆ W PRAWO
KONIEC
```

### 10. Labirynt z lawą
Pętla ∞: przy lawie robot skręca w prawo, przy skarbie kończy.
```plansza
. . . . L . . . .
L . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . L . . .
^ . . . . . . . L
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```

### 11. Znajdź błąd: pętla bez końca
Robot obchodzi planszę w kółko i nie kończy. Czego brakuje?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . * . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Brakuje pytania o skarb z kartą META.

### 12. Znajdź błąd: STOP zamiast META
Robot zebrał skarb i poszedł dalej: BUM! Którą kartę zamienić?
```plansza
. L . . . . . . .
. . . . . . * . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, STOP
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
IDŹ ×3
```
**Rozwiązanie:** STOP kończy tylko pętlę i robot robi IDŹ ×3 spod pętli. META kończy cały program.

---

# Plansze 9 × 9, poziom 3, zestaw A (4/4)

### 13. Skarb w rogu
Dorosły chowa skarb w jednym z rogów ?. Robot idzie wzdłuż ścian.
```plansza
? . . . . . . . ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . ?
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```

### 14. Lawa nie obok lawy
Na polach ? może być lawa, ale nigdy dwie obok siebie. Robot obchodzi każdą.
```plansza
. . . . * . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ? . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    TAK: IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
Ten sam program działa dla każdego ułożenia lawy.

### 15. Wielki labirynt
Trzy pytania w jednej pętli: skarb, lawa i kałuża.
```plansza
. . . . . . . . .
L . . . . . . . .
. . K . . . L . .
K . . . . . . . .
. . . . . K . . .
. . L . . . . . .
K . . . . * . . .
. . . . . . . . .
^ . . . . . . . L
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```

### 16. Twoja misja z pytaniem
Dziecko układa labirynt z lawy, a dorosły pisze program z pętlą ∞. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry program działa też po przestawieniu lawy.
