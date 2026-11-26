# Plansze 5 × 5, poziom 3, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 33. Do ściany po skarby
Robot idzie, aż przed nim będzie ściana. Nie liczymy kroków!
```plansza
. . * . .
. . . . .
. . * . .
. . . . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```

### 34. Gdzie stanie robot? Do ściany i z powrotem
Pętla kończy się przy ścianie. Potem robot robi jeszcze 2 karty.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. > . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
OBRÓĆ SIĘ, IDŹ ×2
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 3. polu od lewej. Robot patrzy w lewo. STOP kończy tylko pętlę, więc robot robi też karty za nią.

### 35. Kałuża w nieznanym miejscu
Dorosły kładzie kałużę na jednym polu ?. Robot idzie do ściany.
```plansza
. . * . .
. . ? . .
. . ? . .
. . ? . .
. . ^ . .
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
Przed kałużą robot skacze, a gdzie indziej idzie. Za każdym razem dojdzie do skarbu.

### 36. Gdzie stanie robot? Lawa na drodze
Robot 4 razy pyta o lawę.
```plansza
. . . . .
L . . . .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×4
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 2. polu od lewej. Robot patrzy w prawo. Dwa kroki, skręt przy lawie i jeszcze jeden krok.

---

# Plansze 5 × 5, poziom 3, zestaw C (2/4)

### 37. Do lawy i w prawo
Robot idzie do lawy, a potem skręca do skarbu.
```plansza
L . . . .
. . . * .
. . . . .
. . . . .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×3
```
STOP kończy pętlę, a robot robi dalej karty za nią.

### 38. Gdzie stanie robot? Dwa pytania
Robot pyta dwa razy, bez pętli.
```plansza
. . . . .
L . . . .
. . . . .
. . K . .
. . ^ . .
```
```program
JEŚLI KAŁUŻA?
  TAK: SKOCZ
  NIE: IDŹ
KONIEC
JEŚLI LAWA?
  TAK: SKRĘĆ W LEWO
  NIE: IDŹ ×2
KONIEC
```
**Rozwiązanie:** Robot stanie w 1. rzędzie od góry, na 3. polu od lewej. Robot patrzy w górę. Najpierw skok nad kałużą. Przed robotem nie ma lawy, więc robi 2 kroki.

### 39. Skarb czy kałuża? Dwa razy
Dorosły rzuca monetą dla każdego pola ?: orzeł to kałuża, reszka to skarb.
```plansza
. . . . .
. . . . .
> ? . ? *
. . . . .
. . . . .
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
Kałużę robot przeskakuje, a na skarb wchodzi. Za każdym razem kończy przy ścianie.

### 40. Znajdź błąd: pętla bez końca
Robot zebrał skarb, ale poszedł dalej i wyszedł poza planszę. Czego brakuje?
```plansza
. . . . .
. . * . .
. . . . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×∞
  IDŹ
KONIEC
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```
Brakuje pytania JEŚLI SKARB? z META. Wtedy robot kończy na skarbie.

---

# Plansze 5 × 5, poziom 3, zestaw C (3/4)

### 41. Labirynt w lewo
Przy lawie robot skręca w lewo. Gdzie znajdzie skarb?
```plansza
. . . . L
L . . . .
. . . . .
. * . . .
. . . . ^
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W LEWO
    NIE: IDŹ
  KONIEC
KONIEC
```

### 42. STOP czy META? Dwa programy
Programy różnią się jedną kartą. Który robot zbierze skarb?
```plansza
L . . . .
. . * . .
. . . . .
. . . . .
^ . . . .
```
```program A
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
```program B
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: META
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
**Rozwiązanie:** Program A. STOP kończy tylko pętlę i robot idzie dalej do skarbu. META kończy cały program, więc robot B zostaje przy lawie.

### 43. Znajdź błąd: META zamiast STOP
Robot nie doszedł do skarbu. Którą kartę wymienić?
```plansza
. . . . L
. * . . .
. . . . .
. . . . .
. . . . ^
```
```program
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: META
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO, IDŹ ×3
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO, IDŹ ×3
```

### 44. Za rogiem jest skarb
Dorosły chowa skarb na jednym polu ?. Przy ścianie robot skręca w lewo.
```plansza
. . . . ?
. . . . ?
. . . . ?
. . L . .
> . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W LEWO
    NIE: IDŹ
  KONIEC
KONIEC
```

---

# Plansze 5 × 5, poziom 3, zestaw C (4/4)

### 45. Lawa czy kałuża?
Dorosły kładzie na polu ? lawę albo kałużę. Jeden program na oba razy.
```plansza
. . * . .
. . . . .
. . ? . .
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ
JEŚLI KAŁUŻA?
  TAK: SKOCZ, IDŹ
  NIE: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
KONIEC
```
Kałużę robot przeskakuje. Lawę obchodzi z prawej strony.

### 46. Lawa albo nic
Dorosły rzuca monetą: orzeł to lawa na polu ?, reszka to nic.
```plansza
. . * . .
. . . . .
. . ? . .
. . . . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
Lawę robot obchodzi i wraca na tę samą linię, 2 pola dalej.

### 47. Po brzegu przez kałuże
Przy ścianie robot skręca w prawo, a nad kałużą skacze.
```plansza
. . K . *
. . . . .
K . . . .
. . . L .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```

### 48. Twoja misja z pytaniem
Dziecko kładzie lawę i kałuże, a dorosły układa program z pętlą ∞ i JEŚLI. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry program działa też po przestawieniu lawy i kałuż.
