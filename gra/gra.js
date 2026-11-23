// Robot i Programista - wersja online (poziomy 1 i 2). Dane gier: gra/gry.js (window.GRY).
// Poziom 2: pętla POWTÓRZ…KONIEC, klucze (@) i drzwi (D), monety 1-6 z sumą, limit kart,
// pytanie JEŚLI…NIE…KONIEC z polami ? (warianty planszy) i przepis A z kartą ZRÓB A.
(function () {
  "use strict";
  var GRY = window.GRY || [];
  var KOLOR = {
    "IDŹ": "#2e9e4f", "SKRĘĆ W PRAWO": "#f08a1c", "SKRĘĆ W LEWO": "#2b6fd6", "OBRÓĆ SIĘ": "#8a4fd1", "SKOCZ": "#0c8599",
    "POWTÓRZ": "#d6336c", "KONIEC": "#495057", "JEŚLI": "#b08900", "NIE": "#e03131", "ZRÓB A": "#364fc7"
  };
  var NAPIS = {
    "IDŹ": ["IDŹ"], "SKRĘĆ W PRAWO": ["SKRĘĆ", "W PRAWO"], "SKRĘĆ W LEWO": ["SKRĘĆ", "W LEWO"], "OBRÓĆ SIĘ": ["OBRÓĆ", "SIĘ"], "SKOCZ": ["SKOCZ"],
    "POWTÓRZ": ["POWTÓRZ"], "JEŚLI": ["JEŚLI"], "ZRÓB A": ["ZRÓB A"]
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
    "ZRÓB A": '<rect x="18" y="6" width="64" height="88" rx="9" fill="none" stroke="currentColor" stroke-width="9"/><polygon points="38,28 72,50 38,72" fill="currentColor"/>'
  };
  var RUCH = ["IDŹ", "SKRĘĆ W PRAWO", "SKRĘĆ W LEWO", "OBRÓĆ SIĘ", "SKOCZ"];
  var PYTANIE = { "LAWA?": "L", "KAŁUŻA?": "K", "SKARB?": "*", "ŚCIANA?": "SCIANA" };
  var PYT_SLOWO = { "LAWA?": "lawa", "KAŁUŻA?": "kałuża", "SKARB?": "skarb", "ŚCIANA?": "ściana" };
  var SLOWO = { 1: "raz", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć" };
  var KIER = "^>v<";
  var DXY = { "^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1] };
  var S = 20, O = 4; // rozmiar pola w SVG i margines
  var MAX = 30, MAX_KROKOW = 400;

  var $ = function (id) { return document.getElementById(id); };
  var stan = {
    przebieg: 0, odpowiedz: null, gra: null, biegnie: false, robot: null, rozmiar: 5, poziom: 1,
    obszary: { program: [], przepis: [] }, obszar: "program", wybrana: { program: -1, przepis: -1 }, nowyId: 1
  };

  // ---------- pamięć w przeglądarce (gwiazdki i wybrany poziom) ----------
  function wczytajGw() { try { return JSON.parse(localStorage.getItem("rip-gwiazdki") || "[]"); } catch (e) { return []; } }
  function zapiszGw(id) {
    var g = wczytajGw(); if (g.indexOf(id) < 0) g.push(id);
    try { localStorage.setItem("rip-gwiazdki", JSON.stringify(g)); } catch (e) { /* bez zapisu */ }
  }
  function zapiszWybor() { try { localStorage.setItem("rip-wybor", JSON.stringify({ p: stan.poziom, r: stan.rozmiar })); } catch (e) { /* bez zapisu */ } }
  function wczytajWybor() {
    try { var w = JSON.parse(localStorage.getItem("rip-wybor") || "null"); if (w) { stan.poziom = w.p === 2 ? 2 : 1; stan.rozmiar = [5, 7, 9].indexOf(w.r) >= 0 ? w.r : 5; } } catch (e) { /* domyślnie */ }
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
  function tekstKarty(c) {
    if (c.k === "POWTÓRZ") return "powtórz " + SLOWO[c.n] + (c.n > 1 ? " razy" : "");
    if (c.k === "JEŚLI") return "jeśli " + PYT_SLOWO[c.q];
    if (c.k === "ZRÓB A") return "zrób przepis A" + (c.n > 1 ? " " + SLOWO[c.n] + " razy" : "");
    if (c.k === "NIE" || c.k === "KONIEC") return c.k;
    return c.k + (c.n > 1 ? " " + SLOWO[c.n] + " razy" : "");
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
    [5, 7, 9].forEach(function (r) { $("tab" + r).setAttribute("aria-selected", stan.rozmiar === r); });
    [1, 2].forEach(function (p) { $("poz" + p).setAttribute("aria-selected", stan.poziom === p); });
    $("opisPoziomu").textContent = stan.poziom === 1
      ? "Karty IDŹ, SKRĘĆ, OBRÓĆ SIĘ i SKOCZ. Liczba mówi, ile razy."
      : "Nowe karty i pola: pętla POWTÓRZ, klucz i drzwi, monety do liczenia, pytanie JEŚLI i przepis A. W każdym zestawie gry idą od najłatwiejszej.";
  }

  // ---------- gra ----------
  function ma(karta) { return stan.gra && stan.gra.karty.indexOf(karta) >= 0; }
  function otworz(id) {
    var gra = GRY.filter(function (g) { return g.id === id; })[0];
    if (!gra) { pokazStart(); return; }
    przerwij();
    stan.gra = gra; stan.obszary = { program: [], przepis: [] }; stan.obszar = "program"; stan.wybrana = { program: -1, przepis: -1 };
    stan.poziom = gra.poziom; stan.rozmiar = gra.size;
    $("ekranStart").hidden = true; $("ekranGra").hidden = false; $("doListy").hidden = false; document.body.classList.add("w-grze");
    $("graTytul").textContent = (gra.poziom > 1 ? "Poziom " + gra.poziom + ", gra " : "Gra ") + gra.nr + ": " + gra.tytul + " (" + gra.size + " × " + gra.size + ")";
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
    if (c[0] === "JEŚLI") t.q = c[1]; else t.n = c[1] || 1;
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
    stan.zebrane = {}; stan.klucze = 0; stan.suma = 0; stan.kroki = 0;
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
    $("licznik").innerHTML = h.join("");
    $("licznik").hidden = !h.length;
  }

  // ---------- karty w programie ----------
  // Dla kart POWTÓRZ / JEŚLI / NIE / KONIEC zwraca indeksy całej grupy: {start, nie, koniec}.
  function grupy(lista) {
    var stos = [], gr = {};
    lista.forEach(function (c, i) {
      if (c.k === "POWTÓRZ" || c.k === "JEŚLI") { var g = { start: i, nie: -1, koniec: -1 }; stos.push(g); gr[i] = g; }
      else if (c.k === "NIE" && stos.length) { stos[stos.length - 1].nie = i; gr[i] = stos[stos.length - 1]; }
      else if (c.k === "KONIEC" && stos.length) { var t = stos.pop(); t.koniec = i; gr[i] = t; }
    });
    return gr;
  }
  function chip(c, obszar, wybrana) {
    var kolor = KOLOR[c.k], tresc;
    if (c.k === "JEŚLI") tresc = ikona("JEŚLI") + "<span>JEŚLI</span>" + pytanieIkona(c.q) + '<span class="q">' + c.q + "</span>";
    else if (c.k === "NIE") tresc = ikona("NIE") + "<span>NIE</span>";
    else if (c.k === "KONIEC") tresc = ikona("KONIEC") + "<span>KONIEC</span>";
    else tresc = ikona(c.k) + "<span>" + c.k + "</span>" + (c.n > 1 || c.k === "POWTÓRZ" ? '<b class="n">×' + c.n + "</b>" : "");
    var aktywny = obszar !== "x";
    return '<button class="chip' + (wybrana ? " wybrana" : "") + '" data-id="' + c.id + '"' + (aktywny ? ' data-a="' + obszar + '" aria-pressed="' + !!wybrana + '"' : ' tabindex="-1"') +
           ' style="color:' + kolor + '">' + tresc + "</button>";
  }
  function pytanieIkona(q) {
    var t = PYTANIE[q];
    if (t === "SCIANA") return '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="1" y="1" width="18" height="18" rx="2" fill="#f1d3c3"/><path d="M1 7 H19 M1 13 H19 M7 1 V7 M13 7 V13 M7 13 V19" stroke="#c0603a" stroke-width="1.6"/></svg>';
    return '<svg viewBox="0 0 20 20" aria-hidden="true">' + rysujPole(t, 0, 0) + "</svg>";
  }
  // Karty jako rząd chipów; POWTÓRZ…KONIEC i JEŚLI…KONIEC w ramce. obszar "x" = tylko do oglądania.
  function rysujKarty(lista, obszar, w) {
    var kursor = '<span class="kursor" aria-hidden="true"></span>', html = "";
    lista.forEach(function (c, i) {
      var otw = c.k === "POWTÓRZ" || c.k === "JEŚLI";
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
    var c = wybrany(), pyt = c && c.k === "JEŚLI";
    $("liczby").hidden = pyt; $("pytania").hidden = !pyt;
    $("tytulLiczb").textContent = pyt ? "O co pyta robot?" : "Ile razy?";
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
    if (nazwa === "ZRÓB A" && ob === "przepis") { komunikat("Kartę ZRÓB A kładziemy w programie, a nie w przepisie.", "zle"); return; }
    if (nazwa === "POWTÓRZ") nowe = [{ k: "POWTÓRZ", n: 2 }, { k: "KONIEC", n: 1 }];
    else if (nazwa === "JEŚLI") nowe = [{ k: "JEŚLI", n: 1, q: (stan.gra.pytania || ["LAWA?"])[0] }, { k: "NIE", n: 1 }, { k: "KONIEC", n: 1 }];
    else nowe = [{ k: nazwa, n: 1 }];
    if (ileKart() + nowe.length > MAX) { komunikat("Program jest już bardzo długi.", "zle"); return; }
    if (stan.gra.limit && ileKart() + nowe.length > stan.gra.limit) {
      komunikat("Masz tylko " + stan.gra.limit + " " + slowoKarty(stan.gra.limit) + ". " + (ma("ZRÓB A") ? "Może przepis A pomoże?" : "Może pomoże POWTÓRZ?"), "zle"); return;
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
    if (c.k === "NIE" || c.k === "KONIEC") { komunikat("Karta " + c.k + " nie ma liczby.", "zle"); return; }
    c.n = n;
    powiedz(c.k === "POWTÓRZ" ? tekstKarty(c) : SLOWO[n] + (n > 1 ? " razy" : ""));
    rysujProgram(); naStart();
  }
  function pytanie(q) {
    var c = wybrany(); if (!c || c.k !== "JEŚLI" || stan.biegnie) return;
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
  var PRZERWANE = {};

  // płaska lista kart -> drzewo (pętle i pytania mają w środku swoje karty)
  function drzewo(lista) {
    var korzen = [], stos = [{ cel: korzen }];
    lista.forEach(function (c) {
      var top = stos[stos.length - 1];
      if (c.k === "POWTÓRZ") { var w = { t: "petla", c: c, cialo: [] }; top.cel.push(w); stos.push({ w: w, cel: w.cialo }); }
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
    return { robot: Object.assign({}, stan.robot), zebrane: Object.assign({}, stan.zebrane), pola: stan.pola.map(function (r) { return r.slice(); }), klucze: stan.klucze, suma: stan.suma };
  }
  // robot wraca do stanu sprzed usuniętej karty (tryb debug)
  function cofnij(przed) {
    stan.robot = przed.robot; stan.zebrane = przed.zebrane; stan.pola = przed.pola; stan.klucze = przed.klucze; stan.suma = przed.suma;
    rysujPlansze($("plansza"), stan.pola, true, stan.zebrane);
    robotBezAnimacji(); rysujLicznik();
  }
  async function sprawdzPrzebieg(przebieg) { if (przebieg !== stan.przebieg) throw PRZERWANE; }

  async function wykonaj(wezly, ctx) {
    for (var i = 0; i < wezly.length; i++) {
      var w = wezly[i];
      if (w.c.usunieta) continue;
      if (w.t === "petla") {
        for (var k = 0; k < w.c.n; k++) {
          podswietl(w.c, true);
          komunikat("POWTÓRZ: " + (k + 1) + " z " + w.c.n, "");
          if (k === 0) await powiedz(tekstKarty(w.c)); else await czekaj(250);
          await sprawdzPrzebieg(ctx.przebieg);
          podswietl(w.c, false);
          await wykonaj(w.cialo, ctx);
        }
        komunikat("", "");
      } else if (w.t === "jesli") {
        podswietl(w.c, true);
        var r = stan.robot, d = DXY[r.d], przed = pole(r.y + d[0], r.x + d[1]);
        var tak = przed === PYTANIE[w.c.q];
        komunikat("Czy przed robotem jest " + PYT_SLOWO[w.c.q] + "? " + (tak ? "TAK!" : "NIE!"), "");
        await powiedz("czy przed robotem jest " + PYT_SLOWO[w.c.q] + "? " + (tak ? "tak" : "nie"));
        await czekaj(500);
        await sprawdzPrzebieg(ctx.przebieg);
        podswietl(w.c, false);
        if (!tak && w.nieC) { podswietl(w.nieC, true); await czekaj(250); podswietl(w.nieC, false); }
        komunikat("", "");
        await wykonaj(tak ? w.tak : w.nie, ctx);
      } else if (w.c.k === "ZRÓB A") {
        for (var z = 0; z < w.c.n; z++) {
          podswietl(w.c, true);
          await powiedz(z === 0 ? tekstKarty(w.c) : "jeszcze raz przepis A");
          await czekaj(200);
          await sprawdzPrzebieg(ctx.przebieg);
          await wykonaj(ctx.przepis, ctx);
          podswietl(w.c, false);
        }
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
    for (var k = 0; k < c.n; k++) {
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
        cofnij(przed);
        c.usunieta = true;
        ["program", "przepis"].forEach(function (ob) {
          var p = stan.obszary[ob], i = p.indexOf(c);
          if (i >= 0) { p.splice(i, 1); stan.wybrana[ob] = Math.min(stan.wybrana[ob], p.length - 1); }
        });
        rysujProgram();
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
        await wykonaj(program, ctx);
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
    zapiszGw(g.id);
    komunikat("Brawo! Robot ma skarb!", "dobrze");
    powiedz("brawo");
    var n = ileKart();
    var karty = n === 1 ? "kartę" : slowoKarty(n);
    var co = g.suma ? "Robot zebrał monety: razem " + g.suma + "." : "Robot zebrał skarb.";
    if (g.warianty) co = "Program zadziałał za każdym razem!";
    $("brawoTekst").textContent = co + " Twój program ma " + n + " " + karty + ".";
    $("brawo").hidden = false;
    $("nastepna").focus();
  }
  function slowoKarty(n) { return n === 1 ? "karta" : (n % 10 >= 2 && n % 10 <= 4 && (n < 10 || n > 20) ? "karty" : "kart"); }
  function nastepna() {
    $("brawo").hidden = true;
    var i = GRY.indexOf(stan.gra), nast = GRY[i + 1];
    if (nast && nast.size === stan.gra.size && nast.poziom === stan.gra.poziom) location.hash = "gra-" + nast.id;
    else location.hash = "";
  }

  // ---------- ekrany i nawigacja ----------
  function pokazStart() {
    $("ekranStart").hidden = false; $("ekranGra").hidden = true; $("doListy").hidden = true; document.body.classList.remove("w-grze"); $("brawo").hidden = true;
    rysujListe();
  }
  function trasa() {
    var h = location.hash.replace("#", "");
    var m = h.match(/^gra-(\d+-\d+(?:-\d+)?)$/);
    if (m) { otworz(m[1]); if (stan.gra) zapiszWybor(); }
    else pokazStart();
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
    $("liczby").innerHTML = [1, 2, 3, 4, 5, 6].map(function (n) { return '<button class="liczba" data-n="' + n + '" aria-label="' + SLOWO[n] + ' razy">' + n + "</button>"; }).join("");
    $("karty").addEventListener("click", function (e) { var b = e.target.closest(".karta"); if (b) dodaj(b.dataset.k); });
    $("liczby").addEventListener("click", function (e) { var b = e.target.closest(".liczba"); if (b) liczba(+b.dataset.n); });
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
    [5, 7, 9].forEach(function (r) { $("tab" + r).addEventListener("click", function () { stan.rozmiar = r; zapiszWybor(); rysujListe(); }); });
    [1, 2].forEach(function (p) { $("poz" + p).addEventListener("click", function () { stan.poziom = p; zapiszWybor(); rysujListe(); }); });
    $("doListy").addEventListener("click", function () { location.hash = ""; });
    $("grajTeraz").addEventListener("click", function () {
      var gw = wczytajGw();
      var tu = GRY.filter(function (g) { return g.size === stan.rozmiar && g.poziom === stan.poziom; });
      var pierwsza = tu.filter(function (g) { return gw.indexOf(g.id) < 0; })[0] || tu[0] || GRY[0];
      location.hash = "gra-" + pierwsza.id;
    });
    $("nastepna").addEventListener("click", nastepna);
    $("jeszczeRaz").addEventListener("click", function () { $("brawo").hidden = true; naStart(); });
    window.addEventListener("hashchange", trasa);
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
    stan: stan
  };
})();
