# Plansze 9 × 9, poziom 3, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 33. Do ściany po trzy skarby
Robot idzie, aż przed nim będzie ściana. Nie liczymy kroków!
```plansza
. . . . * . . . .
. . . . . . . . .
. . . L . L . . .
. . . . * . . . .
. . . L . L . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
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

### 34. Gdzie jest skarb? Długi rząd
Dorosły chowa skarb na jednym polu ?. Robot szuka, aż go znajdzie.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . . ? . ? . ? .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```

### 35. Dwie pętle do dwóch ścian
Pierwsza pętla idzie do górnej ściany, a druga do lewej.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ^
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```

### 36. Gdzie stanie robot? Kałuża w połowie
Robot 3 razy pyta o kałużę. W rzędzie NIE robi aż 3 kroki.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```program
POWTÓRZ ×3
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×3
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot stanie w 1. rzędzie od góry, na 5. polu od lewej. Robot patrzy w górę. 3 kroki, skok i jeszcze 3 kroki.

---

# Plansze 9 × 9, poziom 3, zestaw C (2/4)

### 37. Kałuże co drugie pole
Dorosły rzuca monetą dla każdego pola ?: orzeł to kałuża, reszka to nic.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . ? . ? . ? . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
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

### 38. Lawowy labirynt w prawo
Przy lawie robot skręca w prawo. Gdzie znajdzie skarb?
```plansza
. . . . L . . . .
L . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . L . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . L . . .
^ . . . . . . . .
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

### 39. Gdzie stanie robot? META przy lawie
Czy robot zrobi ostatnie karty?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. L . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: META
  KONIEC
  IDŹ ×2
KONIEC
SKRĘĆ W PRAWO, IDŹ ×6
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 2. polu od lewej. Robot patrzy w górę. META kończy cały program, więc robot nie skręci.

### 40. Znajdź błąd: TAK i NIE
Robot skoczył, a przed nim nie było kałuży. Co zamienić?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . K . . K . . *
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: IDŹ
    NIE: SKOCZ
  KONIEC
KONIEC
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
Karty po TAK i po NIE są zamienione. Gdy jest kałuża, robot ma skoczyć.

---

# Plansze 9 × 9, poziom 3, zestaw C (3/4)

### 41. Gdzie stanie robot? STOP przy lawie
Pętla kończy się przy lawie. Potem robot robi jeszcze 2 karty.
```plansza
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . ^ . .
```
```program
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ ×2
KONIEC
SKRĘĆ W LEWO, IDŹ ×3
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 4. polu od lewej. Robot patrzy w lewo.

### 42. Znajdź błąd: zły skręt
Przy lawie robot skręcił w złą stronę i wyszedł poza planszę. Co zmienić?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . L
. L . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . ^
```
```program
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
Ten labirynt skręca w lewo. Zamiast SKRĘĆ W PRAWO ma być SKRĘĆ W LEWO.

### 43. Dookoła do skarbu
Przy ścianie robot skręca w lewo. Gdzie znajdzie skarb?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . L L L . . .
. . . L . L . . .
* . . L L L . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ^
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

### 44. Do kałuży i za róg
Pętla ∞ kończy się przed kałużą. Potem robot skacze i idzie do skarbu.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . * . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . . . . K . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI KAŁUŻA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKOCZ, SKRĘĆ W LEWO, IDŹ ×5
```

---

# Plansze 9 × 9, poziom 3, zestaw C (4/4)

### 45. STOP czy META? Długa droga
Programy różnią się jedną kartą. Który robot zbierze skarb?
```plansza
. . . . . . . . .
L . . . . . . . .
. . . . . . . . *
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program A
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: META
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×6, IDŹ ×2
```
```program B
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×6, IDŹ ×2
```
**Rozwiązanie:** Program B. STOP kończy tylko pętlę i robot idzie w prawo do skarbu. META kończy cały program, więc robot A zostaje przy lawie.

### 46. Skarb czy lawa w środku?
Dorosły kładzie na polu ? skarb albo lawę. Robot idzie do ściany.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . L . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . . . . . .
. . L . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
Lawę robot obchodzi z prawej strony i wraca na tę samą linię, 2 pola dalej.

### 47. Kostka decyduje
Dorosły rzuca kostką: 1 lub 2 to kałuża na polu ?, 3 lub 4 to skarb, 5 lub 6 to nic.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . L . L . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . L . L . . .
. . . . . . . . .
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
Robot idzie do ściany i skacze tylko wtedy, gdy przed nim jest kałuża.

### 48. Twoja misja z niespodzianką
Dziecko kładzie pola ? i w tajemnicy wybiera, co na nich będzie. Dorosły układa program z JEŚLI. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry program działa przy każdym wyborze dziecka.
