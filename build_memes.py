#!/usr/bin/env python3
"""Build three GTA 6 meme options for make.fun gta6-meme-x-01.

Each meme: one of the user's own GTA VI stills + the make.fun ghost worked
into the scene (drawn to the contest's own description: a white ghost with a
thick black outline, two black four-pointed sparkle eyes and a round little
hand, holding a magenta coin with a white star) + a short caption.
Output: JPEGs sized for X, text still readable at the judge's 480px view.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

SRC = os.path.expanduser('~/workspace/user/media_library/image')
OUT = os.path.expanduser('~/workspace/goals/free-money-hunter-ai/deliverables/gta6-meme-x-01')
FONT = os.path.expanduser('~/workspace/gta-cinematic-editorial/fonts/Anton.ttf')
MAGENTA = (233, 63, 216)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

STILLS = {
    'aerial': 'tGlLWCq6vHdXnUpgDJ2AJFLAiTtrbg0ycFARc9kBXUhfR7-ZkOo7_amUjTYLbskmkqV-mVfXab3oDro64xHWzRZgDPdyFb76u9rfdO36B0GgW25G_15ufUrSCGZ0iMadCWk6H6PCzAyzQEv6jehYal-8lXB_NIbVjuxOaPzngzMFtOStuK8cNiwSj9t0PnyU.jpg',
    'hotel': 'JVrm4plgvD8GghGJ3WsCQgcMnPmyiPHI56nnTbSs3lFOEQkbxTrthnS_zerNpDPra_sXBYbToZy6gwMIK283Kfmu9y0Tp5iobn7rAR30GusqiFN8g84j4UL4QXJg3utTewB9Qr9gtCsAz0pnjTXq5myGY6TNQ7JfT9Kh5dnm42IVulmtd1UW_SYDsHoJNhVw.jpg',
    'lucia': 'bo2-fqHDbsBsFBFcXUPgh4TCg41-kdwIQBeMKdzBPEzwmUNvH0wdQNv1IDkVodf0Z5HHNdneqU1Esr5gJKehjJRtyuTgpoGP_S1AjV4A-H0zjD7eKPaOhV9H74Mde5TJS2ikJx1FOzdtpcKbwNfjSYVmesSLun7ZpSsbzkNatzalIW2Cfv6oZ9QS1QCmPjcP.jpg',
}


def sparkle(cx, cy, r):
    """Four-pointed sparkle polygon (the ghost's eyes)."""
    w = r * 0.20
    return [(cx, cy - r), (cx + w, cy - w), (cx + r, cy), (cx + w, cy + w),
            (cx, cy + r), (cx - w, cy + w), (cx - r, cy), (cx - w, cy - w)]


def star(cx, cy, r):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return pts


def ghost(height):
    """Draw the make.fun ghost at the given pixel height. Returns RGBA image."""
    S = 4  # supersample
    W, H = int(height * 0.86), height
    img = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    w, h = W * S, H * S
    mx = w * 0.10                      # side margin
    top = h * 0.03
    bottom = h * 0.97
    # body outline: dome + straight sides + scalloped bottom
    path = []
    steps = 60
    for i in range(steps + 1):         # dome, left to right
        t = math.pi * (1 - i / steps)
        path.append((w / 2 + (w / 2 - mx) * math.cos(t), top + (h * 0.34) * (1 - math.sin(t)) * 0 + (h * 0.36) * (1 - math.sin(t))))
    # fix dome: recompute cleanly below
    path = []
    dome_h = h * 0.38
    for i in range(steps + 1):
        t = math.pi * (1 - i / steps)  # pi..0
        x = w / 2 + (w / 2 - mx) * math.cos(t)
        y = top + dome_h - dome_h * math.sin(t)
        path.append((x, y))
    path.append((w - mx, bottom - h * 0.06))
    bumps = 3
    for b in range(bumps):             # scalloped bottom, right to left
        cx = (w - mx) - (b + 0.5) * ((w - 2 * mx) / bumps)
        r = (w - 2 * mx) / bumps / 2
        for i in range(1, 13):
            t = math.pi * (i / 12)
            path.append((cx - r * math.cos(t), bottom - h * 0.06 + h * 0.045 * math.sin(t)))
    path.append((mx, bottom - h * 0.06))
    # thick black outline: draw the path scaled up in black, then white on top
    cx0, cy0 = w / 2, h / 2
    big = [(cx0 + (x - cx0) * 1.055, cy0 + (y - cy0) * 1.035) for (x, y) in path]
    d.polygon(big, fill=BLACK + (255,))
    d.polygon(path, fill=WHITE + (255,))
    # eyes: two black four-pointed sparkles
    er = h * 0.075
    d.polygon(sparkle(w * 0.36, h * 0.36, er), fill=BLACK + (255,))
    d.polygon(sparkle(w * 0.60, h * 0.36, er), fill=BLACK + (255,))
    # coin: magenta disc with white star, held low right
    coin_r = h * 0.16
    ccx, ccy = w * 0.70, h * 0.70
    d.ellipse([ccx - coin_r * 1.12, ccy - coin_r * 1.12, ccx + coin_r * 1.12, ccy + coin_r * 1.12], fill=BLACK + (255,))
    d.ellipse([ccx - coin_r, ccy - coin_r, ccx + coin_r, ccy + coin_r], fill=MAGENTA + (255,))
    d.polygon(star(ccx, ccy, coin_r * 0.62), fill=WHITE + (255,))
    # round little hand over the coin edge
    hr = h * 0.075
    hx, hy = w * 0.545, h * 0.635
    d.ellipse([hx - hr * 1.15, hy - hr * 1.15, hx + hr * 1.15, hy + hr * 1.15], fill=BLACK + (255,))
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=WHITE + (255,))
    img = img.resize((W, H), Image.LANCZOS)
    return img


