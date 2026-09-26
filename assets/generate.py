#!/usr/bin/env python3
"""Generates the animated SVG assets for the GitHub profile README."""
import math
import os
import random
from xml.sax.saxutils import escape

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
random.seed(1337)

MONO = "'JetBrains Mono','Fira Code','SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
CYAN, BLUE, VIOLET, PINK, RED = "#22d3ee", "#3b82f6", "#8b5cf6", "#ec4899", "#ff3b5c"
BG = "#070a18"


def write(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(body)
    print("wrote", name, len(body), "bytes")


def f(x):
    return f"{x:.4f}".rstrip("0").rstrip(".")


# --------------------------------------------------------------------------
# HERO — "Aurora Cipher"
# --------------------------------------------------------------------------
def hero():
    W, H = 1200, 380
    T = 10  # decrypt cycle (s)
    name = "NGUYEN VU LONG"
    pitch, size, ny = 46, 66, 190
    x0 = W / 2 - (len(name) - 1) * pitch / 2
    glyphs = "!<>-_\\/[]{}=+*^?#01$%&@ABCDEFXZ"

    css = [f"""
text{{font-family:{MONO};}}
.blob{{transform-box:fill-box;transform-origin:center;}}
.b1{{animation:d1 14s ease-in-out infinite alternate;}}
.b2{{animation:d2 18s ease-in-out infinite alternate;}}
.b3{{animation:d3 16s ease-in-out infinite alternate;}}
.b4{{animation:d4 20s ease-in-out infinite alternate;}}
@keyframes d1{{0%{{transform:translate(0,0) scale(1)}}100%{{transform:translate(260px,60px) scale(1.3)}}}}
@keyframes d2{{0%{{transform:translate(0,0) scale(1.2)}}100%{{transform:translate(-300px,-40px) scale(.9)}}}}
@keyframes d3{{0%{{transform:translate(0,0) scale(.9)}}100%{{transform:translate(180px,-70px) scale(1.25)}}}}
@keyframes d4{{0%{{transform:translate(0,0) scale(1)}}100%{{transform:translate(-200px,50px) scale(1.2)}}}}
.fl{{animation:fl .5s linear infinite;opacity:0;}}
@keyframes fl{{0%,19.9%{{opacity:1}}20%,100%{{opacity:0}}}}
.bit{{animation:rise linear infinite;}}
@keyframes rise{{0%{{transform:translateY(0);opacity:0}}15%{{opacity:.35}}85%{{opacity:.35}}100%{{transform:translateY(-140px);opacity:0}}}}
.scan{{animation:scan 6s linear infinite;}}
@keyframes scan{{0%{{transform:translateY(-60px)}}100%{{transform:translateY({H + 60}px)}}}}
.spin{{transform-box:fill-box;transform-origin:center;animation:spin 4s linear infinite;}}
.spinr{{transform-box:fill-box;transform-origin:center;animation:spin 9s linear infinite reverse;}}
.spins{{transform-box:fill-box;transform-origin:center;animation:spin 14s linear infinite;}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.blip{{animation:blip 4s ease-out infinite;opacity:0;}}
@keyframes blip{{0%{{opacity:0}}5%{{opacity:1}}40%{{opacity:0}}100%{{opacity:0}}}}
.pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-in-out infinite;}}
@keyframes pulse{{0%,100%{{transform:scale(.85);opacity:.7}}50%{{transform:scale(1.1);opacity:1}}}}
.st1{{animation:st1 {T}s linear infinite;}}
.st2{{animation:st2 {T}s linear infinite;}}
@keyframes st1{{0%,41%{{opacity:1}}42%,90%{{opacity:0}}91%,100%{{opacity:1}}}}
@keyframes st2{{0%,41%{{opacity:0}}42%,90%{{opacity:1}}91%,100%{{opacity:0}}}}
.caret{{animation:caret 1s steps(1) infinite;}}
@keyframes caret{{50%{{opacity:0}}}}
"""]

    chars = []
    for i, ch in enumerate(name):
        if ch == " ":
            continue
        x = x0 + i * pitch
        r = 8 + i * 2.4  # percent at which this letter resolves
        css.append(
            f"@keyframes h{i}{{0%,{f(r)}%{{opacity:1}}{f(r + .2)}%,{f(89 + i * .3)}%{{opacity:0}}{f(89.2 + i * .3)}%,100%{{opacity:1}}}}"
            f"@keyframes s{i}{{0%,{f(r)}%{{opacity:0}}{f(r + .2)}%{{opacity:1;fill:#fff}}{f(r + 2.5)}%,{f(89 + i * .3)}%{{opacity:1;fill:url(#nameGrad)}}{f(89.2 + i * .3)}%,100%{{opacity:0}}}}"
        )
        off = random.random() * .5
        scr = "".join(
            f'<text class="fl" x="{f(x)}" y="{ny}" style="animation-delay:-{f(k * .1 + off)}s">{escape(random.choice(glyphs))}</text>'
            for k in range(5)
        )
        chars.append(
            f'<g style="animation:h{i} {T}s linear infinite" fill="{CYAN}" fill-opacity=".75">{scr}</g>'
            f'<text x="{f(x)}" y="{ny}" fill="url(#nameGrad)" style="animation:s{i} {T}s linear infinite;opacity:0" filter="url(#glow)">{ch}</text>'
        )

    bits = []
    for _ in range(38):
        bx, by = random.uniform(20, W - 20), random.uniform(120, H + 20)
        dur, delay = random.uniform(6, 12), random.uniform(0, 12)
        col = random.choice([CYAN, VIOLET, PINK, BLUE])
        bits.append(
            f'<text class="bit" x="{f(bx)}" y="{f(by)}" font-size="{random.randint(10, 14)}" fill="{col}" '
            f'style="animation-duration:{f(dur)}s;animation-delay:-{f(delay)}s">{random.choice(["0", "1", "0x", "#", "::", "01", "ff"])}</text>'
        )

    # radar (top-right)
    rx, ry, rr = 1085, 105, 62
    radar = f"""
<g transform="translate({rx},{ry})" opacity=".9">
  <circle r="{rr}" fill="{CYAN}" fill-opacity=".04" stroke="{CYAN}" stroke-opacity=".45"/>
  <circle r="{rr * .66:.1f}" fill="none" stroke="{CYAN}" stroke-opacity=".25"/>
  <circle r="{rr * .33:.1f}" fill="none" stroke="{CYAN}" stroke-opacity=".25"/>
  <path d="M-{rr} 0H{rr}M0 -{rr}V{rr}" stroke="{CYAN}" stroke-opacity=".18"/>
  <g class="spin"><path d="M0 0L{rr} 0A{rr} {rr} 0 0 0 {f(rr * math.cos(math.radians(-50)))} {f(rr * math.sin(math.radians(-50)))}Z" fill="url(#sweep)"/>
    <line x1="0" y1="0" x2="{rr}" y2="0" stroke="{CYAN}" stroke-width="1.5"/></g>
  <circle class="blip" cx="22" cy="-30" r="3.5" fill="{PINK}" style="animation-delay:.3s"/>
  <circle class="blip" cx="-35" cy="18" r="3" fill="{CYAN}" style="animation-delay:2.4s"/>
  <circle class="blip" cx="30" cy="34" r="3" fill="{VIOLET}" style="animation-delay:1.3s"/>
</g>"""

    # AI core (bottom-left)
    cx, cy = 115, 275
    core = f"""
<g transform="translate({cx},{cy})">
  <circle class="spins" r="58" fill="none" stroke="{VIOLET}" stroke-opacity=".5" stroke-dasharray="2 8"/>
  <circle class="spinr" r="46" fill="none" stroke="{PINK}" stroke-opacity=".55" stroke-width="2" stroke-dasharray="40 14 6 14"/>
  <circle class="spin" r="34" fill="none" stroke="{CYAN}" stroke-opacity=".7" stroke-width="1.5" stroke-dasharray="70 30"/>
  <circle class="pulse" r="16" fill="url(#coreGrad)"/>
</g>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Nguyen Vu Long — AI x CyberSecurity">
<title>Nguyen Vu Long — AI × CyberSecurity</title>
<defs>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
  <filter id="aur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <linearGradient id="nameGrad" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{CYAN}"/><stop offset=".33" stop-color="{VIOLET}"/><stop offset=".66" stop-color="{PINK}"/><stop offset="1" stop-color="{CYAN}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="600 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="border" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{CYAN}"/><stop offset=".25" stop-color="{VIOLET}"/><stop offset=".5" stop-color="{PINK}"/><stop offset=".75" stop-color="{BLUE}"/><stop offset="1" stop-color="{CYAN}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{W} 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".45"/></linearGradient>
  <linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".07"/></linearGradient>
  <radialGradient id="coreGrad"><stop offset="0" stop-color="#fff"/><stop offset=".45" stop-color="{PINK}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#fff" stroke-opacity=".045"/></pattern>
  <radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}" stop-opacity=".85"/></radialGradient>
  <style>{"".join(css)}</style>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#aur)" opacity=".75">
    <ellipse class="blob b1" cx="220" cy="120" rx="300" ry="120" fill="{CYAN}" opacity=".55"/>
    <ellipse class="blob b2" cx="920" cy="260" rx="320" ry="130" fill="{PINK}" opacity=".45"/>
    <ellipse class="blob b3" cx="560" cy="320" rx="340" ry="110" fill="{VIOLET}" opacity=".6"/>
    <ellipse class="blob b4" cx="780" cy="60" rx="260" ry="100" fill="{BLUE}" opacity=".5"/>
  </g>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <g>{"".join(bits)}</g>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  <rect class="scan" x="0" y="0" width="{W}" height="60" fill="url(#scanG)"/>
  {radar}
  {core}
  <g font-size="13" letter-spacing="3" text-anchor="middle">
    <text class="st1" x="{W / 2}" y="112" fill="{PINK}">[ IDENTITY :: DECRYPTING<tspan class="caret">_</tspan> ]</text>
    <text class="st2" x="{W / 2}" y="112" fill="{CYAN}" opacity="0">[ IDENTITY :: VERIFIED ✓ ]</text>
  </g>
  <g font-size="{size}" font-weight="700" text-anchor="middle">{"".join(chars)}</g>
  <text x="{W / 2}" y="252" text-anchor="middle" font-size="22" font-weight="700" letter-spacing="9" fill="url(#nameGrad)">AI  ×  CYBERSECURITY</text>
  <text x="{W / 2}" y="292" text-anchor="middle" font-size="14" letter-spacing="1.5" fill="#c7d2fe" fill-opacity=".75">where neural networks meet threat models</text>
  <text x="{W - 24}" y="{H - 20}" text-anchor="end" font-size="11" fill="#fff" fill-opacity=".35">SEOUL · KR · 37.56°N 126.97°E</text>
  <text x="24" y="30" font-size="11" fill="#fff" fill-opacity=".35">sig: 0x4C4F4E47 · pgp ok</text>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="21" fill="none" stroke="url(#border)" stroke-width="2"/>
</svg>"""


# --------------------------------------------------------------------------
# BATTLE — "Red Team vs Blue Team"
# --------------------------------------------------------------------------
def kt(*ts):
    return ";".join(f(t) for t in ts)


def battle():
    W, H = 1200, 460
    T = 8
    B = (270, 215)   # blue orb
    R = (930, 215)   # red orb
    SH = 100         # shield radius

    attacks = [  # (path, launch, hit, hitpoint)
        (f"M872 205C720 70 470 90 {B[0] + 88} 172", .03, .15, (B[0] + 88, 172)),
        (f"M872 225C720 360 470 350 {B[0] + 88} 258", .28, .40, (B[0] + 88, 258)),
        (f"M872 215L{B[0] + SH} 215", .53, .60, (B[0] + SH, 215)),
    ]
    counter = (.74, .79, .86)  # beam start, hit, end

    def projectile(path, a, b, color, glow):
        out = []
        for j, (rad, op) in enumerate([(7, 1), (5.5, .6), (4, .4), (3, .25), (2, .15)]):
            d = j * .006
            a2, b2 = a + d, b + d
            out.append(
                f'<circle r="{rad}" fill="{"#fff" if j == 0 else color}" opacity="0" filter="{glow if j == 0 else ""}">'
                f'<animateMotion path="{path}" dur="{T}s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="{kt(0, a2, b2, 1)}" calcMode="linear"/>'
                f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;{op};{op};0;0" keyTimes="{kt(0, a2, a2 + .002, b2, b2 + .002, 1)}"/>'
                f"</circle>"
            )
        return "".join(out)

    def burst(x, y, h, color):
        s = [f'<circle cx="{x}" cy="{y}" fill="none" stroke="{color}" stroke-width="3" opacity="0">'
             f'<animate attributeName="r" dur="{T}s" repeatCount="indefinite" values="4;4;46;46" keyTimes="{kt(0, h, h + .07, 1)}"/>'
             f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="{kt(0, h, h + .002, h + .07, 1)}"/></circle>']
        for k in range(8):
            ang = k * math.pi / 4 + .3
            dx, dy = math.cos(ang) * 38, math.sin(ang) * 38
            s.append(
                f'<circle r="2.5" fill="{color}" opacity="0">'
                f'<animate attributeName="cx" dur="{T}s" repeatCount="indefinite" values="{x};{x};{f(x + dx)};{f(x + dx)}" keyTimes="{kt(0, h, h + .06, 1)}"/>'
                f'<animate attributeName="cy" dur="{T}s" repeatCount="indefinite" values="{y};{y};{f(y + dy)};{f(y + dy)}" keyTimes="{kt(0, h, h + .06, 1)}"/>'
                f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="{kt(0, h, h + .002, h + .06, 1)}"/></circle>'
            )
        return "".join(s)

    def peaks(times, base, peak, width=.05):
        pts = [(0, base)]
        for t in times:
            pts += [(t - .001, base), (t, peak), (t + width, base)]
        pts.append((1, base))
        return ";".join(str(v) for _, v in pts), kt(*[t for t, _ in pts])

    hits = [a[2] for a in attacks]
    sh_v, sh_k = peaks(hits, .45, 1)
    shw_v, shw_k = peaks(hits, 2, 6)

    # red charge-up glow before each launch
    ch_pts = [(0, .55)]
    for _, a, _, _ in attacks:
        ch_pts += [(a - .04, .55), (a, 1), (a + .03, .55)]
    ch_pts.append((1, .55))
    ch_v, ch_k = ";".join(str(v) for _, v in ch_pts), kt(*[t for t, _ in ch_pts])

    cs, chit, ce = counter

    def hexagon(cx, cy, r, rot=0):
        return "M" + "L".join(
            f"{f(cx + r * math.cos(math.radians(60 * k + rot)))} {f(cy + r * math.sin(math.radians(60 * k + rot)))}" for k in range(6)) + "Z"

    def star(cx, cy, r1, r2, n):
        pts = []
        for k in range(n * 2):
            r = r1 if k % 2 == 0 else r2
            a = math.pi * k / n
            pts.append(f"{f(cx + r * math.cos(a))},{f(cy + r * math.sin(a))}")
        return " ".join(pts)

    logs = [
        ("RED", "prompt_injection", "BLOCKED", hits[0]),
        ("RED", "sqli_payload", "SANITIZED", hits[1]),
        ("RED", "deepfake_voice", "DETECTED", hits[2]),
        ("BLUE", "incident_response", "CONTAINED", chit),
    ]
    log_svg = []
    for idx, (who, what, res, t) in enumerate(logs):
        t0 = t - .005
        nxt = logs[idx + 1][3] - .015 if idx + 1 < len(logs) else .995
        t1 = min(t + .2, nxt)
        att = f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="{kt(0, t0, t0 + .01, t1 - .01, t1, 1)}"/>'
        c1 = RED if who == "RED" else CYAN
        c2 = CYAN if who == "RED" else RED
        tgt = "BLUE" if who == "RED" else "RED"
        log_svg.append(
            f'<text x="600" y="{H - 34}" text-anchor="middle" font-size="15" opacity="0" xml:space="preserve">{att}'
            f'<tspan fill="{c1}">[{who}]</tspan><tspan fill="#cbd5e1"> {what} </tspan><tspan fill="#64748b">──▶ </tspan>'
            f'<tspan fill="{c2}">[{tgt}]</tspan><tspan fill="#fff" font-weight="700"> {res}</tspan></text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Red Team vs Blue Team — an endless AI duel">
<title>Red Team vs Blue Team</title>
<defs>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
  <filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="beamGlow" filterUnits="userSpaceOnUse" x="0" y="{B[1] - 60}" width="{W}" height="120"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
  <radialGradient id="blueCore"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="{CYAN}"/><stop offset=".75" stop-color="{BLUE}" stop-opacity=".6"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
  <radialGradient id="redCore"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#ff8fa3"/><stop offset=".6" stop-color="{RED}"/><stop offset="1" stop-color="#9d0033" stop-opacity="0"/></radialGradient>
  <linearGradient id="vs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{RED}"/></linearGradient>
  <linearGradient id="beam" gradientUnits="userSpaceOnUse" x1="{B[0] + 40}" y1="0" x2="{R[0] - 40}" y2="0"><stop offset="0" stop-color="#fff"/><stop offset=".2" stop-color="{CYAN}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  <linearGradient id="border" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0">
    <stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{RED}"/>
  </linearGradient>
  <pattern id="hex" width="42" height="72.75" patternUnits="userSpaceOnUse" patternTransform="scale(.7)">
    <path d="M21 0L42 12.12V36.37L21 48.5L0 36.37V12.12ZM21 48.5V72.75" fill="none" stroke="#fff" stroke-opacity=".05"/>
  </pattern>
  <style>
    text{{font-family:{MONO};}}
    .rot{{transform-box:fill-box;transform-origin:center;animation:spin 10s linear infinite;}}
    .rotr{{transform-box:fill-box;transform-origin:center;animation:spin 6s linear infinite reverse;}}
    .rots{{transform-box:fill-box;transform-origin:center;animation:spin 24s linear infinite;}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .vs{{animation:vs 2s ease-in-out infinite;}}
    @keyframes vs{{0%,100%{{opacity:.35}}50%{{opacity:.9}}}}
    .dash{{animation:dash 1.2s linear infinite;}}
    @keyframes dash{{to{{stroke-dashoffset:-24}}}}
    .blink{{animation:blink 1.4s steps(1) infinite;}}
    @keyframes blink{{50%{{opacity:.2}}}}
  </style>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#soft)">
    <ellipse cx="{B[0]}" cy="{B[1]}" rx="300" ry="190" fill="{BLUE}" opacity=".45">
      <animate attributeName="rx" values="280;330;280" dur="7s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="{R[0]}" cy="{R[1]}" rx="300" ry="190" fill="{RED}" opacity=".35">
      <animate attributeName="rx" values="330;280;330" dur="7s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="600" cy="230" rx="170" ry="140" fill="{VIOLET}" opacity=".35"/>
  </g>
  <rect width="{W}" height="{H}" fill="url(#hex)"/>

  <!-- HUD -->
  <g font-size="13" letter-spacing="2">
    <text x="40" y="44" fill="{CYAN}" font-weight="700">BLUE TEAM</text>
    <text x="40" y="64" fill="#94a3b8" font-size="11">// soc · appsec · ai-sec</text>
    <rect x="40" y="76" width="240" height="8" rx="4" fill="#fff" fill-opacity=".08"/>
    <rect x="40" y="76" width="232" height="8" rx="4" fill="{CYAN}">
      <animate attributeName="width" dur="{T}s" repeatCount="indefinite" values="232;232;224;232;232;226;232;232;220;232;232" keyTimes="{kt(0, hits[0], hits[0] + .01, hits[0] + .1, hits[1], hits[1] + .01, hits[1] + .1, hits[2], hits[2] + .01, hits[2] + .1, 1)}"/></rect>
    <text x="{W - 40}" y="44" fill="{RED}" font-weight="700" text-anchor="end">RED TEAM</text>
    <text x="{W - 40}" y="64" fill="#94a3b8" font-size="11" text-anchor="end">offense · adversary.ai //</text>
    <rect x="{W - 280}" y="76" width="240" height="8" rx="4" fill="#fff" fill-opacity=".08"/>
    <rect x="{W - 280}" y="76" width="240" height="8" rx="4" fill="{RED}">
      <animate attributeName="width" dur="{T}s" repeatCount="indefinite" values="240;240;110;110;240" keyTimes="{kt(0, chit, chit + .01, .97, 1)}"/>
      <animate attributeName="x" dur="{T}s" repeatCount="indefinite" values="{W - 280};{W - 280};{W - 150};{W - 150};{W - 280}" keyTimes="{kt(0, chit, chit + .01, .97, 1)}"/></rect>
    <text x="600" y="44" text-anchor="middle" fill="#e2e8f0" fill-opacity=".6" font-size="11" letter-spacing="4">ROUND ∞ · <tspan class="blink" fill="{PINK}">● LIVE</tspan></text>
  </g>

  <text class="vs" x="600" y="238" text-anchor="middle" font-size="64" font-weight="800" fill="url(#vs)" letter-spacing="6">VS</text>

  <!-- BLUE ORB -->
  <g transform="translate({B[0]},{B[1]})">
    <g><animateTransform attributeName="transform" type="translate" values="0 -5;0 5;0 -5" dur="4s" repeatCount="indefinite"/>
      <circle class="rots" r="70" fill="none" stroke="{CYAN}" stroke-opacity=".35" stroke-dasharray="1 6"/>
      <circle class="rotr" r="54" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="30 10 4 10"/>
      <circle class="rot" r="42" fill="none" stroke="{CYAN}" stroke-opacity=".8" stroke-width="1.5" stroke-dasharray="60 20"/>
      <circle r="34" fill="url(#blueCore)"><animate attributeName="r" values="30;36;30" dur="2.4s" repeatCount="indefinite"/></circle>
      <circle r="9" fill="#fff" filter="url(#glow)"/>
    </g>
    <g class="rots">
      <path d="{hexagon(0, 0, SH, 30)}" fill="{CYAN}" fill-opacity=".05" stroke="{CYAN}">
        <animate attributeName="stroke-opacity" dur="{T}s" repeatCount="indefinite" values="{sh_v}" keyTimes="{sh_k}"/>
        <animate attributeName="stroke-width" dur="{T}s" repeatCount="indefinite" values="{shw_v}" keyTimes="{shw_k}"/>
      </path>
      <path d="{hexagon(0, 0, SH - 10, 30)}" fill="none" stroke="{CYAN}" stroke-opacity=".25" stroke-dasharray="6 6" class="dash"/>
    </g>
  </g>

  <!-- RED ORB -->
  <g transform="translate({R[0]},{R[1]})">
    <g>
      <animateTransform attributeName="transform" type="translate" dur="{T}s" repeatCount="indefinite"
        values="0 0;0 0;14 -4;-8 3;5 0;0 0;0 0" keyTimes="{kt(0, chit, chit + .012, chit + .024, chit + .036, chit + .05, 1)}"/>
      <g><animateTransform attributeName="transform" type="translate" values="0 5;0 -5;0 5" dur="4s" repeatCount="indefinite"/>
        <polygon class="rots" points="{star(0, 0, 82, 64, 12)}" fill="none" stroke="{RED}" stroke-opacity=".5"/>
        <circle class="rotr" r="58" fill="none" stroke="{PINK}" stroke-width="2" stroke-dasharray="3 7"/>
        <polygon class="rot" points="{star(0, 0, 46, 36, 3)}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-opacity=".8"/>
        <circle r="36" fill="url(#redCore)">
          <animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="{ch_v}" keyTimes="{ch_k}"/></circle>
        <ellipse rx="4" ry="16" fill="#1a0008"><animate attributeName="ry" values="16;16;2;16;16" keyTimes="0;.9;.93;.96;1" dur="5s" repeatCount="indefinite"/></ellipse>
        <circle r="36" fill="none" stroke="#fff" stroke-width="3" opacity="0">
          <animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="{kt(0, chit, chit + .002, chit + .06, 1)}"/></circle>
      </g>
    </g>
  </g>

  <!-- attacks -->
  {"".join(projectile(p, a, b, RED, "url(#glow)") for p, a, b, _ in attacks)}
  {"".join(burst(hp[0], hp[1], b, CYAN) for _, _, b, hp in attacks)}

  <!-- counter beam -->
  <line x1="{B[0] + 40}" y1="{B[1]}" x2="{R[0] - 40}" y2="{R[1]}" stroke="url(#beam)" stroke-linecap="round" filter="url(#beamGlow)" opacity="0">
    <animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="{kt(0, cs, cs + .005, ce - .03, ce, 1)}"/>
    <animate attributeName="stroke-width" dur="{T}s" repeatCount="indefinite" values="2;2;10;6;2;2" keyTimes="{kt(0, cs, chit, chit + .03, ce, 1)}"/>
    <animate attributeName="x2" dur="{T}s" repeatCount="indefinite" values="{B[0] + 40};{B[0] + 40};{R[0] - 40};{R[0] - 40}" keyTimes="{kt(0, cs, chit, 1)}"/>
  </line>
  {burst(R[0] - 40, R[1], chit, CYAN)}

  <!-- battle log -->
  <line x1="300" y1="{H - 62}" x2="900" y2="{H - 62}" stroke="url(#border)" stroke-opacity=".5" stroke-dasharray="4 4" class="dash"/>
  {"".join(log_svg)}
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="21" fill="none" stroke="url(#border)" stroke-width="2" stroke-opacity=".8"/>
</svg>"""


# --------------------------------------------------------------------------
# TERMINAL card
# --------------------------------------------------------------------------
def terminal():
    W, H = 590, 320
    T = 16
    CW = 9.1  # approx monospace advance at 15px
    lines = [
        ("cmd", "./whoami --verbose"),
        ("out", [("  handle   : ", "#94a3b8"), ("nguyenvulong", CYAN)]),
        ("out", [("  class    : ", "#94a3b8"), ("soc analyst // researcher", "#e2e8f0")]),
        ("out", [("  focus    : ", "#94a3b8"), ("SOC · AppSec · AI Sec", PINK)]),
        ("cmd", "./triage --queue=live"),
        ("out", [("  [ FP ] ", "#4ade80"), ("#4821 phishing_link ...... closed", "#e2e8f0")]),
        ("out", [("  [HIGH] ", RED), ("#4822 impossible_travel .. escalated", "#e2e8f0")]),
        ("out", [("  [WARN] ", "#facc15"), ("coffee level ............. low", "#e2e8f0")]),
    ]
    prompt = [("long", CYAN), ("@", "#64748b"), ("sentinel", VIOLET), (":~$ ", "#64748b")]
    plen = sum(len(s) for s, _ in prompt)
    y0, lh = 72, 26
    t = .6
    end_fade = T - 1.0
    parts, clips = [], []

    def spans(segs):
        return "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in segs)

    for i, (kind, content) in enumerate(lines):
        y = y0 + i * lh
        if kind == "cmd":
            # prompt appears, then command typed char by char
            n = len(content)
            step = .07
            start = t + .35
            vals, kts = ["0"], ["0"]
            for c in range(n + 1):
                vals.append(f(c * CW + 2))
                kts.append(f((start + c * step) / T))
            vals.append(f(n * CW + 2)); kts.append("1")
            clips.append(
                f'<clipPath id="c{i}"><rect x="{f(20 + plen * CW - 1)}" y="{y - 16}" height="22" width="0">'
                f'<animate attributeName="width" dur="{T}s" repeatCount="indefinite" calcMode="discrete" values="{";".join(vals)}" keyTimes="{";".join(kts)}"/></rect></clipPath>'
            )
            show = t / T
            parts.append(
                f'<g opacity="0"><animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" values="0;1;0" keyTimes="{kt(0, show, end_fade / T)}"/>'
                f'<text x="20" y="{y}" xml:space="preserve">{spans(prompt)}</text>'
                f'<text x="{f(20 + plen * CW)}" y="{y}" fill="#f8fafc" clip-path="url(#c{i})">{escape(content)}</text></g>'
            )
            t = start + n * step + .5
        else:
            show = t / T
            parts.append(
                f'<text x="20" y="{y}" xml:space="preserve" opacity="0">'
                f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" values="0;1;0" keyTimes="{kt(0, show, end_fade / T)}"/>{spans(content)}</text>'
            )
            t += .22
    # final prompt with blinking cursor
    y = y0 + len(lines) * lh
    show = (t + .2) / T
    parts.append(
        f'<g opacity="0"><animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" values="0;1;0" keyTimes="{kt(0, show, end_fade / T)}"/>'
        f'<text x="20" y="{y}" xml:space="preserve">{spans(prompt)}</text>'
        f'<rect class="cur" x="{f(20 + plen * CW)}" y="{y - 14}" width="9" height="17" fill="{CYAN}"/></g>'
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="terminal: whoami">
<title>whoami</title>
<defs>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  {"".join(clips)}
  <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
  <linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1024"/><stop offset="1" stop-color="#140a24"/></linearGradient>
  <pattern id="lines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" fill-opacity=".025"/></pattern>
  <style>
    text{{font-family:{MONO};font-size:15px;}}
    .cur{{animation:b 1s steps(1) infinite;}}
    @keyframes b{{50%{{opacity:0}}}}
    .flick{{animation:fk 7s linear infinite;}}
    @keyframes fk{{0%,96%,100%{{opacity:1}}97%{{opacity:.75}}98%{{opacity:1}}99%{{opacity:.85}}}}
  </style>
</defs>
<g clip-path="url(#card)" class="flick">
  <rect width="{W}" height="{H}" fill="url(#bgG)"/>
  <rect width="{W}" height="34" fill="#fff" fill-opacity=".04"/>
  <circle cx="22" cy="17" r="6" fill="#ff5f57"/><circle cx="42" cy="17" r="6" fill="#febc2e"/><circle cx="62" cy="17" r="6" fill="#28c840"/>
  <text x="{W / 2}" y="22" text-anchor="middle" fill="#64748b" style="font-size:12px">long@sentinel — zsh — 80×24</text>
  {"".join(parts)}
  <rect width="{W}" height="{H}" fill="url(#lines)"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="15" fill="none" stroke="url(#bd)" stroke-width="1.5" stroke-opacity=".8"/>
</svg>"""


# --------------------------------------------------------------------------
# STATUS panel card
# --------------------------------------------------------------------------
def status():
    W, H = 590, 320
    rows_y = [78, 124, 170, 216]
    eq = []
    for k in range(7):
        d = random.uniform(.6, 1.3)
        eq.append(
            f'<rect x="{430 + k * 12}" width="7" rx="2" fill="{CYAN}">'
            f'<animate attributeName="height" values="4;18;8;22;6;4" dur="{f(d)}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{rows_y[0] - 4};{rows_y[0] - 18};{rows_y[0] - 8};{rows_y[0] - 22};{rows_y[0] - 6};{rows_y[0] - 4}" dur="{f(d)}s" repeatCount="indefinite"/></rect>'
        )
    seg = []
    for k in range(10):
        col = "#4ade80" if k < 3 else ("#facc15" if k < 6 else RED)
        base = .9 if k < 2 else .12
        if k in (2, 3):
            seg.append(f'<rect x="{430 + k * 12}" y="{rows_y[2] - 16}" width="9" height="18" rx="2" fill="{col}" opacity="{base}">'
                       f'<animate attributeName="opacity" values=".12;.9;.9;.12" keyTimes="0;.3;.6;1" dur="{3 + k}s" repeatCount="indefinite"/></rect>')
        else:
            seg.append(f'<rect x="{430 + k * 12}" y="{rows_y[2] - 16}" width="9" height="18" rx="2" fill="{col}" opacity="{base}"/>')

    # ECG path
    ecg, x = [], 0
    while x < 1200:
        ecg += [f"{x} 0", f"{x + 40} 0", f"{x + 48} -6", f"{x + 54} 0", f"{x + 62} 0", f"{x + 67} 18", f"{x + 74} -36", f"{x + 81} 12", f"{x + 86} 0", f"{x + 100} 0", f"{x + 110} -8", f"{x + 122} 0"]
        x += 150
    ecg_d = "M" + "L".join(ecg)

    def row(y, label, value, vcol, dot=True):
        d = (f'<circle cx="36" cy="{y - 5}" r="5" fill="{vcol}"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>'
             f'<circle cx="36" cy="{y - 5}" r="5" fill="none" stroke="{vcol}"><animate attributeName="r" values="5;13" dur="1.6s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values=".8;0" dur="1.6s" repeatCount="indefinite"/></circle>') if dot else ""
        return (f'{d}<text x="56" y="{y}" fill="#94a3b8" letter-spacing="2">{label}</text>'
                f'<text x="250" y="{y}" fill="{vcol}" font-weight="700">{value}</text>'
                f'<line x1="24" y1="{y + 14}" x2="{W - 24}" y2="{y + 14}" stroke="#fff" stroke-opacity=".06"/>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="system status panel">
<title>system status</title>
<defs>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  <clipPath id="ecgc"><rect x="24" y="238" width="{W - 48}" height="52"/></clipPath>
  <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{PINK}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>
  <linearGradient id="bgG" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1024"/><stop offset="1" stop-color="#140a24"/></linearGradient>
  <linearGradient id="ecgG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".3" stop-color="{CYAN}"/><stop offset=".7" stop-color="{VIOLET}"/><stop offset="1" stop-color="{PINK}" stop-opacity="0"/></linearGradient>
  <filter id="glow" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <style>
    text{{font-family:{MONO};font-size:13px;}}
    .spin{{transform-box:fill-box;transform-origin:center;animation:spin 3s linear infinite;}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .flow{{animation:flow 1s linear infinite;}}
    @keyframes flow{{to{{stroke-dashoffset:-20}}}}
    .ecg{{animation:ecg 4s linear infinite;}}
    @keyframes ecg{{to{{transform:translateX(-600px)}}}}
  </style>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bgG)"/>
  <rect width="{W}" height="34" fill="#fff" fill-opacity=".04"/>
  <text x="24" y="22" fill="#e2e8f0" letter-spacing="4" font-weight="700" style="font-size:12px">SYSTEM STATUS</text>
  <text x="{W - 24}" y="22" fill="{PINK}" text-anchor="end" style="font-size:11px">● REC<animate attributeName="opacity" values="1;.2;1" dur="1.2s" repeatCount="indefinite"/></text>
  {row(rows_y[0], "SIEM FEED", "INGESTING", "#4ade80")}
  {"".join(eq)}
  {row(rows_y[1], "ALERT TRIAGE", "ACTIVE", CYAN)}
  <line x1="430" y1="{rows_y[1] - 5}" x2="{W - 30}" y2="{rows_y[1] - 5}" stroke="{CYAN}" stroke-width="3" stroke-dasharray="10 10" class="flow"/>
  {row(rows_y[2], "THREAT LEVEL", "NOMINAL", "#facc15")}
  {"".join(seg)}
  {row(rows_y[3], "LLM GUARDRAILS", "ENFORCED", VIOLET)}
  <g transform="translate({W - 60},{rows_y[3] - 5})"><circle class="spin" r="11" fill="none" stroke="{VIOLET}" stroke-width="3" stroke-dasharray="20 50" stroke-linecap="round"/>
    <circle r="4" fill="{VIOLET}"/></g>
  <g clip-path="url(#ecgc)"><g class="ecg"><path transform="translate(24,272)" d="{ecg_d}" fill="none" stroke="url(#ecgG)" stroke-width="2" filter="url(#glow)"/></g></g>
  <text x="24" y="304" fill="#64748b" style="font-size:11px">UPTIME ∞</text>
  <text x="{W - 24}" y="304" fill="#64748b" text-anchor="end" style="font-size:11px">heartbeat: stable</text>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="15" fill="none" stroke="url(#bd)" stroke-width="1.5" stroke-opacity=".8"/>
</svg>"""


# --------------------------------------------------------------------------
# DIVIDER
# --------------------------------------------------------------------------
def divider():
    W, H = 1200, 28
    pk = []
    for k, (col, dur) in enumerate([(CYAN, 5), (PINK, 7), (VIOLET, 6), ("#fff", 9)]):
        pk.append(f'<circle r="{3 if col != "#fff" else 2}" cy="14" fill="{col}" filter="url(#g)">'
                  f'<animate attributeName="cx" values="-20;{W + 20}" dur="{dur}s" begin="-{k * 1.7}s" repeatCount="indefinite"/></circle>')
    nodes = "".join(f'<rect x="{x - 4}" y="10" width="8" height="8" transform="rotate(45 {x} 14)" fill="{BG}" stroke="url(#ln)" stroke-width="1.5"/>' for x in (300, 600, 900))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true">
<defs>
  <linearGradient id="ln" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".2" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset=".8" stop-color="{PINK}"/><stop offset="1" stop-color="{PINK}" stop-opacity="0"/>
  </linearGradient>
  <filter id="g" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<line x1="0" y1="14" x2="{W}" y2="14" stroke="url(#ln)" stroke-width="1.5"/>
<line x1="0" y1="14" x2="{W}" y2="14" stroke="url(#ln)" stroke-width="1" stroke-dasharray="2 14" opacity=".8" transform="translate(0,-4)"/>
{nodes}
{"".join(pk)}
</svg>"""


# --------------------------------------------------------------------------
# LINK BUTTONS
# --------------------------------------------------------------------------
ICONS = {
    "linkedin": lambda c: f'<rect x="-11" y="-11" width="22" height="22" rx="4" fill="none" stroke="{c}" stroke-width="2"/><text x="0" y="5" text-anchor="middle" fill="{c}" style="font-size:13px;font-weight:800;font-family:Arial,sans-serif">in</text>',
    "scholar": lambda c: f'<path d="M-13 -3L0 -11L13 -3L0 5Z" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><path d="M-7 1V7C-3 11 3 11 7 7V1" fill="none" stroke="{c}" stroke-width="2"/><path d="M13 -3V6" stroke="{c}" stroke-width="2"/>',
    "patents": lambda c: f'<path d="M-6 3C-10 -1 -10 -12 0 -12C10 -12 10 -1 6 3V6H-6Z" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><path d="M-4 10H4" stroke="{c}" stroke-width="2" stroke-linecap="round"/><path d="M0 -3V3" stroke="{c}" stroke-width="2"/>',
    "email": lambda c: f'<rect x="-12" y="-8" width="24" height="17" rx="3" fill="none" stroke="{c}" stroke-width="2"/><path d="M-11 -6L0 2L11 -6" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/>',
}


def button(key, label, c1, c2, delay):
    W, H = 210, 54
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}">
<title>{label}</title>
<defs>
  <linearGradient id="bd" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{c1}"/><stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{W} 0" dur="3s" begin="-{delay}s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <clipPath id="c"><rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12"/></clipPath>
</defs>
<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{BG}"/>
<g clip-path="url(#c)"><rect y="0" width="60" height="{H}" fill="url(#sh)" transform="skewX(-20)">
  <animate attributeName="x" values="-120;{W + 60};{W + 60}" keyTimes="0;.4;1" dur="4s" begin="-{delay}s" repeatCount="indefinite"/></rect></g>
<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="none" stroke="url(#bd)" stroke-width="2"/>
<g transform="translate(36,{H / 2})">{ICONS[key]("url(#bd)")}</g>
<text x="62" y="{H / 2 + 5}" fill="#e2e8f0" style="font-family:{MONO};font-size:14px;font-weight:700;letter-spacing:3px">{label}</text>
</svg>"""


# --------------------------------------------------------------------------
# FOOTER
# --------------------------------------------------------------------------
def footer():
    W, H = 1200, 220
    cx, cy = W / 2, 92
    shield = f"M{cx} {cy - 44}L{cx + 34} {cy - 30}V{cy + 2}C{cx + 34} {cy + 26} {cx + 16} {cy + 40} {cx} {cy + 48}C{cx - 16} {cy + 40} {cx - 34} {cy + 26} {cx - 34} {cy + 2}V{cy - 30}Z"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="stay curious, stay paranoid">
<title>stay curious · stay paranoid</title>
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
  <linearGradient id="t" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="{CYAN}"/><stop offset=".33" stop-color="{VIOLET}"/><stop offset=".66" stop-color="{PINK}"/><stop offset="1" stop-color="{CYAN}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="600 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <style>
    .beat{{transform-box:fill-box;transform-origin:center;animation:beat 1.6s ease-in-out infinite;}}
    @keyframes beat{{0%,100%{{transform:scale(1)}}14%{{transform:scale(1.12)}}28%{{transform:scale(1)}}42%{{transform:scale(1.08)}}70%{{transform:scale(1)}}}}
    .ring{{transform-box:fill-box;transform-origin:center;animation:ring 3.2s ease-out infinite;}}
    @keyframes ring{{0%{{transform:scale(.6);opacity:.8}}100%{{transform:scale(1.8);opacity:0}}}}
  </style>
</defs>
<circle class="ring" cx="{cx}" cy="{cy}" r="44" fill="none" stroke="url(#g)" stroke-width="2"/>
<circle class="ring" cx="{cx}" cy="{cy}" r="44" fill="none" stroke="url(#g)" stroke-width="2" style="animation-delay:-1.6s"/>
<g class="beat" filter="url(#glow)">
  <path d="{shield}" fill="{BG}" fill-opacity=".85" stroke="url(#g)" stroke-width="3" stroke-linejoin="round"/>
  <rect x="{cx - 12}" y="{cy - 2}" width="24" height="20" rx="4" fill="url(#g)"/>
  <path d="M{cx - 7} {cy - 2}V{cy - 9}A7 7 0 0 1 {cx + 7} {cy - 9}V{cy - 2}" fill="none" stroke="url(#g)" stroke-width="3"/>
  <circle cx="{cx}" cy="{cy + 7}" r="2.5" fill="{BG}"/>
</g>
<text x="{cx}" y="204" text-anchor="middle" fill="url(#t)" style="font-family:{MONO};font-size:16px;letter-spacing:6px;font-weight:700">STAY CURIOUS · STAY PARANOID</text>
</svg>"""


write("hero.svg", hero())
write("battle.svg", battle())
write("terminal.svg", terminal())
write("status.svg", status())
write("divider.svg", divider())
write("footer.svg", footer())
write("btn-linkedin.svg", button("linkedin", "LINKEDIN", CYAN, BLUE, 0))
write("btn-scholar.svg", button("scholar", "SCHOLAR", VIOLET, CYAN, .7))
write("btn-patents.svg", button("patents", "PATENTS", PINK, VIOLET, 1.4))
write("btn-email.svg", button("email", "CONTACT", RED, PINK, 2.1))
