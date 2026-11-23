# Plansze 5 × 5, poziom 4, zestaw B (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 17. Tam i z powrotem
Przepis to 2 kroki i obrót. Zbierz skarb i wróć na START.
```plansza
. . . . .
. L . L .
. . * . .
. . . . .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, OBRÓĆ SIĘ
KONIEC
ZRÓB A ×2
```

### 18. Skok za rogiem
Przepis to skok i skręt. Ile razy go zrobić?
```plansza
. . . . .
. . . . .
. K * . .
K . . . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×2
```

### 19. Gdzie stanie robot? Obrót między przepisami
Robot idzie dopiero przy kartach ZRÓB.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . ^ . .
```
```program
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A, OBRÓĆ SIĘ, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 1. polu od lewej. Robot patrzy w górę.

### 20. Zajrzyj w bok
Przepis A to zajrzenie w lewo i powrót. Zbierz oba skarby.
```plansza
. * . . .
. . . . .
. * . . .
. . . L .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO, IDŹ, OBRÓĆ SIĘ, IDŹ, SKRĘĆ W LEWO
KONIEC
POWTÓRZ ×2
  IDŹ ×2, ZRÓB A
KONIEC
```
Po przepisie robot stoi tam, gdzie przed nim, i patrzy w górę.

---

# Plansze 5 × 5, poziom 4, zestaw B (2/4)

### 21. Gdzie stanie robot? Przepis w przepisie
Przepis B używa przepisu A. Robot liczy na głos.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  ZRÓB A ×2
KONIEC
ZRÓB B, ZRÓB A
```
**Rozwiązanie:** Robot robi przepis A 3 razy. Stanie w 5. rzędzie od góry, na 2. polu od lewej. Robot patrzy w lewo.

### 22. Znajdź błąd: A czy B?
A to schodek w lewo, a B w prawo. Robot zebrał tylko jeden skarb. Co zamienić?
```plansza
. . * . .
. . . . .
* . . . .
. . . . .
. . ^ . .
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB B ×2, ZRÓB A ×2
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2, ZRÓB B ×2
```
Karty ZRÓB A i ZRÓB B są zamienione. Najpierw schodki w lewo, potem w prawo.

### 23. Przepis na obejście
Przepis A obchodzi lawę dookoła i wraca na tę samą linię.
```plansza
. . * . .
. . . . .
. . L . .
. . . . .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
IDŹ, ZRÓB A, IDŹ
```

### 24. Lawa czy nic?
Dorosły rzuca monetą dla każdego pola ?: orzeł to lawa, reszka to nic. Przepis A pyta i woła przepis B.
```plansza
. . * . .
. . ? . .
. . . . .
. . ? . .
. . ^ . .
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
ZRÓB A ×2
```
B obchodzi lawę i kończy 2 pola dalej, tak samo jak IDŹ ×2.

---

# Plansze 5 × 5, poziom 4, zestaw B (3/4)

### 25. Przepis: do lawy i w prawo
Przepis A idzie do lawy, skręca w prawo i kończy się. Zbierz skarby.
```plansza
L . . . .
. . * . L
. . . . .
. . . * .
^ . . L .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI LAWA?
      TAK: SKRĘĆ W PRAWO, META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A ×3
```

### 26. Znajdź błąd: META bez przepisu
Robot zebrał pierwszy skarb i skończył program. Jak to naprawić przepisem?
```plansza
. . . . .
* . . * .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
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
META poza przepisem kończy cały program. W przepisie kończy tylko przepis, więc robot idzie dalej.

### 27. Skoki w lewo
Przepis to skok i skręt w lewo. Ile razy go zrobić?
```plansza
. . . . .
. . . . .
* K . . .
. . K . .
> K . . .
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×3
```

### 28. Gdzie stanie robot? Dwa przepisy
Przepis B używa przepisu A. Robot liczy na głos.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
PRZEPIS A
  IDŹ ×2
KONIEC
PRZEPIS B
  SKRĘĆ W PRAWO, ZRÓB A
KONIEC
ZRÓB A, ZRÓB B ×2
```
**Rozwiązanie:** Robot stanie w 5. rzędzie od góry, na 3. polu od lewej. Robot patrzy w dół.

---

# Plansze 5 × 5, poziom 4, zestaw B (4/4)

### 29. Pół kwadratu
Przepis A to pół kwadratu. Zbierz skarby i wróć na START.
```plansza
. . . . .
. . . . .
* . * . .
. L . . .
^ . * . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

### 30. Znajdź błąd: obrót zamiast skrętu
Robot miał obejść kwadrat, a chodzi tam i z powrotem. Którą kartę zmienić w przepisie?
```plansza
. . . . .
. * . * .
. . L . .
. ^ . * .
. . . . .
```
```program
PRZEPIS A
  IDŹ ×2, OBRÓĆ SIĘ
KONIEC
ZRÓB A ×4
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
Zamiast OBRÓĆ SIĘ ma być SKRĘĆ W PRAWO. Poprawka w przepisie działa we wszystkich 4 ZRÓB A.

### 31. Przepis: do kałuży i hop
Przepis A idzie do kałuży, przeskakuje ją i kończy się. Zbierz oba skarby.
```plansza
* . . K *
K . . . .
. . . . .
. . . . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×∞
    JEŚLI KAŁUŻA?
      TAK: SKOCZ, META
    KONIEC
    IDŹ
  KONIEC
KONIEC
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```

### 32. Kieszenie na małej planszy
Dorosły kładzie skarby na polach ? albo ich nie kładzie. Przepis A zagląda w lewo i bierze skarb, jeśli tam jest.
```plansza
. . * . .
. ? . . .
. . . . .
. ? . . .
. . ^ . .
```
```rozwiazanie
PRZEPIS A
  SKRĘĆ W LEWO
  JEŚLI SKARB?
    TAK: IDŹ, OBRÓĆ SIĘ, IDŹ, SKRĘĆ W LEWO
    NIE: SKRĘĆ W PRAWO
  KONIEC
KONIEC
POWTÓRZ ×2
  IDŹ, ZRÓB A, IDŹ
KONIEC
```