def paste_ghost(base, g, cx, feet_y, reflection=False, shadow=True):
    """Paste ghost centred at cx with its feet at feet_y; optional wet reflection."""
    cx = int(cx)
    feet_y = int(feet_y)
    x = int(cx - g.width / 2)
    y = int(feet_y - g.height)
    if shadow:
        sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
        ds = ImageDraw.Draw(sh)
        ds.ellipse([cx - g.width * 0.34, feet_y - g.height * 0.03,
                    cx + g.width * 0.34, feet_y + g.height * 0.045], fill=(0, 0, 0, 130))
        base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(g.height * 0.03)))
    if reflection:
        refl = g.transpose(Image.FLIP_TOP_BOTTOM)
        refl = refl.resize((g.width, int(g.height * 0.30)), Image.LANCZOS)
        alpha = refl.split()[3].point(lambda a: int(a * 0.35))
        refl.putalpha(alpha)
        base.alpha_composite(refl, (x, feet_y + 2))
    base.alpha_composite(g, (x, y))


def caption(base, text, top=True):
    """Classic meme caption: Anton, white, thick black stroke, auto-fit."""
    W, H = base.size
    d = ImageDraw.Draw(base)
    size = int(W * 0.085)
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        box = d.textbbox((0, 0), text, font=f, stroke_width=size // 11)
        if box[2] - box[0] <= W * 0.94:
            break
        size -= 4
    f = ImageFont.truetype(FONT, size)
    box = d.textbbox((0, 0), text, font=f, stroke_width=size // 11)
    tw = box[2] - box[0]
    th = box[3] - box[1]
    x = (W - tw) / 2 - box[0]
    y = H * 0.028 if top else H - H * 0.028 - th - box[1]
    d.text((x, y), text, font=f, fill=WHITE, stroke_width=size // 11, stroke_fill=BLACK)


def build(name, still_key, top_text, bottom_text, ghost_h_frac, ghost_cx_frac,
          feet_frac, reflection=False, max_w=None):
    im = Image.open(os.path.join(SRC, STILLS[still_key])).convert('RGBA')
    if max_w and im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    W, H = im.size
    g = ghost(int(H * ghost_h_frac))
    paste_ghost(im, g, W * ghost_cx_frac, H * feet_frac, reflection=reflection)
    caption(im, top_text, top=True)
    caption(im, bottom_text, top=False)
    out = os.path.join(OUT, name)
    im.convert('RGB').save(out, quality=90)
    print(out, im.size, os.path.getsize(out), 'bytes')


os.makedirs(OUT, exist_ok=True)

# Meme 1: launch-day sick day, aerial city + police helicopter searchlight;
# the ghost hides on a rooftop just outside the searchlight beam
build('meme-1-sick-day.jpg', 'aerial',
      'MY BOSS LOOKING FOR ME ON LAUNCH DAY', "ME, HOME 'SICK' IN VICE CITY",
      ghost_h_frac=0.30, ghost_cx_frac=0.235, feet_frac=0.845)

# Meme 2: the 13-year wait and the $79.99 check-in, deco hotel forecourt
build('meme-2-check-in.jpg', 'hotel',
      'WAITED 13 YEARS TO CHECK IN', '$79.99 A NIGHT. ZERO REGRETS.',
      ghost_h_frac=0.33, ghost_cx_frac=0.32, feet_frac=0.775, reflection=True, max_w=1800)

# Meme 3: Lucia's new partner, close-up at the car window
build('meme-3-new-partner.jpg', 'lucia',
      'LUCIA GOT A NEW PARTNER IN CRIME', 'SORRY, JASON',
      ghost_h_frac=0.54, ghost_cx_frac=0.815, feet_frac=0.94)
