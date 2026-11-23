// Robot i Programista - wersja online (poziom 1). Dane gier: gra/gry.js (window.GRY).
(function () {
  "use strict";
  var GRY = window.GRY || [];
  var KOLOR = { "IDŹ": "#2e9e4f", "SKRĘĆ W PRAWO": "#f08a1c", "SKRĘĆ W LEWO": "#2b6fd6", "OBRÓĆ SIĘ": "#8a4fd1", "SKOCZ": "#0c8599" };
  var NAPIS = { "IDŹ": ["IDŹ"], "SKRĘĆ W PRAWO": ["SKRĘĆ", "W PRAWO"], "SKRĘĆ W LEWO": ["SKRĘĆ", "W LEWO"], "OBRÓĆ SIĘ": ["OBRÓĆ", "SIĘ"], "SKOCZ": ["SKOCZ"] };
  var IKONA = {
    "IDŹ": '<path d="M50 8 L84 46 L61 46 L61 92 L39 92 L39 46 L16 46 Z" fill="currentColor"/>',
    "SKRĘĆ W PRAWO": '<path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/><path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/>',
    "SKRĘĆ W LEWO": '<g transform="translate(100,0) scale(-1,1)"><path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/><path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/></g>',
    "OBRÓĆ SIĘ": '<path d="M70 92 L70 42 Q70 14 47 14 Q24 14 24 42 L24 56" stroke="currentColor" stroke-width="16" fill="none"/><path d="M6 54 L42 54 L24 86 Z" fill="currentColor"/>',
    "SKOCZ": '<circle cx="45" cy="84" r="9" fill="currentColor" opacity=".35"/><path d="M10 88 C 16 16, 72 8, 80 64" stroke="currentColor" stroke-width="13" fill="none"/><polygon points="64,60 96,60 80,94" fill="currentColor"/>'
  };
  var SLOWO = { 1: "raz", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć" };
  var KIER = "^>v<";
  var DXY = { "^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1] };
  var S = 20, O = 4; // rozmiar pola w SVG i margines
  var MAX = 24;

  var $ = function (id) { return document.getElementById(id); };
  var stan = { gra: null, program: [], wybrana: -1, biegnie: false, robot: null, rozmiar: 5 };

  // ---------- zapamiętane gwiazdki ----------
  function wczytajGw() { try { return JSON.parse(localStorage.getItem("rip-gwiazdki") || "[]"); } catch (e) { return []; } }
  function zapiszGw(id) {
    var g = wczytajGw(); if (g.indexOf(id) < 0) g.push(id);
    try { localStorage.setItem("rip-gwiazdki", JSON.stringify(g)); } catch (e) { /* bez zapisu */ }
  }

  // ---------- mowa ----------
  function powiedz(t) {
    if (!$("glos").checked || !window.speechSynthesis) return;
    try {
      var u = new SpeechSynthesisUtterance(t.toLowerCase());
      u.lang = "pl-PL"; u.rate = 0.9;
      window.speechSynthesis.cancel(); window.speechSynthesis.speak(u);
    } catch (e) { /* brak mowy */ }
  }

  // ---------- rysowanie ----------
  function ikona(nazwa) { return '<svg viewBox="0 0 100 100" aria-hidden="true">' + IKONA[nazwa] + "</svg>"; }
  function gwiazda(cx, cy, r, id) {
    var p = [];
    for (var i = 0; i < 10; i++) {
      var rr = i % 2 === 0 ? r : r * 0.45;
      p.push((cx + rr * Math.sin(i * Math.PI / 5)).toFixed(1) + "," + (cy - rr * Math.cos(i * Math.PI / 5)).toFixed(1));
    }
    return '<polygon ' + (id ? 'id="' + id + '" ' : "") + 'fill="#f5c400" stroke="#b88f00" stroke-width="1.2" points="' + p.join(" ") + '"/>';
  }
  function fale(x, y, kolor) {
    return '<path d="M' + (x + 3) + " " + (y + 7) + ' q3.5 -3 7 0 t7 0" stroke="' + kolor + '" stroke-width="1.6" fill="none"/>' +
           '<path d="M' + (x + 3) + " " + (y + 14) + ' q3.5 -3 7 0 t7 0" stroke="' + kolor + '" stroke-width="1.6" fill="none"/>';
  }
  function rysujPlansze(svg, gra, zRobotem) {
    var rows = gra.plansza.map(function (r) { return r.split(" "); });
    var n = rows.length, w = n * S + 2 * O;
    var h = ['<rect x="0" y="0" width="' + w + '" height="' + w + '" rx="6" fill="#e9dcc6"/>'];
    for (var i = 0; i < n; i++) for (var j = 0; j < n; j++) if ((i + j) % 2) h.push('<rect x="' + (O + j * S) + '" y="' + (O + i * S) + '" width="' + S + '" height="' + S + '" fill="#e2d3b9"/>');
    var start = null;
    rows.forEach(function (r, y) {
      r.forEach(function (t, x) {
        var px = O + x * S, py = O + y * S;
        if (t === "L") h.push('<rect x="' + (px + 1) + '" y="' + (py + 1) + '" width="' + (S - 2) + '" height="' + (S - 2) + '" rx="2" fill="#e03131"/>' + fale(px, py, "#ffa94d"));
        else if (t === "K") h.push('<rect x="' + (px + 1) + '" y="' + (py + 1) + '" width="' + (S - 2) + '" height="' + (S - 2) + '" rx="5" fill="#a5d8ff"/>' + fale(px, py, "#1c7ed6"));
        else if (t === "#") h.push('<rect x="' + (px + 2) + '" y="' + (py + 2) + '" width="' + (S - 4) + '" height="' + (S - 4) + '" rx="3" fill="#a0522d"/><circle cx="' + (px + 7) + '" cy="' + (py + 7) + '" r="2" fill="#c97a4a"/><circle cx="' + (px + 13) + '" cy="' + (py + 7) + '" r="2" fill="#c97a4a"/>');
        else if (t === "*") h.push(gwiazda(px + S / 2, py + S / 2, 8, zRobotem ? "gw-" + y + "-" + x : null));
        else if (KIER.indexOf(t) >= 0) start = { y: y, x: x, d: t };
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
    return { rows: rows, start: start, n: n };
  }
  function ustawRobota(skok) {
    var r = stan.robot, g = $("robot");
    if (!g) return;
    g.classList.toggle("skok", !!skok);
    g.style.transform = "translate(" + (O + r.x * S + S / 2) + "px," + (O + r.y * S + S / 2) + "px) rotate(" + r.kat + "deg)" + (skok ? " scale(1.25)" : "");
    if (skok) setTimeout(function () { g.style.transform = g.style.transform.replace(" scale(1.25)", ""); }, 260);
  }

  // ---------- lista gier ----------
  function rysujListe() {
    var gw = wczytajGw();
    var gry = GRY.filter(function (g) { return g.size === stan.rozmiar; });
    var zest = {};
    gry.forEach(function (g) { (zest[g.zestaw] = zest[g.zestaw] || []).push(g); });
    var html = "";
    Object.keys(zest).sort().forEach(function (z) {
      html += '<div class="zestaw">' + (z ? "<h3>Zestaw " + z + "</h3>" : "") + '<div class="lista">';
      zest[z].forEach(function (g) {
        var done = gw.indexOf(g.id) >= 0;
        html += '<button class="kafel' + (done ? " done" : "") + '" data-id="' + g.id + '"><span class="nr">' + g.nr + '</span><span class="t">' + g.tytul + '</span><span class="s">' + (done ? "★ zrobione" : "") + "</span></button>";
      });
      html += "</div></div>";
    });
    $("lista").innerHTML = html;
    var wszystkie = gry.length, zrobione = gry.filter(function (g) { return gw.indexOf(g.id) >= 0; }).length;
    $("postep").textContent = "Gwiazdki: " + zrobione + " z " + wszystkie;
    $("tab5").setAttribute("aria-selected", stan.rozmiar === 5);
    $("tab7").setAttribute("aria-selected", stan.rozmiar === 7);
    $("tab9").setAttribute("aria-selected", stan.rozmiar === 9);
  }

  // ---------- gra ----------
  function otworz(id) {
    var gra = GRY.filter(function (g) { return g.id === id; })[0];
    if (!gra) { pokazStart(); return; }
    stan.gra = gra; stan.program = []; stan.wybrana = -1; stan.biegnie = false;
    $("ekranStart").hidden = true; $("ekranGra").hidden = false; $("doListy").hidden = false;
    $("graTytul").textContent = "Gra " + gra.nr + ": " + gra.tytul + " (" + gra.size + " × " + gra.size + ")";
    $("graOpis").textContent = gra.opis;
    $("rozw").hidden = true;
    $("rozw").innerHTML = gra.rozwiazanie.map(function (c) { return chip(c[0], c[1]); }).join("");
    naStart();
    rysujProgram();
    komunikat("", "");
    window.scrollTo(0, 0);
  }
  function naStart() {
    var info = rysujPlansze($("plansza"), stan.gra, true);
    stan.info = info;
    stan.robot = { y: info.start.y, x: info.start.x, d: info.start.d, kat: KIER.indexOf(info.start.d) * 90 };
    stan.zebrane = {};
    var g = $("robot"); g.style.transition = "none"; ustawRobota(false);
    g.getBoundingClientRect(); g.style.transition = "";
  }
  function chip(nazwa, n, idx, wybrana) {
    return '<button class="chip' + (wybrana ? " wybrana" : "") + '"' + (idx !== undefined ? ' data-i="' + idx + '" aria-pressed="' + !!wybrana + '"' : ' tabindex="-1"') +
           ' style="color:' + KOLOR[nazwa] + '">' + ikona(nazwa) +
           "<span>" + nazwa + "</span>" + (n > 1 ? '<b class="n">×' + n + "</b>" : "") + "</button>";
  }
  // stan.wybrana: numer karty, za którą wstawiamy nową kartę i której zmieniamy liczbę (-1 = przed pierwszą kartą)
  function rysujProgram() {
    var p = stan.program, w = stan.wybrana;
    var kursor = '<span class="kursor" aria-hidden="true"></span>';
    var html = '<button class="poczatek' + (w < 0 ? " wybrana" : "") + '" data-i="-1" aria-label="Wstaw na początek">▶</button>' + (w < 0 && p.length ? kursor : "");
    p.forEach(function (c, i) {
      html += chip(c.k, c.n, i, i === w);
      if (i === w) html += '<button class="usun" data-usun="' + i + '" aria-label="Usuń kartę ' + c.k + '">✕</button>' + (i < p.length - 1 ? kursor : "");
    });
    if (!p.length) html += '<span class="pusto">Dotknij karty poniżej, żeby dodać polecenie.</span>';
    $("program").innerHTML = html;
  }
  function wybierz(i) {
    stan.wybrana = Math.max(-1, Math.min(i, stan.program.length - 1));
    rysujProgram();
  }
  function usun(i) {
    stan.program.splice(i, 1);
    stan.wybrana = Math.min(i - 1 < 0 && stan.program.length ? 0 : i - 1, stan.program.length - 1);
    rysujProgram(); naStart(); komunikat("", "");
  }
  function komunikat(t, typ) { var k = $("komunikat"); k.textContent = t; k.className = "komunikat " + (typ || ""); }

  function dodaj(nazwa) {
    if (stan.biegnie) return;
    if (stan.program.length >= MAX) { komunikat("Program jest już bardzo długi.", "zle"); return; }
    stan.wybrana += 1;
    stan.program.splice(stan.wybrana, 0, { k: nazwa, n: 1 });
    powiedz(nazwa); rysujProgram(); naStart(); komunikat("", "");
  }
  function liczba(n) {
    if (stan.biegnie) return;
    var p = stan.program;
    if (!p.length) { komunikat("Najpierw wybierz kartę polecenia.", "zle"); return; }
    if (stan.wybrana < 0) { komunikat("Dotknij karty w programie, której chcesz zmienić liczbę.", "zle"); return; }
    p[stan.wybrana].n = n;
    powiedz(SLOWO[n] + (n > 1 ? " razy" : ""));
    rysujProgram(); naStart();
  }

  var tempo = 1; // 0 = bez animacji (do testów)
  function czekaj(ms) { return new Promise(function (r) { setTimeout(r, ms * tempo); }); }
  function pole(y, x) {
    var n = stan.info.n;
    if (y < 0 || x < 0 || y >= n || x >= n) return "SCIANA";
    return stan.info.rows[y][x];
  }
  var BLAD = { "L": "Auć! To lawa! Trzeba ją obejść.", "K": "Plusk! Kałużę trzeba przeskoczyć.", "#": "Bum! Tu stoi klocek.", "SCIANA": "Stop! Tu kończy się plansza." };

  async function uruchom() {
    if (stan.biegnie) return;
    if (!stan.program.length) { komunikat("Program jest pusty. Dodaj karty!", "zle"); return; }
    naStart();
    stan.biegnie = true; $("start").disabled = true;
    komunikat("Robot rusza…", "");
    await czekaj(350);
    var chips = $("program").querySelectorAll(".chip");
    var blad = null;
    outer:
    for (var i = 0; i < stan.program.length; i++) {
      var c = stan.program[i];
      chips[i].classList.add("teraz");
      powiedz(c.k + (c.n > 1 ? " " + SLOWO[c.n] + " razy" : ""));
      for (var k = 0; k < c.n; k++) {
        blad = krok(c.k);
        await czekaj(c.k === "SKOCZ" ? 560 : 430);
        if (blad) break outer;
      }
      chips[i].classList.remove("teraz");
    }
    stan.biegnie = false; $("start").disabled = false;
    if (blad) {
      var g = $("robot"); g.classList.add("potrzasnij");
      setTimeout(function () { g.classList.remove("potrzasnij"); }, 500);
      komunikat(blad + " Popraw program i spróbuj jeszcze raz.", "zle");
      return;
    }
    var gw = stan.info.rows.reduce(function (a, r) { return a + r.filter(function (t) { return t === "*"; }).length; }, 0);
    var mam = Object.keys(stan.zebrane).length;
    var naStarcie = stan.robot.y === stan.info.start.y && stan.robot.x === stan.info.start.x;
    if (mam < gw) { komunikat(mam ? "Jest " + mam + " z " + gw + " skarbów. Robot musi iść dalej!" : "Robot stanął, ale skarb jest dalej.", "zle"); return; }
    if (stan.gra.powrot && !naStarcie) { komunikat("Masz skarb! Teraz wróć na START.", "zle"); return; }
    sukces();
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
    if (BLAD[t]) {
      // robot dochodzi do krawędzi pola i wraca
      return BLAD[t];
    }
    r.y = y; r.x = x; ustawRobota(ile === 2);
    if (t === "*") {
      stan.zebrane[y + "-" + x] = true;
      var s = document.getElementById("gw-" + y + "-" + x); if (s) s.classList.add("zebrany");
    }
    return null;
  }
  function sukces() {
    zapiszGw(stan.gra.id);
    komunikat("Brawo! Robot ma skarb!", "dobrze");
    powiedz("brawo");
    var n = stan.program.reduce(function (a) { return a + 1; }, 0);
    $("brawoTekst").textContent = "Robot zebrał skarb. Twój program ma " + n + " " + (n === 1 ? "kartę" : (n % 10 >= 2 && n % 10 <= 4 && (n < 10 || n > 20) ? "karty" : "kart")) + ".";
    $("brawo").hidden = false;
    $("nastepna").focus();
  }
  function nastepna() {
    $("brawo").hidden = true;
    var i = GRY.indexOf(stan.gra), nast = GRY[i + 1];
    if (nast && nast.size === stan.gra.size) location.hash = "gra-" + nast.id;
    else location.hash = "";
  }

  // ---------- ekrany i nawigacja ----------
  function pokazStart() {
    $("ekranStart").hidden = false; $("ekranGra").hidden = true; $("doListy").hidden = true; $("brawo").hidden = true;
    rysujListe();
  }
  function trasa() {
    var h = location.hash.replace("#", "");
    var m = h.match(/^gra-(\d+-\d+)$/);
    if (m) { otworz(m[1]); if (stan.gra) stan.rozmiar = stan.gra.size; }
    else pokazStart();
  }

  function init() {
    // karty
    $("karty").innerHTML = Object.keys(KOLOR).map(function (k) {
      return '<button class="karta" data-k="' + k + '" style="color:' + KOLOR[k] + '" aria-label="' + k + '">' + ikona(k) + "<span>" + NAPIS[k].join("<br>") + "</span></button>";
    }).join("");
    $("liczby").innerHTML = [1, 2, 3, 4, 5, 6].map(function (n) { return '<button class="liczba" data-n="' + n + '" aria-label="' + SLOWO[n] + ' razy">' + n + "</button>"; }).join("");
    $("karty").addEventListener("click", function (e) { var b = e.target.closest(".karta"); if (b) dodaj(b.dataset.k); });
    $("liczby").addEventListener("click", function (e) { var b = e.target.closest(".liczba"); if (b) liczba(+b.dataset.n); });
    $("program").addEventListener("click", function (e) {
      if (stan.biegnie) return;
      var u = e.target.closest(".usun"); if (u) { usun(+u.dataset.usun); return; }
      var b = e.target.closest("[data-i]"); if (b) wybierz(+b.dataset.i);
    });
    $("start").addEventListener("click", uruchom);
    $("odNowa").addEventListener("click", function () { if (!stan.biegnie) { naStart(); komunikat("", ""); } });
    $("wyczysc").addEventListener("click", function () { if (!stan.biegnie) { stan.program = []; stan.wybrana = -1; rysujProgram(); naStart(); komunikat("", ""); } });
    $("pokazRozw").addEventListener("click", function () { $("rozw").hidden = !$("rozw").hidden; });
    $("lista").addEventListener("click", function (e) { var b = e.target.closest(".kafel"); if (b) location.hash = "gra-" + b.dataset.id; });
    $("tab5").addEventListener("click", function () { stan.rozmiar = 5; rysujListe(); });
    $("tab7").addEventListener("click", function () { stan.rozmiar = 7; rysujListe(); });
    $("tab9").addEventListener("click", function () { stan.rozmiar = 9; rysujListe(); });
    $("doListy").addEventListener("click", function () { location.hash = ""; });
    $("grajTeraz").addEventListener("click", function () {
      var gw = wczytajGw();
      var pierwsza = GRY.filter(function (g) { return g.size === stan.rozmiar && gw.indexOf(g.id) < 0; })[0] || GRY[0];
      location.hash = "gra-" + pierwsza.id;
    });
    $("nastepna").addEventListener("click", nastepna);
    $("jeszczeRaz").addEventListener("click", function () { $("brawo").hidden = true; naStart(); });
    window.addEventListener("hashchange", trasa);
    // podgląd na stronie startowej
    var demo = GRY.filter(function (g) { return g.id === "5-21"; })[0] || GRY[0];
    if (demo) {
      $("demo").innerHTML = '<svg viewBox="0 0 108 108"></svg>';
      rysujPlansze($("demo").firstChild, demo, false);
    }
    trasa();
  }
  init();
  window.RobotGra = { ustawTempo: function (t) { tempo = t; } };
})();
