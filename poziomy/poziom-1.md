# Robot i Programista — poziom 1

Idź, skręć, obróć się, skocz, ile razy. Zabawa ruchowa na podłodze, bez komputera.

## Czego uczy

- **Programu jako listy kroków.** Kolejność ma znaczenie, a robot robi dokładnie to, co jest napisane.
- **Powtarzania.** Karta liczby („ile razy”) to pierwszy krok do pętli.
- **Szukania błędów (debugowania).** Gdy robot nie trafi, szukamy, która karta jest zła.
- **Przy okazji:** czytania krótkich słów, liczenia, odróżniania lewej i prawej strony.

## Przygotowanie (10 minut)

- Wydrukuj karty i potnij je. Jeśli chcesz, żeby przetrwały dłużej, wydrukuj je na grubszym papierze albo zalaminuj.
- Na podłodze zrób siatkę **5 × 5 pól** z taśmy malarskiej albo z kartek A4. Jedno pole to jeden krok dziecka (ok. 40–50 cm). Na początek wystarczy 3 × 3.
- Połóż kartę START i kartę SKARB, a na skarb postaw coś fajnego: klocek, figurkę, cukierek.
- Na niektórych polach połóż **LAWĘ** (nie wolno na nią wejść ani jej przeskoczyć, trzeba ją obejść) i **KAŁUŻE** (nie wolno na nie wejść, ale można je przeskoczyć kartą SKOCZ).

## Polecenia

```legenda
IDŹ: 1 krok do przodu
SKRĘĆ W PRAWO: obrót w miejscu
SKRĘĆ W LEWO: obrót w miejscu
OBRÓĆ SIĘ: obrót tyłem do przodu
SKOCZ: przeskok nad jednym polem
```

Każda karta polecenia ma z boku okienko z ×. Wkładamy tam kartę liczby, która mówi, ile razy wykonać polecenie. Na przykład **IDŹ 3** to trzy kroki. Puste okienko oznacza: raz. Program układamy w rzędzie od lewej do prawej, tak jak się czyta.

## Jak grać: trzy etapy

1. **Dziecko jest robotem.** Dorosły układa program, dziecko czyta kartę po karcie i wykonuje polecenia.
2. **Dziecko jest programistą.** Robotem jest dorosły. Robot robi *dokładnie* to, co jest na kartach, nawet jeśli prowadzi to w ścianę. To najzabawniejsza część, a szukanie błędu to prawdziwe debugowanie.
3. **Program przed startem.** Dziecko układa cały program, patrząc na planszę, i dopiero potem go sprawdza: samo albo przesuwając figurkę Lego po polach. Na tym etapie przydają się misje z dalszych stron.

> **Lewo czy prawo?** Pomóc może gumka albo naklejka na prawej ręce, w tym samym kolorze co karta W PRAWO (pomarańczowa). Gdy robot skręca, nie robi kroku, tylko obraca się w miejscu.

---

```karty
IDŹ ×6
SKRĘĆ W PRAWO ×3
SKRĘĆ W LEWO ×3
OBRÓĆ SIĘ ×2
SKOCZ ×2
LICZBY 1-6 ×2
START ×1
SKARB ×3
LAWA ×4
KAŁUŻA ×4
```

---

# Misje — poziom 1

Niebieskie kółko to robot (biały trójkąt pokazuje, gdzie patrzy). Gwiazdka to skarb, brązowy kwadrat to klocek, czerwone pole to LAWA, niebieskie to KAŁUŻA.

### 1. Prosto do skarbu
Robot patrzy w górę. Ile kroków do skarbu?
```plansza
. . . . .
. . * . .
. . . . .
. . . . .
. . ^ . .
```

### 2. W prawo!
Najpierw trzeba się obrócić.
```plansza
. . . . .
. . . . .
. . . . .
^ . . * .
. . . . .
```

### 3. Za rogiem
Idź, skręć, idź.
```plansza
. . . . .
. * . . .
. . . . .
. . . . .
. . . ^ .
```

### 4. Skarb za plecami
Robot nie widzi skarbu. Co zrobić?
```plansza
. . . . .
. . ^ . .
. . . . .
. . . . .
. . * . .
```

### 5. Omiń klocek
Na klocek nie wolno wejść!
```plansza
. . * . .
. . . . .
. # . . .
. . . . .
. ^ . . .
```

### 6. Wyzwanie
Ułóż program z jak najmniejszej liczby kart.
```plansza
# . . . *
. . . . .
. . . . .
. . . . .
^ . . . #
```

---

# Misje z lawą i kałużą

Niebieskie kółko to robot (biały trójkąt pokazuje, gdzie patrzy). Gwiazdka to skarb, czerwone pole to LAWA, niebieskie to KAŁUŻA.

### 7. Lawa!
Lawę trzeba obejść dookoła.
```plansza
. . * . .
. . . . .
. . L . .
. . . . .
. . ^ . .
```

### 8. Kałuża
Przeskocz kałużę!
```plansza
. . * . .
. . . . .
. . K . .
. . . . .
. . ^ . .
```

### 9. Dwie kałuże
Wystarczy jedna karta i liczba.
```plansza
. * . . .
. K . . .
. . . . .
. K . . .
. ^ . . .
```

### 10. Lawa i kałuża
Robot patrzy w prawo.
```plansza
. . . . .
. . . . .
. . . . *
. . . . .
> K . L .
```

---

# Misje — więcej zadań

Uwaga na robota: nie zawsze patrzy w górę! Biały trójkąt pokazuje, w którą stronę patrzy.

