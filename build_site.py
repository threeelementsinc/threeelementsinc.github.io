#!/usr/bin/env python3
"""Generates the artboard files for the Three Elements site design."""

HEAD = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="canonical" href="https://www.3elementsinc.com/{slug}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.3elementsinc.com/{slug}">
  <meta property="og:image" content="https://www.3elementsinc.com/og.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600&display=swap">
  <style>
    body { margin: 0; background: #0A0D14; color: #F4F5F7; font-family: "DM Sans", "Helvetica Neue", Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #F2A93B; text-decoration: none; } a:hover { color: #FFC66B; }
    h1, h2, h3 { font-family: "Sora", "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif; margin: 0; letter-spacing: -0.02em; text-wrap: pretty; }
    p { margin: 0; text-wrap: pretty; }
    .grain { position: relative; }
    .grain::after { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: 0.05; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E"); }
    img { max-width: 100%; }
    .btn:hover { filter: brightness(1.08); }
    .navlink:hover { color: #F4F5F7 !important; }
    .menu-toggle { display: none; }
    @media (max-width: 1100px) {
      .pad { padding-left: 40px !important; padding-right: 40px !important; }
      .band { margin-left: 40px !important; margin-right: 40px !important; padding: 48px 40px !important; }
      .hero { padding: 64px 40px 56px !important; }
      .hero h1 { font-size: 52px !important; }
      .grid3 { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
      .shots { flex-wrap: wrap !important; }
      .story { flex-direction: column !important; align-items: center !important; }
      .tl-body { grid-template-columns: minmax(0, 1fr) !important; }
      .story-side { position: static !important; }
    }
    @media (max-width: 820px) {
      .nav { padding: 16px 20px !important; flex-wrap: wrap !important; gap: 12px !important; }
      .nav-links { display: none !important; width: 100%; flex-direction: column !important; align-items: flex-start !important; gap: 4px !important; padding: 8px 0 !important; }
      .nav.open .nav-links { display: flex !important; }
      .nav-cta { display: none !important; }
      .menu-toggle { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.14); background: transparent; color: #F4F5F7; cursor: pointer; }
      .nav.open .menu-toggle { background: rgba(255,255,255,0.08); }
      .pad { padding-left: 20px !important; padding-right: 20px !important; padding-top: 24px !important; padding-bottom: 56px !important; }
      .band { margin-left: 20px !important; margin-right: 20px !important; margin-bottom: 56px !important; padding: 36px 24px !important; flex-direction: column !important; align-items: flex-start !important; gap: 28px !important; }
      .band h2, .sec h2 { font-size: 30px !important; }
      .hero { padding: 40px 20px 48px !important; flex-direction: column !important; gap: 40px !important; }
      .hero h1 { font-size: 40px !important; }
      .hero p { font-size: 17px !important; }
      .hero-text { max-width: 100% !important; }
      .phones { width: 100% !important; height: auto !important; display: flex !important; justify-content: center !important; gap: 16px !important; }
      .phones > div { position: static !important; flex: 1 1 0; max-width: 220px; }
      .phones .phone { width: 100% !important; height: auto !important; aspect-ratio: 300 / 620; }
      .card-foot { flex-direction: column !important; align-items: flex-start !important; gap: 10px !important; }
      .grid2, .grid3 { grid-template-columns: minmax(0, 1fr) !important; }
      .shots { gap: 16px !important; }
      .shots .phone { width: 46% !important; max-width: 200px !important; height: auto !important; aspect-ratio: 260 / 540; }
      .eq { flex-direction: column !important; gap: 8px !important; align-items: flex-start !important; }
      .eq-left { width: auto !important; font-size: 19px !important; flex-wrap: wrap !important; }
      .eq-sign { display: none !important; }
      .connect { flex-direction: column !important; gap: 24px !important; }
      .connect-head { width: auto !important; }
      .quote { flex-direction: column !important; gap: 20px !important; padding: 36px 24px !important; }
      .quote p { font-size: 22px !important; }
      .quote-foot { flex-direction: column !important; align-items: flex-start !important; gap: 10px !important; }
      .pricing { width: 100% !important; grid-template-columns: minmax(0, 1fr) !important; }
      .footer-grid { grid-template-columns: minmax(0, 1fr) !important; gap: 28px !important; }
      .footer-bottom { flex-direction: column !important; gap: 8px !important; align-items: flex-start !important; }
      .story-photo { width: 100% !important; height: 320px !important; }
      .tl-body { grid-template-columns: minmax(0, 1fr) !important; gap: 20px !important; padding-bottom: 48px !important; }
      .tl-body h2 { font-size: 26px !important; }
      .tl-body p { font-size: 16px !important; }
      .tl-step { grid-template-columns: 56px minmax(0, 1fr) !important; gap: 12px !important; }
      .tl-wrap > div:first-child, .tl-line { left: 21px !important; }
      .tri { width: 100% !important; height: auto !important; }
      .free { flex-direction: column !important; gap: 28px !important; padding: 36px 24px !important; }
      .free-list { width: 100% !important; }
      .btn { width: 100%; justify-content: center; box-sizing: border-box; }
      .btn-row { flex-direction: column !important; width: 100%; }
      .checks { flex-wrap: wrap !important; gap: 12px 20px !important; }
      h1 { font-size: 40px !important; }
      .sec h2 { font-size: 32px !important; }
      .sec p { font-size: 16px !important; }
    }
  </style>
</head>
<body>
<div style="max-width: 1440px; margin: 0 auto; background: #0A0D14; color: #F4F5F7; display: flex; flex-direction: column; align-items: stretch;">
'''

TAIL = '''</div>
<script>
  var nav = document.querySelector('.nav');
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) { toggle.addEventListener('click', function () { nav.classList.toggle('open'); toggle.setAttribute('aria-expanded', nav.classList.contains('open')); }); }
</script>
</body>
</html>
'''

LOGO = '''<div style="display: flex; align-items: center; gap: 12px;">
  <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="17" cy="11" r="8" stroke="#F2A93B" stroke-width="2.2"></circle>
    <circle cx="11" cy="22" r="8" stroke="#5FD3A6" stroke-width="2.2"></circle>
    <circle cx="23" cy="22" r="8" stroke="#F0678C" stroke-width="2.2"></circle>
  </svg>
  <span style="font-family: Sora, 'Avenir Next', Helvetica, Arial, sans-serif; font-weight: 700; font-size: 18px; letter-spacing: -0.01em; color: #F4F5F7;">Three Elements</span>
</div>'''

def nav(active):
    items = [("Home", "Home", "index.html"), ("Routines", "Routines", "routines.html"), ("Focus", "Focus", "focus.html"), ("Our Story", "OurStory", "our-story.html")]
    links = ""
    for label, key, href in items:
        color = "#F4F5F7" if key == active else "#8E97A8"
        links += f'<a class="navlink" href="{href}" style="color: {color}; font-size: 15px; font-weight: 500; padding: 8px 2px;">{label}</a>\n'
    return f'''
<div class="nav" style="display: flex; align-items: center; justify-content: space-between; padding: 22px 80px; border-bottom: 1px solid rgba(255,255,255,0.06);">
  <a href="index.html" aria-label="Three Elements home">{LOGO}</a>
  <button class="menu-toggle" aria-label="Menu" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button>
  <div class="nav-links" style="display: flex; align-items: center; gap: 36px;">
    {links}
  </div>
  <a class="nav-cta btn" href="#get" style="display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 20px; border-radius: 999px; background: #F4F5F7; color: #0A0D14; font-weight: 600; font-size: 15px;">
    {ICON_DL}
    Get the apps
  </a>
</div>
'''

ICON_DL = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"></path><path d="m7 10 5 5 5-5"></path><path d="M5 21h14"></path></svg>'''
ICON_ARROW = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>'''
ICON_CHECK = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#5FD3A6" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5L20 7"></path></svg>'''
ICON_CLOCK = '''<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#F2A93B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg>'''
ICON_COIN = '''<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5FD3A6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M14.5 9.5c-.4-1-1.4-1.5-2.5-1.5-1.5 0-2.5.8-2.5 2 0 2.6 5 1.2 5 4 0 1.2-1 2-2.5 2-1.2 0-2.2-.6-2.6-1.6"></path><path d="M12 6.5V8m0 8v1.5"></path></svg>'''
ICON_HEART = '''<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#F0678C" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"></path></svg>'''

def primary_btn(label, href="#"):
    return f'''<a class="btn" href="{href}" style="display: inline-flex; align-items: center; gap: 10px; height: 52px; padding: 0 26px; border-radius: 999px; background: #F2A93B; color: #0A0D14; font-weight: 600; font-size: 16px;">{ICON_DL}{label}</a>'''

def ghost_btn(label, href="#"):
    return f'''<a class="btn" href="{href}" style="display: inline-flex; align-items: center; gap: 10px; height: 52px; padding: 0 26px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.18); color: #F4F5F7; font-weight: 600; font-size: 16px;">{label}{ICON_ARROW}</a>'''

FOOTER = f'''
<div class="pad" style="display: flex; flex-direction: column; gap: 40px; padding: 64px 80px 40px; border-top: 1px solid rgba(255,255,255,0.06);">
  <div class="footer-grid" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 40px;">
    <div style="display: flex; flex-direction: column; gap: 14px;">
      {LOGO}
      <p style="color: #8E97A8; font-size: 15px; line-height: 1.6; max-width: 320px;">Small, beautiful iPhone apps built around one idea: Time, Money and Health are connected.</p>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #8E97A8;">Apps</span>
      <a href="https://apps.apple.com/us/app/celebrity-routines/id6755641471" style="color: #F4F5F7; font-size: 15px;">Celebrity Routines</a>
      <a href="https://apps.apple.com/us/app/focus-daily-goals/id6760952606" style="color: #F4F5F7; font-size: 15px;">Focus: Daily Goals</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #8E97A8;">Company</span>
      <a href="our-story.html" style="color: #F4F5F7; font-size: 15px;">Our Story</a>
      <a href="mailto:support@3elementsinc.com" style="color: #F4F5F7; font-size: 15px;">support@3elementsinc.com</a>
      <a href="privacy.html" style="color: #F4F5F7; font-size: 15px;">Privacy Policy</a>
    </div>
  </div>
  <div class="footer-bottom" style="display: flex; justify-content: space-between; align-items: center; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.06);">
    <span style="color: #5C6578; font-size: 13px;">© 2026 Three Elements Inc. All rights reserved.</span>
    <span style="color: #5C6578; font-size: 13px;">Made in the Bay Area</span>
  </div>
</div>
'''

# ---------- phone mockups (drawn) ----------

def phone(inner, w=300, h=620, bg="#141B29", extra_style=""):
    return f'''<div style="width: {w}px; height: {h}px; border-radius: 44px; background: #1B2130; padding: 10px; box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.08); {extra_style}">
  <div style="width: 100%; height: 100%; border-radius: 36px; background: {bg}; overflow: hidden; display: flex; flex-direction: column;">
    {inner}
  </div>
</div>'''

ROUTINE_ROWS = [
    ("5:00 AM", "Wake up", "#F2A93B"),
    ("5:30 AM", "Workout", "#F0678C"),
    ("7:00 AM", "Deep work block", "#F2A93B"),
    ("12:30 PM", "Lunch & walk", "#5FD3A6"),
    ("6:00 PM", "Reading", "#8E97A8"),
    ("10:00 PM", "Lights out", "#8E97A8"),
]

def routines_phone():
    rows = ""
    for t, label, c in ROUTINE_ROWS:
        rows += f'''<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: {c}; flex: none;"></span>
      <span style="font-size: 11px; color: #8E97A8; width: 56px; flex: none;">{t}</span>
      <span style="font-size: 13px; font-weight: 500; color: #F4F5F7;">{label}</span>
    </div>'''
    inner = f'''
    <div style="padding: 54px 20px 0; display: flex; flex-direction: column; gap: 14px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <div style="width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, #F2A93B, #F0678C);"></div>
        <div style="display: flex; flex-direction: column; gap: 3px;">
          <span style="font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 16px; color: #F4F5F7;">Elon Musk</span>
          <span style="font-size: 12px; color: #8E97A8;">Entrepreneur · Tech Leader</span>
        </div>
      </div>
      <div style="display: flex; gap: 8px;">
        <span style="font-size: 11px; font-weight: 600; padding: 6px 10px; border-radius: 999px; background: rgba(242,169,59,0.16); color: #F2A93B;">Daily routine</span>
        <span style="font-size: 11px; font-weight: 600; padding: 6px 10px; border-radius: 999px; background: rgba(255,255,255,0.06); color: #8E97A8;">Principles</span>
        <span style="font-size: 11px; font-weight: 600; padding: 6px 10px; border-radius: 999px; background: rgba(255,255,255,0.06); color: #8E97A8;">Books</span>
      </div>
      <div style="display: flex; flex-direction: column;">{rows}</div>
    </div>'''
    return phone(inner)

def focus_phone():
    goals = [("Ship the app update", True), ("45-min run", True), ("Call Mom", False)]
    cards = ""
    grads = ["linear-gradient(135deg, #5B6CFF, #9B5CFF)", "linear-gradient(135deg, #F0678C, #F2A93B)", "linear-gradient(135deg, #2FB6A8, #5FD3A6)"]
    for (g, done), grad in zip(goals, grads):
        check = ICON_CHECK if done else '<span style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid rgba(255,255,255,0.7); display: inline-block;"></span>'
        cards += f'''<div style="display: flex; align-items: center; justify-content: space-between; padding: 18px 16px; border-radius: 18px; background: {grad}; color: #FFFFFF;">
      <span style="font-size: 14px; font-weight: 600;">{g}</span>
      <span style="display: inline-flex; width: 26px; height: 26px; border-radius: 50%; background: rgba(255,255,255,0.22); align-items: center; justify-content: center;">{check}</span>
    </div>'''
    cells = ""
    import random
    random.seed(7)
    for i in range(7*10):
        v = random.random()
        col = "#2A3244" if v < 0.35 else ("#4C5BD9" if v < 0.7 else "#8B7CFF")
        cells += f'<span style="width: 8px; height: 8px; border-radius: 2px; background: {col};"></span>'
    inner = f'''
    <div style="padding: 54px 20px 0; display: flex; flex-direction: column; gap: 16px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline;">
        <span style="font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 18px; color: #F4F5F7;">Today</span>
        <span style="font-size: 12px; font-weight: 600; color: #F2A93B;">12-day streak</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 10px;">{cards}</div>
      <span style="font-size: 12px; color: #8E97A8; margin-top: 6px;">This quarter</span>
      <div style="display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 5px;">{cells}</div>
    </div>'''
    return phone(inner, bg="#0F1420")

def screenshot_phone(src, w=300, h=620):
    return f'''<div class="phone" style="width: {w}px; height: {h}px; border-radius: 44px; background: #1B2130; padding: 10px; box-sizing: border-box; box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.08);">
  <div style="width: 100%; height: 100%; border-radius: 36px; overflow: hidden; display: flex;">
    <img src="img/{src}" alt="App screenshot" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: top;">
  </div>
</div>'''

# ---------- shared sections ----------

def element_cards():
    items = [
        (ICON_CLOCK, "Time", "Your most precious resource", "Time is the one thing you can't earn back. Everyone gets 24 hours — the difference is what you do with them. Track it intentionally and align daily actions with long-term goals."),
        (ICON_COIN, "Money", "Your financial freedom", "Money converts your time and skills into security, opportunity and freedom. Managed well, it buys back time and protects your health."),
        (ICON_HEART, "Health", "Your foundation for everything", "Physical, mental and emotional wellbeing. True productivity means reaching your goals while keeping the health to enjoy them."),
    ]
    out = ""
    for icon, name, sub, body in items:
        out += f'''<div style="display: flex; flex-direction: column; gap: 18px; padding: 32px; border-radius: 24px; background: #121722; border: 1px solid rgba(255,255,255,0.06);">
      <span style="display: inline-flex; width: 52px; height: 52px; border-radius: 16px; background: rgba(255,255,255,0.05); align-items: center; justify-content: center;">{icon}</span>
      <div style="display: flex; flex-direction: column; gap: 6px;">
        <h3 style="font-size: 24px; font-weight: 700;">{name}</h3>
        <span style="font-size: 14px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #8E97A8;">{sub}</span>
      </div>
      <p style="font-size: 16px; line-height: 1.6; color: #B7BFCC;">{body}</p>
    </div>'''
    return f'<div class="grid3" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px;">{out}</div>'

def equations():
    rows = [
        ("Time", "Health", "The capacity to pursue meaningful goals and enjoy life's experiences."),
        ("Time", "Money", "The freedom to choose how you live and what you pursue."),
        ("Money", "Health", "The resources and vitality to create lasting security and joy."),
    ]
    colors = {"Time": "#F2A93B", "Money": "#5FD3A6", "Health": "#F0678C"}
    out = ""
    for a, b, res in rows:
        out += f'''<div class="eq" style="display: flex; align-items: center; gap: 28px; padding: 26px 0; border-top: 1px solid rgba(255,255,255,0.08);">
      <div class="eq-left" style="display: flex; align-items: center; gap: 12px; width: 300px; flex: none; font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 22px;">
        <span style="color: {colors[a]};">{a}</span><span style="color: #5C6578;">+</span><span style="color: {colors[b]};">{b}</span>
      </div>
      <span class="eq-sign" style="color: #5C6578; font-family: Sora, Helvetica, Arial, sans-serif; font-size: 22px;">=</span>
      <p style="font-size: 18px; line-height: 1.5; color: #B7BFCC;">{res}</p>
    </div>'''
    out += f'''<div class="eq" style="display: flex; align-items: center; gap: 28px; padding: 26px 0; border-top: 1px solid rgba(255,255,255,0.08); border-bottom: 1px solid rgba(255,255,255,0.08);">
      <div class="eq-left" style="display: flex; align-items: center; gap: 12px; width: 300px; flex: none; font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 22px;">
        <span style="color: #F2A93B;">Time</span><span style="color: #5C6578;">+</span><span style="color: #5FD3A6;">Money</span><span style="color: #5C6578;">+</span><span style="color: #F0678C;">Health</span>
      </div>
      <span class="eq-sign" style="color: #5C6578; font-family: Sora, Helvetica, Arial, sans-serif; font-size: 22px;">=</span>
      <p style="font-size: 18px; line-height: 1.5; color: #F4F5F7; font-weight: 600;">True wealth — and the foundation for a fulfilling life.</p>
    </div>'''
    return out

def section_heading(eyebrow, title, sub=None, align="left", maxw=760):
    a = "center" if align == "center" else "flex-start"
    t = "center" if align == "center" else "left"
    subp = f'<p style="font-size: 18px; line-height: 1.6; color: #8E97A8; max-width: 640px; text-align: {t};">{sub}</p>' if sub else ""
    return f'''<div class="sec" style="display: flex; flex-direction: column; gap: 16px; align-items: {a}; max-width: {maxw}px;">
      <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #F2A93B;">{eyebrow}</span>
      <h2 style="font-size: 44px; font-weight: 700; line-height: 1.1; text-align: {t};">{title}</h2>
      {subp}
    </div>'''

def cta_band():
    return f'''
<div id="get" class="grain band" style="margin: 0 80px 96px; padding: 72px; border-radius: 32px; background: radial-gradient(120% 140% at 10% 0%, rgba(242,169,59,0.28) 0%, rgba(242,169,59,0) 55%), radial-gradient(90% 120% at 100% 100%, rgba(91,108,255,0.28) 0%, rgba(91,108,255,0) 60%), #121722; border: 1px solid rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: space-between; gap: 48px;">
  <div style="display: flex; flex-direction: column; gap: 14px; max-width: 620px;">
    <h2 style="font-size: 40px; font-weight: 700; line-height: 1.1;">Start with one routine. Or just three goals.</h2>
    <p style="font-size: 18px; line-height: 1.6; color: #B7BFCC;">Both apps are on the App Store for iPhone. Routines comes with a 7-day free trial. Focus is free, forever.</p>
  </div>
  <div class="btn-row" style="display: flex; flex-direction: column; gap: 12px; flex: none;">
    {primary_btn("Get Celebrity Routines", "https://apps.apple.com/us/app/celebrity-routines/id6755641471")}
    {ghost_btn("Get Focus — it's free", "https://apps.apple.com/us/app/focus-daily-goals/id6760952606")}
  </div>
</div>
'''

# ---------- pages ----------

def home():
    return HEAD.replace("{title}","Three Elements Inc. — iPhone apps for Time, Money and Health").replace("{desc}","Three Elements builds small, beautiful iPhone apps: Celebrity Routines and Focus: Daily Goals. Master your time, grow every element of your life.").replace("{slug}","") + nav("Home") + f'''
<div class="grain hero" style="position: relative; overflow: hidden; padding: 96px 80px 80px; display: flex; align-items: center; justify-content: space-between; gap: 60px; background: radial-gradient(70% 90% at 85% 20%, rgba(242,169,59,0.18) 0%, rgba(242,169,59,0) 60%), #0A0D14;">
  <div class="hero-text" style="display: flex; flex-direction: column; gap: 28px; max-width: 640px; position: relative; z-index: 1;">
    <span style="display: inline-flex; align-items: center; gap: 10px; align-self: flex-start; padding: 8px 14px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.12); font-size: 13px; font-weight: 600; color: #B7BFCC;">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: #5FD3A6;"></span>
      Two apps, now on the App Store
    </span>
    <h1 style="font-size: 72px; font-weight: 800; line-height: 1.02;">Master your time.<br>Grow every element of your life.</h1>
    <p style="font-size: 20px; line-height: 1.6; color: #B7BFCC; max-width: 560px;">Three Elements builds small, beautiful iPhone apps around one idea: Time, Money and Health are connected. Steal a routine from the world's best. Then focus on three things a day.</p>
    <div class="btn-row" style="display: flex; gap: 14px; flex-wrap: wrap;">
      {primary_btn("Get Celebrity Routines", "https://apps.apple.com/us/app/celebrity-routines/id6755641471")}
      {ghost_btn("Get Focus — it's free", "https://apps.apple.com/us/app/focus-daily-goals/id6760952606")}
    </div>
    <div class="checks" style="display: flex; align-items: center; gap: 28px; color: #8E97A8; font-size: 14px;">
      <span style="display: inline-flex; align-items: center; gap: 8px;">{ICON_CHECK}600+ routines</span>
      <span style="display: inline-flex; align-items: center; gap: 8px;">{ICON_CHECK}7-day free trial</span>
      <span style="display: inline-flex; align-items: center; gap: 8px;">{ICON_CHECK}No ads, ever</span>
    </div>
  </div>
  <div class="phones" style="position: relative; width: 560px; height: 660px; flex: none;">
    <div style="position: absolute; left: 0; top: 40px;">{screenshot_phone("r-profiles.jpg")}</div>
    <div style="position: absolute; left: 260px; top: 0;">{screenshot_phone("f-today.jpg")}</div>
  </div>
</div>

<div class="pad" style="padding: 40px 80px 96px; display: flex; flex-direction: column; gap: 40px;">
  {section_heading("The apps", "Two apps. One philosophy.", "Each one does a single thing well and stays out of your way.")}
  <div class="grid2" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px;">
    <div style="display: flex; flex-direction: column; gap: 22px; padding: 40px; border-radius: 28px; background: #121722; border: 1px solid rgba(255,255,255,0.06);">
      <div style="display: flex; align-items: center; justify-content: space-between;">
        <img src="img/icon-routines.png" alt="Celebrity Routines app icon" style="width: 64px; height: 64px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
        <span style="font-size: 13px; font-weight: 600; padding: 6px 12px; border-radius: 999px; background: rgba(242,169,59,0.14); color: #F2A93B;">7-day free trial</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <h3 style="font-size: 30px; font-weight: 700;">Celebrity Routines</h3>
        <p style="font-size: 17px; line-height: 1.6; color: #B7BFCC;">The daily habits of 600+ athletes, founders, musicians, authors and leaders — wake times, workouts, work blocks, principles and book picks. Build your own routine from the ones that fit you.</p>
      </div>
      <div class="card-foot" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 8px;">
        <span style="font-size: 15px; color: #8E97A8;">Premium from <strong style="color: #F4F5F7;">$6.99/mo</strong> billed yearly</span>
        <a href="routines.html" style="display: inline-flex; align-items: center; gap: 8px; color: #F2A93B; font-weight: 600; font-size: 15px;">Explore Routines {ICON_ARROW}</a>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 22px; padding: 40px; border-radius: 28px; background: #121722; border: 1px solid rgba(255,255,255,0.06);">
      <div style="display: flex; align-items: center; justify-content: space-between;">
        <img src="img/icon-focus.png" alt="Focus app icon" style="width: 64px; height: 64px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
        <span style="font-size: 13px; font-weight: 600; padding: 6px 12px; border-radius: 999px; background: rgba(95,211,166,0.14); color: #5FD3A6;">Free forever</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <h3 style="font-size: 30px; font-weight: 700;">Focus: Daily Goals</h3>
        <p style="font-size: 17px; line-height: 1.6; color: #B7BFCC;">What if you only had to focus on three things today? Set three goals, check them off, and watch streaks compound into real change. No ads, no paywall, no locked features.</p>
      </div>
      <div class="card-foot" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 8px;">
        <span style="font-size: 15px; color: #8E97A8;"><strong style="color: #F4F5F7;">$0</strong> — our way of giving back</span>
        <a href="focus.html" style="display: inline-flex; align-items: center; gap: 8px; color: #F2A93B; font-weight: 600; font-size: 15px;">Explore Focus {ICON_ARROW}</a>
      </div>
    </div>
  </div>
</div>

<div class="pad" style="padding: 0 80px 96px; display: flex; flex-direction: column; gap: 40px;">
  {section_heading("The three elements", "Time. Money. Health.", "You can't optimize one without affecting the others. Every app we make is designed to grow all three at once — not trade one for another.")}
  {element_cards()}
</div>

<div class="pad connect" style="padding: 0 80px 96px; display: flex; gap: 80px; align-items: flex-start;">
  <div class="connect-head" style="width: 400px; flex: none;">
    {section_heading("How they connect", "Together, they add up to something bigger.")}
  </div>
  <div style="display: flex; flex-direction: column; flex-grow: 1;">{equations()}</div>
</div>

<div class="band quote" style="margin: 0 80px 96px; padding: 64px 72px; border-radius: 32px; background: #121722; border: 1px solid rgba(255,255,255,0.06); display: flex; gap: 64px; align-items: center;">
  <svg width="56" height="56" viewBox="0 0 24 24" fill="#F2A93B" style="flex: none; opacity: 0.9;"><path d="M7.2 6C4.9 6 3 7.9 3 10.2c0 2 1.4 3.7 3.3 4.1-.4 1.4-1.4 2.5-2.9 3.2v1.5c3.7-.6 6.3-3.6 6.3-7.6V6H7.2Zm10 0C14.9 6 13 7.9 13 10.2c0 2 1.4 3.7 3.3 4.1-.4 1.4-1.4 2.5-2.9 3.2v1.5c3.7-.6 6.3-3.6 6.3-7.6V6h-2.5Z"></path></svg>
  <div style="display: flex; flex-direction: column; gap: 22px;">
    <p style="font-family: Sora, Helvetica, Arial, sans-serif; font-size: 30px; font-weight: 600; line-height: 1.35; letter-spacing: -0.01em;">"If I cooked more to eat healthy, I lost time. If I saved time with food delivery, I spent more money. If I focused on work to earn more, my health took a hit. That cycle became the seed for Three Elements."</p>
    <div class="quote-foot" style="display: flex; align-items: center; justify-content: space-between;">
      <span style="font-size: 15px; color: #8E97A8;"><strong style="color: #F4F5F7;">Harks</strong> — Founder, Three Elements Inc.</span>
      <a href="our-story.html" style="display: inline-flex; align-items: center; gap: 8px; color: #F2A93B; font-weight: 600; font-size: 15px;">Read our story {ICON_ARROW}</a>
    </div>
  </div>
</div>

{cta_band()}
{FOOTER}
''' + TAIL


def routines():
    global HEAD
    cats = ["Athletes", "Entrepreneurs", "Musicians", "Authors", "Tech Leaders", "World Leaders", "Scientists", "Actors", "Content Creators"]
    chips = "".join(f'<span style="font-size: 15px; font-weight: 500; padding: 12px 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.12); color: #F4F5F7;">{c}</span>' for c in cats)
    feats = [
        ("Full daily schedules", "Wake and sleep times, exercise, work blocks and wind-down — hour by hour."),
        ("Principles and philosophies", "The rules each person actually lives by, in their own words."),
        ("Quotes and book picks", "What they read, and the lines they keep coming back to."),
        ("Career turning points", "The moments that changed everything, and the lessons they took from them."),
        ("Build your own routine", "Borrow the pieces that fit you and assemble a day that's yours."),
        ("Request new profiles", "Premium members can request the people they want added next."),
    ]
    fgrid = "".join(f'''<div style="display: flex; flex-direction: column; gap: 10px; padding: 28px; border-radius: 20px; background: #121722; border: 1px solid rgba(255,255,255,0.06);">
      <h3 style="font-size: 20px; font-weight: 700;">{t}</h3>
      <p style="font-size: 15px; line-height: 1.6; color: #B7BFCC;">{d}</p>
    </div>''' for t, d in feats)
    return HEAD.replace("{title}","Celebrity Routines — daily routines of the world's best | Three Elements").replace("{desc}","Browse 600+ daily routines from athletes, founders, musicians and leaders, then build your own. 7-day free trial on iPhone.").replace("{slug}","routines.html") + nav("Routines") + f'''
<div class="grain hero" style="position: relative; overflow: hidden; padding: 96px 80px 80px; display: flex; align-items: center; justify-content: space-between; gap: 60px; background: radial-gradient(70% 90% at 85% 30%, rgba(242,169,59,0.2) 0%, rgba(242,169,59,0) 60%), #0A0D14;">
  <div class="hero-text" style="display: flex; flex-direction: column; gap: 26px; max-width: 640px; position: relative; z-index: 1;">
    <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #F2A93B;">Celebrity Routines · for iPhone</span>
    <h1 style="font-size: 68px; font-weight: 800; line-height: 1.04;">How the world's best actually spend their day.</h1>
    <p style="font-size: 20px; line-height: 1.6; color: #B7BFCC; max-width: 560px;">Browse the daily routines of 600+ people like Elon Musk, Oprah Winfrey, LeBron James and Taylor Swift — then build your own from the pieces that work for you.</p>
    <div class="btn-row" style="display: flex; gap: 14px; flex-wrap: wrap;">
      {primary_btn("Start 7-day free trial", "https://apps.apple.com/us/app/celebrity-routines/id6755641471")}
    </div>
    <span style="font-size: 14px; color: #8E97A8;">Rated 5.0 on the App Store · Requires iOS 17 or later</span>
  </div>
  <div class="phones" style="position: relative; width: 560px; height: 660px; flex: none;">
    <div style="position: absolute; left: 0; top: 40px;">{screenshot_phone("r-timeline.jpg")}</div>
    <div style="position: absolute; left: 260px; top: 0;">{screenshot_phone("r-profiles.jpg")}</div>
  </div>
</div>

<div class="pad" style="padding: 40px 80px 96px; display: flex; flex-direction: column; gap: 40px;">
  {section_heading("What's inside", "Every profile, in full.", "Not a listicle. A complete picture of how someone structures their time — and why.")}
  <div class="grid3" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px;">{fgrid}</div>
</div>

<div class="pad shots" style="padding: 0 80px 96px; display: flex; justify-content: center; gap: 32px; align-items: flex-end;">
  {screenshot_phone("r-kickstart.jpg", 260, 540)}
  {screenshot_phone("r-profiles.jpg", 260, 540)}
  {screenshot_phone("r-today.jpg", 260, 540)}
  {screenshot_phone("r-timeline.jpg", 260, 540)}
</div>

<div class="pad" style="padding: 0 80px 96px; display: flex; flex-direction: column; gap: 32px;">
  {section_heading("600+ profiles across", "Nine categories.")}
  <div style="display: flex; flex-wrap: wrap; gap: 12px;">{chips}</div>
</div>

<div class="pad" style="padding: 0 80px 96px; display: flex; flex-direction: column; gap: 40px; align-items: center;">
  {section_heading("Pricing", "Try everything free for 7 days.", "Browse for free. Premium unlocks all 600+ profiles, exclusive content and profile requests. Cancel anytime.", align="center")}
  <div class="pricing" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; width: 880px; max-width: 100%;">
    <div style="display: flex; flex-direction: column; gap: 22px; padding: 40px; border-radius: 28px; background: #121722; border: 2px solid #F2A93B; position: relative;">
      <span style="position: absolute; top: -14px; left: 32px; font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 6px 12px; border-radius: 999px; background: #F2A93B; color: #0A0D14;">Best value · Save 30%</span>
      <div style="display: flex; flex-direction: column; gap: 6px;">
        <h3 style="font-size: 22px; font-weight: 700;">Yearly</h3>
        <div style="display: flex; align-items: baseline; gap: 6px;">
          <span style="font-family: Sora, Helvetica, Arial, sans-serif; font-size: 56px; font-weight: 800; letter-spacing: -0.03em;">$84</span>
          <span style="font-size: 16px; color: #8E97A8;">/year</span>
        </div>
        <span style="font-size: 15px; color: #5FD3A6; font-weight: 600;">About $6.99 a month</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 12px; font-size: 15px; color: #B7BFCC;">
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}All 600+ profiles</span>
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}Request new profiles</span>
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}7-day free trial, cancel anytime</span>
      </div>
      {primary_btn("Start free trial", "https://apps.apple.com/us/app/celebrity-routines/id6755641471")}
    </div>
    <div style="display: flex; flex-direction: column; gap: 22px; padding: 40px; border-radius: 28px; background: #121722; border: 1px solid rgba(255,255,255,0.08);">
      <div style="display: flex; flex-direction: column; gap: 6px;">
        <h3 style="font-size: 22px; font-weight: 700;">Monthly</h3>
        <div style="display: flex; align-items: baseline; gap: 6px;">
          <span style="font-family: Sora, Helvetica, Arial, sans-serif; font-size: 56px; font-weight: 800; letter-spacing: -0.03em;">$9.99</span>
          <span style="font-size: 16px; color: #8E97A8;">/month</span>
        </div>
        <span style="font-size: 15px; color: #8E97A8;">Billed monthly</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 12px; font-size: 15px; color: #B7BFCC;">
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}All 600+ profiles</span>
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}Request new profiles</span>
        <span style="display: flex; align-items: center; gap: 10px;">{ICON_CHECK}7-day free trial, cancel anytime</span>
      </div>
      {ghost_btn("Start free trial", "https://apps.apple.com/us/app/celebrity-routines/id6755641471")}
    </div>
  </div>
  <p style="font-size: 13px; color: #5C6578; text-align: center; max-width: 560px;">Trial requires a payment method. You'll be charged at the end of the 7 days unless you cancel. Manage or cancel in your Apple ID settings.</p>
</div>

{cta_band()}
{FOOTER}
''' + TAIL


def focus():
    feats = [
        ("Three goals a day", "Intentional limitation. Three gradient cards, three checkboxes, nothing else competing for your attention."),
        ("Streaks that compound", "Complete all three and the streak grows. Miss a day and you start again — honestly."),
        ("A year at a glance", "A heat map of every day this year, so consistency is something you can see."),
        ("Weekly and monthly insights", "How often you finish, when you slip, and what a good week looks like for you."),
        ("End-of-day reflection", "A quick vibe check before bed. 365 unique daily messages to go with it."),
        ("Share your progress", "Insight cards you can post or send when a streak is worth celebrating."),
    ]
    fgrid = "".join(f'''<div style="display: flex; flex-direction: column; gap: 10px; padding: 28px; border-radius: 20px; background: #121722; border: 1px solid rgba(255,255,255,0.06);">
      <h3 style="font-size: 20px; font-weight: 700;">{t}</h3>
      <p style="font-size: 15px; line-height: 1.6; color: #B7BFCC;">{d}</p>
    </div>''' for t, d in feats)
    return HEAD.replace("{title}","Focus: Daily Goals — three goals a day, free forever | Three Elements").replace("{desc}","A beautifully simple daily goal app. Set three goals, build streaks, see a year at a glance. Free, no ads, no paywall.").replace("{slug}","focus.html") + nav("Focus") + f'''
<div class="grain hero" style="position: relative; overflow: hidden; padding: 96px 80px 80px; display: flex; align-items: center; justify-content: space-between; gap: 60px; background: radial-gradient(70% 90% at 85% 30%, rgba(91,108,255,0.24) 0%, rgba(91,108,255,0) 60%), #0A0D14;">
  <div class="hero-text" style="display: flex; flex-direction: column; gap: 26px; max-width: 640px; position: relative; z-index: 1;">
    <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #9B9CFF;">Focus: Daily Goals · iPhone</span>
    <h1 style="font-size: 68px; font-weight: 800; line-height: 1.04;">What if you only had to focus on three things today?</h1>
    <p style="font-size: 20px; line-height: 1.6; color: #B7BFCC; max-width: 560px;">Focus is a beautifully simple daily goal app built on one idea: intentional limitation. Set three goals, check them off, and build streaks that turn into real change.</p>
    <div class="btn-row" style="display: flex; gap: 14px; flex-wrap: wrap;">
      <a class="btn" href="https://apps.apple.com/us/app/focus-daily-goals/id6760952606" style="display: inline-flex; align-items: center; gap: 10px; height: 52px; padding: 0 26px; border-radius: 999px; background: linear-gradient(135deg, #5B6CFF, #9B5CFF); color: #FFFFFF; font-weight: 600; font-size: 16px;">{ICON_DL}Download free</a>
    </div>
    <span style="font-size: 14px; color: #8E97A8;">Free forever · No ads · No paywall · Rated 5.0 on the App Store</span>
  </div>
  <div class="phones" style="position: relative; width: 560px; height: 660px; flex: none;">
    <div style="position: absolute; left: 0; top: 40px;">{screenshot_phone("f-insights.jpg")}</div>
    <div style="position: absolute; left: 260px; top: 0;">{screenshot_phone("f-today.jpg")}</div>
  </div>
</div>

<div class="pad" style="padding: 40px 80px 96px; display: flex; flex-direction: column; gap: 40px;">
  {section_heading("How it works", "Less to manage. More to finish.")}
  <div class="grid3" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px;">{fgrid}</div>
</div>

<div class="pad shots" style="padding: 0 80px 96px; display: flex; justify-content: center; gap: 32px; align-items: flex-end;">
  {screenshot_phone("f-today.jpg", 260, 540)}
  {screenshot_phone("f-share.jpg", 260, 540)}
  {screenshot_phone("f-reflect.jpg", 260, 540)}
  {screenshot_phone("f-month.jpg", 260, 540)}
</div>

<div class="band free" style="margin: 0 80px 96px; padding: 64px 72px; border-radius: 32px; background: linear-gradient(135deg, rgba(91,108,255,0.18), rgba(155,92,255,0.10)), #121722; border: 1px solid rgba(255,255,255,0.08); display: flex; gap: 64px; align-items: center; justify-content: space-between;">
  <div style="display: flex; flex-direction: column; gap: 18px; max-width: 640px;">
    <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #9B9CFF;">Why it's free</span>
    <h2 style="font-size: 40px; font-weight: 700; line-height: 1.1;">Everything you see is everything you get.</h2>
    <p style="font-size: 18px; line-height: 1.6; color: #B7BFCC;">Focus is our way of giving back. No ads, no paywalls, no locked features — and nothing that auto-renews. If it helps you and you'd like to support more apps like it, there's a tip jar in Settings. No pressure at all.</p>
  </div>
  <div class="free-list" style="display: flex; flex-direction: column; gap: 10px; flex: none; width: 300px;">
    <div style="display: flex; justify-content: space-between; padding: 14px 18px; border-radius: 14px; background: rgba(255,255,255,0.05);"><span style="font-weight: 500;">Coffee</span><span style="color: #9B9CFF; font-weight: 600;">$1.99</span></div>
    <div style="display: flex; justify-content: space-between; padding: 14px 18px; border-radius: 14px; background: rgba(255,255,255,0.05);"><span style="font-weight: 500;">Pizza</span><span style="color: #9B9CFF; font-weight: 600;">$4.99</span></div>
    <div style="display: flex; justify-content: space-between; padding: 14px 18px; border-radius: 14px; background: rgba(255,255,255,0.05);"><span style="font-weight: 500;">Dinner</span><span style="color: #9B9CFF; font-weight: 600;">$14.99</span></div>
    <span style="font-size: 13px; color: #8E97A8; text-align: center; margin-top: 6px;">Tips never auto-renew. You're always in control.</span>
  </div>
</div>

{cta_band()}
{FOOTER}
''' + TAIL


def story():
    steps = [
        ("01", "The move", "Bay Area, California",
         "When I moved to the Bay Area for my first job out of college, life felt exciting — new city, new opportunities, and my first real paycheck. For the first time, I could afford the things I wanted.",
         None),
        ("02", "Something was off", "The 9-to-5 years",
         "Working a 9-to-5 meant less time for myself. I began eating out more, spending without thinking, and letting my health slip. Whenever I tried to fix one part of my life, another would fall behind.",
         None),
        ("03", "The trade-offs", "Every fix broke something else",
         "If I cooked more to eat healthy, I lost time. If I saved time with food delivery, I spent more money. If I focused on work to earn more, my health took a hit.",
         "tradeoff"),
        ("04", "The realization", "After a few years of the cycle",
         "Time, Health, and Money are deeply connected. You can't optimize one without affecting the others. The real challenge isn't mastering one — it's finding balance among all three.",
         "triangle"),
        ("05", "Three Elements Inc.", "A company built around harmony",
         "That realization became the seed for Three Elements. My goal is to create tools that help people live more intentionally, manage their time better, stay healthy, and make smarter financial choices — all without losing balance.",
         None),
        ("06", "Today", "Two apps, one idea",
         "Because true growth doesn't come from chasing one thing at a time — it comes from aligning all three.",
         "apps"),
    ]
    colors = {"Time": "#F2A93B", "Money": "#5FD3A6", "Health": "#F0678C"}

    def meter(label):
        c = colors[label]
        return f'''<div style="display: flex; flex-direction: column; gap: 8px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 600;"><span style="color: {c};">{label}</span><span class="m-{label.lower()}-txt" style="color: #8E97A8;">steady</span></div>
          <div style="height: 8px; border-radius: 999px; background: rgba(255,255,255,0.08); overflow: hidden;"><div class="m-{label.lower()}" style="height: 100%; width: 60%; background: {c}; border-radius: 999px; transition: width .6s cubic-bezier(.2,.8,.2,1);"></div></div>
        </div>'''

    tradeoff = f'''<div class="tradeoff" style="display: flex; flex-direction: column; gap: 22px; padding: 28px; border-radius: 24px; background: #121722; border: 1px solid rgba(255,255,255,0.08);">
      <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #8E97A8;">Try it — pick what I tried</span>
      <div class="tr-btns" style="display: flex; gap: 10px; flex-wrap: wrap;">
        <button class="tr-btn" data-t="cook" style="height: 44px; padding: 0 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.14); background: transparent; color: #F4F5F7; font: 600 15px 'DM Sans', Helvetica, Arial, sans-serif; cursor: pointer;">Cook more</button>
        <button class="tr-btn" data-t="delivery" style="height: 44px; padding: 0 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.14); background: transparent; color: #F4F5F7; font: 600 15px 'DM Sans', Helvetica, Arial, sans-serif; cursor: pointer;">Order delivery</button>
        <button class="tr-btn" data-t="work" style="height: 44px; padding: 0 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.14); background: transparent; color: #F4F5F7; font: 600 15px 'DM Sans', Helvetica, Arial, sans-serif; cursor: pointer;">Work harder</button>
      </div>
      <div style="display: flex; flex-direction: column; gap: 14px;">{meter("Time")}{meter("Money")}{meter("Health")}</div>
      <p class="tr-note" style="font-size: 15px; line-height: 1.6; color: #B7BFCC; min-height: 48px;">Pick one to see what happened to the other two.</p>
    </div>'''

    triangle = '''<div style="display: flex; align-items: center; justify-content: center; padding: 28px; border-radius: 24px; background: #121722; border: 1px solid rgba(255,255,255,0.08);">
      <svg class="tri" width="300" height="270" viewBox="0 0 300 270" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path class="tri-edge" d="M150 40 L260 220 L40 220 Z" stroke="rgba(255,255,255,0.18)" stroke-width="2" stroke-dasharray="720" stroke-dashoffset="720"></path>
        <circle cx="150" cy="40" r="26" fill="#0A0D14" stroke="#F2A93B" stroke-width="3"></circle>
        <circle cx="260" cy="220" r="26" fill="#0A0D14" stroke="#5FD3A6" stroke-width="3"></circle>
        <circle cx="40" cy="220" r="26" fill="#0A0D14" stroke="#F0678C" stroke-width="3"></circle>
        <text x="150" y="15" text-anchor="middle" fill="#F2A93B" font-family="Sora, Helvetica, Arial, sans-serif" font-weight="700" font-size="14">TIME</text>
        <text x="260" y="262" text-anchor="middle" fill="#5FD3A6" font-family="Sora, Helvetica, Arial, sans-serif" font-weight="700" font-size="14">MONEY</text>
        <text x="40" y="262" text-anchor="middle" fill="#F0678C" font-family="Sora, Helvetica, Arial, sans-serif" font-weight="700" font-size="14">HEALTH</text>
        <circle class="tri-dot" r="5" fill="#F4F5F7"><animateMotion dur="6s" repeatCount="indefinite" path="M150 40 L260 220 L40 220 Z"></animateMotion></circle>
        <text x="150" y="168" text-anchor="middle" fill="#8E97A8" font-family="DM Sans, Helvetica, Arial, sans-serif" font-size="13">move one, the others move</text>
      </svg>
    </div>'''

    apps = f'''<div style="display: flex; flex-direction: column; gap: 12px;">
      <a href="routines.html" style="display: flex; align-items: center; gap: 16px; padding: 18px 20px; border-radius: 20px; background: #121722; border: 1px solid rgba(255,255,255,0.08); color: #F4F5F7;">
        <img src="img/icon-routines.png" alt="Celebrity Routines app icon" style="width: 52px; height: 52px; border-radius: 14px;">
        <div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 17px;">Celebrity Routines</span><span style="font-size: 14px; color: #8E97A8;">Borrow a day from the world's best</span></div>
        <span style="margin-left: auto; color: #F2A93B;">{ICON_ARROW}</span>
      </a>
      <a href="focus.html" style="display: flex; align-items: center; gap: 16px; padding: 18px 20px; border-radius: 20px; background: #121722; border: 1px solid rgba(255,255,255,0.08); color: #F4F5F7;">
        <img src="img/icon-focus.png" alt="Focus app icon" style="width: 52px; height: 52px; border-radius: 14px;">
        <div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 17px;">Focus: Daily Goals</span><span style="font-size: 14px; color: #8E97A8;">Three things a day, free forever</span></div>
        <span style="margin-left: auto; color: #F2A93B;">{ICON_ARROW}</span>
      </a>
    </div>'''

    widgets = {"tradeoff": tradeoff, "triangle": triangle, "apps": apps}
    rows = ""
    for num, title, sub, body, w in steps:
        side = widgets.get(w, "")
        rows += f'''<div class="tl-step" style="display: grid; grid-template-columns: 72px minmax(0, 1fr); gap: 24px; opacity: 0; transform: translateY(24px); transition: opacity .7s ease, transform .7s ease;">
      <div style="display: flex; flex-direction: column; align-items: center;">
        <span class="tl-dot" style="width: 44px; height: 44px; border-radius: 50%; border: 2px solid rgba(255,255,255,0.14); background: #0A0D14; display: inline-flex; align-items: center; justify-content: center; font-family: Sora, Helvetica, Arial, sans-serif; font-weight: 700; font-size: 13px; color: #8E97A8; flex: none; transition: border-color .4s, color .4s;">{num}</span>
      </div>
      <div class="tl-body" style="display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); gap: 32px; align-items: start; padding-bottom: 72px;">
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #F2A93B;">{sub}</span>
          <h2 style="font-size: 34px; font-weight: 700; line-height: 1.1;">{title}</h2>
          <p style="font-size: 18px; line-height: 1.7; color: #D5DAE3;">{body}</p>
        </div>
        <div>{side}</div>
      </div>
    </div>'''

    script = '''<script>
(function () {
  var steps = document.querySelectorAll('.tl-step');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.style.opacity = 1; e.target.style.transform = 'none';
        var d = e.target.querySelector('.tl-dot'); if (d) { d.style.borderColor = '#F2A93B'; d.style.color = '#F2A93B'; }
        var t = e.target.querySelector('.tri-edge'); if (t) { t.style.transition = 'stroke-dashoffset 2.4s ease'; t.style.strokeDashoffset = 0; }
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.25 });
  steps.forEach(function (s) { io.observe(s); });

  var line = document.querySelector('.tl-line');
  var wrap = document.querySelector('.tl-wrap');
  function onScroll() {
    if (!line || !wrap) return;
    var r = wrap.getBoundingClientRect();
    var vh = window.innerHeight;
    var p = Math.min(1, Math.max(0, (vh * 0.6 - r.top) / r.height));
    line.style.height = (p * 100) + '%';
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var data = {
    cook:     { time: [30, 'lost'],   money: [70, 'better'], health: [85, 'better'], note: 'Cooking every meal was healthier and cheaper — and it ate my evenings.' },
    delivery: { time: [85, 'saved'],  money: [30, 'drained'], health: [45, 'slipped'], note: 'Delivery gave me back my time, and quietly emptied my wallet.' },
    work:     { time: [40, 'gone'],   money: [90, 'up'],     health: [35, 'took a hit'], note: 'More hours meant more money — and no energy left for anything else.' }
  };
  var btns = document.querySelectorAll('.tr-btn');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (x) { x.style.background = 'transparent'; x.style.borderColor = 'rgba(255,255,255,0.14)'; x.style.color = '#F4F5F7'; });
      b.style.background = '#F2A93B'; b.style.borderColor = '#F2A93B'; b.style.color = '#0A0D14';
      var d = data[b.getAttribute('data-t')];
      ['time', 'money', 'health'].forEach(function (k) {
        var bar = document.querySelector('.m-' + k); var txt = document.querySelector('.m-' + k + '-txt');
        if (bar) bar.style.width = d[k][0] + '%';
        if (txt) txt.textContent = d[k][1];
      });
      var n = document.querySelector('.tr-note'); if (n) n.textContent = d.note;
    });
  });
})();
</script>'''

    return HEAD.replace("{title}","Our Story — Three Elements Inc.").replace("{desc}","Why Three Elements exists: Time, Health and Money are deeply connected. The founder's story, step by step.").replace("{slug}","our-story.html") + nav("OurStory") + f'''
<div class="pad" style="padding: 96px 80px 48px; display: flex; flex-direction: column; gap: 20px; align-items: center;">
  <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #F2A93B;">Our story</span>
  <h1 style="font-size: 64px; font-weight: 800; line-height: 1.05; text-align: center; max-width: 900px;">You can't optimize one without affecting the others.</h1>
  <p style="font-size: 18px; line-height: 1.6; color: #8E97A8; text-align: center; max-width: 560px;">How a first paycheck in the Bay Area turned into a company. A note from Harks, founder — scroll through.</p>
</div>

<div class="pad" style="padding: 24px 80px 48px; display: flex; justify-content: center;">
  <div class="tl-wrap" style="position: relative; width: 100%; max-width: 1100px;">
    <div style="position: absolute; left: 21px; top: 44px; bottom: 72px; width: 2px; background: rgba(255,255,255,0.08);"></div>
    <div class="tl-line" style="position: absolute; left: 21px; top: 44px; width: 2px; height: 0%; background: linear-gradient(#F2A93B, #F0678C); transition: height .2s linear;"></div>
    <div style="display: flex; flex-direction: column; position: relative;">{rows}</div>
  </div>
</div>

<div class="pad" style="padding: 0 80px 96px; display: flex; flex-direction: column; gap: 40px;">
  {section_heading("What we build around", "Time. Money. Health.")}
  {element_cards()}
</div>

{cta_band()}
{FOOTER}
{script}
''' + TAIL


# ---------- privacy policies (verbatim from ~/Documents/Apps/*/…privacy… ) ----------

ROUTINES_POLICY = """
Three Elements Inc ("we," "us," or "our") operates the Celebrity Routines mobile application (the "App" or "Routines"). This Privacy Policy explains how we collect, use, and protect your information when you use our App.

## 1. Information We Collect

### Account Information
When you sign in using Google or Apple, we receive:
- Your email address
- Your name (if provided by the authentication service)
- A unique user identifier

We do not have access to your Google or Apple account passwords.

### Usage Data
We collect information about how you use the App:
- Daily app activity (dates when you open the App)
- Subscription status and billing cycle information
- Feature usage patterns

### Device Information
We may collect:
- Device type and operating system version
- App version
- General location (country/region) for analytics purposes

## 2. How We Use Your Information

We use the information we collect to:
- Provide and maintain the App
- Process your subscription and manage your account
- Track your loyalty program progress (daily app opens)
- Apply promotional offers and discounts you've earned
- Send important notifications about your account or subscription
- Improve and optimize the App experience
- Respond to your support requests

## 3. Third-Party Services

We use the following third-party services:

### Firebase (Google)
- Authentication: Securely manages your sign-in
- Firestore: Stores your activity data and preferences
- Privacy Policy: https://firebase.google.com/support/privacy

### RevenueCat
- Manages subscriptions and in-app purchases
- Privacy Policy: https://www.revenuecat.com/privacy

### Apple App Store
- Processes payments for subscriptions
- Privacy Policy: https://www.apple.com/legal/privacy

### Google Sign-In
- Provides authentication services
- Privacy Policy: https://policies.google.com/privacy

## 4. Data Retention

We retain your data for as long as your account is active or as needed to provide you services. If you delete your account, we will delete your personal data within 30 days, except where we are required to retain it for legal purposes.

## 5. Data Security

We implement appropriate security measures to protect your personal information, including:
- Encrypted data transmission (HTTPS/TLS)
- Secure authentication through Google and Apple
- Access controls on our database systems

## 6. Your Rights

You have the right to:
- Access the personal data we hold about you
- Request correction of inaccurate data
- Request deletion of your account and data
- Opt out of promotional communications

To exercise these rights, contact us at support@3elementsinc.com.

## 7. Children's Privacy

The App is not intended for children under 13. We do not knowingly collect personal information from children under 13. If you believe we have collected information from a child under 13, please contact us immediately.

## 8. Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy in the App and updating the "Last Updated" date.

## 9. Contact Us

If you have questions about this Privacy Policy, please contact us:

Three Elements Inc
Email: support@3elementsinc.com

By using the Routines app, you agree to the collection and use of information in accordance with this Privacy Policy.
"""

FOCUS_POLICY = """
## Introduction

Three Elements Inc ("we," "our," or "us") operates the Focus: Daily Goals mobile application ("Focus"). This Privacy Policy explains how we handle your information when you use our app.

## Our Privacy Promise

**We value your privacy 100%.** Focus is designed from the ground up to be completely private. We do not collect, store, transmit, or share any of your personal data. Period.

## Information We Collect

### We Collect Nothing

Focus does not collect any personal information. Specifically, we do **NOT** collect:

- Names, email addresses, or any contact information
- Location data
- Device identifiers or advertising IDs
- Usage analytics or behavioral data
- Health or fitness data
- Financial information
- Browsing history
- Crash reports or diagnostics
- Any form of tracking data

### No Accounts Required

Focus does not require account creation. There are no sign-ups, logins, passwords, or user profiles.

### No Third-Party Services

Focus does not use any third-party analytics, advertising, or tracking services. There are:

- No analytics SDKs (no Google Analytics, no Firebase, no Mixpanel)
- No advertising networks
- No crash reporting services
- No social media trackers

### Tip Jar (In-App Purchases)

Focus offers optional one-time tips via Apple's in-app purchase system. If you choose to leave a tip:

- The transaction is processed entirely by Apple through the App Store
- We do not collect or store your payment information, credit card details, or billing address
- Apple may share a transaction record with us (purchase date, product, and amount) but no personal identity information
- Tips are voluntary, never auto-renew, and do not unlock any additional features
- You can tip as many times as you like

## Data Storage

### On-Device Storage

All your data — goals, streaks, settings, and history — is stored exclusively on your device using Apple's SwiftData framework.

### iCloud Sync

If you have iCloud enabled on your device, Focus uses Apple's CloudKit to sync your data across your Apple devices signed into the same Apple ID. This sync is:

- **Managed entirely by Apple** — we have no access to your iCloud data
- **Encrypted** — data is encrypted in transit and at rest by Apple
- **Tied to your Apple ID** — only you can access your data
- **Optional** — if iCloud is disabled, the app works fully offline with local storage only

We do not operate any servers. We cannot see, access, or retrieve your data from iCloud.

For more information about iCloud privacy, see [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

## Data Sharing

We do **NOT** sell, trade, rent, or share your data with anyone. There is no data to share because we don't collect any.

## Data Deletion

Since all data is stored on your device and in your personal iCloud account:

- **Delete from device**: Use Settings > Reset All Data within the app to delete all local data
- **Delete from iCloud**: Deleting the app and removing it from iCloud (Settings > Apple ID > iCloud > Manage Storage) removes all synced data
- **No request needed**: Since we don't have your data, there's nothing for us to delete

## Children's Privacy

Focus does not collect any personal information from anyone, including children. The app is rated 4+ and is safe for all ages. We comply with the Children's Online Privacy Protection Act (COPPA) and similar regulations by simply not collecting any data.

## Offline Functionality

Focus works 100% offline. No internet connection is required to use any feature of the app. When an internet connection is available and iCloud is enabled, data syncs automatically in the background.

## Changes to This Policy

We may update this Privacy Policy periodically. Any changes will be reflected in the "Last Updated" date at the top of this policy. Since we don't collect email addresses, we recommend checking this policy occasionally.

## Contact Us

For privacy-related questions:
- Email: support@3elementsinc.com
- Company: Three Elements Inc
"""


def md_to_html(text, accent):
    """Tiny converter for the policy markdown above: ##, ###, - lists, **bold**, [t](u), bare URLs/emails."""
    import html as _html, re as _re

    def inline(s):
        s = _html.escape(s, quote=False)
        s = _re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        s = _re.sub(r"(?<![\"'>])(https?://[^\s<]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
        s = _re.sub(r"([\w.+-]+@[\w-]+\.[\w.]+)", r'<a href="mailto:\1">\1</a>', s)
        s = _re.sub(r"\*\*([^*]+)\*\*", r'<strong style="color: #F4F5F7; font-weight: 600;">\1</strong>', s)
        return s

    P = 'style="font-size: 16px; line-height: 1.75; color: #B7BFCC;"'
    H2 = 'style="font-size: 22px; font-weight: 700; line-height: 1.2; margin-top: 12px;"'
    H3 = 'style="font-size: 16px; font-weight: 600; line-height: 1.3; color: #F4F5F7; margin-top: 4px;"'
    UL = 'style="margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 8px; font-size: 16px; line-height: 1.65; color: #B7BFCC;"'
    LI = f'style="padding-left: 4px;"'

    out, para, items = [], [], []

    def flush_para():
        if para:
            out.append(f"<p {P}>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        if items:
            lis = "".join(f'<li {LI}>{inline(i)}</li>' for i in items)
            out.append(f'<ul class="policy-list" {UL} data-accent="{accent}">{lis}</ul>')
            items.clear()

    for raw in text.strip().splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        if line.startswith("### "):
            flush_para(); flush_list(); out.append(f"<h3 {H3}>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_para(); flush_list(); out.append(f"<h2 {H2}>{inline(line[3:])}</h2>")
        elif line.startswith("- "):
            flush_para(); items.append(line[2:])
        else:
            flush_list(); para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(out)


def privacy():
    apps = [
        ("routines", "Celebrity Routines", "img/icon-routines.png", "December 25, 2025", "#F2A93B",
         "Requires a Google or Apple sign-in and a subscription, so it collects the minimum needed to run your account.",
         ROUTINES_POLICY),
        ("focus", "Focus: Daily Goals", "img/icon-focus.png", "March 2026", "#7B7CFF",
         "Collects nothing. No accounts, no analytics, no servers — your data stays on your device and in your own iCloud.",
         FOCUS_POLICY),
    ]

    chips = ""
    for slug, name, icon, updated, accent, _, _ in apps:
        chips += f'''<a class="btn" href="#{slug}" style="display: inline-flex; align-items: center; gap: 10px; height: 48px; padding: 0 18px 0 8px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.14); background: #121722; color: #F4F5F7; font-weight: 600; font-size: 15px;">
          <img src="{icon}" alt="" width="32" height="32" style="border-radius: 9px;">{name}<span style="color: {accent};">{ICON_ARROW}</span></a>\n'''

    sections = ""
    for slug, name, icon, updated, accent, blurb, body in apps:
        sections += f'''
  <section id="{slug}" class="legal-card" style="scroll-margin-top: 24px; display: flex; flex-direction: column; gap: 24px; padding: 40px; border-radius: 28px; background: #121722; border: 1px solid rgba(255,255,255,0.08); border-top: 3px solid {accent};">
    <div class="legal-head" style="display: flex; align-items: center; gap: 18px;">
      <img src="{icon}" alt="{name} app icon" width="64" height="64" style="border-radius: 16px; flex-shrink: 0;">
      <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0;">
        <h2 style="font-size: 28px; font-weight: 800; line-height: 1.1;">{name}</h2>
        <span style="font-size: 13px; color: #8E97A8;">Privacy Policy · Last updated <span style="color: #F4F5F7;">{updated}</span></span>
      </div>
    </div>
    <p style="font-size: 17px; line-height: 1.6; color: #F4F5F7; padding: 16px 20px; border-radius: 16px; background: rgba(255,255,255,0.04); border-left: 3px solid {accent};">{blurb}</p>
    <div class="policy" style="display: flex; flex-direction: column; gap: 14px;">
{md_to_html(body, accent)}
    </div>
  </section>
'''

    return HEAD.replace("{title}","Privacy Policy — Three Elements Inc.").replace("{desc}","Privacy policies for Celebrity Routines and Focus: Daily Goals by Three Elements Inc.").replace("{slug}","privacy.html") + nav("Privacy") + f'''
<style>
  .policy a {{ overflow-wrap: anywhere; }}
  .policy-list li::marker {{ color: #8E97A8; }}
  .policy-list[data-accent="#F2A93B"] li::marker {{ color: #F2A93B; }}
  .policy-list[data-accent="#7B7CFF"] li::marker {{ color: #9B5CFF; }}
  @media (max-width: 820px) {{
    .legal-card {{ padding: 28px 20px !important; border-radius: 22px !important; }}
    .legal-head h2 {{ font-size: 24px !important; }}
    .legal-wrap {{ gap: 28px !important; }}
  }}
</style>
<div class="pad" style="padding: 80px 80px 96px; display: flex; flex-direction: column; align-items: center;">
  <div class="legal-wrap" style="width: 100%; max-width: 820px; display: flex; flex-direction: column; gap: 40px;">
    <div style="display: flex; flex-direction: column; gap: 18px;">
      <span style="font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: #F2A93B;">Legal</span>
      <h1 style="font-size: 52px; font-weight: 800; line-height: 1.05;">Privacy Policy</h1>
      <p style="font-size: 18px; line-height: 1.65; color: #B7BFCC; max-width: 640px;">Three Elements Inc. makes two iPhone apps, and each has its own privacy policy. Jump to the app you use — both are written to be read, not skimmed past.</p>
      <div class="btn-row" style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 6px;">
{chips}      </div>
    </div>
{sections}
    <p style="font-size: 15px; line-height: 1.7; color: #8E97A8;">Questions about either policy? Email <a href="mailto:support@3elementsinc.com">support@3elementsinc.com</a>. Three Elements Inc. · Bay Area, California.</p>
  </div>
</div>
{FOOTER}
''' + TAIL

if __name__ == "__main__":
    import os
    os.makedirs("site/img", exist_ok=True)
    for fname, fn in [("index.html", home), ("routines.html", routines), ("focus.html", focus), ("our-story.html", story), ("privacy.html", privacy)]:
        with open(f"site/{fname}", "w") as f:
            f.write(fn())
        print("wrote", fname)
