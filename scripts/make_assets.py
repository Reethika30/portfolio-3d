"""Generate branded PNG textures for tech balls and project preview cards."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "public/images"
os.makedirs(OUT, exist_ok=True)


def get_font(size: int):
    for name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()


# ---------- Tech ball textures (square, used as MeshPhysicalMaterial map) ----------
TECH = [
    ("python",       "Python",      "#3776AB", "#FFD43B"),
    ("sql",          "SQL",         "#003B57", "#F0F0F0"),
    ("snowflake",    "Snowflake",   "#29B5E8", "#FFFFFF"),
    ("bigquery",     "BigQuery",    "#669DF6", "#FFFFFF"),
    ("airflow",      "Airflow",     "#017CEE", "#FFFFFF"),
    ("dbt",          "dbt",         "#FF694A", "#FFFFFF"),
    ("aws",          "AWS",         "#232F3E", "#FF9900"),
    ("azure",        "Azure",       "#0078D4", "#FFFFFF"),
    ("gcp",          "GCP",         "#4285F4", "#FFFFFF"),
    ("spark",        "Spark",       "#E25A1C", "#FFFFFF"),
    ("pytorch",      "PyTorch",     "#EE4C2C", "#FFFFFF"),
    ("huggingface",  "HF \U0001F917", "#FFD21F", "#1F2937"),
]


def render_tech(slug: str, label: str, bg: str, fg: str):
    size = 512
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    # subtle inner ring
    d.ellipse([20, 20, size - 20, size - 20], outline=fg, width=4)
    # label
    f = get_font(96 if len(label) <= 7 else 72)
    bbox = d.textbbox((0, 0), label, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]),
           label, fill=fg, font=f)
    path = f"{OUT}/tech-{slug}.png"
    img.save(path, "PNG", optimize=True)
    return path


for slug, label, bg, fg in TECH:
    p = render_tech(slug, label, bg, fg)
    print("tech:", p)


# ---------- Project preview cards (used by Work carousel <img>) ----------
PROJECTS = [
    ("retaildw",  "Retail Data Warehouse",         "Snowflake \u00b7 dbt \u00b7 Airflow",        "#0E7490", "#67E8F9"),
    ("nlp",       "Seq2Seq + Bahdanau Attention",  "PyTorch \u00b7 Gradio \u00b7 Hugging Face",  "#7C3AED", "#C4B5FD"),
    ("yolo",      "YOLOv8 + ByteTrack",            "Ultralytics \u00b7 Streamlit \u00b7 Docker", "#DB2777", "#FBCFE8"),
    ("sentiment", "Sentiment & Emotion Dashboard", "XLM-RoBERTa \u00b7 Streamlit \u00b7 Plotly", "#059669", "#A7F3D0"),
]


def render_project(slug: str, title: str, sub: str, bg: str, accent: str):
    W, H = 1280, 800
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    # decorative circles
    d.ellipse([-200, -200, 400, 400], outline=accent, width=8)
    d.ellipse([W - 380, H - 380, W + 220, H + 220], outline=accent, width=8)
    d.ellipse([W - 260, -120, W + 100, 240], fill=accent)

    # title
    ft = get_font(86)
    fs = get_font(40)
    # word-wrap title at ~22 chars
    words = title.split(); lines = []; cur = ""
    for w in words:
        if len(cur + " " + w) > 22:
            lines.append(cur.strip()); cur = w
        else:
            cur += " " + w
    if cur:
        lines.append(cur.strip())
    y = 200
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=ft)
        d.text((90 - bbox[0], y - bbox[1]), line, fill="#FFFFFF", font=ft)
        y += (bbox[3] - bbox[1]) + 16
    # subtitle
    bbox = d.textbbox((0, 0), sub, font=fs)
    d.text((90 - bbox[0], y + 30 - bbox[1]), sub, fill=accent, font=fs)
    # corner tag
    fc = get_font(28)
    d.text((90, H - 90), "Live demo \u2192", fill="#FFFFFF", font=fc)
    path = f"{OUT}/project-{slug}.png"
    img.save(path, "PNG", optimize=True)
    return path


for slug, title, sub, bg, ac in PROJECTS:
    p = render_project(slug, title, sub, bg, ac)
    print("project:", p)
