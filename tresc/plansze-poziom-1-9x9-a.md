# Plansze 9 × 9, poziom 1, zestaw A (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Karty liczb są do 6, więc 8 kroków to IDŹ ×6 i IDŹ ×2.

### 1. Daleka droga
Ile kroków do skarbu? Policz pola.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×6
```

### 2. Na sam szczyt
Aż 8 kroków, a karty liczb są do 6. Jak to ułożyć?
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×6, IDŹ ×2
```
8 = 6 + 2. Można też 5 + 3 albo 4 + 4.

### 3. Wielkie L
Idź w górę, skręć i idź do skarbu.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . * . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
IDŹ ×5, SKRĘĆ W PRAWO, IDŹ ×5
```

### 4. Trzy skarby w rzędzie
Robot patrzy w prawo. Zbierz wszystkie skarby.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
> . * . . * . . *
```
```rozwiazanie
IDŹ ×6, IDŹ ×2
```

---

# Plansze 9 × 9, poziom 1, zestaw A (2/4)

### 5. Robot patrzy w dół
Uwaga: gdy robot patrzy w dół, jego prawo jest po naszej lewej!
```plansza
. . . . v . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. * . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
IDŹ ×5, SKRĘĆ W PRAWO, IDŹ ×3
```

### 6. Rzeka
Przez rzekę trzeba przeskoczyć. Kałuży nie wolno dotknąć.
```plansza
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K K K K K K K K K
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×3, SKOCZ, IDŹ ×3
```

### 7. Skoki po kałużach
Ile skoków do skarbu?
```plansza
. . . . * . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . K . . . .
. . . . ^ . . . .
```
```rozwiazanie
SKOCZ ×4
```

### 8. Gdzie stanie robot? Spacer
Programista kładzie figurkę tam, gdzie stanie robot. Robot sprawdza.
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
IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ
```
**Rozwiązanie:** Robot stanie w 7. rzędzie od góry, na 5. polu od lewej. Robot patrzy w prawo.

---

# Plansze 9 × 9, poziom 1, zestaw A (3/4)

### 9. Znajdź błąd: zły skręt
Robot miał dojść do skarbu, ale uderzył w ścianę: BUM! Którą kartę zmienić?
```plansza
. . . . . . . . .
. . * . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . ^
```
```program
IDŹ ×6, IDŹ, SKRĘĆ W PRAWO, IDŹ ×6
```
```rozwiazanie
IDŹ ×6, IDŹ, SKRĘĆ W LEWO, IDŹ ×6
```
Przy ścianie po prawej robot musi skręcić w lewo.

### 10. Wróć na START
Weź skarb i wróć na START. Kałuży nie wolno dotknąć.
```plansza
. . . . . . . . .
. . . . * . . . .
. . . . . . . . .
. . . . . . . . .
. . . . K . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . ^ . . . .
```
```rozwiazanie
IDŹ ×3, SKOCZ, IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×2, SKOCZ, IDŹ ×3
```

### 11. Skarby po bokach
Robot stoi na środku. Zbierz skarb po lewej i po prawej.
```plansza
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
* . . . ^ . . . *
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```
```rozwiazanie
SKRĘĆ W LEWO, IDŹ ×4, OBRÓĆ SIĘ, IDŹ ×6, IDŹ ×2
```

### 12. Lawa i kałuża
Kałużę można przeskoczyć, lawę trzeba obejść.
```plansza
L * . . . . . . .
L . . . . . . . .
L . . . . . . . .
L . . . . . . . .
. . . . . . . . .
. . . . . . . . .
K . . . . . . . .
. . . . . . . . .
^ . . . . . . . .
```
```rozwiazanie
IDŹ, SKOCZ, IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×4
```

---

# Plansze 9 × 9, poziom 1, zestaw A (4/4)

### 13. Mur z lawy
W murze z lawy jest jedna dziura. Znajdź ją!
```plansza
. . . . . . . . .
. . . . . . . . .
. * . . . . . . .
. . . . . . . . .
L L L L L L L . L
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. ^ . . . . . . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×6, SKRĘĆ W LEWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×6
```

### 14. Dwa mury
Pod jednym murem, nad drugim. Klocków nie wolno przesuwać.
```plansza
. . # . . . . . .
. . # . . . . . *
. . # . . # . . .
. . # . . # . . .
. . # . . # . . .
. . # . . # . . .
. . # . . # . . .
. . . . . # . . .
> . . . . # . . .
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×6, IDŹ, SKRĘĆ W PRAWO, IDŹ ×4
```

### 15. Slalom
Omiń klocki i zbierz oba skarby.
```plansza
. . . . . . . . .
. * . . . . . . .
. . . . . . . . .
. . # # # # # # #
. . . . . . . . .
. . . . * . . . .
# # # # # # # . .
. . . . . . . . .
> . . . . . . . .
```
```rozwiazanie
IDŹ ×6, IDŹ, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×6, SKRĘĆ W PRAWO, IDŹ ×4
```

### 16. Twoja wielka misja
Dziecko układa planszę z lawą, kałużami i skarbami, a dorosły pisze program. Potem zamiana!
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
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Kto wymyślił planszę, ten sprawdza program, chodząc jako Robot.