### 11. Dwa skarby
Zbierz oba skarby.
```plansza
. . . . .
. . . . .
* . . * .
. . . . .
^ . . . .
```

### 12. Robot patrzy w lewo
Gdzie jest jego prawa ręka?
```plansza
. * . . .
. . . . .
. . . . <
. . . . .
. . . . .
```

### 13. Robot patrzy w dół
Podpowiedź: stań tak jak robot.
```plansza
. . v . .
. . . . .
. . . . .
. . . . *
. . . . .
```

### 14. Gdzie skończy robot?
Przeczytaj program i połóż skarb tam, gdzie robot się zatrzyma.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
^ . . . .
```
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
```

---

# Misje — więcej zadań, ciąg dalszy

### 15. Znajdź błąd
Robot nie trafił do skarbu. Która karta jest zła?
```plansza
. . . . .
. . . * .
. . . . .
. . . . .
. ^ . . .
```
```program
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2
```

### 16. Literka U
Przejdź dookoła ściany z klocków.
```plansza
. . . . .
. # . . .
. # . . .
. # . . .
^ # * . .
```

### 17. Kałuża i lawa
Kałużę można przeskoczyć, lawy nie.
```plansza
. . * . .
. . L . .
. . . . .
. . K . .
. . ^ . .
```

### 18. Trzy skarby
Robot patrzy w prawo. Zbierz wszystkie skarby.
```plansza
. . . . .
. . . . .
. . * . *
. . . L .
> . * . .
```

---

# Misje — jeszcze więcej

### 19. Ile pól?
Ile pól przejdzie robot? SKOK to 2 pola. Sprawdź na podłodze.
```program
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×3, SKOCZ
```

### 20. Twoja misja
Narysuj planszę dla dorosłego. Niech dorosły ułoży program, a ty sprawdź, czy robot dojdzie do skarbu.
```plansza
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```

---

# Rozwiązania dla dorosłego

To przykładowe rozwiązania. Każdy program, który dojdzie do skarbu bez wchodzenia na klocek, lawę ani kałużę, jest dobry.

### 1. Prosto do skarbu
```program
IDŹ ×3
```

### 2. W prawo!
```program
SKRĘĆ W PRAWO, IDŹ ×3
```

### 3. Za rogiem
```program
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2
```

### 4. Skarb za plecami
```program
OBRÓĆ SIĘ, IDŹ ×3
```

### 5. Omiń klocek
```program
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3
```

### 6. Wyzwanie
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4, SKRĘĆ W LEWO, IDŹ ×2
```

### 7. Lawa!
```program
IDŹ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×3, SKRĘĆ W LEWO, IDŹ
```

### 8. Kałuża
```program
IDŹ, SKOCZ, IDŹ
```

### 9. Dwie kałuże
```program
SKOCZ ×2
```

### 10. Lawa i kałuża
```program
SKOCZ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```

---

# Rozwiązania: więcej zadań

### 11. Dwa skarby
```program
IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×3
```

### 12. Robot patrzy w lewo
```program
IDŹ ×3, SKRĘĆ W PRAWO, IDŹ ×2
```
Robot patrzy w lewo, więc jego prawa ręka wskazuje w górę.

### 13. Robot patrzy w dół
```program
IDŹ ×3, SKRĘĆ W LEWO, IDŹ ×2
```
Robot patrzy w dół, więc „w lewo” dla niego to w prawo na kartce. Niech dziecko stanie na podłodze tak jak robot.

### 14. Gdzie skończy robot?
W drugim rzędzie od góry, na czwartym polu od lewej.

### 15. Znajdź błąd
Zamiast SKRĘĆ W LEWO powinno być SKRĘĆ W PRAWO.

### 16. Literka U
```program
IDŹ ×4, SKRĘĆ W PRAWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×4
```

### 17. Kałuża i lawa
```program
SKOCZ, SKRĘĆ W PRAWO, IDŹ, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W LEWO, IDŹ
```

### 18. Trzy skarby
```program
IDŹ ×2, SKRĘĆ W LEWO, IDŹ ×2, SKRĘĆ W PRAWO, IDŹ ×2
```

### 19. Ile pól?
2 + 3 + 2 = 7 pól.

---

# Zabawy dodatkowe

## Wersja bez przygotowania (bez drukowania)

- **Program z klocków Lego.** Kolor klocka oznacza polecenie: zielony to IDŹ, niebieski to W LEWO, pomarańczowy lub czerwony to W PRAWO, żółty to OBRÓĆ SIĘ. Wieża z kilku klocków tego samego koloru oznacza „tyle razy”. Program to rząd wież na stole.
- **Plansza bez taśmy.** Wystarczą płytki na podłodze, wzór dywanu albo chodnik na spacerze.
- **Robot słucha.** Dziecko mówi polecenia na głos („idź dwa razy, skręć w prawo”), a dorosły wykonuje je co do joty.
- **Pułapka.** Dziecko układa planszę z lawą i kałużami dla dorosłego, a dorosły pisze program. Dziecko sprawdza, czy robot nie wpadł do lawy.

## Bonus: matematyka

- **Ile kroków razem?** W programie IDŹ 2, SKRĘĆ, IDŹ 3 robot zrobi 2 + 3 = 5 kroków.
- **Skróć program.** Dwie karty IDŹ 2 i IDŹ 1 obok siebie można zamienić na jedną IDŹ 3.
- **Najkrótszy program.** Kto ułoży program z najmniejszej liczby kart? Policzcie je.
