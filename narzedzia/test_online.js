// Test gry online: każde rozwiązanie z gra/gry.js musi dać BRAWO w prawdziwej grze (index.html).
// Użycie: node narzedzia/test_online.js   (potrzebny Playwright z Chromium)
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const url = "file://" + path.resolve(__dirname, "..", "index.html");
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const bledy = [];
  page.on("pageerror", (e) => bledy.push("JS: " + e.message));
  await page.goto(url);
  const gry = await page.evaluate(() => window.GRY.map((g) => ({ id: g.id, rozw: g.rozwiazanie, w: (g.warianty || []).length })));
  await page.evaluate(() => window.RobotGra.ustawTempo(0));
  let ok = 0;
  for (const g of gry) {
    await page.evaluate((id) => { location.hash = "gra-" + id; }, g.id);
    await page.waitForFunction((id) => window.RobotGra.stan.gra && window.RobotGra.stan.gra.id === id, g.id);
    await page.evaluate((r) => window.RobotGra.ustawProgram(r), g.rozw);
    await page.click("#start");
    await page.waitForFunction(() => !document.getElementById("brawo").hidden || !window.RobotGra.stan.biegnie, null, { timeout: 20000 });
    await page.waitForTimeout(5);
    const wynik = await page.evaluate(() => ({ brawo: !document.getElementById("brawo").hidden, k: document.getElementById("komunikat").textContent }));
    if (wynik.brawo) ok++; else bledy.push(`${g.id}: ${wynik.k}`);
    await page.evaluate(() => { document.getElementById("brawo").hidden = true; });
  }
  console.log(`OK ${ok} z ${gry.length}`);
  // przykłady z pomocy (gra/pomoc.js): „Wypróbuj” wkłada gotowy program, START musi dać BRAWO
  const przyklady = await page.evaluate(() => window.RobotGra.przyklady());
  let okP = 0;
  for (const id of przyklady) {
    await page.evaluate((id) => { location.hash = "przyklad-" + id; }, id);
    await page.waitForFunction((id) => window.RobotGra.stan.gra && window.RobotGra.stan.gra.id === "przyklad-" + id, id);
    await page.click("#start");
    await page.waitForFunction(() => !document.getElementById("brawo").hidden || !window.RobotGra.stan.biegnie, null, { timeout: 20000 });
    await page.waitForTimeout(5);
    const wynik = await page.evaluate(() => ({ brawo: !document.getElementById("brawo").hidden, k: document.getElementById("komunikat").textContent }));
    if (wynik.brawo) okP++; else bledy.push(`przykład ${id}: ${wynik.k}`);
    await page.evaluate(() => { document.getElementById("brawo").hidden = true; });
  }
  console.log(`Przykłady w pomocy: OK ${okP} z ${przyklady.length}`);
  // złe programy w grach z literami i monetami: gra ma powiedzieć, co jest nie tak (bez BRAWO)
  const zle = [
    { id: "5-97", program: [["IDŹ", 3]], tekst: "Masz KO" },
    { id: "5-101", program: [["IDŹ", 1], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 1], ["SKRĘĆ W LEWO", 1], ["IDŹ", 1]], tekst: "To litera K, a teraz trzeba litery S" },
    { id: "5-107", program: [["IDŹ", 2], ["SKRĘĆ W PRAWO", 1], ["IDŹ", 2]], tekst: "Litera T teraz nie pasuje" },
    { id: "5-113", program: [["IDŹ", 2]], tekst: "Masz 2, a trzeba 5" },
  ];
  for (const z of zle) {
    await page.evaluate((id) => { location.hash = "gra-" + id; }, z.id);
    await page.waitForFunction((id) => window.RobotGra.stan.gra && window.RobotGra.stan.gra.id === id, z.id);
    await page.evaluate((p) => window.RobotGra.ustawProgram({ program: p }), z.program);
    await page.click("#start");
    await page.waitForFunction(() => !document.getElementById("brawo").hidden || !window.RobotGra.stan.biegnie, null, { timeout: 20000 });
    await page.waitForTimeout(5);
    const w = await page.evaluate(() => ({ brawo: !document.getElementById("brawo").hidden, k: document.getElementById("komunikat").textContent }));
    if (w.brawo || w.k.indexOf(z.tekst) < 0) bledy.push(`zły program ${z.id}: ${w.brawo ? "BRAWO" : w.k}`);
    await page.evaluate(() => { document.getElementById("brawo").hidden = true; });
  }
  console.log(`Złe programy (litery i monety): sprawdzone ${zle.length}`);
  if (bledy.length) { console.log(bledy.join("\n")); process.exitCode = 1; }
  await browser.close();
})();
