# Plansze 5 × 5, poziom 3 (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 1. Do ściany
Robot idzie, aż dojdzie do brzegu planszy. Nie liczymy kroków!
```plansza
. . * . .
. . . . L
L . . . .
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
OBRÓĆ SIĘ
```
STOP kończy pętlę, a OBRÓĆ SIĘ to taniec radości na końcu.

### 2. Robot pyta o kałużę
Dorosły rzuca monetą: orzeł to kałuża na polu ?, reszka to puste pole. Jeden program na oba razy.
```plansza
. . * . .
. . ? . .
. . ^ . .
. . . . .
. . . . .
```
```rozwiazanie
JEŚLI KAŁUŻA?
  TAK: SKOCZ
  NIE: IDŹ ×2
KONIEC
```

### 3. Gdzie stanie robot? Pytanie
Robot pyta o pole przed sobą. Gdzie stanie?
```plansza
. . . . .
. . . . .
. . . . .
. . L . .
. . ^ . .
```
```program
JEŚLI LAWA?
  TAK: SKRĘĆ W PRAWO, IDŹ ×2
  NIE: IDŹ ×2
KONIEC
```
**Rozwiązanie:** Przed robotem jest lawa, więc działa rząd TAK. Robot stanie w 5. rzędzie od góry, na 5. polu od lewej. Robot patrzy w prawo.

### 4. Gdzie jest skarb?
Dorosły chowa skarb na jednym z pól ?. Program ma zatrzymać robota na skarbie.
```plansza
. . ? . .
. . ? . .
. . ? . .
. . ? . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```
META kończy cały program, gdy robot stanie na skarbie.

---

# Plansze 5 × 5, poziom 3 (2/4)

### 5. Dwie monety
Dorosły rzuca monetą dla każdego pola ?. Kałuża albo nic. Pętla z pytaniem w środku.
```plansza
. . * . .
. . ? . .
. . . . .
. . ? . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×2
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
```
Skok i dwa kroki prowadzą tak samo daleko: 2 pola.

### 6. Gdzie stanie robot? STOP
STOP kończy pętlę, ale nie program. Co robot zrobi potem?
```plansza
. . . . .
. . * . .
. . . . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
IDŹ, SKRĘĆ W PRAWO, IDŹ
```
**Rozwiązanie:** Robot stanie w 2. rzędzie od góry, na 4. polu od lewej. Robot patrzy w prawo. Po STOP robot robi karty spod pętli.

### 7. Gdzie stanie robot? Pętla z pytaniem
Robot 6 razy pyta o lawę. Ile razy skręci?
```plansza
. . L . .
L . . . .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×6
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot skręci raz i stanie w 3. rzędzie od góry, na 4. polu od lewej. Robot patrzy w prawo.

### 8. Tam i z powrotem
STOP kończy tylko pętlę, w której jest. Zbierz oba skarby.
```plansza
L . . . .
. . . . .
* . > . *
. . . . .
. . . . L
```
```rozwiazanie
POWTÓRZ ×2
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: STOP
    KONIEC
    IDŹ
  KONIEC
  OBRÓĆ SIĘ
KONIEC
```
Wewnętrzna pętla idzie do ściany, a zewnętrzna robi to 2 razy.

---

# Plansze 5 × 5, poziom 3 (3/4)

### 9. Znajdź błąd: TAK i NIE
Robot wpadł do kałuży. Coś jest zamienione. Co?
```plansza
. . * . .
. . . . .
. . K . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×3
  JEŚLI KAŁUŻA?
    TAK: IDŹ
    NIE: SKOCZ
  KONIEC
KONIEC
```
**Rozwiązanie:** Karty w rzędach TAK i NIE były zamienione.

### 10. Do rogu
Dwie pętle do ściany, jedna po drugiej. Zbierz skarby.
```plansza
* . . . *
. . . . .
. . L . .
. . . . .
^ . . . .
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

### 11. Labirynt w lewo
Napisz program z pętlą ∞: przy lawie robot skręca w lewo.
```plansza
L . . . .
. . . . L
. * . . .
. . L . .
L . . . ^
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

### 12. Znajdź błąd: tuż przed skarbem
Robot zatrzymał się tuż przed skarbem i go nie zebrał. Czego brakuje?
```plansza
L . . . .
. . . * .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** W rzędzie TAK brakuje IDŹ przed META. Robot widzi skarb przed sobą, więc musi jeszcze zrobić krok.

---

# Plansze 5 × 5, poziom 3 (4/4)

### 13. Znajdź błąd: pętla bez końca
Robot chodzi dookoła i nigdy nie kończy. Czego brakuje?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . * . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Brakuje pytania o skarb z kartą META. Bez niej pętla ∞ nie ma końca.

### 14. STOP czy META? Gdzie stanie?
Programy różnią się jedną kartą. Gdzie stanie robot w A, a gdzie w B?
```plansza
. . . . .
. * . . .
. . . . .
. . . . .
. ^ . . .
```
```program A
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
```program B
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
**Rozwiązanie:** W A robot stanie w 2. rzędzie od góry, na 4. polu od lewej. Robot patrzy w prawo. W B stanie na skarbie, w 2. rzędzie od góry, na 2. polu od lewej. Robot patrzy w górę.

### 15. Lawa w nieznanym miejscu
Dorosły kładzie lawę na jednym z pól ?. Robot ją omija i idzie dalej obok.
```plansza
. . . * .
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
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    NIE: IDŹ
  KONIEC
KONIEC
```
Po obejściu lawy robot idzie dalej sąsiednim rzędem, aż do ściany.

### 16. Twoja misja z pytaniem
Dziecko kładzie lawę i kałuże, a dorosły układa program z JEŚLI. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Ten sam program sprawdźcie na dwóch różnych planszach.
