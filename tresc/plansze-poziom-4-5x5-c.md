# Plansze 5 × 5, poziom 4, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 33. Przepis na kwadrat
Przepis A to 2 kroki i skręt. Zbierz skarby i wróć na START.
```plansza
. . . . .
. . . . .
* . * . .
. L . . .
^ . * . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```

### 34. Przepis na schodek
Przepis A to jeden schodek. Ile schodków do skarbu?
```plansza
. . . . *
. . . . L
. . * . .
. . L . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

### 35. Znajdź błąd: za dużo razy
Robot zebrał skarb i wyszedł poza planszę. Którą liczbę zmienić?
```plansza
. . * . .
. . . . .
. L . L .
. . . . .
. . ^ . .
```
```program
PRZEPIS A
  IDŹ ×2
KONIEC
ZRÓB A ×3
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2
KONIEC
ZRÓB A ×2
```
Przepis to 2 kroki. Do skarbu są 4 kroki, więc ZRÓB A ×2.

### 36. Skoki w kółko
Przepis A to skok i skręt w lewo. Zbierz oba skarby.
```plansza
. . . . .
. . . . .
. . * K .
. . K . K
. . * . ^
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3
```

---

# Plansze 5 × 5, poziom 4, zestaw C (2/4)

### 37. Gdzie stanie robot? Trzy razy A
Robot idzie dopiero przy kartach ZRÓB.
```plansza
. . . . .
. . . . .
. . ^ . .
. . . . .
. . . . .
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3, IDŹ ×2
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 4. polu od lewej. Robot patrzy w prawo. Po trzech przepisach robot patrzy w prawo i robi jeszcze 2 kroki.

### 38. Znajdź błąd: przepis bez ZRÓB
Robot w ogóle nie ruszył. Czego brakuje?
```plansza
. . . . .
. L . L .
. . * . .
. . . . .
. . ^ . .
```
```program
PRZEPIS A
  IDŹ ×2, OBRÓĆ SIĘ
KONIEC
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, OBRÓĆ SIĘ
KONIEC
ZRÓB A ×2
```
Przepis robot tylko zapamiętuje. Idzie dopiero po karcie ZRÓB A. Zrób A dwa razy: do skarbu i z powrotem na START.

### 39. Dwa przepisy: A i B
A skręca w prawo, a B w lewo. Zbierz oba skarby.
```plansza
. . . . *
. . . . .
. . * . .
. . . . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A, ZRÓB B
```

### 40. Gdzie stanie robot? META w przepisie
Przepis ma kartę META w środku. Ile kroków zrobi robot?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. ^ . . .
```
```program
PRZEPIS A
  IDŹ, META, IDŹ
KONIEC
ZRÓB A ×3
```
**Rozwiązanie:** Robot stanie w 2. rzędzie od góry, na 2. polu od lewej. Robot patrzy w górę. META kończy tylko przepis, więc w każdym przepisie robot robi 1 krok. Razem 3 kroki.

---

# Plansze 5 × 5, poziom 4, zestaw C (3/4)

### 41. Krok, skok i skręt
Przepis A to krok, skok i skręt w prawo. Zbierz oba skarby.
```plansza
. . . . .
. . K * .
K . . . .
. . . K .
^ . . * .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKOCZ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
```

### 42. Gdzie stanie robot? B woła A
Przepis B używa przepisu A. Robot liczy na głos.
```plansza
. . . . .
. . . . .
. . . . ^
. . . . .
. . . . .
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO
KONIEC
PRZEPIS B
  ZRÓB A ×2, IDŹ ×2
KONIEC
ZRÓB B
```
**Rozwiązanie:** Robot stanie w 4. rzędzie od góry, na 4. polu od lewej. Robot patrzy w dół.

### 43. Dwa klocki, jeden przepis
Przepis A obchodzi klocek i wraca na tę samą linię.
```plansza
. . * . .
. . # . .
. . * . .
. . # . .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```

### 44. Szukaj skarbu dwa razy
Przepis A szuka skarbu. META kończy przepis, a nie cały program.
```plansza
. . . . .
* . . * .
. . . . .
. . L . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI SKARB?
      TAK: IDŹ, META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

---

# Plansze 5 × 5, poziom 4, zestaw C (4/4)

### 45. Znajdź błąd: kolejność w przepisie
Robot wszedł do lawy. Które karty w przepisie zamienić?
```plansza
* . . . .
. . . . .
. . * . .
. . . . .
. . . L ^
```
```program
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ
KONIEC
ZRÓB A ×4
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
Najpierw krok w górę, a dopiero potem skręt w lewo.

### 46. Kałuża czy nic?
Dorosły rzuca monetą dla każdego pola ?: orzeł to kałuża, reszka to nic. Przepis A pyta o kałużę.
```plansza
. . * . .
. . ? . .
. . . . .
. . ? . .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
ZRÓB A ×2
```
Skok i IDŹ ×2 przesuwają robota o 2 pola, więc przepis działa za każdym razem.

### 47. Do ściany i w prawo
Przepis A idzie do ściany i skręca w prawo. Zbierz skarby i wróć na START.
```plansza
* . . . *
. . . . .
. . L . .
. . . . .
^ . . . *
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: SKRĘĆ W PRAWO, META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A ×4
```

### 48. Twój przepis
Dziecko wymyśla przepis, a dorosły kładzie skarby tam, gdzie przepis dojdzie. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry przepis robi się kilka razy.
