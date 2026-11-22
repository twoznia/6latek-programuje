#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zamienia pliki poziomy/*.md na strony do druku (HTML, a jeśli jest Chrome, to też PDF).

Użycie:
    python3 narzedzia/drukuj.py              # wszystkie poziomy
    python3 narzedzia/drukuj.py poziomy/poziom-1.md
    python3 narzedzia/drukuj.py --bez-pdf    # tylko HTML (wydrukuj z przeglądarki: Ctrl+P)

Wymaga tylko Pythona 3 (bez dodatkowych pakietów). PDF powstaje, jeśli na komputerze
jest Chrome, Chromium albo Edge. Wyniki trafiają do katalogu druk/.

Specjalne bloki w plikach .md (w ```):
    karty      lista kart do wycięcia, np. "IDŹ ×6", "LICZBY 1-6 ×2", "LAWA ×4"
    legenda    "NAZWA: opis" - legenda poleceń z ikonami
    plansza    siatka pól: . puste, ^ > v < robot, * skarb, # klocek, L lawa, K kałuża, ? niewiadoma
    program    program; wcięcie 2 spacje = wnętrze POWTÓRZ/JEŚLI; "A, B, C" w jednej linii = karty w rzędzie
Linia "---" zaczyna nową stronę. Strona z tytułem "Misje..." układa sekcje ### w ramki misji.
"""
import html, math, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ karty i ikony
COL = {"idz":"#2e9e4f","lewo":"#2b6fd6","prawo":"#f08a1c","obroc":"#8a4fd1","skocz":"#0c8599",
       "powtorz":"#d6336c","koniec":"#495057","jesli":"#b08900","stop":"#e03131","meta":"#212529"}
LABEL = {"idz":("IDŹ",""),"prawo":("SKRĘĆ","W PRAWO"),"lewo":("SKRĘĆ","W LEWO"),"obroc":("OBRÓĆ","SIĘ"),
         "skocz":("SKOCZ",""),"powtorz":("POWTÓRZ",""),"koniec":("KONIEC",""),"jesli":("JEŚLI",""),
         "stop":("STOP",""),"meta":("META","")}
CMD = {" ".join(x for x in v if x): k for k, v in LABEL.items()}
SLOT = {"koniec":None, "stop":None, "meta":None, "jesli":"?"}
COND = {"lawa":("LAWA?","#e03131"),"kaluza":("KAŁUŻA?","#1c7ed6"),"skarb":("SKARB?","#b88f00"),"sciana":("ŚCIANA?","#a0522d")}
COND_BY_NAME = {v[0]: k for k, v in COND.items()}

ICON = {
 "idz":'<path d="M50 8 L84 46 L61 46 L61 92 L39 92 L39 46 L16 46 Z" fill="currentColor"/>',
 "prawo":'<path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/><path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/>',
 "obroc":'<path d="M70 92 L70 42 Q70 14 47 14 Q24 14 24 42 L24 56" stroke="currentColor" stroke-width="16" fill="none"/><path d="M6 54 L42 54 L24 86 Z" fill="currentColor"/>',
 "skocz":'<circle cx="45" cy="84" r="9" fill="currentColor" opacity=".35"/><path d="M10 88 C 16 16, 72 8, 80 64" stroke="currentColor" stroke-width="13" fill="none"/><polygon points="64,60 96,60 80,94" fill="currentColor"/>',
 "powtorz":'<path d="M80 52 A30 30 0 1 1 66 26" stroke="currentColor" stroke-width="13" fill="none"/><path d="M52 6 L84 26 L54 44 Z" fill="currentColor"/>',
 "koniec":'<path d="M28 12 L68 12 L68 88 L28 88" stroke="currentColor" stroke-width="14" fill="none" stroke-linejoin="round"/>',
 "jesli":'<text x="50" y="84" text-anchor="middle" font-size="96" font-weight="800" font-family="Inter,DejaVu Sans,Arial" fill="currentColor">?</text>',
 "stop":'<polygon points="30,6 70,6 94,30 94,70 70,94 30,94 6,70 6,30" fill="currentColor"/><rect x="24" y="44" width="52" height="12" rx="3" fill="#fff"/>',
 "meta":'<rect x="14" y="6" width="7" height="90" fill="currentColor"/>' + "".join(
     f'<rect x="{21+c*17}" y="{8+r*14}" width="17" height="14" fill="{"currentColor" if (r+c)%2==0 else "#fff"}" stroke="currentColor" stroke-width="1.5"/>'
     for r in range(4) for c in range(4)),
}

def icon(kind, size):
    body = ICON["prawo" if kind == "lewo" else kind]
    tr = ' transform="translate(100,0) scale(-1,1)"' if kind == "lewo" else ''
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" style="color:{COL[kind]}"><g{tr}>{body}</g></svg>'

def lab(k):
    return " ".join(x for x in LABEL[k] if x)

def cmd_card(k):
    a, b = LABEL[k]; c = COL[k]; slot = SLOT.get(k, "×")
    s = (f'<div class="slot" style="border-color:{c};background:{c}14"><span style="color:{c}">{slot}</span></div>' if slot else '')
    return (f'<div class="card cmd2{" noslot" if not slot else ""}" style="border-color:{c}">'
            f'<div class="op">{icon(k,"50mm")}<div class="lbl" style="color:{c}">{a}<br>{b or "&nbsp;"}</div></div>{s}</div>')

DOTS = {1:[(50,50)],2:[(28,28),(72,72)],3:[(25,25),(50,50),(75,75)],4:[(28,28),(72,28),(28,72),(72,72)],
        5:[(26,26),(74,26),(50,50),(26,74),(74,74)],6:[(28,22),(72,22),(28,50),(72,50),(28,78),(72,78)]}
WORD = {1:"JEDEN",2:"DWA",3:"TRZY",4:"CZTERY",5:"PIĘĆ",6:"SZEŚĆ",7:"SIEDEM",8:"OSIEM",9:"DZIEWIĘĆ",10:"DZIESIĘĆ"}

def small(inner, word, border="#444", top=""):
    wc = border if border != "#444" else "#222"
    return f'<div class="num2" style="border-color:{border}">{top}{inner}<div class="word" style="color:{wc}">{word}</div></div>'

def num_card(n):
    if n in DOTS:
        d = "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#e23b3b"/>' for x, y in DOTS[n])
        inner = f'<svg viewBox="0 0 100 100" width="22mm" height="22mm"><rect x="3" y="3" width="94" height="94" rx="14" fill="none" stroke="#ccc" stroke-width="3"/>{d}</svg>'
    else:
        inner = ''
    return small(inner, WORD.get(n, ""), top=f'<div class="big">{n}</div>')

def inf_card():
    return small('', "ZAWSZE", top='<div class="big" style="font-size:64pt">∞</div>')

def waves(color, ys, sw=5):
    return "".join(f'<path d="M8 {y} q10 -8 20 0 t20 0 t20 0 t20 0" stroke="{color}" stroke-width="{sw}" fill="none"/>' for y in ys)

def star(cx, cy, r):
    pts = " ".join(f"{cx+(r if i%2==0 else r*0.45)*math.sin(i*math.pi/5):.1f},{cy-(r if i%2==0 else r*0.45)*math.cos(i*math.pi/5):.1f}" for i in range(10))
    return f'<polygon fill="#f5c400" stroke="#b88f00" stroke-width="1.5" points="{pts}"/>'

def tile_svg(kind):
    if kind == "lawa":
        return '<rect x="2" y="2" width="96" height="96" rx="10" fill="#e03131"/>' + waves("#ffa94d", (30,52,74))
    if kind == "kaluza":
        return '<rect x="2" y="2" width="96" height="96" rx="10" fill="#a5d8ff"/>' + waves("#1c7ed6", (30,52,74))
    if kind == "skarb":
        return star(50, 52, 44)
    rows = "".join(f'<rect x="{x}" y="{y}" width="28" height="18" rx="2" fill="#c0603a"/>'
                   for i, y in enumerate((8,30,52,74)) for x in ((4,36,68) if i%2==0 else (-12,20,52,84)))
    return f'<clipPath id="cw"><rect x="2" y="2" width="96" height="96" rx="8"/></clipPath><g clip-path="url(#cw)"><rect width="100" height="100" fill="#f1d3c3"/>{rows}</g>'

def cond_card(k):
    w, c = COND[k]
    return small(f'<svg viewBox="0 0 100 100" width="28mm" height="28mm">{tile_svg(k)}</svg>', w, border=c)

def yesno_card(yes):
    c = "#2e9e4f" if yes else "#e03131"
    mark = ('<path d="M26 52 L44 70 L76 32" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if yes
            else '<path d="M32 32 L68 68 M68 32 L32 68" stroke="#fff" stroke-width="12" stroke-linecap="round"/>')
    return small(f'<svg viewBox="0 0 100 100" width="28mm" height="28mm"><circle cx="50" cy="50" r="46" fill="{c}"/>{mark}</svg>', "TAK" if yes else "NIE", border=c)

def robot(cx, cy, r, dirn):
    ang = {"^":0, ">":90, "v":180, "<":270}[dirn]
    return (f'<g transform="rotate({ang} {cx} {cy})"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#2b6fd6"/>'
            f'<polygon points="{cx},{cy-r*0.75} {cx+r*0.5},{cy+r*0.35} {cx-r*0.5},{cy+r*0.35}" fill="#fff"/></g>')

def big_tile(kind):
    if kind == "start":
        return f'<div class="card tile"><svg viewBox="0 0 100 90" width="70mm" height="63mm">{robot(50,45,32,"^")}</svg><div class="lbl" style="color:#2b6fd6">START</div></div>'
    if kind == "skarb":
        return f'<div class="card tile"><svg viewBox="0 0 100 90" width="70mm" height="63mm">{star(50,45,36)}</svg><div class="lbl" style="color:#b88f00">SKARB</div></div>'
    bg, fg, wc, word = (("#e03131","#fff","#ffa94d","LAWA") if kind == "lawa" else ("#a5d8ff","#0b4f8a","#1c7ed6","KAŁUŻA"))
    w = "".join(f'<path d="M5 {y} q11 -9 22.5 0 t22.5 0 t22.5 0 t22.5 0" stroke="{wc}" stroke-width="4" fill="none"/>' for y in (15,40,65,90))
    return (f'<div class="card tile" style="background:{bg};border-color:{bg}"><svg viewBox="0 0 100 100" width="76mm" height="76mm">{w}</svg>'
            f'<div class="lbl" style="color:{fg}">{word}</div></div>')

# ------------------------------------------------------------------ bloki specjalne
COUNT_RE = re.compile(r'^(.*?)\s*[×x]\s*(\d+|∞)\s*$')

def split_count(t):
    m = COUNT_RE.match(t.strip())
    return (m.group(1).strip(), m.group(2)) if m else (t.strip(), None)

def block_karty(lines):
    cmds, smalls, tiles = [], [], []
    for line in lines:
        if not line.strip():
            continue
        name, n = split_count(line)
        n = int(n) if n and n != "∞" else 1
        m = re.match(r'^LICZBY\s+(\d+)\s*-\s*(\d+)$', name)
        if m:
            smalls += [num_card(i) for i in range(int(m.group(1)), int(m.group(2)) + 1)] * n
        elif name in CMD:
            cmds += [cmd_card(CMD[name])] * n
        elif name in COND_BY_NAME:
            smalls += [cond_card(COND_BY_NAME[name])] * n
        elif name in ("TAK", "NIE"):
            smalls += [yesno_card(name == "TAK")] * n
        elif name in ("ZAWSZE", "∞"):
            smalls += [inf_card()] * n
        elif name in ("START", "SKARB", "LAWA", "KAŁUŻA"):
            tiles += [big_tile({"START":"start","SKARB":"skarb","LAWA":"lawa","KAŁUŻA":"kaluza"}[name])] * n
        else:
            sys.exit(f"Nieznana karta: {name!r}")
    out = []
    out += [f'<section class="page land cards4l">{"".join(cmds[i:i+4])}</section>' for i in range(0, len(cmds), 4)]
    out += [f'<section class="page land nums">{"".join(smalls[i:i+12])}</section>' for i in range(0, len(smalls), 12)]
    out += [f'<section class="page cards4">{"".join(tiles[i:i+4])}</section>' for i in range(0, len(tiles), 4)]
    return out

def block_legenda(lines):
    items = []
    for line in lines:
        if ":" not in line:
            continue
        name, desc = line.split(":", 1)
        k = CMD[name.strip()]
        items.append(f'<div class="leg">{icon(k,"12mm")}<div><b style="color:{COL[k]}">{lab(k)}</b><br>{inline(desc.strip())}</div></div>')
    return f'<div class="legs">{"".join(items)}</div>'

def block_plansza(lines):
    rows = [l.split() for l in lines if l.strip()]
    s, o = 20, 4
    h, w = len(rows), max(len(r) for r in rows)
    out = [f'<svg class="plansza" viewBox="0 0 {w*s+2*o} {h*s+2*o}" width="{50*w/5:.0f}mm" height="{50*h/5:.0f}mm">']
    for r in range(h):
        for c in range(w):
            out.append(f'<rect x="{o+c*s}" y="{o+r*s}" width="{s}" height="{s}" fill="#fafafa" stroke="#999" stroke-width="0.8"/>')
    for r, row in enumerate(rows):
        for c, t in enumerate(row):
            x, y = o + c*s, o + r*s
            if t == "#":
                out.append(f'<rect x="{x+2}" y="{y+2}" width="{s-4}" height="{s-4}" rx="3" fill="#a0522d"/><circle cx="{x+7}" cy="{y+7}" r="2" fill="#c97a4a"/><circle cx="{x+13}" cy="{y+7}" r="2" fill="#c97a4a"/>')
            elif t in ("L", "K"):
                fill, wc = ("#e03131","#ffa94d") if t == "L" else ("#a5d8ff","#1c7ed6")
                out.append(f'<rect x="{x+.6}" y="{y+.6}" width="{s-1.2}" height="{s-1.2}" fill="{fill}"/>'
                           + "".join(f'<path d="M{x+3} {y+yy} q3.5 -3 7 0 t7 0" stroke="{wc}" stroke-width="1.6" fill="none"/>' for yy in (7,14)))
            elif t == "?":
                out.append(f'<text x="{x+s/2}" y="{y+s/2+5}" text-anchor="middle" font-size="14" font-weight="800" font-family="Inter,DejaVu Sans,Arial" fill="#b08900">?</text>')
            elif t == "*":
                out.append(star(x+s/2, y+s/2, 8))
            elif t in "^><v":
                out.append(robot(x+s/2, y+s/2, 7.5, t))
    out.append('</svg>')
    return "".join(out)

def chip(k, n=None):
    t = f'{icon(k,"6mm")}<span style="color:{COL[k]}">{lab(k)}</span>'
    if n and n != "1":
        t += f'<b class="n">×{n}</b>'
    return f'<span class="chip">{t}</span>'

def cchip(k):
    w, c = COND[k]
    return f'<span class="chip"><svg viewBox="0 0 100 100" width="6mm" height="6mm">{tile_svg(k)}</svg><span style="color:{c}">{w}</span></span>'

def ynchip(yes):
    return f'<span class="chip yn" style="color:{"#2e9e4f" if yes else "#e03131"}">{"✓ TAK" if yes else "✗ NIE"}</span>'

def item_chip(t):
    name, n = split_count(t)
    if name in CMD:
        return chip(CMD[name], n)
    if name in COND_BY_NAME:
        return cchip(COND_BY_NAME[name])
    sys.exit(f"Nieznane polecenie w programie: {t!r}")

def block_program(lines, title=""):
    rows = []
    for line in lines:
        if not line.strip():
            continue
        ind = (len(line) - len(line.lstrip(" "))) // 2
        t = line.strip()
        if t.startswith("JEŚLI "):
            html_ = chip("jesli") + item_chip(t[6:])
        elif t[:4] in ("TAK:", "NIE:"):
            html_ = ynchip(t.startswith("TAK")) + "".join(item_chip(x) for x in t[4:].split(",") if x.strip())
        else:
            html_ = "".join(item_chip(x) for x in t.split(","))
        rows.append(f'<div class="pl" style="margin-left:{ind*9}mm">{html_}</div>')
    head = f'<b class="ptitle">{html.escape(title)}</b>' if title else ""
    return f'<div class="given">{head}{"".join(rows)}</div>'

# ------------------------------------------------------------------ prosty Markdown
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    return t

def render_blocks(lines):
    """Zwraca listę (rodzaj, html). Rodzaje: h1,h2,h3,p,ul,ol,tip,special,karty."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1; continue
        if s.startswith("```"):
            info = s[3:].strip().split(None, 1)
            kind = info[0] if info else ""
            arg = info[1] if len(info) > 1 else ""
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i]); i += 1
            i += 1
            if kind == "karty":
                out.append(("karty", block_karty(body)))
            elif kind == "legenda":
                out.append(("special", block_legenda(body)))
            elif kind == "plansza":
                out.append(("plansza", block_plansza(body)))
            elif kind == "program":
                out.append(("program", block_program(body, arg)))
            else:
                out.append(("special", f'<pre>{html.escape(chr(10).join(body))}</pre>'))
            continue
        m = re.match(r'^(#{1,3})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1))
            out.append((f"h{lvl}", f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')); i += 1; continue
        if s.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append(("tip", f'<div class="tip">{inline(" ".join(buf))}</div>')); continue
        if re.match(r'^(-|\d+\.)\s', s):
            ordered = bool(re.match(r'^\d+\.', s))
            items = []
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("```", "#", ">")):
                t = lines[i].strip()
                mm = re.match(r'^(-|\d+\.)\s+(.*)$', t)
                if mm:
                    items.append(mm.group(2))
                elif items:
                    items[-1] += " " + t
                i += 1
            tag = "ol" if ordered else "ul"
            out.append((tag, f'<{tag}>' + "".join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("```", "#", "> ", "- ")) \
                and not re.match(r'^\d+\.\s', lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append(("p", f'<p>{inline(" ".join(buf))}</p>'))
    return out

BOXES = '<div class="prog">' + '<span class="box"></span>' * 6 + '</div>'

def render_page(lines):
    blocks = render_blocks(lines)
    sections, cur = [], []
    heads = [h for k, h in blocks if k in ("h1", "h2")]
    missions = bool(heads) and re.sub('<[^>]+>', '', heads[0]).startswith("Misje")

    def flush():
        if cur:
            sections.append(f'<section class="page">{"".join(cur)}</section>')
            cur.clear()

    if not missions:
        for k, h in blocks:
            if k == "karty":
                flush(); sections += h
            else:
                cur.append(h)
        flush()
        return sections

    # strona z misjami: każde ### to ramka
    pre, boxes, box, post = [], [], None, None
    for k, h in blocks:
        if post is not None or (k in ("h1", "h2") and box is not None):
            post = (post or []) + [h]
        elif k == "h3":
            box = [h]; boxes.append(box)
        elif box is None:
            pre.append(h)
        else:
            box.append((k, h) if k in ("plansza", "program") else h)
    html_boxes = []
    for b in boxes:
        parts, progs, has_plansza = [b[0]], [], False
        for x in b[1:]:
            if isinstance(x, tuple):
                if x[0] == "program":
                    progs.append(x[1])
                else:
                    has_plansza = True; parts.append(x[1])
            else:
                parts.append(x)
        if len(progs) > 1:
            parts.append(f'<div class="two">{"".join(progs)}</div>')
        elif progs:
            parts.append(progs[0])
        elif has_plansza:
            parts.append(BOXES)
        html_boxes.append(f'<div class="mis">{"".join(parts)}</div>')
    sections.append(f'<section class="page">{"".join(pre)}<div class="misgrid">{"".join(html_boxes)}</div>{"".join(post or [])}</section>')
    return sections

def convert(md_path):
    text = open(md_path, encoding="utf-8").read()
    pages, cur = [], []
    for line in text.splitlines():
        if line.strip() == "---":
            pages.append(cur); cur = []
        else:
            cur.append(line)
    pages.append(cur)
    title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "Robot i Programista")
    css = open(os.path.join(ROOT, "narzedzia", "styl.css"), encoding="utf-8").read()
    body = "".join(s for p in pages if any(l.strip() for l in p) for s in render_page(p))
    return (f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{css}</style></head><body>{body}</body></html>')

def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "msedge", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    for p in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
        if os.path.exists(p):
            return p
    return None

def main(argv):
    want_pdf = "--bez-pdf" not in argv
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        d = os.path.join(ROOT, "poziomy")
        files = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md"))
    out_dir = os.path.join(ROOT, "druk")
    os.makedirs(out_dir, exist_ok=True)
    chrome = find_chrome() if want_pdf else None
    if want_pdf and not chrome:
        print("Nie znalazłem Chrome ani Chromium, więc robię tylko HTML. Otwórz go w przeglądarce i wydrukuj (Ctrl+P).")
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        html_path = os.path.join(out_dir, name + ".html")
        with open(html_path, "w", encoding="utf-8") as fh:
            fh.write(convert(f))
        print("HTML:", os.path.relpath(html_path, ROOT))
        if chrome:
            pdf_path = os.path.join(out_dir, name + ".pdf")
            subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={pdf_path}", "file://" + os.path.abspath(html_path)],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("PDF: ", os.path.relpath(pdf_path, ROOT))

if __name__ == "__main__":
    main(sys.argv[1:])
