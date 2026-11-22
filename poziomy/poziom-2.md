# Robot i Programista — poziom 2

POWTÓRZ, czyli pętla. Potrzebne są też karty z poziomu 1.

## Czego uczy

- **Pętli.** Na poziomie 1 liczba w okienku powtarzała jedno polecenie. Teraz powtarzamy cały kawałek programu.
- **Czytania kodu.** Zanim robot ruszy, zgadujemy, gdzie skończy.
- **Szukania wzorów.** Dziecko szuka w drodze kawałka, który się powtarza.
- **Przy okazji:** dodawania tych samych liczb (2 + 2 + 2), czyli wstępu do mnożenia.

## Nowe karty

```legenda
POWTÓRZ: początek pętli, okienko na liczbę
KONIEC: koniec pętli
```

## Jak układać program

Od tego poziomu program układamy **z góry na dół**, jak listę zakupów. Karty między POWTÓRZ a KONIEC przesuwamy trochę w prawo. To jest **wcięcie**, prawdziwi programiści robią tak samo.

```program
POWTÓRZ ×3
  IDŹ
  SKRĘĆ W PRAWO
KONIEC
```

Robot wykonuje karty po kolei. Gdy dojdzie do KONIEC, wraca do POWTÓRZ i zaczyna od nowa, aż zrobi to tyle razy, ile mówi liczba w okienku. Potem idzie dalej, za KONIEC.

> **Licznik powtórzeń.** Za każdym razem, gdy robot wraca do POWTÓRZ, dziecko kładzie klocek Lego na karcie. Gdy klocków jest tyle, ile mówi liczba, pętla się kończy.

## Jak grać

1. Zacznijcie od zabawy bez planszy: „POWTÓRZ 3: podskocz, klaśnij”. Dziecko układa karty, dorosły wykonuje, i na odwrót.
2. Potem misje z następnej strony. Najpierw dziecko układa program „długi” (bez pętli), a potem szuka, co się powtarza, i skraca go kartą POWTÓRZ.
3. Misje 4 i 5 to zagadki: program już jest, trzeba zgadnąć, co zrobi robot, albo znaleźć błąd.

---

```karty
POWTÓRZ ×4
KONIEC ×4
```

---

# Misje — poziom 2

Niebieskie kółko to robot (biały trójkąt pokazuje, gdzie patrzy). Gwiazdka to skarb, brązowy kwadrat to klocek, czerwone pole to LAWA, niebieskie to KAŁUŻA.

### 1. Schodki
Znajdź kawałek, który się powtarza. Lawy nie wolno dotknąć!
```plansza
L . . . *
. . . . .
. . . L .
. . L . .
^ . . . L
```

### 2. Dookoła klocka
Obejdź klocek i wróć na START. Ile kroków razem?
```plansza
. . . . .
. . . . .
. . # . .
. ^ . . .
. . . . .
```

### 3. Kałuże po schodach
Robot patrzy w prawo. Skacz i wspinaj się.
```plansza
. . . . .
. . . . .
. . . . *
L . . K .
> K . L .
```

### 4. Taniec robota
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
  IDŹ
  OBRÓĆ SIĘ
  IDŹ
  OBRÓĆ SIĘ
KONIEC
```

---

# Misje — poziom 2, ciąg dalszy

### 5. Znajdź błąd
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
  IDŹ
  SKRĘĆ W PRAWO
  IDŹ
  SKRĘĆ W LEWO
KONIEC
```

### 6. Twoja misja
Dziecko rysuje planszę, a dorosły pisze program. Potem zamiana!
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```

## Ile kroków?

- POWTÓRZ ×3 (IDŹ ×2): ile kroków zrobi robot? ______
- POWTÓRZ ×2 (IDŹ ×3): ile kroków? ______
- POWTÓRZ ×4 (SKRĘĆ W PRAWO): gdzie patrzy robot na końcu? ______

---

# Rozwiązania dla dorosłego

### 1. Schodki
```program
POWTÓRZ ×4
  IDŹ
  SKRĘĆ W PRAWO
  IDŹ
  SKRĘĆ W LEWO
KONIEC
```
Bez pętli byłoby to 16 kart, a z pętlą wystarczy 6.

### 2. Dookoła klocka
```program
POWTÓRZ ×4
  IDŹ ×2
  SKRĘĆ W PRAWO
KONIEC
```
Kroków razem: 2 + 2 + 2 + 2 = 8. Robot wraca na START i patrzy w górę, tak jak na początku.

### 3. Kałuże po schodach
```program
POWTÓRZ ×2
  SKOCZ
  SKRĘĆ W LEWO
  IDŹ
  SKRĘĆ W PRAWO
KONIEC
```

### 4. Taniec robota
Robot wraca na swoje pole, bo w każdym powtórzeniu idzie krok i wraca. Możecie zmienić jedną kartę (np. drugie IDŹ na SKRĘĆ) i znowu zgadywać.

### 5. Znajdź błąd
Pętla wykonuje się tylko 2 razy, a schodków są 3. W okienku POWTÓRZ trzeba zmienić 2 na 3.

### Ile kroków?
2 + 2 + 2 = 6; 3 + 3 = 6 (ten sam wynik, inny program!); robot obróci się dookoła i patrzy tam, gdzie na początku.

---

# Zabawy bez przygotowania

- **Wzory z klocków.** Ułóż czerwony, niebieski, czerwony, niebieski… Dziecko mówi, co się powtarza i ile razy, a potem samo buduje wzór „POWTÓRZ 3: żółty, żółty, zielony”.
- **Pociąg na torze.** Tor w kółko to pętla. „POWTÓRZ 5 okrążeń”: dziecko liczy okrążenia i zatrzymuje pociąg.
- **Gimnastyka.** „POWTÓRZ 4: przysiad, podskok”. Dziecko mówi program, dorosły ćwiczy.
