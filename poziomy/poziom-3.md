# Robot i Programista — poziom 3

JEŚLI, TAK, NIE, a także STOP i META. Potrzebne są karty z poziomów 1 i 2.

## Czego uczy

- **Warunków (if / then / else).** Robot sprawdza, co jest na polu przed nim, i sam wybiera, co zrobić.
- **Przerywania pętli (break).** Karta STOP kończy powtarzanie, a robot czyta dalej program za KONIEC.
- **Kończenia programu (return).** Karta META kończy cały program. Robot staje i nic więcej nie robi.
- **Programu na każdą planszę.** Dobry program działa nawet wtedy, gdy nie wiemy, gdzie leżą kałuże.

## Nowe karty

- **JEŚLI**: w okienko wkładamy kartę pytania. Pytanie zawsze dotyczy pola tuż przed robotem: **LAWA?** **KAŁUŻA?** **SKARB?** **ŚCIANA?** (ściana to koniec planszy).
- **TAK** i **NIE**: kładziemy je na początku dwóch rzędów pod kartą JEŚLI.
- **∞ ZAWSZE**: wkładamy w okienko POWTÓRZ. Pętla powtarza się bez końca, aż trafi na STOP albo METĘ.
- **STOP** i **META**: zobacz wyżej.

## Jak układać JEŚLI

```program
JEŚLI LAWA?
  TAK: OBRÓĆ SIĘ
  NIE: IDŹ
KONIEC
```

Robot patrzy na pole przed sobą i odpowiada na pytanie. Jeśli odpowiedź to TAK, wykonuje karty z rzędu TAK, a jeśli NIE, to z rzędu NIE. Potem idzie dalej, za KONIEC. Rząd NIE może zostać pusty.

> **Mów na głos.** Robot zadaje pytanie głośno: „Czy przede mną jest lawa? NIE! To idę.” Dzięki temu dziecko słyszy, jak działa warunek.

## Jak grać

1. Najpierw samo JEŚLI, bez pętli (misja 1).
2. Potem JEŚLI w środku pętli POWTÓRZ ×∞ (misje 2 i 4).
3. Na końcu różnica między STOP a METĄ (misja 3).

---

```karty
JEŚLI ×2
STOP ×1
META ×1
KONIEC ×4
LAWA? ×2
KAŁUŻA? ×2
SKARB? ×1
ŚCIANA? ×1
TAK ×2
NIE ×2
ZAWSZE ×2
```

---

# Misje — poziom 3

Żółty znak ? to pole, na którym może coś leżeć, ale nie wiemy co.

### 1. Robot pyta
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

### 2. Tajemnicza ścieżka
Ułóż program, zanim dorosły położy kałuże na polach ze znakiem ?. Kałuże nigdy nie leżą obok siebie.
```plansza
. . * . .
. . ? . .
. . ? . .
. . ? . .
. . ^ . .
```

---

# Misje — poziom 3, ciąg dalszy

### 3. STOP czy META?
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

### 4. Labirynt z lawą
Napisz jeden program z pętlą ∞ i dwoma JEŚLI: robot sam omija lawę i staje na skarbie.
```plansza
L . . . .
. . . * .
. . L . .
. . . L .
^ . . . .
```

---

# Rozwiązania dla dorosłego

### 1. Robot pyta
Program jest już na planszy. Powtórzcie kilka razy, a potem dziecko zamienia karty w rzędach TAK i NIE na własne.

### 2. Tajemnicza ścieżka
```program
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
Pierwsze JEŚLI zatrzymuje pętlę na końcu planszy (robot stoi wtedy na skarbie). Drugie wybiera między skokiem a krokiem. Po STOP robot czyta dalej, więc obraca się z radości.

### 3. STOP czy META?
**A**: STOP przerywa tylko pętlę, więc robot dochodzi do skarbu i robi OBRÓĆ SIĘ. **B**: META kończy cały program, więc robot staje na skarbie i się nie obraca. W programowaniu to różnica między *break* a *return*.

### 4. Labirynt z lawą
```program
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
Kolejność JEŚLI ma znaczenie: najpierw sprawdzamy skarb, potem lawę. Robot idzie w górę, przy lawie skręca w prawo i dochodzi do skarbu.

---

# Zabawy bez przygotowania

- **Sortowanie klocków.** „POWTARZAJ ZAWSZE: weź klocek z pudełka. JEŚLI jest czerwony, TAK: połóż na stół, NIE: odłóż do pudełka nr 2. JEŚLI pudełko puste: STOP.”
- **Kolorowe komendy.** Dorosły pokazuje klocek. „JEŚLI zielony, to podskocz, INACZEJ klaśnij.” Potem dziecko wymyśla zasady dla dorosłego.
- **Szukanie skarbu w worku.** „POWTARZAJ ZAWSZE: wyciągnij klocek. JEŚLI żółty: STOP.” Policzcie, ile razy trzeba było losować.
- **Kostka i warunek.** Rzuć kostką. „JEŚLI wypadło więcej niż 3, TAK: IDŹ tyle kroków, NIE: SKOCZ.” Ćwiczy porównywanie liczb.
- **Tor z rozjazdem.** Zwrotnica w torze to JEŚLI: „JEŚLI wagon jest niebieski, jedzie w lewo, INACZEJ w prawo”.

## Co dalej (poziom 4)

Własne „przepisy” (funkcje): dziecko nazywa kawałek programu, np. TANIEC, i używa go jak jednej karty. Wtedy META w przepisie oznacza „wróć z przepisu”, czyli prawdziwe *return*.
