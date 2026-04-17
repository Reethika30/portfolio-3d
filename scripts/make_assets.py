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
    # decorative circles only - no big text (carousel shows the project name)
    d.ellipse([-260, -260, 460, 460], outline=accent, width=10)
    d.ellipse([W - 420, H - 420, W + 260, H + 260], outline=accent, width=10)
    d.ellipse([W - 300, -160, W + 140, 280], fill=accent)
    d.ellipse([-120, H - 320, 360, H + 160], fill=accent)
    fc = get_font(34)
    d.text((70, H - 80), sub, fill="#FFFFFF", font=fc)
    path = f"{OUT}/project-{slug}.png"
    img.save(path, "PNG", optimize=True)
    return path


for slug, title, sub, bg, ac in PROJECTS:
    p = render_project(slug, title, sub, bg, ac)
    print("project:", p)
