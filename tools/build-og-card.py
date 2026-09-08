"""Build the 1200x630 og:image for educationaluplift.com.

Renders through Chrome so the card uses the site's own self-hosted Nunito and
the same palette tokens as index.html — an approximation drawn with a raster
library would drift from the page it represents.

Font and wordmark are base64-embedded rather than linked: Chrome applies CORS
to @font-face over file://, and an inline data: URI sidesteps that entirely.
"""
import base64
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
LANDING = HERE.parent          # the repo root

font_b64 = base64.b64encode((LANDING / "fonts/nunito-latin.woff2").read_bytes()).decode()
mark_b64 = base64.b64encode((LANDING / "edup-wordmark.png").read_bytes()).decode()

# Every colour below is a token value copied from the :root block in
# index.html. Nothing is invented for the card.
HTML = f"""<!doctype html>
<html lang="et"><head><meta charset="utf-8">
<style>
@font-face{{font-family:Nunito;font-style:normal;font-weight:400 1000;
  src:url(data:font/woff2;base64,{font_b64}) format('woff2');}}
:root{{
  --accent:#4978A7;
  --accent-soft:#DDEDFF;
  --bg-primary:#F4F9FF;
  --surface-card:#FFFFFF;
  --text-primary:#1B2025;
  --text-secondary:#65696F;
  --border-color:rgba(0,0,0,.09);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px}}
body{{
  font-family:Nunito,system-ui,sans-serif;
  background:var(--bg-primary);
  color:var(--text-primary);
  position:relative;
  overflow:hidden;
}}
/* Rounder, not faceted: one soft disc of the accent tint bleeding off the
   right edge, so the card has depth without any hard geometry. */
.blob{{
  position:absolute;
  width:760px;height:760px;border-radius:50%;
  right:-250px;top:-190px;
  background:var(--accent-soft);
}}
.in{{
  position:relative;
  height:100%;
  padding:58px 72px;
  display:flex;flex-direction:column;
  /* Left-aligned, like every page shell in the app. */
  align-items:flex-start;
}}
/* Sized by height per brand/README.md — the arrow rises well above the
   lettering, so a height that looks generous still sets modest letters. */
.mark{{height:130px;width:auto;display:block;margin-left:-6px}}
h1{{
  font-size:64px;line-height:1.1;font-weight:800;
  letter-spacing:-.5px;
  /* Narrow enough that it breaks on word boundaries into three lines; no
     soft hyphen, which rendered a literal "matemaatika-ülesanded". */
  max-width:720px;
  margin-top:auto;
  padding-top:20px;
}}
.pills{{
  display:flex;gap:12px;list-style:none;
  margin-top:30px;
}}
.pills li{{
  background:var(--surface-card);
  border:1px solid var(--border-color);
  color:var(--accent);
  font-size:23px;font-weight:700;
  padding:11px 24px;border-radius:999px;
  white-space:nowrap;
}}
.foot{{
  margin-top:auto;
  font-size:24px;font-weight:600;
  color:var(--text-secondary);
}}
</style></head>
<body>
<div class="blob"></div>
<div class="in">
  <img class="mark" src="data:image/png;base64,{mark_b64}" alt="EdUp">
  <h1>Diferentseeritud matemaatikaülesanded 1.–9.&nbsp;klassile</h1>
  <ul class="pills">
    <li>1.–9. klass</li>
    <li>Riiklik õppekava</li>
    <li>Matemaatika</li>
  </ul>
  <p class="foot">educationaluplift.com</p>
</div>
</body></html>
"""

src = HERE / ".card.build.html"   # scratch, git-ignored
src.write_text(HTML, encoding="utf-8")
out = LANDING / "og-card.png"

chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
r = subprocess.run([
    chrome, "--headless", "--disable-gpu", "--no-sandbox",
    "--hide-scrollbars", "--force-device-scale-factor=1",
    f"--screenshot={out}", "--window-size=1200,630",
    f"file://{src}",
], capture_output=True, text=True, timeout=120)

print("chrome exit:", r.returncode)
if not out.exists():
    print(r.stderr[-2000:])
else:
    print("wrote", out, out.stat().st_size, "bytes")
