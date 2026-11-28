// Pomoc w grze online: jak działa każda karta, pytanie i pole, z przykładami dla poziomów 1-7.
// Plik pisany ręcznie (nie generowany). Każdy przykład to mała gra: przycisk „Wypróbuj” otwiera ją
// z gotowym programem, a narzedzia/test_online.js sprawdza, że każdy przykład kończy się BRAWO.
// Format przykładu jak gra w gra/gry.js: plansza (kwadrat), program/przepis jako karty [nazwa, liczba|pytanie].
(function () {
  "use strict";
  var R = ["IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ"];
  var K2 = R.concat(["POWTÓRZ", "JEŚLI", "ZRÓB A"]);
  var K3 = R.concat(["POWTÓRZ", "DOPÓKI", "JEŚLI"]);
  var K4 = K3.concat(["N =", "N +", "N −"]);
  var K6 = K4.concat(["ZRÓB A"]);
  var K7 = K6.concat(["META"]);

  window.POMOC = [
    {
      poziom: 1,
      wstep: "Ułóż karty w rzędzie. Robot robi je po kolei. Potem naciśnij START.",
      rzeczy: [
        { karta: "IDŹ", tekst: "Robot idzie o jedno pole do przodu. Tam, gdzie patrzy.",
          przyklad: { id: "idz", tytul: "Trzy kroki", wynik: "Trzy kroki i skarb!", karty: R,
            plansza: [". * . .", ". . . .", ". . . .", ". ^ . ."], program: [["IDŹ", 3]] } },
        { liczba: true, nazwa: "Liczba", tekst: "Liczba mówi, ile razy. IDŹ ×3 to to samo, co IDŹ, IDŹ, IDŹ." },
        { karta: "SKRĘĆ W PRAWO", tekst: "Robot obraca się w prawo. Stoi na tym samym polu.",
          przyklad: { id: "prawo", tytul: "Skręt w prawo", wynik: "Obrót w prawo, potem dwa kroki.", karty: R,
            plansza: [". . .", ". . .", "^ . *"], program: [["SKRĘĆ W PRAWO", 1], ["IDŹ", 2]] } },
        { karta: "SKRĘĆ W LEWO", tekst: "Robot obraca się w lewo. Stoi na tym samym polu.",
          przyklad: { id: "lewo", tytul: "Skręt w lewo", wynik: "Dwa kroki, obrót w lewo, dwa kroki.", karty: R,
            plansza: ["* . .", ". . .", ". . ^"], program: [["IDŹ", 2], ["SKRĘĆ W LEWO", 1], ["IDŹ", 2]] } },
        { karta: "OBRÓĆ SIĘ", tekst: "Robot odwraca się do tyłu.",
          przyklad: { id: "obroc", tytul: "Do tyłu", wynik: "Robot się odwraca i idzie w dół.", karty: R,
            plansza: [". ^ .", ". . .", ". * ."], program: [["OBRÓĆ SIĘ", 1], ["IDŹ", 2]] } },
        { karta: "SKOCZ", tekst: "Robot skacze nad kałużą. Ląduje dwa pola dalej. Skacze tylko nad kałużą!",
          przyklad: { id: "skocz", tytul: "Hop nad kałużą", wynik: "Hop! Robot jest za kałużą.", karty: R,
            plansza: [". * .", ". K .", ". ^ ."], program: [["SKOCZ", 1]] } },
        { pole: "k", nazwa: "Litery", tekst: "Robot zbiera literę, gdy na niej stanie. Litery trzeba zbierać po kolei, tak jak w słowie. Na literę, która teraz nie pasuje, nie wolno wejść. Nad planszą widać, ile liter już jest.",
          przyklad: { id: "litery", tytul: "Słowo KOT", wynik: "K, O, T: robot ułożył słowo KOT!", karty: R, slowo: "KOT",
            plansza: [". . . .", ". o t .", ". k . .", ". ^ . ."], program: [["IDŹ", 2], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1]] } },
        { pole: "3", nazwa: "Monety", tekst: "Robot zbiera monetę, gdy na niej stanie. Dodaj liczby z monet. Razem ma być dokładnie tyle, ile mówi zadanie. Nad planszą widać sumę.",
          przyklad: { id: "monety1", tytul: "Razem 7", wynik: "3 + 4 = 7. Moneta 5 dałaby za dużo!", karty: R, suma: 7,
            plansza: [". 4 5 .", ". . . .", ". 3 . .", ". ^ . ."], program: [["IDŹ", 3]] } }
      ],
      pola: [
        { pole: "^", nazwa: "Robot", tekst: "Tu robot zaczyna. Trójkąt pokazuje, gdzie patrzy." },
        { pole: "*", nazwa: "Skarb", tekst: "Tu idzie robot. Zbierz wszystkie gwiazdki." },
        { pole: "L", nazwa: "Lawa", tekst: "Nie wolno wejść ani skakać. Obejdź ją." },
        { pole: "K", nazwa: "Kałuża", tekst: "Przeskocz ją kartą SKOCZ." },
        { pole: "#", nazwa: "Klocek", tekst: "Tu nie wolno wejść." }
      ],
      przyciski: true
    },
    {
      poziom: 2,
      wstep: "Nowe karty: pętla, pytanie i przepis. Nowe pola: klucz, drzwi, monety i niespodzianka.",
      rzeczy: [
        { karta: "POWTÓRZ", nazwa: "POWTÓRZ … KONIEC", tekst: "Karty między POWTÓRZ a KONIEC robot robi kilka razy. Liczba mówi, ile razy.",
          przyklad: { id: "powtorz", tytul: "Schodki", wynik: "Jeden schodek to 4 karty. POWTÓRZ ×4 robi cztery schodki.", karty: K2,
            plansza: [". . . . *", ". . . . .", ". . . . .", ". . . . .", "^ . . . ."],
            program: [["POWTÓRZ", 4], ["IDŹ", 1], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1], ["SKRĘĆ W LEWO", 1], ["KONIEC", 1]] } },
        { karta: "JEŚLI", nazwa: "JEŚLI … NIE … KONIEC", tekst: "Robot pyta, co jest przed nim. TAK: robi karty zaraz po pytaniu. NIE: robi karty po karcie NIE.",
          przyklad: { id: "jesli", tytul: "Kałuża czy nie?", wynik: "Raz jest kałuża i robot skacze. Raz jej nie ma i robot idzie.", karty: K2,
            pytania: ["KAŁUŻA?", "LAWA?", "SKARB?"], warianty: ["K", "."],
            plansza: [". * .", ". ? .", ". ^ ."],
            program: [["JEŚLI", "KAŁUŻA?"], ["SKOCZ", 1], ["NIE", 1], ["IDŹ", 2], ["KONIEC", 1]] } },
        { karta: "ZRÓB A", nazwa: "Przepis A i ZRÓB A", tekst: "W górnym rzędzie ułóż przepis A. Karta ZRÓB A w programie znaczy: zrób cały przepis. ZRÓB A ×3 robi go trzy razy.",
          przyklad: { id: "przepis", tytul: "Trzy rogi", wynik: "Przepis: dwa kroki i skręt. Trzy razy przepis to trzy skarby.", karty: K2,
            plansza: ["* . *", ". . .", "^ . *"],
            przepis: [["IDŹ", 2], ["SKRĘĆ W PRAWO", 1]], program: [["ZRÓB A", 3]] } },
        { pole: "@", nazwa: "Klucz i drzwi", tekst: "Wejdź na klucz, żeby go wziąć. Z kluczem drzwi się otworzą. Jeden klucz otwiera jedne drzwi.",
          przyklad: { id: "klucz", tytul: "Klucz do drzwi", wynik: "Robot bierze klucz, otwiera drzwi i ma skarb.", karty: R,
            plansza: [". * . .", ". D . .", ". @ . .", ". ^ . ."], program: [["IDŹ", 3]] } },
        { pole: "3", nazwa: "Monety", tekst: "Wejdź na monetę, żeby ją zebrać. Dodaj liczby. Suma musi być dokładnie taka, jak w zadaniu.",
          przyklad: { id: "monety", tytul: "Razem 5", wynik: "2 + 3 = 5. Dokładnie tyle trzeba!", karty: R, suma: 5,
            plansza: [". 3 .", ". 2 .", ". ^ ."], program: [["IDŹ", 2]] } },
        { pole: "?", nazwa: "Niespodzianka", tekst: "Pole ? przy każdej próbie może być inne. Program musi zadziałać za każdym razem. Pomaga karta JEŚLI." },
        { limit: true, nazwa: "Limit kart", tekst: "„Karty: 4 z 6” znaczy: masz najwyżej 6 kart. Za mało? Pomoże POWTÓRZ albo przepis." }
      ]
    },
    {
      poziom: 3,
      dla: "dla 8-latka",
      wstep: "Pętla w pętli i nowa pętla DOPÓKI. Działa też wszystko z poziomów 1 i 2.",
      rzeczy: [
        { karta: "POWTÓRZ", nazwa: "Pętla w pętli", tekst: "W POWTÓRZ można włożyć drugie POWTÓRZ. Mała pętla robi się cała przy każdym obrocie dużej.",
          przyklad: { id: "petla2", tytul: "Górka", wynik: "Mała pętla robi dwa schodki. Duża pętla: w górę, skręt, w dół.", karty: K3,
            plansza: [". . . . .", ". . . . .", ". . * . .", ". . . . .", "^ . . . *"],
            program: [["POWTÓRZ", 2], ["POWTÓRZ", 2], ["IDŹ", 1], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1], ["SKRĘĆ W LEWO", 1], ["KONIEC", 1], ["SKRĘĆ W PRAWO", 1], ["KONIEC", 1]] } },
        { karta: "DOPÓKI", nazwa: "DOPÓKI … KONIEC", tekst: "Robot powtarza karty tak długo, jak odpowiedź na pytanie brzmi TAK. Gdy NIE, idzie dalej za KONIEC. Nie trzeba liczyć kroków.",
          przyklad: { id: "dopoki", tytul: "Aż do ściany", wynik: "Robot idzie, dopóki przed nim jest wolne. Skarb raz jest bliżej, raz dalej.", karty: K3,
            pytania: ["WOLNE?", "NIE ŚCIANA?", "NIE SKARB?", "KAŁUŻA?"], warianty: ["*.", ".*"],
            plansza: [". . ? . .", ". . . . .", ". . ? . .", ". . . . .", ". . ^ . ."],
            program: [["DOPÓKI", "WOLNE?"], ["IDŹ", 1], ["KONIEC", 1]] } },
        { karta: "JEŚLI", nazwa: "JEŚLI w pętli", tekst: "W pętli robot może pytać przy każdym kroku: kałuża? To SKOCZ. Nie? To IDŹ.",
          przyklad: { id: "jesli-petla", tytul: "Kałuża po drodze", wynik: "Przy kałuży robot skacze, a dalej idzie. Przed skarbem pętla się kończy.", karty: K3,
            pytania: ["NIE SKARB?", "KAŁUŻA?", "WOLNE?"],
            plansza: [". . * . .", ". . . . .", ". . . . .", ". . K . .", ". . ^ . ."],
            program: [["DOPÓKI", "NIE SKARB?"], ["JEŚLI", "KAŁUŻA?"], ["SKOCZ", 1], ["NIE", 1], ["IDŹ", 1], ["KONIEC", 1], ["KONIEC", 1], ["IDŹ", 1]] } }
      ],
      pytania: [
        { q: "WOLNE?", tekst: "Czy na polu przed robotem można stanąć? Nie ma tam lawy, kałuży, klocka, drzwi ani końca planszy." },
        { q: "ŚCIANA?", tekst: "Czy przed robotem kończy się plansza?" },
        { q: "SKARB?", tekst: "Czy przed robotem jest skarb? Tak samo LAWA? i KAŁUŻA?." },
        { q: "NIE ŚCIANA?", tekst: "Słowo NIE odwraca odpowiedź. NIE ŚCIANA? to TAK, gdy przed robotem plansza się nie kończy." }
      ]
    },
    {
      poziom: 4,
      dla: "dla 12-latka",
      wstep: "Zmienna N: robot pamięta jedną liczbę i może ją zmieniać. Licznik N widać nad planszą.",
      rzeczy: [
        { karta: "N =", nazwa: "USTAW N", tekst: "Robot zapamiętuje liczbę. USTAW N 3 znaczy: od teraz N = 3. Na starcie N = 0." },
        { karta: "N +", nazwa: "N + i N −", karty: ["N +", "N −"], tekst: "N + 1 dodaje 1 do N. N − 2 odejmuje 2 od N." },
        { liczba: "N", nazwa: "N w okienku", tekst: "Zamiast liczby w okienku karty połóż N. IDŹ ×N idzie tyle pól, ile teraz wynosi N. Działa też POWTÓRZ ×N.",
          przyklad: { id: "spirala", tytul: "Spirala", wynik: "Za każdym razem N rośnie o 1, więc robot idzie 1, 2, 3, a potem 4 pola.", karty: K4,
            plansza: [". . . . .", ". . . . *", ". . ^ . .", ". . . . .", "* . . . *"],
            program: [["N =", 1], ["POWTÓRZ", 4], ["IDŹ", "N"], ["SKRĘĆ W PRAWO", 1], ["N +", 1], ["KONIEC", 1]] } },
        { pytanie: "N > 0?", nazwa: "Pytania o N", tekst: "N > 0? pyta, czy N jest większe od zera. N = 0? pyta, czy N jest zerem. Tak liczy się w dół.",
          przyklad: { id: "odliczanie", tytul: "Odliczanie", wynik: "N = 3, 2, 1, 0. Przy zerze pętla się kończy: robot zrobił 3 kroki.", karty: K4,
            pytania: ["N > 0?", "N = 0?", "WOLNE?"],
            plansza: [". * . .", ". . . .", ". . . .", ". ^ . ."],
            program: [["N =", 3], ["DOPÓKI", "N > 0?"], ["IDŹ", 1], ["N −", 1], ["KONIEC", 1]] } }
      ]
    },
    {
      poziom: 5,
      dla: "dla początkującego programisty",
      wstep: "Pytania złożone ze słów NIE, I, LUB oraz czujniki z boku robota. Labirynty z polami ? za każdym razem są inne, więc wygrywa ogólny algorytm.",
      rzeczy: [
        { pytanie: "NIE SKARB?", nazwa: "NIE", tekst: "NIE odwraca odpowiedź: TAK zmienia się w NIE, a NIE w TAK. DOPÓKI NIE SKARB? znaczy: idź, aż zobaczysz skarb.",
          przyklad: { id: "nie", tytul: "Gdzie jest skarb?", wynik: "Skarb stoi za każdym razem gdzie indziej, a program jest jeden.", karty: K3,
            pytania: ["NIE SKARB?", "SKARB?", "WOLNE?"], warianty: ["*..", ".*.", "..*"],
            plansza: [". . ? . .", ". . ? . .", ". . ? . .", ". . . . .", ". . ^ . ."],
            program: [["DOPÓKI", "NIE SKARB?"], ["IDŹ", 1], ["KONIEC", 1], ["IDŹ", 1]] } },
        { pytanie: "WOLNE W LEWO?", nazwa: "Czujniki z boku", tekst: "WOLNE W LEWO? i WOLNE W PRAWO? pytają o pole obok robota, a nie przed nim. Robot się przy tym nie obraca." },
        { pytanie: "NIE WOLNE? I WOLNE W LEWO?", nazwa: "I", tekst: "X I Y to TAK tylko wtedy, gdy oba są TAK. Tu: przed robotem zamknięte I w lewo wolne, więc trzeba skręcić w lewo.",
          przyklad: { id: "i", tytul: "Zakręt", wynik: "Robot idzie prosto. Gdy przed nim koniec, a w lewo wolne, skręca.", karty: K3,
            pytania: ["NIE SKARB?", "NIE WOLNE? I WOLNE W LEWO?", "WOLNE?", "WOLNE W LEWO?"],
            plansza: ["* . . .", "L L L .", "L L L .", "L L L ^"],
            program: [["DOPÓKI", "NIE SKARB?"], ["JEŚLI", "NIE WOLNE? I WOLNE W LEWO?"], ["SKRĘĆ W LEWO", 1], ["NIE", 1], ["IDŹ", 1], ["KONIEC", 1], ["KONIEC", 1], ["IDŹ", 1]] } },
        { pytanie: "LAWA? LUB KLOCEK?", nazwa: "LUB", tekst: "X LUB Y to TAK, gdy choć jedno jest TAK. Jedno pytanie łapie i lawę, i klocek.",
          przyklad: { id: "lub", tytul: "Lawa, klocek albo nic", wynik: "Lawa albo klocek: robot obchodzi. Pusto: idzie prosto.", karty: K3,
            pytania: ["LAWA? LUB KLOCEK?", "LAWA?", "KLOCEK?", "WOLNE?"], warianty: ["L", "#", "."],
            plansza: [". * .", "? . .", "^ . ."],
            program: [["JEŚLI", "LAWA? LUB KLOCEK?"], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1], ["SKRĘĆ W LEWO", 1], ["IDŹ", 2], ["NIE", 1], ["IDŹ", 2], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1], ["KONIEC", 1]] } }
      ]
    },
    {
      poziom: 6,
      dla: "dla średniego programisty",
      wstep: "Przepis z parametrem: liczba na karcie ZRÓB A trafia do przepisu jako N.",
      rzeczy: [
        { karta: "ZRÓB A", nazwa: "ZRÓB A z parametrem", tekst: "ZRÓB A N=4 robi przepis A jeden raz, a w środku przepisu N = 4. Po przepisie N wraca do tego, co było przed nim. ZRÓB A ×N przekazuje bieżące N.",
          przyklad: { id: "parametr", tytul: "Długie i krótkie", wynik: "Ten sam przepis raz idzie 4 pola, raz 2 pola.", karty: K6, parametr: true,
            plansza: ["* . . . *", ". . . . .", ". . . . *", ". . . . .", "^ . . . ."],
            przepis: [["IDŹ", "N"], ["SKRĘĆ W PRAWO", 1]], program: [["ZRÓB A", 4], ["ZRÓB A", 4], ["ZRÓB A", 2]] } },
        { pytanie: "N > 0?", nazwa: "Pętla z licznikiem", tekst: "USTAW N, potem DOPÓKI N > 0? i w środku N − 1. Pętla zrobi się tyle razy, ile było N. To samo daje POWTÓRZ ×N." }
      ]
    },
    {
      poziom: 7,
      dla: "trudny",
      wstep: "Rekurencja: przepis woła sam siebie. Do tego META i ogólne algorytmy z limitem kart.",
      rzeczy: [
        { karta: "ZRÓB A", nazwa: "Rekurencja", tekst: "Na tym poziomie kartę ZRÓB A można położyć w samym przepisie A. Wtedy przepis zaczyna się od nowa, a potem wraca i kończy to, co zostało. Potrzebne jest pytanie, które zatrzyma wołanie.",
          przyklad: { id: "rekurencja", tytul: "Tam i z powrotem", wynik: "Każde IDŹ za ZRÓB A czeka na powrót. Robot idzie do ściany, odwraca się i wraca na START.", karty: K7,
            rekurencja: true, wymagaj: "rekurencja", powrot: true, pytania: ["WOLNE?", "NIE WOLNE?", "SKARB?"],
            plansza: [". . . . .", ". . . . .", "> . . . *", ". . . . .", ". . . . ."],
            przepis: [["JEŚLI", "WOLNE?"], ["IDŹ", 1], ["ZRÓB A", 1], ["IDŹ", 1], ["NIE", 1], ["OBRÓĆ SIĘ", 1], ["KONIEC", 1]], program: [["ZRÓB A", 1]] } },
        { karta: "META", tekst: "META w przepisie kończy przepis od razu i wraca tam, skąd go zawołano. META w programie kończy cały program.",
          przyklad: { id: "meta", tytul: "Stop przy skarbie", wynik: "Przepis woła sam siebie krok po kroku. Przy skarbie: IDŹ i META, koniec.", karty: K7,
            rekurencja: true, pytania: ["SKARB?", "NIE SKARB?", "WOLNE?"], warianty: ["*..", ".*.", "..*"],
            plansza: [". . ? . .", ". . ? . .", ". . ? . .", ". . . . .", ". . ^ . ."],
            przepis: [["JEŚLI", "SKARB?"], ["IDŹ", 1], ["META", 1], ["NIE", 1], ["KONIEC", 1], ["IDŹ", 1], ["ZRÓB A", 1]], program: [["ZRÓB A", 1]] } }
      ]
    }
  ];
})();
