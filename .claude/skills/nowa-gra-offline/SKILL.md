---
name: nowa-gra-offline
description: Projektowanie nowej gry lub nowego poziomu bez komputera, które uczą 6-latka programowania (sekwencje, pętle, warunki, funkcje) i przy okazji czytania i matematyki. Użyj, gdy ktoś prosi o nową grę, nowy poziom albo nową mechanikę do projektu 6latek-programuje.
---

# Nowa gra offline dla 6-latka

Cel projektu: dziecko uczy się logicznego myślenia i programowania (sekwencja, pętla, if/then/else, break/return, a później funkcje) przez zabawę ruchową, bez ekranu. Przy okazji ćwiczy czytanie i matematykę.

## Kim jest gracz

- Ma 6 lat, zna litery i cyfry, liczy do 100 i dodaje do 10. Czyta sylaby i krótkie słowa WIELKIMI LITERAMI.
- Gra sam albo z dorosłym. Najlepiej działa zabawa ruchowa na podłodze.
- W domu są: drukarka, Lego, drewniane klocki, tory, Clicks i taśma malarska.
- Przed nową grą sprawdź pamięć projektu. Gdy dziecko urośnie, poprawka może już tam być.

## Zasady projektowania

1. **Jedno nowe pojęcie na raz.** Każda gra albo poziom wprowadza dokładnie jedną nową rzecz z programowania. Reszta to znane karty.
2. **Ciało przed kartką.** Najpierw dziecko robi rzecz samo (jest robotem), potem programuje dorosłego, a na końcu układa cały program przed startem.
3. **Robot robi dokładnie to, co napisano.** Błąd jest zabawny, a nie karany. Szukanie błędu, czyli debugowanie, to osobny typ zadania.
4. **Czytanie wbudowane w grę.** Na kartach są krótkie słowa WIELKIMI LITERAMI (IDŹ, SKOCZ, JEŚLI, TAK, NIE). Liczby mają kropki jak na kostce i słowo (TRZY).
5. **Matematyka wbudowana w grę.** Liczby w okienku „×”, liczenie pól i kroków, dodawanie powtórzeń (2 + 2 + 2), porównywanie („więcej niż 3”).
6. **Dwa warianty.** Każda gra ma wersję z wydrukiem i wersję bez przygotowania: z klockami Lego (kolor to polecenie, wysokość wieży to liczba), mówioną albo z torami czy Clicks.
7. **Rodzaje zadań do mieszania:** dojdź do skarbu; zbierz kilka skarbów; omiń lawę (nie wolno jej przeskoczyć); przeskocz kałużę (SKOCZ działa tylko nad kałużą); gdzie skończy robot? (czytanie kodu); znajdź błąd; najkrótszy program; zadanie do wymyślenia przez dziecko („pułapka dla dorosłego”).
8. **Kolejność trudności.** W zestawie zadania idą od najłatwiejszego. Robot najpierw patrzy w górę, a dopiero później w lewo, w prawo i w dół.

## Wygląd kart (zasady Tomka)

- Bez szarych podpisów i opisów na kartach i obrazkach. Na karcie jest tylko ikona i słowo albo liczba.
- Karty poleceń są poziome, z okienkiem po prawej (przerywana ramka z „×”) na kartę liczby. Karta liczby ma 4 × 7,4 cm i mieści się w okienku.
- Każde polecenie ma własny kolor: IDŹ zielony, W PRAWO pomarańczowy, W LEWO niebieski, OBRÓĆ SIĘ fioletowy, SKOCZ morski, POWTÓRZ różowy, KONIEC grafitowy, JEŚLI ciemnożółty, STOP czerwony, META czarna.
- Żadnych prawie pustych stron. Strony z grami mają zawsze 4 gry.
- Spójne nazwy plików: `instrukcja`, `karty`, `plansze-poziom-<poziom>-<plansza>[-<zestaw>]`, małymi literami, bez polskich znaków.

## Plansza na podłogę (do instrukcji)

- Taśma malarska: 5 × 5 pól po ok. 40 cm (razem ok. 2 × 2 m), czyli 6 linii poziomych i 6 pionowych. Plansza 7 × 7 ma ok. 2,8 m albo pola po 30 cm.
- Bez taśmy: kartki A4 (przyklejone od spodu), płytki w kuchni lub łazience, kreda na chodniku.
- Wersja na lata: cerata albo baner ok. 2 × 2 m z liniami z markera lub taśmy izolacyjnej.
- Przy jednym brzegu warto przykleić strzałkę „góra”, żeby misje z kartki łatwo przenieść na podłogę.

## Kroki

1. Ustal z Tomkiem jedno nowe pojęcie i formę gry (podłoga, stół, klocki). Jeśli prośba jest jasna, nie pytaj, tylko zacznij i powiedz, jak ją rozumiesz.
2. Zaproponuj krótki plan (2–4 punkty): nowe karty, zasady, rodzaje zadań, wariant bez druku. Przy dużej zmianie poczekaj na uwagi.
3. Treść zapisz w repo według skilla `robot-programista-plansze`: instrukcja w `tresc/instrukcja.md`, karty w `tresc/karty.md`, plansze w nowym pliku `tresc/plansze-…md`.
4. Jeśli gra potrzebuje nowej karty albo symbolu na planszy, dopisz je w `narzedzia/drukuj.py` (słowniki COL, LABEL, ICON, COND, TILES) i w symulatorze `narzedzia/sprawdz.py`. Opisz je też w README.
5. Każde rozwiązanie sprawdź symulatorem (`make sprawdz`). Zadania z `?` i „gdzie skończy robot?” prześledź ręcznie, krok po kroku.
6. Wygeneruj wydruki (`make`) i obejrzyj każdą stronę jako obrazek (`pdftoppm -r 50 -png`). Sprawdź, czy nic nie wychodzi poza stronę i czy nie ma pustych stron.
7. Zrób commit, PR i merge do `main`. Tomek tak chce na koniec każdej zmiany. Wyślij PDF-y w wątku.
8. Nowe fakty o dziecku albo zasadach zapisz w pamięci projektu.

## Pomysły na kolejne poziomy

- **Poziom 4, funkcje („przepisy”):** dziecko nazywa kawałek programu (np. TANIEC), rysuje go na osobnej karcie i używa jak jednej karty. META w przepisie oznacza „wróć z przepisu” (return).
- **Zmienne („kieszeń”):** robot zbiera klocki i liczy je w kieszeni. JEŚLI w kieszeni są 3 klocki, to META.
- **Dwa roboty:** dwoje dzieci, dwa programy, a roboty nie mogą wejść na to samo pole (kolejność, synchronizacja).
- **Sortowanie klocków:** pętla z JEŚLI na kolorach Lego (algorytmy).
