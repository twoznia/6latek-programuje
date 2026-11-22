# Plansze 5 × 5, poziomy 2 i 3 (1/4)

Kółko to START, a trójkąt pokazuje, gdzie Robot patrzy. Rozwiązanie na dole karty można przed grą zagiąć. Gry 1–11 to poziom 2 (POWTÓRZ), gry 12–15 to poziom 3 (JEŚLI, STOP, META), a gra 16 to plansza do wymyślenia.

### 1. Dookoła klocka
Obejdź klocek i wróć na START. Ile kroków razem?
```plansza
. . . . .
. . . . .
. . # . .
. ^ . . .
. . . . .
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
Kroków razem: 2 + 2 + 2 + 2 = 8. Robot wraca na START i patrzy w górę, tak jak na początku.

### 2. Kwadrat z kałużami
Robot skacze dookoła lawy, zbiera skarby i wraca na START.
```plansza
. . . . .
. * K * .
. K L K .
. ^ K * .
. . . . .
```
```rozwiazanie
POWTÓRZ ×4
  SKOCZ, SKRĘĆ W PRAWO
KONIEC
```
Bez pętli to 8 kart, z pętlą tylko 4.

### 3. Spacer po brzegu
Zbierz skarby w rogach i wróć na START.
```plansza
* . . . *
. . . . .
. . # . .
. . . . .
^ . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×4, SKRĘĆ W PRAWO
KONIEC
```
Kroków razem: 4 + 4 + 4 + 4 = 16.

### 4. Znajdź błąd: zły skręt w pętli
Robot miał obejść kwadrat, zebrać skarby i wrócić. Uderzył w ścianę: BUM! Co zmienić?
```plansza
. . . . .
. . . . .
* . * . .
. . . . .
^ . * . .
```
```program
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W LEWO
KONIEC
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ ×2, SKRĘĆ W PRAWO
KONIEC
```
W pętli ma być SKRĘĆ W PRAWO. Wystarczy zmienić jedną kartę, a robot zrobi to 4 razy.

---

# Plansze 5 × 5, poziomy 2 i 3 (2/4)

### 5. Schodki
Znajdź kawałek, który się powtarza. Lawy nie wolno dotknąć!
```plansza
L . . . *
. . . . .
. . . L .
. . L . .
^ . . . L
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
Bez pętli byłoby to 16 kart, a z pętlą wystarczy 6.

### 6. Kałuże po schodach
Robot patrzy w prawo. Skacz i wspinaj się.
```plansza
. . . . .
. . . . .
. . . . *
L . . K .
> K . L .
```
```rozwiazanie
POWTÓRZ ×2
  SKOCZ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

### 7. Taniec robota
Gdzie skończy robot? Postaw tam skarb i sprawdź.
```plansza
. . . . .
. . . . .
. . . . .
. . ^ . .
. . . . .
```
```program
POWTÓRZ ×3
  IDŹ, OBRÓĆ SIĘ, IDŹ, OBRÓĆ SIĘ
KONIEC
```
**Rozwiązanie:** Robot wraca na swoje pole, bo w każdym powtórzeniu idzie krok i wraca. Możecie zmienić jedną kartę (np. drugie IDŹ na SKRĘĆ) i znowu zgadywać.

### 8. Znajdź błąd
Robot miał dojść po schodkach do skarbu, ale się zatrzymał. Co trzeba zmienić?
```plansza
. . . . .
. . . * .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×2
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
**Rozwiązanie:** Pętla wykonuje się tylko 2 razy, a schodków są 3. W okienku POWTÓRZ trzeba zmienić 2 na 3.

---

# Plansze 5 × 5, poziomy 2 i 3 (3/4)

### 9. Schody w dół
Robot patrzy w dół. Zbierz skarby po schodkach.
```plansza
v . . . .
. * . . .
. . * . .
. . . * .
. . . . *
```
```rozwiazanie
POWTÓRZ ×4
  IDŹ, SKRĘĆ W LEWO, IDŹ, SKRĘĆ W PRAWO
KONIEC
```

### 10. Gdzie stanie robot? Pętla
Programista kładzie figurkę tam, gdzie stanie robot. Robot liczy powtórzenia.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
POWTÓRZ ×3
  IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
**Rozwiązanie:** W 2. rzędzie od góry, na 4. polu od lewej. Robot patrzy w górę.

### 11. Wąż
Zbierz cztery skarby. Znajdź kawałek, który się powtarza.
```plansza
* . * . .
. . . . .
. . . . .
. . . . .
^ * . * .
```
```rozwiazanie
POWTÓRZ ×2
  IDŹ ×4, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W PRAWO, IDŹ ×4
  SKRĘĆ W LEWO, IDŹ, SKRĘĆ W LEWO
KONIEC
```
Bez pętli to 20 kart, z pętlą 11.

### 12. Robot pyta
Dorosły rzuca monetą: orzeł oznacza, że kładzie lawę przed robotem, a reszka, że nie. Jeden program musi działać za każdym razem.
```plansza
. . . . .
. . ? . .
. . ^ . .
. . . . .
. . . . .
```
```program
JEŚLI LAWA?
  TAK: OBRÓĆ SIĘ
  NIE: IDŹ
KONIEC
```
**Rozwiązanie:** Program jest już na planszy. Powtórzcie kilka razy, a potem dziecko zamienia karty w rzędach TAK i NIE na własne.

---

# Plansze 5 × 5, poziomy 2 i 3 (4/4)

### 13. Tajemnicza ścieżka
Ułóż program, zanim dorosły położy kałuże na polach ze znakiem ?. Kałuże nigdy nie leżą obok siebie.
```plansza
. . * . .
. . ? . .
. . ? . .
. . ? . .
. . ^ . .
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
OBRÓĆ SIĘ
```
Pierwsze JEŚLI kończy pętlę na końcu planszy, a drugie wybiera skok albo krok.

### 14. STOP czy META?
Te dwa programy różnią się jedną kartą. W którym robot na końcu obróci się z radości?
```plansza
. . . . .
. . * . .
. . . . .
. . . . .
. . ^ . .
```
```program A
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, STOP
  KONIEC
  IDŹ
KONIEC
OBRÓĆ SIĘ
```
```program B
POWTÓRZ ×∞
  JEŚLI SKARB?
    TAK: IDŹ, META
  KONIEC
  IDŹ
KONIEC
OBRÓĆ SIĘ
```
**Rozwiązanie:** W programie A. STOP kończy tylko pętlę, więc robot potem się obraca. META w programie B kończy cały program (to różnica między *break* a *return*).

### 15. Labirynt z lawą
Napisz jeden program z pętlą ∞ i dwoma JEŚLI: robot sam omija lawę i staje na skarbie.
```plansza
L . . . .
. . . * .
. . L . .
. . . L .
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
Najpierw sprawdzamy skarb, potem lawę.

### 16. Twoja misja
Dziecko rysuje planszę, a dorosły pisze program. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```
**Rozwiązanie:** Tu nie ma jednego rozwiązania. Kto wymyślił planszę, ten sprawdza program, chodząc jako Robot.
