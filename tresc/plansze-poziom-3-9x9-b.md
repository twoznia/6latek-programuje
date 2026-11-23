# Plansze 9 × 9, poziom 3, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Pole ? to niespodzianka: dorosły kładzie na nim kałużę, lawę albo skarb dopiero po ułożeniu programu. Program musi działać za każdym razem.

### 17. Stop przed lawą
Robot zbiera skarby i staje tuż przed lawą. Nie liczymy kroków!
```plansza
. . L . . . . . .
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . L . . .
. . * . . . . . .
. . . . . . . . .
L . . . . . . . .
. . ^ . . . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
    NIE: IDŹ
  KONIEC
KONIEC
```

### 18. Skarby i kałuże na zmianę
Dorosły rzuca kostką dla każdego pola ?: parzysta liczba to skarb, nieparzysta to kałuża. Robot idzie do ściany.
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
Kałużę robot przeskakuje, a na skarb wchodzi. Za każdym razem kończy na skarbie przy prawej ścianie.

### 19. Gdzie stanie robot? Lawa na drodze
Robot 4 razy pyta o lawę. W rzędzie NIE robi aż 2 kroki.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```program
POWTÓRZ ×4
  JEŚLI LAWA?
    TAK: SKRĘĆ W LEWO
    NIE: IDŹ ×2
  KONIEC
KONIEC
```
**Rozwiązanie:** Dwa kroki w górę, skręt przy lawie i dwa razy po dwa kroki w lewo. Robot stanie w 7. rzędzie od góry, na 1. polu od lewej. Robot patrzy w lewo.

### 20. Gdzie jest skarb? Za rogiem
Dorosły chowa skarb na jednym polu ?. Robot idzie do ściany, skręca i szuka skarbu.
```plansza
. . ? . ? . ? . ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . L . . L . .
. . . . . . . . .
. . . . . . . . .
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
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
```

---

# Plansze 9 × 9, poziom 3, zestaw B (2/4)

### 21. Gdzie stanie robot? Skręt przy skarbie
Robot widzi skarb i skręca. Czy go zbierze?
```plansza
> . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: SKRĘĆ W PRAWO
  KONIEC
  JEŚLI ŚCIANA?
    TAK: META
  KONIEC
  IDŹ
KONIEC
```
**Rozwiązanie:** Robot nie zbierze skarbu. Skręci tuż przed nim i zejdzie w dół do ściany. Stanie w 9. rzędzie od góry, na 4. polu od lewej. Robot patrzy w dół.

### 22. Znajdź błąd: za wcześnie META
Robot zebrał pierwszy skarb i skończył program. Jak zebrać oba?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . L . . . . .
> . . * . . . * .
. . . . . . L . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
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
META kończy cały program już na pierwszym skarbie. Lepiej pytać o ścianę: robot przejdzie cały rząd i zbierze oba skarby.

### 23. Schody z lawy
Przy lawie robot robi krok w bok. Przy ścianie koniec.
```plansza
. . . L . . . . .
. . . . * . . . .
. . L . . . . . .
. . . * . . . . .
. L . . . . . . .
. . . . . . . . .
L * . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
    NIE: IDŹ
  KONIEC
KONIEC
```

### 24. Znajdź błąd: długa droga
Robot znalazł skarb, ale szedł dookoła całej planszy. Którą kartę zmienić, żeby szedł krótko?
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
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
Z SKRĘĆ W LEWO robot idzie w górę, wraca w dół, idzie w prawo i dopiero potem w górę do skarbu. Z SKRĘĆ W PRAWO idzie w górę i od razu w prawo.

---

# Plansze 9 × 9, poziom 3, zestaw B (3/4)

### 25. Ślimak z lawy
Przy lawie robot skręca w prawo. Idzie coraz bliżej środka, aż znajdzie skarb.
```plansza
L . . . . . . . .
. . . . . . . . L
. . L . . . . . .
. . . . . . L . .
. . . . . . . . .
. . . . . * . . .
. . . . . . . . .
. L . . . . . . .
^ . . . . . . L .
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

### 26. Dziura w murze z lawy
Dorosły kładzie lawę na wszystkich polach ? oprócz jednego, a nad tą dziurą kładzie skarb w 1. rzędzie. Robot sprawdza mur pole po polu.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
? ? ? ? ? ? ? ? ?
> . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  SKRĘĆ W LEWO
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ
    NIE: STOP
  KONIEC
KONIEC
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
```
W pierwszej pętli robot patrzy na mur. Lawa: wraca w prawo i robi krok. Dziura: STOP. W drugiej pętli idzie w górę do skarbu.

### 27. Od ściany do ściany
Wewnętrzna pętla idzie do ściany, a zewnętrzna robi to 2 razy. Zbierz oba skarby.
```plansza
. . . . . . . . .
. . . L . . . . .
. . . . . . . . .
. . . . . . . . .
* . > . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
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

### 28. Gdzie stanie robot? Kałuże w pętli
Robot 4 razy pyta o kałużę. Ile pól przejdzie?
```plansza
. . . . . . . . .
. . . . . . . . .
> . K . . K . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```program
POWTÓRZ ×4
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
**Rozwiązanie:** Krok, skok, krok i skok. Robot stanie w 3. rzędzie od góry, na 7. polu od lewej. Robot patrzy w prawo.

---

# Plansze 9 × 9, poziom 3, zestaw B (4/4)

### 29. Lawa czy kałuża?
Dorosły rzuca monetą dla każdego pola ?: orzeł to lawa, reszka to kałuża. Jeden program na 4 ułożenia.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ? . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
  KONIEC
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ
  KONIEC
KONIEC
```
Lawę robot obchodzi z prawej strony, a kałużę przeskakuje. Za każdym razem wraca na swoją drogę 2 pola dalej.

### 30. Znajdź błąd: złe pytanie
Robot miał stanąć przed lawą i skręcić do skarbu, ale wszedł na lawę. Co zmienić?
```plansza
. . . . . . . . .
. . . . . . . . .
. L . . . . . . .
. . . . . . . * .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI ŚCIANA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×6
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: STOP
  KONIEC
  IDŹ
KONIEC
SKRĘĆ W PRAWO, IDŹ ×6
```
Robot pyta o ścianę, a ma pytać o lawę. Trzeba zmienić ŚCIANA? na LAWA?.

### 31. Gdzie stanie robot? Pętla przy ścianie
Robot 6 razy pyta o ścianę. Ile razy skręci?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```program
POWTÓRZ ×6
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ ×2
  KONIEC
KONIEC
```
**Rozwiązanie:** Robot skręci 2 razy. Stanie w prawym górnym rogu, w 1. rzędzie od góry, na 9. polu od lewej. Robot patrzy w dół.

### 32. Dookoła planszy po skarby
Dorosły kładzie skarby na kilku polach ?. Robot idzie przy ścianach dookoła, aż zobaczy lawę.
```plansza
. . . . ? . . . ?
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
? . . . . . . . ?
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
L . . . ? . . . .
```
```rozwiazanie
POWTÓRZ ×∞
  JEŚLI LAWA?
    TAK: META
  KONIEC
  JEŚLI ŚCIANA?
    TAK: SKRĘĆ W PRAWO
    NIE: IDŹ
  KONIEC
KONIEC
```
Robot obchodzi całą planszę i zbiera każdy skarb po drodze. Lawa przy starcie kończy program.
