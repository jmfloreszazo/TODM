#!/usr/bin/env python3
"""Build a contact sheet from the PDF pages rendered by the review workflow."""
from pathlib import Path
from PIL import Image, ImageDraw
root = Path(__file__).resolve().parents[1]
pages = sorted((root / "paper/v2-review-pages").glob("page-*.png"))
assert pages
width, height, columns = 420, 610, 3
sheet = Image.new("RGB", (width * columns, height * ((len(pages) + columns - 1) // columns)), "#e5e5e5")
for index, path in enumerate(pages):
    image = Image.open(path).convert("RGB")
    image.thumbnail((width - 20, height - 35))
    x, y = (index % columns) * width, (index // columns) * height
    ImageDraw.Draw(sheet).text((x + 10, y + 5), f"Page {index + 1}", fill="black")
    sheet.paste(image, (x + (width - image.width) // 2, y + 25))
sheet.save(root / "paper/TODM_Preview_v2.0.png")
