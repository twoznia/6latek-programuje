# Plansze 5 × 5, poziom 1, zestaw F (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 81. Korytarz z lawy
Po bokach jest lawa. Ile kroków do skarbu?
```plansza
. . . . .
. L * L .
. L . L .
. L . L .
. . ^ . .
```
```rozwiazanie
IDŹ ×3
```

### 82. Kałuża przed skarbem
Dojdź do kałuży i przeskocz ją.
```plansza
. . * . .
. . K . .
L . . . L
. . . . .
. . ^ . .
```
```rozwiazanie
IDŹ ×2, SKOCZ
```

### 83. Hop i hop
Dwie kałuże, jedna za drugą. Ile razy skoczyć?
```plansza
. . * . .
. . K . .
. . . . .
. . K . .
. . ^ . .
```
```rozwiazanie
SKOCZ ×2
```

### 84. Skarb za plecami
Skarb jest za robotem. Jak się do niego odwrócić?
```plansza
. . L . .
. . ^ . .
. . . . .
. . . . .
. . * . .
```
```rozwiazanie
OBRÓĆ SIĘ, IDŹ ×3
```

---

# Plansze 5 × 5, poziom 1, zestaw F (2/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 85. Do rogu w lewo
Robot patrzy w lewo. Skarb jest w rogu.
```plansza
* . . . .
. . . . .
. . . . .
. . . . .
. . . . <
```
```rozwiazanie
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×4
```
Robot patrzy w lewo, więc SKRĘĆ W PRAWO obraca go w górę.

### 86. Robot patrzy w dół
W którą stronę skręcić, żeby dojść do skarbu?
```plansza
. . v . .
. . . . .
* . . . .
. . . . .
. . . . .
```
```rozwiazanie
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```
Gdy robot patrzy w dół, jego prawa ręka jest po lewej stronie planszy.

### 87. Dwa skarby po bokach
Robot stoi w środku. Zbierz oba skarby.
```plansza
. . . . .
. . L . .
* . ^ . *
. . L . .
. . . . .
```
```rozwiazanie
SKRĘĆ W LEWO, IDŹ ×2, OBRÓĆ SIĘ, IDŹ ×4
```

### 88. Gdzie stanie robot? Tam i z powrotem
Programista kładzie figurkę tam, gdzie stanie robot. Robot sprawdza.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×3, OBRÓĆ SIĘ, IDŹ
```
**Rozwiązanie:** Robot stanie w 3. rzędzie od góry, na 3. polu od lewej. Robot patrzy w lewo.

---

# Plansze 5 × 5, poziom 1, zestaw F (3/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 89. Lawa w rogu
Lawa stoi na drodze. Obejdź ją do skarbu.
```plansza
. . . * L
. . . . .
. . . . .
. . . . .
. . . . ^
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO, IDŹ
```

### 90. Znajdź błąd: zły skręt
Robot poszedł w złą stronę. Którą kartę wymienić?
```plansza
. . . . .
* . . . .
. . . . .
. . . . .
. . ^ . .
```
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×2
```
```rozwiazanie
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2
```
Skarb jest po lewej, więc zamiast SKRĘĆ W PRAWO ma być SKRĘĆ W LEWO.

### 91. Kałuża za rogiem
Idź w prawo, przeskocz kałużę i skręć do skarbu.
```plansza
> . . K .
. . . . .
. . . . .
. . . . .
. . . . *
```
```rozwiazanie
IDŹ ×2, SKOCZ, SKRĘĆ W PRAWO, IDŹ ×4
```

### 92. Mur z kałużą
Mur z klocków ma jedno przejście: kałużę.
```plansza
. . * . .
. . . . .
# # K # #
. . . . .
. ^ . . .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ, SKOCZ, IDŹ
```

---

# Plansze 5 × 5, poziom 1, zestaw F (4/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć.

### 93. Gdzie stanie robot? Skok
Program ma skok. Robot liczy na głos.
```plansza
. . . . .
. . . . .
. . . . .
. K . . .
. ^ . . .
```
```program
SKOCZ, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ
```
**Rozwiązanie:** Robot stanie w 2. rzędzie od góry, na 4. polu od lewej. Robot patrzy w górę.

### 94. Klockowy labirynt
Na klocki nie wolno wchodzić. Znajdź drogę do skarbu.
```plansza
* # . . .
. # # # .
. . . # .
# # . . .
^ . . # .
```
```rozwiazanie
SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```

### 95. Pięć skarbów
Zbierz wszystkie skarby. Uda się tylko z 6 kartami?
```plansza
. . . . .
* . . . .
* . L . .
* * * . .
^ . . . .
```
```rozwiazanie
IDŹ ×3, OBRÓĆ SIĘ, IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2
```
Najpierw w górę, potem z powrotem i w prawo.

### 96. Twoja misja
Dziecko kładzie skarby, lawę i kałuże, a dorosły układa program. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Robot sprawdza program, idąc po planszy.
