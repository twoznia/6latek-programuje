# -*- coding: utf-8 -*-
COL = {"idz":"#2e9e4f","lewo":"#2b6fd6","prawo":"#f08a1c","obroc":"#8a4fd1","num":"#444"}
UP = '<path d="M50 8 L84 46 L61 46 L61 92 L39 92 L39 46 L16 46 Z" fill="currentColor"/>'
RIGHT = ('<path d="M34 92 L34 52 Q34 30 56 30 L64 30" stroke="currentColor" stroke-width="17" fill="none"/>'
         '<path d="M60 8 L92 30 L60 52 Z" fill="currentColor"/>')
UTURN = ('<path d="M70 92 L70 42 Q70 14 47 14 Q24 14 24 42 L24 56" stroke="currentColor" stroke-width="16" fill="none"/>'
         '<path d="M6 54 L42 54 L24 86 Z" fill="currentColor"/>')
def icon(kind, size):
    body = {"idz":UP,"prawo":RIGHT,"lewo":RIGHT,"obroc":UTURN}[kind]
    tr = ' transform="translate(100,0) scale(-1,1)"' if kind=="lewo" else ''
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" style="color:{COL[kind]}"><g{tr}>{body}</g></svg>'

LABEL = {"idz":("IDŹ",""),"prawo":("SKRĘĆ","W PRAWO"),"lewo":("SKRĘĆ","W LEWO"),"obroc":("OBRÓĆ","SIĘ")}
HINT = {"idz":"1 krok do przodu","prawo":"obrót w miejscu","lewo":"obrót w miejscu","obroc":"obrót tyłem do przodu"}
def cmd_card(k):
    a,b = LABEL[k]; c=COL[k]
    return f'''<div class="card cmd2" style="border-color:{c}">
      <div class="op">{icon(k,"50mm")}<div class="lbl" style="color:{c}">{a}<br>{b or "&nbsp;"}</div></div>
      <div class="slot" style="border-color:{c};background:{c}14"><span style="color:{c}">×</span></div></div>'''

DOTS = {1:[(50,50)],2:[(28,28),(72,72)],3:[(25,25),(50,50),(75,75)],4:[(28,28),(72,28),(28,72),(72,72)],
        5:[(26,26),(74,26),(50,50),(26,74),(74,74)],6:[(28,22),(72,22),(28,50),(72,50),(28,78),(72,78)]}
WORD = {1:"JEDEN",2:"DWA",3:"TRZY",4:"CZTERY",5:"PIĘĆ",6:"SZEŚĆ"}
def num_card(n):
    d = "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#e23b3b"/>' for x,y in DOTS[n])
    return f'''<div class="num2"><div class="big">{n}</div>
      <svg viewBox="0 0 100 100" width="22mm" height="22mm"><rect x="3" y="3" width="94" height="94" rx="14" fill="none" stroke="#ccc" stroke-width="3"/>{d}</svg>
      <div class="word">{WORD[n]}</div></div>'''

STAR = lambda cx,cy,r: '<polygon fill="#f5c400" stroke="#b88f00" stroke-width="1.5" points="'+" ".join(
    f"{cx+ (r if i%2==0 else r*0.45)*__import__('math').sin(i*3.14159/5):.1f},{cy- (r if i%2==0 else r*0.45)*__import__('math').cos(i*3.14159/5):.1f}" for i in range(10))+'"/>'
def robot(cx,cy,r,dirn):
    ang={"up":0,"right":90,"down":180,"left":270}[dirn]
    return (f'<g transform="rotate({ang} {cx} {cy})"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#2b6fd6"/>'
            f'<polygon points="{cx},{cy-r*0.75} {cx+r*0.5},{cy+r*0.35} {cx-r*0.5},{cy+r*0.35}" fill="#fff"/></g>')

def big_tile(kind):
    if kind=="start":
        g = robot(50,45,32,"up"); t="START"; c="#2b6fd6"
    else:
        g = STAR(50,45,36); t="SKARB"; c="#b88f00"
    return f'<div class="card tile"><svg viewBox="0 0 100 90" width="70mm" height="63mm">{g}</svg><div class="lbl" style="color:{c}">{t}</div></div>'

