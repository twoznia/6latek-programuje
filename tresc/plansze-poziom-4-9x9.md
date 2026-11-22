# Plansze 9 × 9, poziom 4 (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 1. Wielki kwadrat
Przepis A to bok kwadratu. Zbierz skarby i wróć na START.
```plansza
. . . . . . . . .
. * . . . . . * .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . * .
. . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×6, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```

### 2. Gdzie stanie robot? Przepis
Robot idzie dopiero przy kartach ZRÓB.
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
ZRÓB A ×2, SKRĘĆ W LEWO, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 6. rzędzie od góry, na 7. polu od lewej. Robot patrzy w dół.

### 3. Bardzo długie schody
Przepis to jeden schodek. Schodków jest 8, a karty liczb są do 6.
```plansza
. . . . . . . . *
. . . . . . . . .
. . . . . . * . L
. . . . . . . . .
. . . . * . L . .
. . . . . . . . .
. . * . L . . . .
. . . . . . . . .
^ . L . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×6, ZRÓB A ×2
```
8 = 6 + 2.

### 4. Skoki dookoła planszy
Przepis to cztery skoki i skręt. Zbierz skarby i wróć na START.
```plansza
* K . K . K . K *
K . . . . . . . K
. . . . . . . . .
K . . . . . . . K
. . . . . . . . .
K . . . . . . . K
. . . . . . . . .
K . . . . . . . K
^ K . K . K . K *
```
```rozwiazanie
PRZEPIS A
  SKOCZ ×4, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```

---

# Plansze 9 × 9, poziom 4 (2/4)

### 5. Znajdź błąd w przepisie
Robot wypadł z planszy na pierwszym schodku: BUM! Popraw przepis.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . . L . * . .
. . . . . . . . .
. . . . . . L . ^
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
Schody idą w lewo, więc najpierw SKRĘĆ W LEWO.

### 6. Wieża: A i B
A to duży schodek, B to schodek ze skoków. Zbierz skarby.
```plansza
. . . . . . . K *
. . . . . . K . .
. . . . . . * . .
. . . . . . . . .
. . . K * . . . .
. . K . . . . . .
. . * . L . . . .
. . . . . . . . .
^ . L . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
PRZEPIS B
  SKOCZ, SKRĘĆ W PRAWO, SKOCZ, SKRĘĆ W LEWO
KONIEC
POWTÓRZ ×2
  ZRÓB A, ZRÓB B
KONIEC
```

### 7. Przepis: do ściany
Przepis A idzie do ściany. Zbierz skarby.
```plansza
* . . . . . . . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . . . . . L . .
. . > . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . *
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI ŚCIANA?
      TAK: META
    KONIEC
    IDŹ
  KONIEC
KONIEC
POWTÓRZ ×4
  ZRÓB A, SKRĘĆ W PRAWO
KONIEC
```

### 8. Gdzie stanie robot? B i A
Przepis B używa A. Robot liczy na głos.
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
  IDŹ ×2
KONIEC
PRZEPIS B
  ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO
KONIEC
ZRÓB B ×3
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 7. polu od lewej. Robot patrzy w górę.

---

# Plansze 9 × 9, poziom 4 (3/4)

### 9. Wielki grzebień
Przepis to jeden ząbek. Zbierz wszystkie skarby.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . * . * . * . *
. . . . . . . . .
. L . L . L . L .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×3
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4, IDŹ ×3
```

### 10. Bezpieczny krok
Na polach ? mogą być kałuże. Przepis pyta i skacze albo idzie.
```plansza
* ? . ? . ? . ? *
? . . . . . . . .
. . . . . . . . .
? . . . . . . . .
. . . . . . . . .
? . . . . . . . .
. . . . . . . . .
? . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
ZRÓB A ×4, SKRĘĆ W PRAWO, ZRÓB A ×4
```
Ten program działa w 256 ułożeniach kałuż!

### 11. Przepis: do skarbu
Przepis A idzie do skarbu. Robot robi go 3 razy.
```plansza
. . . . . * . . .
. . . . . . . . .
L . . . . . . . .
* . . . . * L . .
. . . . . . . . .
. . . L . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
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
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W LEWO, ZRÓB A
```

### 12. Znajdź błąd: brakuje skrętu
Robot miał obejść płot i wrócić, ale wypadł z planszy: BUM! Czego brakuje?
```plansza
. . . . . . . . .
. . . . . * . . .
. . . . # . . . .
. . . . # . . . .
. . . . # . . . .
. . . . # . . . .
. . . . # . . . .
. . . ^ . * . . .
. . . . . . . . .
```
```program
PRZEPIS A
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×2
KONIEC
ZRÓB A ×2
```
```rozwiazanie
PRZEPIS A
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```
Na końcu przepisu brakuje SKRĘĆ W PRAWO. Wróć na START, żeby sprawdzić.

---

# Plansze 9 × 9, poziom 4 (4/4)

### 13. Wielki kwiatek
A to płatek, B to płatek i obrót. Zbierz skarby i wróć na START.
```plansza
. . . . . . . . .
. . . . . . . . .
. . * . . . * . .
. . . L . L . . .
. . . . ^ . . . .
. . . L . L . . .
. . * . . . * . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
KONIEC
PRZEPIS B
  ZRÓB A, SKRĘĆ W PRAWO
KONIEC
ZRÓB B ×4
```

### 14. Gdzie stanie robot? META w przepisie
Przy lawie przepis kończy się wcześniej. Gdzie stanie robot?
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
L . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```program
PRZEPIS A
  JEŚLI LAWA?
    TAK: SKRĘĆ W PRAWO, META
  KONIEC
  IDŹ ×2
KONIEC
ZRÓB A ×4
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 3. polu od lewej. Robot patrzy w prawo. W trzecim ZRÓB A robot tylko skręca i kończy przepis.

### 15. Przepis: do lawy
Przepis A idzie, aż przed robotem jest lawa. Zbierz skarby.
```plansza
. . . . . . . . .
L . . . . . . . .
. . . . . . * L .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . * L
. . . . . . L . .
^ . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI LAWA?
      TAK: META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W PRAWO
ZRÓB A, SKRĘĆ W LEWO, ZRÓB A
```

### 16. Twój wielki przepis
Dziecko wymyśla przepis, a dorosły planszę, na której przepis się przyda. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Policzcie, ile kart oszczędził przepis.
