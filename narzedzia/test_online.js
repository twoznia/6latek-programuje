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
  if (bledy.length) { console.log(bledy.join("\n")); process.exitCode = 1; }
  await browser.close();
})();
