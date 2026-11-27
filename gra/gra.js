// Robot i Programista - wersja online (poziomy 1-7). Dane gier: gra/gry.js (window.GRY).
// Poziom 2: pętla POWTÓRZ…KONIEC, klucze (@) i drzwi (D), monety 1-6 z sumą, limit kart,
// pytanie JEŚLI…NIE…KONIEC z polami ? (warianty planszy) i przepis A z kartą ZRÓB A.
// Poziom 3+: DOPÓKI…KONIEC, zmienna N (N =, N +, N −, liczba N w okienku), pytania złożone
// (NIE, I, LUB, czujniki w lewo i w prawo), przepis z parametrem, rekurencja i META.
// Ta sama logika jest w narzedzia/symulator.py (sprawdzanie rozwiązań).
(function () {
  "use strict";
  var GRY = window.GRY || [];
  var KOLOR = {
    "IDŹ": "#2e9e4f", "SKRĘĆ W PRAWO": "#f08a1c", "SKRĘĆ W LEWO": "#2b6fd6", "OBRÓĆ SIĘ": "#8a4fd1", "SKOCZ": "#0c8599",
    "POWTÓRZ": "#d6336c", "KONIEC": "#495057", "JEŚLI": "#b08900", "NIE": "#e03131", "ZRÓB A": "#364fc7",
    "DOPÓKI": "#0b7285", "N =": "#6741d9", "N +": "#6741d9", "N −": "#6741d9", "META": "#1d2a36"
  };
  var NAPIS = {
    "IDŹ": ["IDŹ"], "SKRĘĆ W PRAWO": ["SKRĘĆ", "W PRAWO"], "SKRĘĆ W LEWO": ["SKRĘĆ", "W LEWO"], "OBRÓĆ SIĘ": ["OBRÓĆ", "SIĘ"], "SKOCZ": ["SKOCZ"],
    "POWTÓRZ": ["POWTÓRZ"], "JEŚLI": ["JEŚLI"], "ZRÓB A": ["ZRÓB A"],
    "DOPÓKI": ["DOPÓKI"], "N =": ["USTAW N"], "N +": ["N +"], "N −": ["N −"], "META": ["META"]
  };
  var IKONA = {
    "IDŹ": '<path d="M50 8 L84 46 L61 46 L61 92 L39 92 L39 46 L16 46 Z" fill="currentColor"/>',
    "SKRĘĆ W PRAWO": '<path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/><path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/>',
    "SKRĘĆ W LEWO": '<g transform="translate(100,0) scale(-1,1)"><path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/><path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/></g>',
    "OBRÓĆ SIĘ": '<path d="M70 92 L70 42 Q70 14 47 14 Q24 14 24 42 L24 56" stroke="currentColor" stroke-width="16" fill="none"/><path d="M6 54 L42 54 L24 86 Z" fill="currentColor"/>',
    "SKOCZ": '<circle cx="45" cy="84" r="9" fill="currentColor" opacity=".35"/><path d="M10 88 C 16 16, 72 8, 80 64" stroke="currentColor" stroke-width="13" fill="none"/><polygon points="64,60 96,60 80,94" fill="currentColor"/>',
    "POWTÓRZ": '<path d="M80 52 A30 30 0 1 1 66 26" stroke="currentColor" stroke-width="13" fill="none"/><path d="M52 6 L84 26 L54 44 Z" fill="currentColor"/>',
    "KONIEC": '<path d="M28 12 L68 12 L68 88 L28 88" stroke="currentColor" stroke-width="14" fill="none" stroke-linejoin="round"/>',
    "JEŚLI": '<text x="50" y="84" text-anchor="middle" font-size="96" font-weight="800" font-family="Arial,sans-serif" fill="currentColor">?</text>',
    "NIE": '<circle cx="50" cy="50" r="44" fill="currentColor"/><path d="M32 32 L68 68 M68 32 L32 68" stroke="#fff" stroke-width="13" stroke-linecap="round"/>',
    "TAK": '<circle cx="50" cy="50" r="44" fill="currentColor"/><path d="M26 52 L44 70 L76 32" stroke="#fff" stroke-width="13" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "ZRÓB A": '<rect x="18" y="6" width="64" height="88" rx="9" fill="none" stroke="currentColor" stroke-width="9"/><polygon points="38,28 72,50 38,72" fill="currentColor"/>',
    "DOPÓKI": '<path d="M80 52 A30 30 0 1 1 66 26" stroke="currentColor" stroke-width="13" fill="none"/><path d="M52 6 L84 26 L54 44 Z" fill="currentColor"/><text x="50" y="66" text-anchor="middle" font-size="40" font-weight="800" font-family="Arial,sans-serif" fill="currentColor">?</text>',
    "N =": '<rect x="10" y="14" width="80" height="72" rx="14" fill="none" stroke="currentColor" stroke-width="9"/><text x="50" y="70" text-anchor="middle" font-size="54" font-weight="800" font-family="Arial,sans-serif" fill="currentColor">N</text>',
    "N +": '<text x="34" y="70" text-anchor="middle" font-size="56" font-weight="800" font-family="Arial,sans-serif" fill="currentColor">N</text><path d="M66 34 V72 M47 53 H85" stroke="currentColor" stroke-width="11"/>',
    "N −": '<text x="34" y="70" text-anchor="middle" font-size="56" font-weight="800" font-family="Arial,sans-serif" fill="currentColor">N</text><path d="M47 53 H85" stroke="currentColor" stroke-width="11"/>',
    "META": '<path d="M22 92 V10" stroke="currentColor" stroke-width="9"/><path d="M26 12 H84 V52 H26 Z" fill="currentColor"/><path d="M26 12 H45 V32 H26 Z M45 32 H64 V52 H45 Z M64 12 H84 V32 H64 Z" fill="#fff"/>'
  };
  var RUCH = ["IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ"];
  var PYTANIE = { "LAWA?": "L", "KAŁUŻA?": "K", "SKARB?": "*", "ŚCIANA?": "SCIANA" };
  var PYT_SLOWO = { "LAWA?": "lawa", "KAŁUŻA?": "kałuża", "SKARB?": "skarb", "ŚCIANA?": "ściana" };
  var SLOWO = { 1: "raz", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć" };
  var KIER = "^>v<";
  var DXY = { "^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1] };
  var S = 20, O = 4; // rozmiar pola w SVG i margines
  var MAX = 30, MAX_KROKOW = 600;
  var OTWIERA = { "POWTÓRZ": 1, "JEŚLI": 1, "DOPÓKI": 1 };
  var ZMIENNA = { "N =": 1, "N +": 1, "N −": 1 };
  var NIE_WOLNO = { "L": 1, "K": 1, "#": 1, "SCIANA": 1, "D": 1 };
  var OPIS_POZIOMU = {
    1: "Karty IDŹ, SKRĘĆ, OBRÓĆ SIĘ i SKOCZ. Liczba mówi, ile razy.",
    2: "Nowe karty i pola: pętla POWTÓRZ, klucz i drzwi, monety do liczenia, pytanie JEŚLI i przepis A. W każdym zestawie gry idą od najłatwiejszej.",
    3: "Dla 8-latka: pętla w pętli i nowa pętla DOPÓKI, która kręci się tak długo, jak odpowiedź brzmi TAK.",
    4: "Dla 12-latka: zmienna N. Robot pamięta liczbę N, może ją zmieniać i używać w okienku karty (IDŹ ×N).",
    5: "Dla początkującego programisty: pytania złożone (NIE, I, LUB), czujniki w lewo i w prawo oraz labirynty, które za każdym razem są inne.",
    6: "Dla średniego programisty: przepis z parametrem (ZRÓB A ×3 daje N = 3 w przepisie) i pętle z licznikiem.",
    7: "Trudny: rekurencja (przepis woła sam siebie), META i ogólne algorytmy z limitem kart."
  };

  var $ = function (id) { return document.getElementById(id); };
  var stan = {
    przebieg: 0, odpowiedz: null, gra: null, biegnie: false, robot: null, rozmiar: 5, poziom: 1, N: 0,
    obszary: { program: [], przepis: [] }, obszar: "program", wybrana: { program: -1, przepis: -1 }, nowyId: 1
  };

  // ---------- pamięć w przeglądarce (gwiazdki i wybrany poziom) ----------
  function wczytajGw() { try { return JSON.parse(localStorage.getItem("rip-gwiazdki") || "[]"); } catch (e) { return []; } }
  function zapiszGw(id) {
    var g = wczytajGw(); if (g.indexOf(id) < 0) g.push(id);
    try { localStorage.setItem("rip-gwiazdki", JSON.stringify(g)); } catch (e) { /* bez zapisu */ }
  }
  // ---------- rozmiary plansz (11 × 11 i 13 × 13 tylko na komputerze: szeroki ekran i mysz) ----------
  var ROZMIARY = [5, 7, 9, 11, 13], DUZE = [11, 13];
  var KOMPUTER = window.matchMedia ? window.matchMedia("(min-width: 900px) and (pointer: fine)") : { matches: true };
  function dozwolony(r) { return DUZE.indexOf(r) < 0 || KOMPUTER.matches; }
  function maGry(r) { return GRY.some(function (g) { return g.size === r && g.poziom === stan.poziom; }); }
  function zapiszWybor() { try { localStorage.setItem("rip-wybor", JSON.stringify({ p: stan.poziom, r: stan.rozmiar })); } catch (e) { /* bez zapisu */ } }
  function wczytajWybor() {
    try { var w = JSON.parse(localStorage.getItem("rip-wybor") || "null"); if (w) { stan.poziom = poziomy().indexOf(w.p) >= 0 ? w.p : 1; stan.rozmiar = ROZMIARY.indexOf(w.r) >= 0 ? w.r : 5; } } catch (e) { /* domyślnie */ }
  }

  // ---------- mowa ----------
  // Zwraca obietnicę, która kończy się, gdy robot skończy mówić (albo od razu, gdy mowa jest wyłączona).
  function powiedz(t) {
    return new Promise(function (gotowe) {
      if (!$("glos").checked || !window.speechSynthesis) { gotowe(); return; }
      var koniec = false;
      function zakoncz() { if (!koniec) { koniec = true; gotowe(); } }
      try {
        var u = new SpeechSynthesisUtterance(t.toLowerCase());
        u.lang = "pl-PL"; u.rate = 0.9;
        u.onend = zakoncz; u.onerror = zakoncz;
        window.speechSynthesis.cancel(); window.speechSynthesis.speak(u);
        setTimeout(zakoncz, 1500 + 130 * t.length);
      } catch (e) { zakoncz(); }
    });
  }
  function slowoLiczby(n) { return n === "N" ? "N" : (SLOWO[n] || String(n)); }
  function tekstPytania(q) {
    return q.toLowerCase().replace(/\?/g, "").replace(/ > /g, " większe od ").replace(/ = /g, " równe ").replace(/ 0/g, " zero");
  }
  function tekstKarty(c) {
    if (c.k === "POWTÓRZ") return "powtórz " + slowoLiczby(c.n) + (c.n !== 1 ? " razy" : "");
    if (c.k === "JEŚLI") return "jeśli " + (PYT_SLOWO[c.q] || tekstPytania(c.q));
    if (c.k === "DOPÓKI") return "dopóki " + (PYT_SLOWO[c.q] || tekstPytania(c.q));
    if (c.k === "N =") return "N równa się " + c.n;
    if (c.k === "N +") return "N plus " + c.n;
    if (c.k === "N −") return "N minus " + c.n;
    if (c.k === "META") return "meta";
    if (c.k === "ZRÓB A" && maParametr()) return "zrób przepis A, N równa się " + slowoLiczby(c.n);
    if (c.k === "ZRÓB A") return "zrób przepis A" + (c.n !== 1 ? " " + slowoLiczby(c.n) + " razy" : "");
    if (c.k === "NIE" || c.k === "KONIEC") return c.k;
    return c.k + (c.n !== 1 ? " " + slowoLiczby(c.n) + " razy" : "");
  }

  // ---------- rysowanie ----------
  function ikona(nazwa) { return '<svg viewBox="0 0 100 100" aria-hidden="true">' + IKONA[nazwa] + "</svg>"; }
  function gwiazda(cx, cy, r) {
    var p = [];
    for (var i = 0; i < 10; i++) {
      var rr = i % 2 === 0 ? r : r * 0.45;
      p.push((cx + rr * Math.sin(i * Math.PI / 5)).toFixed(1) + "," + (cy - rr * Math.cos(i * Math.PI / 5)).toFixed(1));
    }
    return '<polygon fill="#f5c400" stroke="#b88f00" stroke-width="1.2" points="' + p.join(" ") + '"/>';
  }
  function fale(x, y, kolor) {
    return '<path d="M' + (x + 3) + " " + (y + 7) + ' q3.5 -3 7 0 t7 0" stroke="' + kolor + '" stroke-width="1.6" fill="none"/>' +
           '<path d="M' + (x + 3) + " " + (y + 14) + ' q3.5 -3 7 0 t7 0" stroke="' + kolor + '" stroke-width="1.6" fill="none"/>';
  }
  function klucz(px, py) {
    return '<g transform="translate(' + px + "," + py + ')"><circle cx="6.5" cy="10" r="3.6" fill="none" stroke="#c99700" stroke-width="2.2"/>' +
      '<path d="M10 10 H17 M14.5 10 V13.5 M17 10 V13" stroke="#c99700" stroke-width="2.2" stroke-linecap="round" fill="none"/></g>';
  }
  // jedno pole planszy (px, py = lewy górny róg)
  function rysujPole(t, px, py) {
    if (t === "L") return '<rect x="' + (px + 1) + '" y="' + (py + 1) + '" width="' + (S - 2) + '" height="' + (S - 2) + '" rx="2" fill="#e03131"/>' + fale(px, py, "#ffa94d");
    if (t === "K") return '<rect x="' + (px + 1) + '" y="' + (py + 1) + '" width="' + (S - 2) + '" height="' + (S - 2) + '" rx="5" fill="#a5d8ff"/>' + fale(px, py, "#1c7ed6");
    if (t === "#") return '<rect x="' + (px + 2) + '" y="' + (py + 2) + '" width="' + (S - 4) + '" height="' + (S - 4) + '" rx="3" fill="#a0522d"/><circle cx="' + (px + 7) + '" cy="' + (py + 7) + '" r="2" fill="#c97a4a"/><circle cx="' + (px + 13) + '" cy="' + (py + 7) + '" r="2" fill="#c97a4a"/>';
    if (t === "*") return gwiazda(px + S / 2, py + S / 2, 8);
    if (t === "@") return klucz(px, py);
    if (t === "D") return '<rect x="' + (px + 3) + '" y="' + (py + 1.5) + '" width="' + (S - 6) + '" height="' + (S - 3) + '" rx="2" fill="#8d5524" stroke="#5c3613" stroke-width="1"/>' +
      '<circle cx="' + (px + 10) + '" cy="' + (py + 9) + '" r="1.9" fill="#ffd43b"/><path d="M' + (px + 10) + " " + (py + 10) + ' v3.5" stroke="#ffd43b" stroke-width="1.6"/>';
    if (t === "o") return '<rect x="' + (px + 3) + '" y="' + (py + 1.5) + '" width="' + (S - 6) + '" height="' + (S - 3) + '" rx="2" fill="none" stroke="#8d5524" stroke-width="1" stroke-dasharray="2 1.5"/>';
    if (t === "?") return '<rect x="' + (px + 1.5) + '" y="' + (py + 1.5) + '" width="' + (S - 3) + '" height="' + (S - 3) + '" rx="4" fill="#e5dbff" stroke="#7048e8" stroke-width="1"/>' +
      '<text x="' + (px + S / 2) + '" y="' + (py + 15) + '" text-anchor="middle" font-size="14" font-weight="800" font-family="Arial,sans-serif" fill="#7048e8">?</text>';
    if (/^[1-9]$/.test(t)) return '<circle cx="' + (px + S / 2) + '" cy="' + (py + S / 2) + '" r="8.2" fill="#ffd43b" stroke="#e8a400" stroke-width="1.3"/>' +
      '<text x="' + (px + S / 2) + '" y="' + (py + 14.2) + '" text-anchor="middle" font-size="11.5" font-weight="800" font-family="Arial,sans-serif" fill="#5c3d00">' + t + "</text>";
    return "";
  }
  // rows: aktualne pola (tablica tablic), zebrane: {"y-x": true} dla zebranych skarbów
  function rysujPlansze(svg, rows, zRobotem, zebrane) {
    var n = rows.length, w = n * S + 2 * O;
    var h = ['<rect x="0" y="0" width="' + w + '" height="' + w + '" rx="6" fill="#e9dcc6"/>'];
    for (var i = 0; i < n; i++) for (var j = 0; j < n; j++) if ((i + j) % 2) h.push('<rect x="' + (O + j * S) + '" y="' + (O + i * S) + '" width="' + S + '" height="' + S + '" fill="#e2d3b9"/>');
    var start = null;
    rows.forEach(function (r, y) {
      r.forEach(function (t, x) {
        if (KIER.indexOf(t) >= 0) { start = { y: y, x: x, d: t }; return; }
        var zb = t === "*" && zebrane && zebrane[y + "-" + x];
        h.push('<g id="' + (zRobotem ? "p-" + y + "-" + x : "") + '"' + (zb ? ' class="zebrany"' : "") + ">" + rysujPole(t, O + x * S, O + y * S) + "</g>");
      });
    });
    // taśma malarska
    for (var k = 0; k <= n; k++) {
      h.push('<rect x="' + (O + k * S - 0.9) + '" y="' + (O - 0.9) + '" width="1.8" height="' + (n * S + 1.8) + '" fill="#f7e7a8" stroke="#d9c477" stroke-width=".3"/>');
      h.push('<rect x="' + (O - 0.9) + '" y="' + (O + k * S - 0.9) + '" width="' + (n * S + 1.8) + '" height="1.8" fill="#f7e7a8" stroke="#d9c477" stroke-width=".3"/>');
    }
    if (start) {
      h.push('<circle cx="' + (O + start.x * S + S / 2) + '" cy="' + (O + start.y * S + S / 2) + '" r="8.6" fill="none" stroke="#2b6fd6" stroke-width="1" stroke-dasharray="2 1.6"/>');
      if (zRobotem) h.push('<g id="robot"><circle r="7.6" fill="#2b6fd6"/><polygon points="0,-5.7 3.8,2.7 -3.8,2.7" fill="#fff"/></g>');
      else h.push('<g transform="translate(' + (O + start.x * S + S / 2) + "," + (O + start.y * S + S / 2) + ') rotate(' + KIER.indexOf(start.d) * 90 + ')"><circle r="7.6" fill="#2b6fd6"/><polygon points="0,-5.7 3.8,2.7 -3.8,2.7" fill="#fff"/></g>');
    }
    svg.setAttribute("viewBox", "0 0 " + w + " " + w);
    svg.innerHTML = h.join("");
    return { start: start, n: n };
  }
  function ustawRobota(skok) {
    var r = stan.robot, g = $("robot");
    if (!g) return;
    g.classList.toggle("skok", !!skok);
    g.style.transform = "translate(" + (O + r.x * S + S / 2) + "px," + (O + r.y * S + S / 2) + "px) rotate(" + r.kat + "deg)" + (skok ? " scale(1.25)" : "");
    if (skok) setTimeout(function () { g.style.transform = g.style.transform.replace(" scale(1.25)", ""); }, 260);
  }
  function robotBezAnimacji() {
    var g = $("robot"); if (!g) return;
    g.style.transition = "none"; ustawRobota(false);
    g.getBoundingClientRect(); g.style.transition = "";
  }
  function odswiezPole(y, x) {
    var g = document.getElementById("p-" + y + "-" + x); if (!g) return;
    g.innerHTML = rysujPole(stan.pola[y][x], O + x * S, O + y * S);
    g.classList.toggle("zebrany", stan.pola[y][x] === "*" && !!stan.zebrane[y + "-" + x]);
  }
  function plansza(gra) { return gra.plansza.map(function (r) { return r.split(" "); }); }

  // ---------- lista gier ----------
  function rysujListe() {
    var gw = wczytajGw();
    if (DUZE.indexOf(stan.rozmiar) >= 0 && (!dozwolony(stan.rozmiar) || !maGry(stan.rozmiar))) stan.rozmiar = 5;
    var gry = GRY.filter(function (g) { return g.size === stan.rozmiar && g.poziom === stan.poziom; });
    var zest = {}, nazwy = {};
    gry.forEach(function (g) { (zest[g.zestaw] = zest[g.zestaw] || []).push(g); if (g.zestawNazwa) nazwy[g.zestaw] = g.zestawNazwa; });
    var html = "";
    Object.keys(zest).sort().forEach(function (z) {
      var tyt = nazwy[z] ? z + ". " + nazwy[z] : (z ? "Zestaw " + z : "");
      html += '<div class="zestaw">' + (tyt ? "<h3>" + tyt + "</h3>" : "") + '<div class="lista">';
      zest[z].forEach(function (g) {
        var done = gw.indexOf(g.id) >= 0;
        html += '<button class="kafel' + (done ? " done" : "") + '" data-id="' + g.id + '"><span class="nr">' + g.nr + '</span><span class="t">' + g.tytul + '</span><span class="s">' + (done ? "★ zrobione" : "") + "</span></button>";
      });
      html += "</div></div>";
    });
    $("lista").innerHTML = html;
    var wszystkie = gry.length, zrobione = gry.filter(function (g) { return gw.indexOf(g.id) >= 0; }).length;
    $("postep").textContent = "Gwiazdki: " + zrobione + " z " + wszystkie;
    ROZMIARY.forEach(function (r) {
      $("tab" + r).setAttribute("aria-selected", stan.rozmiar === r);
      if (DUZE.indexOf(r) >= 0) $("tab" + r).hidden = !dozwolony(r) || !maGry(r);
    });
    $("tylkoKomputer").hidden = KOMPUTER.matches || !DUZE.some(maGry);
    document.querySelectorAll(".tab[data-poziom]").forEach(function (b) { b.setAttribute("aria-selected", stan.poziom === +b.dataset.poziom); });
    $("opisPoziomu").textContent = OPIS_POZIOMU[stan.poziom] || "";
  }
  function poziomy() {
    var p = [];
    GRY.forEach(function (g) { if (p.indexOf(g.poziom) < 0) p.push(g.poziom); });
    return p.sort(function (a, b) { return a - b; });
  }

  // ---------- gra ----------
  function ma(karta) { return stan.gra && stan.gra.karty.indexOf(karta) >= 0; }
  function otworz(id) {
    var gra = GRY.filter(function (g) { return g.id === id; })[0];
    if (!gra) { pokazStart(); return; }
    if (!dozwolony(gra.size)) { stan.poziom = gra.poziom; location.hash = ""; pokazStart(); return; }
    otworzGre(gra);
    // powrót z przykładu w pomocy: program, który dziecko układało, wraca na miejsce
    var s = stan.schowek;
    if (s && s.id === gra.id) {
      stan.obszary = s.obszary; stan.wybrana = s.wybrana; stan.obszar = s.obszar; stan.schowek = null;
      rysujProgram(); naStart();
      if (s.pomoc) otworzPomoc(s.poziom);
    }
  }
  function otworzGre(gra) {
    przerwij();
    stan.gra = gra; stan.obszary = { program: [], przepis: [] }; stan.obszar = "program"; stan.wybrana = { program: -1, przepis: -1 };
    if (!gra.przyklad) { stan.poziom = gra.poziom; stan.rozmiar = gra.size; }
    $("ekranStart").hidden = true; $("ekranGra").hidden = false; $("doListy").hidden = false; document.body.classList.add("w-grze");
    stan.N = 0;
    $("graTytul").textContent = gra.przyklad ? "Przykład: " + gra.tytul : (gra.poziom > 1 ? "Poziom " + gra.poziom + ", gra " : "Gra ") + gra.nr + ": " + gra.tytul + " (" + gra.size + " × " + gra.size + ")";
    $("graOpis").textContent = gra.opis;
    $("rozw").hidden = true;
    stan.nieudane = 0; $("pokazRozw").hidden = true;
    var r = gra.rozwiazanie;
    $("rozw").innerHTML = (r.przepis ? '<div class="rz"><b>Przepis A:</b> ' + rysujKarty(r.przepis.map(tokenZDanych), "x") + "</div>" : "") +
      '<div class="rz">' + (r.przepis ? "<b>Program:</b> " : "") + rysujKarty(r.program.map(tokenZDanych), "x") + "</div>";
    $("bprzepis").hidden = !ma("ZRÓB A");
    rysujPaleteKart();
    naStart();
    rysujProgram();
    komunikat("", "");
    window.scrollTo(0, 0);
  }
  function tokenZDanych(c) {
    var t = { k: c[0], n: 1, id: stan.nowyId++ };
    if (c[0] === "JEŚLI" || c[0] === "DOPÓKI") t.q = c[1]; else t.n = c[1] === undefined ? 1 : c[1];
    return t;
  }
  function wariantPlanszy(w) {
    var rows = plansza(stan.gra), i = 0;
    if (w) rows.forEach(function (r) { r.forEach(function (t, x) { if (t === "?") r[x] = w[i++]; }); });
    return rows;
  }
  // robot na START, plansza bez zmian (pola ? jeszcze nieodkryte)
  function naStart(w) {
    stan.pola = wariantPlanszy(w);
    stan.zebrane = {}; stan.klucze = 0; stan.suma = 0; stan.kroki = 0; stan.N = 0; stan.glebokosc = 0;
    var info = rysujPlansze($("plansza"), stan.pola, true, stan.zebrane);
    stan.info = info;
    stan.robot = { y: info.start.y, x: info.start.x, d: info.start.d, kat: KIER.indexOf(info.start.d) * 90 };
    robotBezAnimacji();
    rysujLicznik();
  }
  function ileKart() { return stan.obszary.program.length + stan.obszary.przepis.length; }
  function rysujLicznik() {
    var g = stan.gra, h = [];
    if (!g) return;
    if (g.limit) h.push('<span class="' + (ileKart() > g.limit ? "zle" : "") + '">Karty: ' + ileKart() + " z " + g.limit + "</span>");
    if (g.plansza.some(function (r) { return r.indexOf("@") >= 0; })) h.push('<span><svg viewBox="0 0 20 20" aria-hidden="true">' + klucz(0, 0) + "</svg> " + stan.klucze + "</span>");
    if (g.suma) h.push("<span>Suma: " + stan.suma + " z " + g.suma + "</span>");
    if (ma("N =") || ma("N +") || g.parametr) h.push('<span class="zm">N = ' + stan.N + "</span>");
    $("licznik").innerHTML = h.join("");
    $("licznik").hidden = !h.length;
  }

  // ---------- karty w programie ----------
  // Dla kart POWTÓRZ / JEŚLI / NIE / KONIEC zwraca indeksy całej grupy: {start, nie, koniec}.
  function grupy(lista) {
    var stos = [], gr = {};
    lista.forEach(function (c, i) {
      if (OTWIERA[c.k]) { var g = { start: i, nie: -1, koniec: -1 }; stos.push(g); gr[i] = g; }
      else if (c.k === "NIE" && stos.length && lista[stos[stos.length - 1].start].k === "JEŚLI") { stos[stos.length - 1].nie = i; gr[i] = stos[stos.length - 1]; }
      else if (c.k === "KONIEC" && stos.length) { var t = stos.pop(); t.koniec = i; gr[i] = t; }
    });
    return gr;
  }
  function chip(c, obszar, wybrana) {
    var kolor = KOLOR[c.k], tresc;
    if (c.k === "JEŚLI" || c.k === "DOPÓKI") tresc = ikona(c.k) + "<span>" + c.k + "</span>" + pytanieIkona(c.q) + '<span class="q">' + c.q + "</span>";
    else if (ZMIENNA[c.k]) tresc = ikona(c.k) + "<span>" + c.k + '</span><b class="n">' + c.n + "</b>";
    else if (c.k === "META") tresc = ikona("META") + "<span>META</span>";
    else if (c.k === "ZRÓB A" && maParametr()) tresc = ikona(c.k) + "<span>ZRÓB A</span>" + '<b class="n">N=' + c.n + "</b>";
    else if (c.k === "NIE") tresc = ikona("NIE") + "<span>NIE</span>";
    else if (c.k === "KONIEC") tresc = ikona("KONIEC") + "<span>KONIEC</span>";
    else tresc = ikona(c.k) + "<span>" + c.k + "</span>" + (c.n !== 1 || c.k === "POWTÓRZ" ? '<b class="n">×' + c.n + "</b>" : "");
    var aktywny = obszar !== "x";
    return '<button class="chip' + (wybrana ? " wybrana" : "") + '" data-id="' + c.id + '"' + (aktywny ? ' data-a="' + obszar + '" aria-pressed="' + !!wybrana + '"' : ' tabindex="-1"') +
           ' style="color:' + kolor + '">' + tresc + "</button>";
  }
  // Pomoc rysuje przykłady z parametrem (poziom 6) także wtedy, gdy otwarta gra go nie ma.
  var parametrWidoku = null;
  function maParametr() { return parametrWidoku !== null ? parametrWidoku : !!(stan.gra && stan.gra.parametr); }
  function pytanieIkona(q) {
    var t = PYTANIE[q];
    if (q === "KLOCEK?") t = "#";
    if (q === "WOLNE?") return '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="1" y="1" width="18" height="18" rx="3" fill="#e9dcc6" stroke="#2e9e4f" stroke-width="1.4"/><path d="M10 15 V5 M6 9 L10 5 L14 9" stroke="#2e9e4f" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
    if (q === "WOLNE W LEWO?" || q === "WOLNE W PRAWO?") return '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="1" y="1" width="18" height="18" rx="3" fill="#e9dcc6" stroke="#2e9e4f" stroke-width="1.4"/><path d="' + (q === "WOLNE W LEWO?" ? "M15 10 H5 M9 6 L5 10 L9 14" : "M5 10 H15 M11 6 L15 10 L11 14") + '" stroke="#2e9e4f" stroke-width="2" fill="none" stroke-linecap="round"/></svg>';
    if (!t) return "";
    if (t === "SCIANA") return '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="1" y="1" width="18" height="18" rx="2" fill="#f1d3c3"/><path d="M1 7 H19 M1 13 H19 M7 1 V7 M13 7 V13 M7 13 V19" stroke="#c0603a" stroke-width="1.6"/></svg>';
    return '<svg viewBox="0 0 20 20" aria-hidden="true">' + rysujPole(t, 0, 0) + "</svg>";
  }
  // Karty jako rząd chipów; POWTÓRZ…KONIEC i JEŚLI…KONIEC w ramce. obszar "x" = tylko do oglądania.
  function rysujKarty(lista, obszar, w) {
    var kursor = '<span class="kursor" aria-hidden="true"></span>', html = "";
    lista.forEach(function (c, i) {
      var otw = !!OTWIERA[c.k];
      if (otw) html += '<span class="grupa" style="--c:' + KOLOR[c.k] + '">';
      html += chip(c, obszar, i === w);
      if (c.k === "JEŚLI" && i !== w) html += '<span class="tak" aria-hidden="true">' + ikona("TAK") + "TAK</span>";
      if (c.k === "KONIEC") html += "</span>";
      if (i === w && obszar !== "x") html += '<button class="usun" data-usun="' + i + '" data-a="' + obszar + '" aria-label="Usuń kartę ' + c.k + '">✕</button>' + (i < lista.length - 1 ? kursor : "");
    });
    return html;
  }
  function rysujObszar(obszar) {
    var p = stan.obszary[obszar], w = stan.wybrana[obszar], aktywny = stan.obszar === obszar;
    var kursor = '<span class="kursor" aria-hidden="true"></span>';
    var html = '<button class="poczatek' + (aktywny && w < 0 ? " wybrana" : "") + (obszar === "przepis" ? " pa" : "") + '" data-i="-1" data-a="' + obszar + '" aria-label="Wstaw na początek ' + (obszar === "przepis" ? "przepisu A" : "programu") + '">' + (obszar === "przepis" ? "A" : "▶") + "</button>" +
      (aktywny && w < 0 && p.length ? kursor : "");
    html += rysujKarty(p, obszar, aktywny ? w : -2);
    if (!p.length) html += '<span class="pusto">' + (obszar === "przepis" ? "Przepis A: dotknij tu, potem karty." : "Dotknij karty poniżej.") + "</span>";
    var el = $(obszar === "przepis" ? "przepis" : "program");
    el.innerHTML = html;
    el.closest(".box").classList.toggle("aktywny", aktywny && ma("ZRÓB A"));
    pokazWProgramie(el, el.querySelector(".wybrana"));
  }
  function rysujProgram() {
    rysujObszar("program");
    if (ma("ZRÓB A")) rysujObszar("przepis");
    rysujPanelLiczb();
    rysujLicznik();
  }
  // przewija pasek programu (na telefonie jest w jednym rzędzie) tak, żeby karta była widoczna
  function pokazWProgramie(box, el) {
    if (!el || box.scrollWidth <= box.clientWidth) return;
    var l = el.offsetLeft, r = l + el.offsetWidth + 44;
    if (l < box.scrollLeft) box.scrollLeft = l - 8;
    else if (r > box.scrollLeft + box.clientWidth) box.scrollLeft = r - box.clientWidth;
  }
  function wybrany() { var w = stan.wybrana[stan.obszar]; return w >= 0 ? stan.obszary[stan.obszar][w] : null; }
  function rysujPanelLiczb() {
    var c = wybrany(), pyt = c && (c.k === "JEŚLI" || c.k === "DOPÓKI");
    $("liczby").hidden = pyt; $("pytania").hidden = !pyt;
    $("tytulLiczb").textContent = pyt ? "O co pyta robot?" : (c && ZMIENNA[c.k] ? "Jaka liczba?" : "Ile razy?");
    var zN = stan.gra && (ma("N =") || ma("N +") || stan.gra.parametr);
    $("liczby").querySelectorAll(".liczba").forEach(function (b) {
      if (b.dataset.n === "0") b.hidden = !(stan.gra && ma("N ="));
      if (b.dataset.n === "N") b.hidden = !zN;
    });
    if (pyt) {
      $("pytania").innerHTML = (stan.gra.pytania || Object.keys(PYTANIE)).map(function (q) {
        return '<button class="pytanie' + (q === c.q ? " wyb" : "") + '" data-q="' + q + '">' + pytanieIkona(q) + "<span>" + q + "</span></button>";
      }).join("");
    }
  }
  function wybierz(obszar, i) {
    stan.obszar = obszar;
    stan.wybrana[obszar] = Math.max(-1, Math.min(i, stan.obszary[obszar].length - 1));
    rysujProgram();
  }
  function usun(obszar, i) {
    var p = stan.obszary[obszar], c = p[i];
    var g = grupy(p)[i], do_usuniecia = [i];
    if (g) do_usuniecia = [g.start, g.nie, g.koniec].filter(function (x) { return x >= 0; });
    do_usuniecia.sort(function (a, b) { return b - a; }).forEach(function (x) { p.splice(x, 1); });
    var nowa = do_usuniecia[do_usuniecia.length - 1] - 1;
    stan.obszar = obszar;
    stan.wybrana[obszar] = Math.min(nowa < 0 && p.length ? 0 : nowa, p.length - 1);
    if (c) powiedz("usuwam");
    rysujProgram(); naStart(); komunikat("", "");
  }
  function komunikat(t, typ) { var k = $("komunikat"); k.textContent = t; k.className = "komunikat " + (typ || ""); }

  function dodaj(nazwa) {
    if (stan.biegnie) return;
    var ob = stan.obszar, p = stan.obszary[ob];
    var nowe;
    if (nazwa === "ZRÓB A" && ob === "przepis" && !stan.gra.rekurencja) { komunikat("Kartę ZRÓB A kładziemy w programie, a nie w przepisie.", "zle"); return; }
    if (nazwa === "POWTÓRZ") nowe = [{ k: "POWTÓRZ", n: 2 }, { k: "KONIEC", n: 1 }];
    else if (nazwa === "JEŚLI") nowe = [{ k: "JEŚLI", n: 1, q: (stan.gra.pytania || ["LAWA?"])[0] }, { k: "NIE", n: 1 }, { k: "KONIEC", n: 1 }];
    else if (nazwa === "DOPÓKI") nowe = [{ k: "DOPÓKI", n: 1, q: (stan.gra.pytania || ["WOLNE?"])[0] }, { k: "KONIEC", n: 1 }];
    else if (nazwa === "N =") nowe = [{ k: "N =", n: 0 }];
    else nowe = [{ k: nazwa, n: 1 }];
    if (ileKart() + nowe.length > MAX) { komunikat("Program jest już bardzo długi.", "zle"); return; }
    if (stan.gra.limit && ileKart() + nowe.length > stan.gra.limit) {
      komunikat("Masz tylko " + stan.gra.limit + " " + slowoKarty(stan.gra.limit) + ". " + (ma("ZRÓB A") ? "Może przepis A pomoże?" : ma("DOPÓKI") ? "Może pomoże pętla?" : "Może pomoże POWTÓRZ?"), "zle"); return;
    }
    nowe.forEach(function (c) { c.id = stan.nowyId++; });
    var w = stan.wybrana[ob] + 1;
    Array.prototype.splice.apply(p, [w, 0].concat(nowe));
    stan.wybrana[ob] = w;
    powiedz(tekstKarty(nowe[0])); rysujProgram(); naStart(); komunikat("", "");
  }
  function liczba(n) {
    if (stan.biegnie) return;
    var p = stan.obszary[stan.obszar];
    if (!p.length) { komunikat("Najpierw wybierz kartę polecenia.", "zle"); return; }
    var c = wybrany();
    if (!c) { komunikat("Dotknij karty w programie, której chcesz zmienić liczbę.", "zle"); return; }
    if (c.k === "NIE" || c.k === "KONIEC" || c.k === "META") { komunikat("Karta " + c.k + " nie ma liczby.", "zle"); return; }
    if (c.k === "JEŚLI" || c.k === "DOPÓKI") return;
    if (n === 0 && c.k !== "N =") { komunikat("Zero pasuje tylko do karty USTAW N.", "zle"); return; }
    if (n === "N" && ZMIENNA[c.k]) { komunikat("Tu wybierz zwykłą liczbę.", "zle"); return; }
    c.n = n;
    powiedz(c.k === "POWTÓRZ" || ZMIENNA[c.k] || c.k === "ZRÓB A" ? tekstKarty(c) : slowoLiczby(n) + (n !== 1 ? " razy" : ""));
    rysujProgram(); naStart();
  }
  function pytanie(q) {
    var c = wybrany(); if (!c || (c.k !== "JEŚLI" && c.k !== "DOPÓKI") || stan.biegnie) return;
    c.q = q; powiedz(tekstKarty(c)); rysujProgram(); naStart();
  }

  // ---------- wykonanie programu ----------
  var tempo = 1; // 0 = bez animacji (do testów)
  function czekaj(ms) { return new Promise(function (r) { setTimeout(r, ms * tempo); }); }
  function pole(y, x) {
    var n = stan.info.n;
    if (y < 0 || x < 0 || y >= n || x >= n) return "SCIANA";
    return stan.pola[y][x];
  }
  var BLAD = { "L": "Auć! To lawa! Trzeba ją obejść.", "K": "Plusk! Kałużę trzeba przeskoczyć.", "#": "Bum! Tu stoi klocek.", "SCIANA": "Stop! Tu kończy się plansza." };
  function Blad(t) { this.tekst = t; }
  var PRZERWANE = {}, KONIEC_PRZEPISU = {};
  function ile(n) { return n === "N" ? stan.N : n; }
  // pytanie złożone: "X LUB Y", "X I Y", "NIE X" (LUB łączy słabiej niż I)
  function prawda(q) {
    return q.split(" LUB ").some(function (cz) { return cz.split(" I ").every(atom); });
  }
  function atom(q) {
    q = q.trim();
    if (q.indexOf("NIE ") === 0) return !atom(q.slice(4));
    var r = stan.robot, i = KIER.indexOf(r.d);
    function obok(o) { var d = DXY[KIER[(i + o) % 4]]; return pole(r.y + d[0], r.x + d[1]); }
    if (PYTANIE[q]) return obok(0) === PYTANIE[q];
    if (q === "KLOCEK?") return obok(0) === "#";
    if (q === "WOLNE?") return !NIE_WOLNO[obok(0)];
    if (q === "WOLNE W LEWO?") return !NIE_WOLNO[obok(3)];
    if (q === "WOLNE W PRAWO?") return !NIE_WOLNO[obok(1)];
    if (q === "N > 0?") return stan.N > 0;
    if (q === "N = 0?") return stan.N === 0;
    return false;
  }
  function tik() { if (++stan.kroki > MAX_KROKOW) throw new Blad("Uff, robot jest zmęczony. Program kręci się za długo."); }

  // płaska lista kart -> drzewo (pętle i pytania mają w środku swoje karty)
  function drzewo(lista) {
    var korzen = [], stos = [{ cel: korzen }];
    lista.forEach(function (c) {
      var top = stos[stos.length - 1];
      if (c.k === "POWTÓRZ" || c.k === "DOPÓKI") { var w = { t: c.k === "POWTÓRZ" ? "petla" : "dopoki", c: c, cialo: [] }; top.cel.push(w); stos.push({ w: w, cel: w.cialo }); }
      else if (c.k === "JEŚLI") { var j = { t: "jesli", c: c, tak: [], nie: [] }; top.cel.push(j); stos.push({ w: j, cel: j.tak }); }
      else if (c.k === "NIE") { if (top.w && top.w.t === "jesli") { top.w.nieC = c; top.cel = top.w.nie; } }
      else if (c.k === "KONIEC") { if (stos.length > 1) { top.w.koniecC = c; stos.pop(); } }
      else top.cel.push({ t: "karta", c: c });
    });
    return korzen;
  }
  function podswietl(c, tak) {
    var el = document.querySelector('.chip[data-id="' + c.id + '"]');
    if (!el) return;
    el.classList.toggle("teraz", tak);
    if (tak) pokazWProgramie(el.closest(".program"), el);
  }
  function stanRobota() {
    return { robot: Object.assign({}, stan.robot), zebrane: Object.assign({}, stan.zebrane), pola: stan.pola.map(function (r) { return r.slice(); }), klucze: stan.klucze, suma: stan.suma, N: stan.N };
  }
  // robot wraca do stanu sprzed usuniętej karty (tryb debug)
  // (pozycja, kierunek, skarby, klucze, drzwi i monety). Robot widocznie cofa się na stare miejsce.
  function cofnij(przed) {
    stan.zebrane = przed.zebrane; stan.pola = przed.pola; stan.klucze = przed.klucze; stan.suma = przed.suma; stan.N = przed.N;
    rysujPlansze($("plansza"), stan.pola, true, stan.zebrane);
    robotBezAnimacji();          // nowy rysunek: robot najpierw stoi tam, gdzie skończył
    stan.robot = przed.robot;
    var g = $("robot"); if (g) g.classList.add("cofa");
    ustawRobota(false);          // ...i wraca na miejsce sprzed karty
    rysujLicznik();
  }
  async function sprawdzPrzebieg(przebieg) { if (przebieg !== stan.przebieg) throw PRZERWANE; }

  async function wykonaj(wezly, ctx) {
    for (var i = 0; i < wezly.length; i++) {
      var w = wezly[i];
      if (w.c.usunieta) continue;
      if (w.t === "petla") {
        var ileRazy = ile(w.c.n);
        for (var k = 0; k < ileRazy; k++) {
          tik();
          podswietl(w.c, true);
          komunikat("POWTÓRZ: " + (k + 1) + " z " + ileRazy, "");
          if (k === 0) await powiedz(tekstKarty(w.c)); else await czekaj(250);
          await sprawdzPrzebieg(ctx.przebieg);
          podswietl(w.c, false);
          await wykonaj(w.cialo, ctx);
        }
        komunikat("", "");
      } else if (w.t === "dopoki") {
        for (var runda = 0; ; runda++) {
          podswietl(w.c, true);
          var dalej = prawda(w.c.q);
          komunikat(w.c.q + " " + (dalej ? "TAK! Kręcimy dalej." : "NIE! Koniec pętli."), "");
          if (runda === 0) await powiedz("dopóki " + (PYT_SLOWO[w.c.q] || tekstPytania(w.c.q))); else await czekaj(300);
          await sprawdzPrzebieg(ctx.przebieg);
          podswietl(w.c, false);
          if (!dalej) break;
          tik();
          await wykonaj(w.cialo, ctx);
        }
        komunikat("", "");
      } else if (w.t === "jesli") {
        podswietl(w.c, true);
        var tak = prawda(w.c.q);
        if (PYT_SLOWO[w.c.q]) {
          komunikat("Czy przed robotem jest " + PYT_SLOWO[w.c.q] + "? " + (tak ? "TAK!" : "NIE!"), "");
          await powiedz("czy przed robotem jest " + PYT_SLOWO[w.c.q] + "? " + (tak ? "tak" : "nie"));
        } else {
          komunikat(w.c.q + " " + (tak ? "TAK!" : "NIE!"), "");
          await powiedz("czy " + tekstPytania(w.c.q) + "? " + (tak ? "tak" : "nie"));
        }
        await czekaj(500);
        await sprawdzPrzebieg(ctx.przebieg);
        podswietl(w.c, false);
        if (!tak && w.nieC) { podswietl(w.nieC, true); await czekaj(250); podswietl(w.nieC, false); }
        komunikat("", "");
        await wykonaj(tak ? w.tak : w.nie, ctx);
      } else if (w.c.k === "ZRÓB A") {
        var param = !!stan.gra.parametr, nA = ile(w.c.n);
        for (var z = 0; z < (param ? 1 : nA); z++) {
          podswietl(w.c, true);
          await powiedz(z === 0 ? (param ? "zrób przepis A, N równa się " + nA : tekstKarty(w.c)) : "jeszcze raz przepis A");
          await czekaj(200);
          await sprawdzPrzebieg(ctx.przebieg);
          if (++stan.glebokosc > 40) throw new Blad("Przepis woła sam siebie bez końca. Potrzebne pytanie, które go zatrzyma.");
          var stareN = stan.N;
          if (param) { stan.N = nA; rysujLicznik(); }
          try { await wykonaj(ctx.przepis, ctx); }
          catch (e) { if (e !== KONIEC_PRZEPISU) throw e; }
          stan.glebokosc--;
          if (param) { stan.N = stareN; rysujLicznik(); }
          podswietl(w.c, false);
        }
      } else if (w.c.k === "META") {
        podswietl(w.c, true);
        await powiedz("meta");
        await czekaj(250);
        podswietl(w.c, false);
        throw KONIEC_PRZEPISU;
      } else {
        await wykonajKarte(w.c, ctx);
      }
    }
  }
  async function wykonajKarte(c, ctx) {
    podswietl(c, true);
    var przed = stanRobota(), blad = null;
    await powiedz(tekstKarty(c));
    await sprawdzPrzebieg(ctx.przebieg);
    if (ZMIENNA[c.k]) {
      if (++stan.kroki > MAX_KROKOW) blad = "Uff, robot jest zmęczony. Program jest za długi.";
      else stan.N = c.k === "N =" ? c.n : c.k === "N +" ? stan.N + c.n : stan.N - c.n;
      rysujLicznik();
      await czekaj(350);
      await sprawdzPrzebieg(ctx.przebieg);
    }
    var razy = ZMIENNA[c.k] ? 0 : ile(c.n);
    for (var k = 0; k < razy; k++) {
      if (++stan.kroki > MAX_KROKOW) { blad = "Uff, robot jest zmęczony. Program jest za długi."; break; }
      blad = krok(c.k);
      rysujLicznik();
      await czekaj(c.k === "SKOCZ" ? 560 : 430);
      await sprawdzPrzebieg(ctx.przebieg);
      if (blad) break;
    }
    if (ctx.debug && !ctx.potwierdzone[c.id]) {
      // tryb debug: po każdej karcie pytamy, czy ją zostawić, czy usunąć
      if (blad) komunikat(blad + " Usunąć tę kartę?", "zle");
      else komunikat("Dobrze? Zostaw ✓ albo usuń ✗", "");
      var dobrze = await zapytaj();
      await sprawdzPrzebieg(ctx.przebieg);
      komunikat("", "");
      if (!dobrze) {
        komunikat("Robot wraca tam, gdzie był.", "");
        cofnij(przed);
        c.usunieta = true;
        ["program", "przepis"].forEach(function (ob) {
          var p = stan.obszary[ob], i = p.indexOf(c);
          if (i >= 0) { p.splice(i, 1); stan.wybrana[ob] = Math.min(stan.wybrana[ob], p.length - 1); }
        });
        rysujProgram();
        await czekaj(700);
        var rob = $("robot"); if (rob) rob.classList.remove("cofa");
        komunikat("", "");
        await sprawdzPrzebieg(ctx.przebieg);
        return;
      }
      ctx.potwierdzone[c.id] = true;
    }
    podswietl(c, false);
    if (blad) throw new Blad(blad);
  }

  function pomieszaj(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  async function uruchom() {
    if (stan.biegnie) return;
    var g = stan.gra;
    if (!stan.obszary.program.length) { komunikat("Program jest pusty. Dodaj karty!", "zle"); return; }
    if (ma("ZRÓB A") && stan.obszary.program.some(function (c) { return c.k === "ZRÓB A"; }) && !stan.obszary.przepis.length) {
      komunikat("Przepis A jest pusty. Ułóż go w górnym rzędzie.", "zle"); return;
    }
    stan.biegnie = true; $("start").disabled = true;
    var przebieg = ++stan.przebieg;
    var ctx = { przebieg: przebieg, debug: $("debug").checked, potwierdzone: {} };
    var warianty = g.warianty ? pomieszaj(g.warianty) : [null];
    try {
      for (var t = 0; t < warianty.length; t++) {
        naStart(warianty[t]);
        ctx.przepis = drzewo(stan.obszary.przepis);
        var program = drzewo(stan.obszary.program);
        if (warianty.length > 1) komunikat((t === 0 ? "Co jest na polu ? Patrz! " : "") + "Próba " + (t + 1) + " z " + warianty.length, "");
        else komunikat("Robot rusza…", "");
        await czekaj(warianty.length > 1 ? 900 : 350);
        await sprawdzPrzebieg(przebieg);
        komunikat("", "");
        try { await wykonaj(program, ctx); }
        catch (e) { if (e !== KONIEC_PRZEPISU) throw e; }
        var wynik = ocen();
        if (wynik) { nieudana(); komunikat(wynik + (warianty.length > 1 ? " (próba " + (t + 1) + " z " + warianty.length + ")" : ""), "zle"); koniecBiegu(); return; }
        if (t < warianty.length - 1) {
          komunikat("Udało się! Ale pole ? za chwilę będzie inne…", "dobrze");
          await czekaj(1500);
          await sprawdzPrzebieg(przebieg);
        }
      }
    } catch (e) {
      if (e === PRZERWANE) return;
      if (!(e instanceof Blad)) throw e;
      koniecBiegu();
      nieudana();
      var r = $("robot"); if (r) { r.classList.add("potrzasnij"); setTimeout(function () { r.classList.remove("potrzasnij"); }, 500); }
      komunikat(e.tekst + " Popraw program i spróbuj jeszcze raz.", "zle");
      return;
    }
    koniecBiegu();
    sukces();
  }
  function koniecBiegu() {
    stan.biegnie = false; $("start").disabled = false;
    document.querySelectorAll(".chip.teraz").forEach(function (el) { el.classList.remove("teraz"); });
  }
  // null = wygrana, inaczej tekst, czego brakuje
  function ocen() {
    var g = stan.gra, gw = 0;
    stan.pola.forEach(function (r) { r.forEach(function (t) { if (t === "*") gw++; }); });
    var mam = Object.keys(stan.zebrane).length;
    var naStarcie = stan.robot.y === stan.info.start.y && stan.robot.x === stan.info.start.x;
    if (mam < gw) return mam ? "Jest " + mam + " z " + gw + " skarbów. Robot musi iść dalej!" : "Robot stanął, ale skarb jest dalej.";
    if (g.suma && stan.suma < g.suma) return "Masz " + stan.suma + ", a trzeba " + g.suma + ". Zbierz więcej!";
    if (g.suma && stan.suma > g.suma) return "Masz " + stan.suma + ", a trzeba " + g.suma + ". To za dużo!";
    if (g.powrot && !naStarcie) return "Masz skarb! Teraz wróć na START.";
    if (g.wymagaj === "rekurencja" && !stan.obszary.przepis.some(function (c) { return c.k === "ZRÓB A"; }))
      return "Skarby są, ale tu trzeba rekurencji: połóż ZRÓB A w samym przepisie A.";
    return null;
  }
  // ---------- tryb debug ----------
  function zapytaj() {
    $("debugPytanie").hidden = false;
    $("debugTak").focus();
    return new Promise(function (r) { stan.odpowiedz = r; });
  }
  function odpowiedz(tak) {
    $("debugPytanie").hidden = true;
    var r = stan.odpowiedz; stan.odpowiedz = null;
    if (r) r(tak);
  }
  function przerwij() {
    stan.przebieg++; koniecBiegu();
    $("debugPytanie").hidden = true; stan.odpowiedz = null;
  }
  function krok(nazwa) {
    var r = stan.robot;
    if (nazwa === "SKRĘĆ W PRAWO") { r.d = KIER[(KIER.indexOf(r.d) + 1) % 4]; r.kat += 90; ustawRobota(); return null; }
    if (nazwa === "SKRĘĆ W LEWO") { r.d = KIER[(KIER.indexOf(r.d) + 3) % 4]; r.kat -= 90; ustawRobota(); return null; }
    if (nazwa === "OBRÓĆ SIĘ") { r.d = KIER[(KIER.indexOf(r.d) + 2) % 4]; r.kat += 180; ustawRobota(); return null; }
    var d = DXY[r.d], ile = nazwa === "SKOCZ" ? 2 : 1;
    if (ile === 2) {
      var srodek = pole(r.y + d[0], r.x + d[1]);
      if (srodek === "L") return "Lawy nie da się przeskoczyć. Trzeba ją obejść.";
      if (srodek === "#") return "Klocka nie da się przeskoczyć.";
      if (srodek === "SCIANA") return BLAD.SCIANA;
      if (srodek !== "K") return "HOP? Tu nie ma kałuży! Skaczemy tylko przez kałużę.";
    }
    var y = r.y + ile * d[0], x = r.x + ile * d[1], t = pole(y, x);
    if (BLAD[t]) return BLAD[t];
    if (t === "D") {
      if (!stan.klucze) return "Drzwi są zamknięte. Najpierw weź klucz!";
      stan.klucze--; stan.pola[y][x] = "o"; odswiezPole(y, x);
    }
    r.y = y; r.x = x; ustawRobota(ile === 2);
    if (t === "*") { stan.zebrane[y + "-" + x] = true; odswiezPole(y, x); }
    else if (t === "@") { stan.klucze++; zniknij(y, x); }
    else if (/^[1-9]$/.test(t)) { stan.suma += +t; zniknij(y, x); }
    return null;
  }
  function zniknij(y, x) {
    stan.pola[y][x] = ".";
    var el = document.getElementById("p-" + y + "-" + x);
    if (el) { el.classList.add("zebrany"); setTimeout(function () { if (stan.pola[y] && stan.pola[y][x] === ".") odswiezPole(y, x); }, 300 * tempo); }
  }
  // Rozwiązanie dla dorosłego pojawia się dopiero po 2 nieudanych próbach.
  var PROG_PODPOWIEDZI = 2;
  function nieudana() {
    stan.nieudane = (stan.nieudane || 0) + 1;
    if (stan.nieudane >= PROG_PODPOWIEDZI) $("pokazRozw").hidden = false;
  }
  function sukces() {
    var g = stan.gra;
    if (!g.przyklad) zapiszGw(g.id);
    komunikat("Brawo! Robot ma skarb!", "dobrze");
    powiedz("brawo");
    var n = ileKart();
    var karty = n === 1 ? "kartę" : slowoKarty(n);
    var co = g.suma ? "Robot zebrał monety: razem " + g.suma + "." : "Robot zebrał skarb.";
    if (g.warianty) co = "Program zadziałał za każdym razem!";
    $("brawoTekst").textContent = g.przyklad ? g.wynik : co + " Twój program ma " + n + " " + karty + ".";
    $("nastepna").textContent = g.przyklad ? "Wróć do pomocy" : "Następna gra";
    $("brawo").hidden = false;
    $("nastepna").focus();
  }
  function slowoKarty(n) { return n === 1 ? "karta" : (n % 10 >= 2 && n % 10 <= 4 && (n < 10 || n > 20) ? "karty" : "kart"); }
  function nastepna() {
    $("brawo").hidden = true;
    if (stan.gra.przyklad) { wrocZPrzykladu(); return; }
    var i = GRY.indexOf(stan.gra), nast = GRY[i + 1];
    if (nast && nast.size === stan.gra.size && nast.poziom === stan.gra.poziom) location.hash = "gra-" + nast.id;
    else location.hash = "";
  }

  // ---------- pomoc: jak działa każda karta, z przykładami (dane w gra/pomoc.js) ----------
  var POMOC = window.POMOC || [], PRZYKLADY = {};
  POMOC.forEach(function (poz) {
    poz.rzeczy.forEach(function (r) {
      var p = r.przyklad; if (!p) return;
      PRZYKLADY[p.id] = {
        id: "przyklad-" + p.id, przyklad: true, poziom: poz.poziom, size: p.plansza.length, nr: 0, tytul: p.tytul,
        opis: r.tekst + " Naciśnij START i patrz!", wynik: p.wynik, plansza: p.plansza, karty: p.karty,
        rozwiazanie: { program: p.program, przepis: p.przepis }, pytania: p.pytania, warianty: p.warianty,
        suma: p.suma, parametr: !!p.parametr, rekurencja: !!p.rekurencja, wymagaj: p.wymagaj, powrot: !!p.powrot
      };
      if (!p.przepis) delete PRZYKLADY[p.id].rozwiazanie.przepis;
    });
  });
  var NAZWA_POLA = { "@": "klucz", "D": "drzwi", "?": "niespodzianka" };
  function ikonaPola(t) {
    if (KIER.indexOf(t) >= 0) return '<svg viewBox="0 0 20 20" aria-hidden="true"><g transform="translate(10,10)"><circle r="7.6" fill="#2b6fd6"/><polygon points="0,-5.7 3.8,2.7 -3.8,2.7" fill="#fff"/></g></svg>';
    if (t === "@") return '<svg viewBox="0 0 40 20" aria-hidden="true">' + klucz(0, 0) + rysujPole("D", 20, 0) + "</svg>";
    return '<svg viewBox="0 0 20 20" aria-hidden="true">' + rysujPole(t, 0, 0) + "</svg>";
  }
  // ikona pytania złożonego: obrazek ostatniej części, bez słowa NIE
  function ikonaPytania(q) { return pytanieIkona(q.split(/ I | LUB /).pop().replace(/^NIE /, "")); }
  function kartaPomocy(k) {
    return '<span class="karta mala" style="color:' + KOLOR[k] + '">' + ikona(k) + "<span>" + NAPIS[k].join("<br>") + "</span></span>";
  }
  function znakRzeczy(r) {
    if (r.karta) return (r.karty || [r.karta]).map(kartaPomocy).join("");
    if (r.liczba) return '<span class="liczba mala">' + (r.liczba === "N" ? "N" : "3") + "</span>";
    if (r.pytanie) return '<span class="pytanie">' + ikonaPytania(r.pytanie) + "<span>" + r.pytanie + "</span></span>";
    if (r.pole) return '<span class="pole-ikona">' + ikonaPola(r.pole) + "</span>";
    if (r.limit) return '<span class="licznik-pomoc">Karty: 4 z 6</span>';
    return "";
  }
  function przykladHTML(p, poziom) {
    var tok = function (c) { return tokenZDanych(c); };
    parametrWidoku = !!p.parametr;
    var prog = (p.przepis ? '<div class="rz"><b>Przepis A:</b> ' + rysujKarty(p.przepis.map(tok), "x") + "</div>" : "") +
      '<div class="rz">' + (p.przepis ? "<b>Program:</b> " : "") + rysujKarty(p.program.map(tok), "x") + "</div>";
    parametrWidoku = null;
    return '<div class="pk-przyklad"><svg class="mini" data-przyklad="' + p.id + '" role="img" aria-label="Plansza przykładu"></svg>' +
      '<div class="pk-prog"><div class="male">Przykład: ' + p.tytul + (p.warianty ? " (pole ? za każdym razem inne)" : "") + "</div>" + prog +
      '<p class="pk-wynik">' + p.wynik + "</p>" +
      '<button class="btn wyprobuj" data-przyklad="' + p.id + '" data-poziom="' + poziom + '">▶ Wypróbuj</button></div></div>';
  }
  function rysujPomoc(poziom) {
    var poz = POMOC.filter(function (x) { return x.poziom === poziom; })[0] || POMOC[0];
    if (!poz) return;
    stan.poziomPomocy = poz.poziom;
    $("pomocTaby").innerHTML = POMOC.map(function (x) {
      return '<button class="tab" role="tab" data-poziom="' + x.poziom + '" aria-selected="' + (x.poziom === poz.poziom) + '">Poziom ' + x.poziom + "</button>";
    }).join("");
    var h = '<p class="pk-wstep">' + (poz.dla ? "<b>Poziom " + poz.poziom + ", " + poz.dla + ".</b> " : "") + poz.wstep + "</p>";
    poz.rzeczy.forEach(function (r) {
      h += '<article class="pk"><div class="pk-glowa">' + znakRzeczy(r) + "<h4>" + (r.nazwa || r.karta) + "</h4></div>" +
        "<p>" + r.tekst + "</p>" + (r.przyklad ? przykladHTML(r.przyklad, poz.poziom) : "") + "</article>";
    });
    if (poz.pytania) {
      h += '<h3 class="pk-dzial">Pytania</h3><div class="pk-siatka">' + poz.pytania.map(function (q) {
        return '<div class="pk-maly"><span class="pytanie">' + ikonaPytania(q.q) + "<span>" + q.q + "</span></span><p>" + q.tekst + "</p></div>";
      }).join("") + "</div>";
    }
    if (poz.pola) {
      h += '<h3 class="pk-dzial">Pola na planszy</h3><div class="pk-siatka">' + poz.pola.map(function (f) {
        return '<div class="pk-maly"><span class="pole-ikona">' + ikonaPola(f.pole) + "</span><p><b>" + f.nazwa + ".</b> " + f.tekst + "</p></div>";
      }).join("") + "</div>";
    }
    if (poz.przyciski) {
      h += '<h3 class="pk-dzial">Układanie programu</h3><ul class="pk-lista">' +
        "<li>Dotknij karty w programie, żeby ją wybrać. Nowa karta stanie zaraz za nią. Liczba zmienia wybraną kartę.</li>" +
        "<li>Czerwony ✕ przy wybranej karcie usuwa ją. Przycisk ▶ na początku wstawia kartę na sam początek.</li>" +
        "<li><b>START</b> uruchamia robota. <b>Na start</b> stawia go z powrotem. <b>Wyczyść</b> zabiera wszystkie karty.</li>" +
        "<li><b>Czytaj</b>: robot czyta karty na głos. <b>Debug</b>: robot idzie karta po karcie, a ty mówisz ✓ zostaw albo ✗ usuń.</li>" +
        "<li>Po dwóch nieudanych próbach pojawia się żarówka z rozwiązaniem dla dorosłego.</li></ul>";
    }
    $("pomocTresc").innerHTML = h;
    $("pomocTresc").querySelectorAll("svg.mini").forEach(function (svg) {
      var g = PRZYKLADY[svg.dataset.przyklad];
      rysujPlansze(svg, plansza(g), false);
    });
    $("pomocTresc").scrollTop = 0;
  }
  function otworzPomoc(poziom) {
    if (stan.odpowiedz || stan.biegnie) przerwij();
    rysujPomoc(poziom || (stan.gra ? stan.gra.poziom : stan.poziom));
    var d = $("pomoc");
    if (d.showModal) { if (!d.open) d.showModal(); } else d.setAttribute("open", "");
  }
  function zamknijPomoc() { var d = $("pomoc"); if (d.close) d.close(); else d.removeAttribute("open"); }
  function otworzPrzyklad(g) {
    otworzGre(g);
    stan.obszary = { program: g.rozwiazanie.program.map(tokenZDanych), przepis: (g.rozwiazanie.przepis || []).map(tokenZDanych) };
    stan.wybrana = { program: stan.obszary.program.length - 1, przepis: -1 }; stan.obszar = "program";
    rysujProgram(); naStart();
    komunikat("Program jest gotowy. Naciśnij START!", "");
  }
  function wyprobuj(id, poziom) {
    var g = stan.gra && !stan.gra.przyklad ? stan.gra : null;
    if (!stan.gra || !stan.gra.przyklad) {
      stan.schowek = g ? { id: g.id, obszary: stan.obszary, wybrana: stan.wybrana, obszar: stan.obszar, hash: "gra-" + g.id, poziom: poziom, pomoc: false }
                       : { id: null, hash: "", poziom: poziom, pomoc: false };
    } else if (stan.schowek) stan.schowek.poziom = poziom;
    zamknijPomoc();
    if (location.hash === "#przyklad-" + id) otworzPrzyklad(PRZYKLADY[id]);
    else location.hash = "przyklad-" + id;
  }
  function wrocZPrzykladu() {
    var s = stan.schowek;
    if (!s) { location.hash = ""; return; }
    s.pomoc = true;
    location.hash = s.hash;
  }

  // ---------- ekrany i nawigacja ----------
  function pokazStart() {
    przerwij(); stan.gra = null;
    $("ekranStart").hidden = false; $("ekranGra").hidden = true; $("doListy").hidden = true; document.body.classList.remove("w-grze"); $("brawo").hidden = true;
    rysujListe();
  }
  function trasa() {
    var h = location.hash.replace("#", "");
    var m = h.match(/^gra-(\d+-\d+(?:-\d+)?)$/), p = h.match(/^przyklad-([a-z0-9-]+)$/);
    if (m) { otworz(m[1]); if (stan.gra) zapiszWybor(); }
    else if (p && PRZYKLADY[p[1]]) otworzPrzyklad(PRZYKLADY[p[1]]);
    else { pokazStart(); if (stan.schowek && stan.schowek.id === null && stan.schowek.pomoc) { var poz = stan.schowek.poziom; stan.schowek = null; otworzPomoc(poz); } }
  }
  function rysujPaleteKart() {
    var karty = stan.gra ? stan.gra.karty : RUCH;
    $("karty").innerHTML = karty.map(function (k) {
      return '<button class="karta" data-k="' + k + '" style="color:' + KOLOR[k] + '" aria-label="' + k + '">' + ikona(k) + "<span>" + NAPIS[k].join("<br>") + "</span></button>";
    }).join("");
    $("karty").classList.toggle("duzo", karty.length > 5);
  }

  function init() {
    wczytajWybor();
    $("liczby").innerHTML = [0, 1, 2, 3, 4, 5, 6, "N"].map(function (n) { return '<button class="liczba" data-n="' + n + '" aria-label="' + (n === 0 ? "zero" : n === "N" ? "N razy" : SLOWO[n] + " razy") + '"' + (n === 0 || n === "N" ? " hidden" : "") + ">" + n + "</button>"; }).join("");
    $("poziomyTaby").innerHTML = poziomy().map(function (p) { return '<button class="tab" role="tab" data-poziom="' + p + '" aria-selected="false">Poziom ' + p + "</button>"; }).join("");
    $("karty").addEventListener("click", function (e) { var b = e.target.closest(".karta"); if (b) dodaj(b.dataset.k); });
    $("liczby").addEventListener("click", function (e) { var b = e.target.closest(".liczba"); if (b) liczba(b.dataset.n === "N" ? "N" : +b.dataset.n); });
    $("pytania").addEventListener("click", function (e) { var b = e.target.closest(".pytanie"); if (b) pytanie(b.dataset.q); });
    function klikProgram(e) {
      if (stan.biegnie) return;
      var u = e.target.closest(".usun"); if (u) { usun(u.dataset.a, +u.dataset.usun); return; }
      var b = e.target.closest("[data-a]");
      var ob = e.currentTarget.id === "przepis" ? "przepis" : "program";
      if (b && b.dataset.i !== undefined) { wybierz(ob, +b.dataset.i); return; }
      if (b && b.dataset.id) { var i = stan.obszary[ob].map(function (c) { return String(c.id); }).indexOf(b.dataset.id); wybierz(ob, i); return; }
      if (stan.obszar !== ob) { stan.obszar = ob; rysujProgram(); }
    }
    $("program").addEventListener("click", klikProgram);
    $("przepis").addEventListener("click", klikProgram);
    $("start").addEventListener("click", uruchom);
    $("debugTak").addEventListener("click", function () { odpowiedz(true); });
    $("debugNie").addEventListener("click", function () { odpowiedz(false); });
    $("odNowa").addEventListener("click", function () { if (stan.odpowiedz || stan.biegnie) przerwij(); naStart(); rysujProgram(); komunikat("", ""); });
    $("wyczysc").addEventListener("click", function () {
      if (stan.odpowiedz || stan.biegnie) przerwij();
      stan.obszary = { program: [], przepis: [] }; stan.wybrana = { program: -1, przepis: -1 }; stan.obszar = "program";
      rysujProgram(); naStart(); komunikat("", "");
    });
    $("pokazRozw").addEventListener("click", function () { $("rozw").hidden = !$("rozw").hidden; });
    $("lista").addEventListener("click", function (e) { var b = e.target.closest(".kafel"); if (b) location.hash = "gra-" + b.dataset.id; });
    ROZMIARY.forEach(function (r) { $("tab" + r).addEventListener("click", function () { stan.rozmiar = r; zapiszWybor(); rysujListe(); }); });
    $("poziomyTaby").addEventListener("click", function (e) { var b = e.target.closest(".tab[data-poziom]"); if (b) { stan.poziom = +b.dataset.poziom; zapiszWybor(); rysujListe(); } });
    $("doListy").addEventListener("click", function () { location.hash = ""; });
    $("grajTeraz").addEventListener("click", function () {
      var gw = wczytajGw();
      var tu = GRY.filter(function (g) { return g.size === stan.rozmiar && g.poziom === stan.poziom; });
      var pierwsza = tu.filter(function (g) { return gw.indexOf(g.id) < 0; })[0] || tu[0] || GRY[0];
      location.hash = "gra-" + pierwsza.id;
    });
    $("nastepna").addEventListener("click", nastepna);
    $("pomocBtn").addEventListener("click", function () { otworzPomoc(); });
    $("pomocZamknij").addEventListener("click", zamknijPomoc);
    $("pomoc").addEventListener("click", function (e) {
      if (e.target === $("pomoc")) { zamknijPomoc(); return; }
      var t = e.target.closest(".tab[data-poziom]"); if (t) { rysujPomoc(+t.dataset.poziom); return; }
      var w = e.target.closest(".wyprobuj"); if (w) wyprobuj(w.dataset.przyklad, +w.dataset.poziom);
    });
    $("jeszczeRaz").addEventListener("click", function () { $("brawo").hidden = true; naStart(); });
    window.addEventListener("hashchange", trasa);
    function zmianaEkranu() {
      if (stan.gra && !$("ekranGra").hidden && !dozwolony(stan.gra.size)) location.hash = "";
      else if (!$("ekranStart").hidden) rysujListe();
    }
    if (KOMPUTER.addEventListener) KOMPUTER.addEventListener("change", zmianaEkranu);
    else if (KOMPUTER.addListener) KOMPUTER.addListener(zmianaEkranu);
    // podgląd na stronie startowej
    var demo = GRY.filter(function (g) { return g.id === "5-21"; })[0] || GRY[0];
    if (demo) {
      $("demo").innerHTML = '<svg viewBox="0 0 108 108"></svg>';
      rysujPlansze($("demo").firstChild, plansza(demo), false);
    }
    trasa();
  }
  init();
  // do testów: tempo 0 = bez animacji; ustawProgram wkłada rozwiązanie gry do programu
  window.RobotGra = {
    ustawTempo: function (t) { tempo = t; },
    ustawProgram: function (rozw) {
      stan.obszary = { program: rozw.program.map(tokenZDanych), przepis: (rozw.przepis || []).map(tokenZDanych) };
      stan.wybrana = { program: stan.obszary.program.length - 1, przepis: -1 }; stan.obszar = "program";
      rysujProgram(); naStart();
    },
    stan: stan,
    przyklady: function () { return Object.keys(PRZYKLADY); },
    pomoc: otworzPomoc
  };
})();
