# Plansze 5 × 5, poziom 3, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 17. Stój przed lawą!
Dorosły kładzie lawę na jednym polu ?. Robot ma stanąć tuż przed nią.
```plansza
. ? . . .
. ? . . .
. ? . . .
. . . . .
. ^ . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
    NIE: IDŹ
  KONIEC
KONIEC
```
Robot idzie, dopóki przed nim nie ma lawy. Lawa w 1. rzędzie: robot stanie w 2. rzędzie. Lawa w 3. rzędzie: robot stanie w 4. rzędzie.

### 18. Gdzie stanie robot? Kałuża
Robot 3 razy pyta o kałużę. Gdzie stanie?
```plansza
. . . . .
. . . . .
K . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×3
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Krok, skok i krok. Robot stanie w 1. rzędzie od góry, na 1. polu od lewej. Robot patrzy w górę.

### 19. Skarb czy kałuża?
Dorosły kładzie na polu ? skarb albo kałużę. Jeden program na oba razy.
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
  TAK: SKOCZ
  NIE: IDŹ ×2
KONIEC
IDŹ
```
Kałuża: robot przeskakuje ją i idzie do skarbu. Skarb: robot staje na nim po drodze i zbiera oba.

### 20. Gdzie stanie robot? META w pętli
Czy robot zbierze skarb? Co zrobi ostatnia karta IDŹ?
```plansza
. . . . .
. . . . .
> . . * .
. . . . .
. . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: META
  KONIEC
  IDŹ
KONIEC
IDŹ
```
**Rozwiązanie:** Robot stanie tuż przed skarbem, w 3. rzędzie od góry, na 3. polu od lewej, i nie zbierze go. Patrzy w prawo. META kończy cały program, więc ostatnie IDŹ się nie wykona.

---

# Plansze 5 × 5, poziom 3, zestaw B (2/4)

### 21. Znajdź błąd: złe pytanie
Robot wszedł do kałuży. Które pytanie jest złe?
```plansza
. . * . .
. . . . .
. . K . .
. . . . .
. . ^ . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
Robot pyta o lawę, a na drodze jest kałuża. Trzeba zmienić LAWA? na KAŁUŻA?.

### 22. Po brzegu do skarbu
Przy ścianie robot skręca w lewo. Gdzie znajdzie skarb?
```plansza
. . * . .
. . . . .
. . L . .
. . . . .
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

### 23. Labirynt w prawo
Przy lawie robot skręca w prawo. Napisz program z pętlą ∞.
```plansza
L . . . .
. . . . L
. . . . .
. . . * .
^ . . . .
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

### 24. Do lawy, potem do skarbu
Dwie pętle ∞, jedna po drugiej. Pierwsza kończy się przy lawie, druga przy skarbie.
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
SKRĘĆ W PRAWO
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```

---

# Plansze 5 × 5, poziom 3, zestaw B (3/4)

### 25. Kałuża i lawa w pętli
Dorosły rzuca monetą: orzeł to kałuża na polu ?, reszka to nic. Robot staje przed lawą i skręca do skarbu.
```plansza
. . L . .
. . . . *
. . . . .
. . ? . .
. . ^ . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
Orzeł: skok, krok i STOP przed lawą. Reszka: trzy kroki i STOP. Za każdym razem robot staje w 2. rzędzie i idzie w prawo do skarbu.

### 26. Znajdź błąd: robot stoi w miejscu
Robot przeskoczył kałużę, a potem stoi i nic nie robi. Czego brakuje?
```plansza
. * . . .
. . . . .
. . . . .
. K . . .
. ^ . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
  KONIEC
KONIEC
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
Brakuje rzędu NIE: IDŹ. Bez niego robot idzie tylko wtedy, gdy przed nim jest kałuża.

### 27. Gdzie stanie robot? Do ściany i w bok
Pętla kończy się przy ścianie. Co robot zrobi potem?
```plansza
. . . . .
. > . . .
. . . . .
. . . . .
. . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×2
```
**Rozwiązanie:** Robot dojdzie do prawej ściany i zejdzie 2 pola w dół. Stanie w 4. rzędzie od góry, na 5. polu od lewej. Robot patrzy w dół.

### 28. Gdzie jest kałuża?
Dorosły kładzie kałużę na jednym polu ?. Robot ją przeskakuje i staje na skarbie.
```plansza
* . . . .
. . . . .
? . . . .
? . . . .
^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
Po skoku robot zawsze ma jeszcze pole przed skarbem, więc pytanie o skarb go zatrzyma.

---

# Plansze 5 × 5, poziom 3, zestaw B (4/4)

### 29. STOP w pętli z liczbą
Pętla ma liczbę 4, ale STOP może ją skończyć wcześniej. Zbierz skarb.
```plansza
. . * . .
. . . . .
> . . L .
. . . . .
. . . . .
```
```rozwiazanie
POWTÓRZ ×4
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W LEWO, IDŹ ×2
```
Robot zrobi tylko 2 kroki. Przy lawie STOP kończy pętlę, chociaż w okienku jest 4.

### 30. Znajdź błąd: za duży krok
Robot miał stanąć przy ścianie, a wypadł z planszy: BUM! Co zmienić?
```plansza
. . * . .
. . . . .
. . . . .
. . ^ . .
. . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ ×2
KONIEC
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```
Robot pyta tylko o pole tuż przed sobą. Po pytaniu może zrobić tylko 1 krok.

### 31. Trzy pytania
W pętli robot pyta o skarb, lawę i kałużę. Dojdź do skarbu.
```plansza
L . . . .
. . K . *
K . . . .
. . . . .
^ . . . .
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

### 32. Twoja misja z niespodzianką
Dziecko kładzie pola ? i w tajemnicy wybiera, co na nich będzie. Dorosły układa program z JEŚLI. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Sprawdźcie program na dwóch różnych ułożeniach.
