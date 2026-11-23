# Plansze 9 × 9, poziom 4, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 17. Przepis na 4 kroki
Przepis A to 4 kroki. Ile razy go zrobić, żeby dojść do skarbu?
```plansza
. . . . * . . . .
. . . . . . . . .
. . . L . L . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . L . L . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×4
KONIEC
ZRÓB A ×2
```
2 razy po 4 kroki to 8 kroków.

### 18. Prostokąt z przepisu
Przepis A to połowa prostokąta. Zbierz skarby i wróć na START.
```plansza
. . . . . . . . .
. * . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . L . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . * . . . .
. . . . . . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```

### 19. Gdzie stanie robot? Trzy razy w lewo
Robot idzie dopiero przy karcie ZRÓB.
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
PRZEPIS A
  IDŹ ×3, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3
```
**Rozwiązanie:** Robot stanie w 9. rzędzie od góry, na 6. polu od lewej. Robot patrzy w prawo.

### 20. Choinka
Przepis A to zajrzenie na gałązkę w prawo i powrót. Zbierz wszystkie skarby.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . ^ . . . . . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W PRAWO, IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
POWTÓRZ ×4
  IDŹ ×2, ZRÓB A
KONIEC
```

---

# Plansze 9 × 9, poziom 4, zestaw B (2/4)

### 21. Kwadraty jeden nad drugim
A to mały kwadrat, a B to przejście w górę. Zbierz skarby.
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
  POWTÓRZ ×4
    IDŹ ×2, SKRĘĆ W PRAWO
  KONIEC
KONIEC
PRZEPIS B
  IDŹ ×4
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A, ZRÓB B
```
Po przepisie A robot jest znowu w rogu kwadratu i patrzy w górę.

### 22. Znajdź błąd: za mało ZRÓB
Robot wchodził po schodach, ale nie doszedł do skarbu. Co poprawić?
```plansza
. . . . . . . . *
. . . . . . . . L
. . . . . . . . .
. . . . . . L . .
. . . . . . . . .
. . . . L . . . .
. . . . . . . . .
. . L . . . . . .
^ . . . . . . . .
```
```program
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```
Przepis jest dobry. Schodków jest 4, więc przy ZRÓB A trzeba zmienić 3 na 4.

### 23. Gdzie stanie robot? B i A
Przepis B używa przepisu A. Robot liczy na głos.
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
PRZEPIS A
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
PRZEPIS B
  ZRÓB A ×2, OBRÓĆ SIĘ
KONIEC
ZRÓB B, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 7. polu od lewej. Robot patrzy w lewo.

### 24. Trzy ściany
Przepis A idzie do ściany, skręca w prawo i się kończy. Zbierz skarby w rogach.
```plansza
* . . . . . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . L . . . .
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
    IDŹ
  KONIEC
KONIEC
ZRÓB A ×3
```

---

# Plansze 9 × 9, poziom 4, zestaw B (3/4)

### 25. Lawa czy nic? Długa droga
Dorosły rzuca monetą dla każdego pola ?: orzeł to lawa, reszka to nic. A pyta, a B obchodzi lawę.
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
PRZEPIS B
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
PRZEPIS A
  JEŚLI LAWA?
    TAK: ZRÓB B
    NIE: IDŹ ×2
  KONIEC
KONIEC
ZRÓB A ×4
```
Ten program działa dla wszystkich 16 ułożeń lawy.

### 26. Skarby w kieszeniach
Dorosły kładzie skarby na kilku polach ?. Przepis A zagląda w lewo i bierze skarb, jeśli tam jest.
```plansza
. . . ? . . . . .
. . . . . . . . .
. . . ? . . . . .
. . . . . . . . .
. . . ? . . . . .
. . . . . . . . .
. . . ? . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO
  JEŚLI SKARB?
    TAK: IDŹ, OBRÓĆ SIĘ, IDŹ, SKRĘĆ W LEWO
    NIE: SKRĘĆ W PRAWO
  KONIEC
KONIEC
POWTÓRZ ×4
  IDŹ ×2, ZRÓB A
KONIEC
```
Po przepisie A robot zawsze wraca na swoją drogę i patrzy w górę.