def grid(robot_rc, rdir, skarb, klocki=()):
    s=20; o=4; n=5
    out=[f'<svg viewBox="0 0 {n*s+2*o} {n*s+2*o}" width="50mm" height="50mm">']
    for r in range(n):
        for c in range(n):
            out.append(f'<rect x="{o+c*s}" y="{o+r*s}" width="{s}" height="{s}" fill="#fafafa" stroke="#999" stroke-width="0.8"/>')
    for (r,c) in klocki:
        out.append(f'<rect x="{o+(c-1)*s+2}" y="{o+(r-1)*s+2}" width="{s-4}" height="{s-4}" rx="3" fill="#a0522d"/>'
                   f'<circle cx="{o+(c-1)*s+7}" cy="{o+(r-1)*s+7}" r="2" fill="#c97a4a"/><circle cx="{o+(c-1)*s+13}" cy="{o+(r-1)*s+7}" r="2" fill="#c97a4a"/>')
    r,c=skarb; out.append(STAR(o+(c-.5)*s,o+(r-.5)*s,8))
    r,c=robot_rc; out.append(robot(o+(c-.5)*s,o+(r-.5)*s,7.5,rdir))
    out.append('</svg>'); return "".join(out)

def chip(k,n=None):
    a,b=LABEL[k]
    t = f'{icon(k,"6mm")}<span style="color:{COL[k]}">{a} {b}</span>'
    if n: t += f'<b class="n">×{n}</b>'
    return f'<span class="chip">{t}</span>'

MISSIONS = [
 ("1. Prosto do skarbu","Robot patrzy w górę. Ile kroków do skarbu?",((5,3),"up",(2,3),()),[("idz",3)]),
 ("2. W prawo!","Najpierw trzeba się obrócić.",((4,1),"up",(4,4),()),[("prawo",None),("idz",3)]),
 ("3. Za rogiem","Idź, skręć, idź.",((5,4),"up",(2,2),()),[("idz",3),("lewo",None),("idz",2)]),
 ("4. Skarb za plecami","Robot nie widzi skarbu. Co zrobić?",((2,3),"up",(5,3),()),[("obroc",None),("idz",3)]),
 ("5. Omiń klocek","Na klocek nie wolno wejść!",((5,2),"up",(1,3),((3,2),)),[("idz",1),("prawo",None),("idz",1),("lewo",None),("idz",3)]),
 ("6. Wyzwanie","Ułóż program z jak najmniejszej liczby kart.",((5,1),"up",(1,5),((1,1),(5,5))),[("idz",2),("prawo",None),("idz",4),("lewo",None),("idz",2)]),
]

def mission(m):
    t,d,g,_ = m
    boxes = "".join('<span class="box"></span>' for _ in range(6))
    return f'<div class="mis"><h3>{t}</h3><p>{d}</p>{grid(*g)}<div class="prog">{boxes}</div></div>'

cmds = ["idz"]*7 + ["prawo"]*3 + ["lewo"]*3 + ["obroc"]*3
pages=[]
pages.append(open("intro.html",encoding="utf-8").read().replace("Karta liczby kładziona za poleceniem mówi, ile razy je wykonać.","Każda karta polecenia ma z boku okienko z ×. Wkładamy tam kartę liczby, która mówi, ile razy wykonać polecenie.").replace("Polecenie bez liczby wykonujemy raz.","Puste okienko oznacza: raz.").replace("{{LEG}}",
   "".join(f'<div class="leg">{icon(k,"12mm")}<div><b style="color:{COL[k]}">{" ".join(LABEL[k]).strip()}</b><br>{HINT[k]}</div></div>' for k in ["idz","prawo","lewo","obroc"])))
for i in range(0,len(cmds),4):
    pages.append('<section class="page land cards4l">'+"".join(cmd_card(k) for k in cmds[i:i+4])+'</section>')
pages.append('<section class="page land nums">'+"".join(num_card(n) for n in list(range(1,7))*2)+'</section>')
pages.append('<section class="page cards4">'+"".join(big_tile(k) for k in ["start","skarb","skarb","skarb"])+'</section>')
pages.append('<section class="page"><h1 class="mh">Misje — poziom 1</h1><p class="sub">Niebieskie kółko to robot (biały trójkąt pokazuje, gdzie patrzy). Gwiazdka to skarb. Brązowy kwadrat to klocek. Ułóż karty, a potem sprawdź na podłodze albo figurką. W kratkach możesz narysować strzałki.</p><div class="misgrid">'
             +"".join(mission(m) for m in MISSIONS)+'</div></section>')
ans = "".join(f'<div class="ans"><b>{m[0]}</b><div>'+"".join(chip(k,n) for k,n in m[3])+'</div></div>' for m in MISSIONS)
pages.append(f'<section class="page"><h1 class="mh">Rozwiązania dla dorosłego</h1><p class="sub">To przykładowe rozwiązania. Każdy program, który dojdzie do skarbu bez wchodzenia na klocek, jest dobry.</p>{ans}'
             + open("outro.html",encoding="utf-8").read() + '</section>')
html = open("head.html",encoding="utf-8").read().replace("</style>",open("v2.css",encoding="utf-8").read()+"</style>") + "".join(pages) + "</body></html>"
open("robot2.html","w",encoding="utf-8").write(html)
