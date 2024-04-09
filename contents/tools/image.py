import os
import glob
# pip install pillow
from PIL import Image, ImageDraw, ImageFont


def chen_van_ban_vao_anh(duong_dan_anh):
    anh = Image.open(duong_dan_anh)
    draw = ImageDraw.Draw(anh)
    font = ImageFont.truetype("arial.ttf", 100)
    draw.text((0, 0), "Vũ Văn Nghĩa 20206205", fill=(255, 255, 5), font=font)
    anh.save(duong_dan_anh)


root = r"../../"
png_files = glob.glob(os.path.join(root, "**/*.png"), recursive=True)
for i in png_files:
    if i.endswith(".excalidraw.png"):
        continue
    chen_van_ban_vao_anh(i)
