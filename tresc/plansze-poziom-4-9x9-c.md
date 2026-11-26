# Plansze 9 × 9, poziom 4, zestaw C (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 33. Długi przepis
Przepis A to 4 kroki. Ile razy go zrobić?
```plansza
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . ^ . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×4
KONIEC
ZRÓB A ×2
```

### 34. Wielka runda w lewo
Przepis A to cały bok planszy i skręt w lewo. Zbierz skarby i wróć na START.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . . . . . . . ^
```
```rozwiazanie
PRZEPIS A
  IDŹ ×6, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

### 35. Schody z przepisu
Przepis A to jeden duży schodek. Pod schodami jest lawa.
```plansza
. . . . . . . . *
. . . . . . . L .
. . . . . . . . .
. . . . . L . . .
. . . . * . . . .
. . . L . . . . .
. . . . . . . . .
. L . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

### 36. Krok i skok
Przepis A to krok i skok. Po przepisach robot idzie jeszcze do skarbu.
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
```rozwiazanie
PRZEPIS A
  IDŹ, SKOCZ
KONIEC
ZRÓB A ×2, IDŹ ×2
```

---

# Plansze 9 × 9, poziom 4, zestaw C (2/4)

### 37. Gdzie stanie robot? Obrót w przepisie B
Przepis B używa przepisu A i się obraca.
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
PRZEPIS A
  IDŹ ×3, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  ZRÓB A ×2, OBRÓĆ SIĘ
KONIEC
ZRÓB B, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 4. polu od lewej. Robot patrzy w prawo.

### 38. Trzy lawy w kolumnie
Przepis A obchodzi lawę i wraca na tę samą linię.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . L . . . .
. . . . ^ . . . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3, IDŹ ×2
```

### 39. Znajdź błąd: zły skręt w przepisie
Robot zebrał jeden skarb i wyszedł poza planszę. Co zmienić w przepisie?
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
PRZEPIS A
  IDŹ ×4, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3
```
```rozwiazanie
PRZEPIS A
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×3
```
Skarby są po prawej, więc w przepisie ma być SKRĘĆ W PRAWO.

### 40. Wieża z przepisów
Przepis A to róg kwadratu. Przepis B robi kwadrat i idzie wyżej.
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
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  ZRÓB A ×4, IDŹ ×4
KONIEC
ZRÓB B ×2
```

---

# Plansze 9 × 9, poziom 4, zestaw C (3/4)

### 41. Gdzie stanie robot? Do ściany dwa razy
Przepis A idzie do ściany. Robot liczy na głos.
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
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A, SKRĘĆ W LEWO, ZRÓB A, SKRĘĆ W LEWO, IDŹ ×3
```
**Rozwiązanie:** Robot stanie w 4. rzędzie od góry, na 1. polu od lewej. Robot patrzy w dół. META kończy tylko przepis, więc robot robi też karty po ZRÓB A.

### 42. Gwiazda z przepisu
Robot stoi w środku. Przepis A idzie na koniec ramienia i wraca.
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
PRZEPIS A
  IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
Po powrocie do środka robot patrzy w drugą stronę, więc SKRĘĆ W PRAWO obraca go do następnego ramienia.

### 43. Przepis do lawy
Przepis A idzie do lawy, skręca w lewo i kończy się. Zbierz oba skarby.
```plansza
. . . . . . . . .
. . . . . . . . L
. . L . . * . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . * . . .
. . . L . . . . .
. . . . . . . . ^
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI LAWA?
      TAK: SKRĘĆ W LEWO, META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A ×3, IDŹ ×2
```

### 44. Znajdź błąd: zamienione ZRÓB
Robot zebrał tylko jeden skarb. Co zamienić?
```plansza
* . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . . . . . . . .
. . . . . . . . .
. . . L . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
PRZEPIS A
  IDŹ ×4
KONIEC
PRZEPIS B
  SKRĘĆ W PRAWO, IDŹ ×4
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A
```
```rozwiazanie
PRZEPIS A
  IDŹ ×4
KONIEC
PRZEPIS B
  SKRĘĆ W PRAWO, IDŹ ×4
KONIEC
ZRÓB A ×2, ZRÓB B
```

---

# Plansze 9 × 9, poziom 4, zestaw C (4/4)

### 45. Schody z kałużami
Na każdym schodku jest kałuża. Przepis A to skok i schodek.
```plansza
. . . . . . . . *
. . . . . . K . .
. . . . . . . . .
. . . . K . . . .
. . . . * . . . .
. . K . . . . . .
. . . . . . . . .
K . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

### 46. Przepis z niespodzianką
Dorosły rzuca monetą dla każdego pola ?: orzeł to kałuża, reszka to nic. Przepis A pyta o kałużę.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> ? . ? . ? . ? *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
ZRÓB A ×4
```
Skok i IDŹ ×2 przesuwają robota o 2 pola, więc przepis działa za każdym razem.

### 47. Po brzegu z kałużami
Przepis A idzie do ściany, skacze nad kałużami i skręca w prawo. Zbierz skarby w rogach.
```plansza
* . . K . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K . . . L . . . K
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . *
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: SKRĘĆ W PRAWO, META
    KONIEC
    JEŚLI KAŁUŻA?
      TAK: SKOCZ
      NIE: IDŹ
    KONIEC
  KONIEC
KONIEC
ZRÓB A ×3
```

### 48. Twój przepis na wzór
Dziecko wymyśla przepis i mówi, ile razy go zrobić. Dorosły zgaduje, jaki wzór narysuje robot. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Robot sprawdza zgadywanie, idąc po planszy.
