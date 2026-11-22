# Plansze 5 × 5, poziom 4 (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. PRZEPIS A … KONIEC robot tylko zapamiętuje. Karta ZRÓB A znaczy: zrób teraz cały przepis A. META w przepisie kończy tylko przepis.

### 1. Pierwszy przepis
Przepis A to bok kwadratu. Zrób go 4 razy, zbierz skarby i wróć na START.
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

### 2. Gdzie stanie robot? Przepis
Robot najpierw czyta przepis, a idzie dopiero przy ZRÓB.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . ^
```
```program
PRZEPIS A
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2, SKRĘĆ W PRAWO, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 1. polu od lewej. Robot patrzy w dół.

### 3. Schody z przepisu
Ułóż przepis na jeden schodek. Ile razy go zrobić?
```plansza
. . . . *
. . . * .
. . * . L
. * . L .
^ . L . .
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

### 4. Skoki dookoła
Przepis to skok i skręt. Zbierz skarby i wróć na START.
```plansza
. . . . .
. . . . .
* K * . .
K . K . .
> K * . .
```
```rozwiazanie
PRZEPIS A
  SKOCZ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```

---

# Plansze 5 × 5, poziom 4 (2/4)

### 5. Znajdź błąd w przepisie
Robot schodzi po schodach, ale wypadł z planszy: BUM! Popraw przepis.
```plansza
. . . . v
. . . * .
. . * . .
. * . . .
* . . . .
```
```program
PRZEPIS A
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
ZRÓB A ×4
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×4
```
Wystarczy poprawić przepis, a wszystkie 4 ZRÓB A same się naprawią.

### 6. Dwa przepisy
Przepis A to marsz, a B to skoki. Obejdź planszę i wróć na START.
```plansza
* K . K *
. . . . .
. . L . .
. . . . .
^ K . K *
```
```rozwiazanie
PRZEPIS A
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  SKOCZ ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A, ZRÓB B
```

### 7. Gdzie stanie robot? A i B
Dwa przepisy na zmianę. Robot liczy na głos.
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
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 3. polu od lewej. Robot patrzy w prawo.

### 8. Taniec z pętlą
W przepisie jest pętla: mały kwadracik. Zbierz skarby.
```plansza
. . L . .
. * . . .
. . . L .
. * . . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO
  KONIEC
KONIEC
ZRÓB A, IDŹ ×2, ZRÓB A
```

---

# Plansze 5 × 5, poziom 4 (3/4)

### 9. Przepis: do ściany
Przepis A idzie do ściany. META w przepisie kończy tylko przepis!
```plansza
. . . . *
. L . . .
. . ^ . .
. . . . .
* . . . *
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
Po META robot wraca do programu i robi kolejną kartę.

### 10. Górka
Przepis B używa przepisu A. Zbierz skarby.
```plansza
. . . . .
. . . . .
. . * . .
. . L . .
^ . L . *
```
```rozwiazanie
PRZEPIS A
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
PRZEPIS B
  ZRÓB A ×2, SKRĘĆ W PRAWO
KONIEC
ZRÓB B ×2
```

### 11. Znajdź błąd: przepis B
Robot miał obejść planszę, ale uderzył w ścianę: BUM! Co poprawić w B?
```plansza
* K . K *
. . . . .
. . L . .
. . . . .
^ K . K *
```
```program
PRZEPIS A
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
PRZEPIS B
  SKOCZ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A, ZRÓB B, ZRÓB A, ZRÓB B
```
**Rozwiązanie:** W przepisie B ma być SKRĘĆ W PRAWO.

### 12. Ząbki
Przepis to jeden ząbek. Policz, ile kart oszczędza.
```plansza
. . . . .
. . . . .
* . * . *
. L . L .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2
  SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO
KONIEC
ZRÓB A ×2, IDŹ ×2
```
Bez przepisu to 13 kart poleceń, z przepisem 10.

---

# Plansze 5 × 5, poziom 4 (4/4)

### 13. Bezpieczny krok
Przepis pyta o kałużę. Na polach ? dorosły kładzie kałuże albo nic.
```plansza
. ? . ? *
? . . . .
. . . . .
? . . . .
^ . . . .
```
```rozwiazanie
PRZEPIS A
  JEŚLI KAŁUŻA?
    TAK: SKOCZ
    NIE: IDŹ ×2
  KONIEC
KONIEC
ZRÓB A ×2, SKRĘĆ W PRAWO, ZRÓB A ×2
```
Przepis zawsze przesuwa robota o 2 pola, z kałużą czy bez.

### 14. Przepis: do skarbu
Przepis A idzie do skarbu. Robot robi go 3 razy.
```plansza
L . . . .
* . . * .
. . . . .
. L . . .
^ . . * .
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
ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A, SKRĘĆ W PRAWO, ZRÓB A
```
META w przepisie kończy przepis, a robot idzie dalej w programie.

### 15. Kwiatek
Przepis A to płatek, a B to płatek i obrót. Zbierz skarby i wróć na START.
```plansza
L . . . L
. * . * .
. . ^ . .
. * . * .
L . . . L
```
```rozwiazanie
PRZEPIS A
  POWTÓRZ ×4
    IDŹ, SKRĘĆ W PRAWO
  KONIEC
KONIEC
PRZEPIS B
  ZRÓB A, SKRĘĆ W PRAWO
KONIEC
ZRÓB B ×4
```

### 16. Twój przepis
Wymyślcie własny przepis i nazwijcie go. Kto zrobi nim najładniejszy wzór?
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Dobry przepis robi się kilka razy.
