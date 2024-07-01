import requests
import ctypes
from PIL import Image
import os

wallpaper_url = "PATH"

response = requests.get(wallpaper_url)
with open("wallpaper.jpg", "wb") as f:
    f.write(response.content)

img_path = os.path.abspath("wallpaper.jpg")
img = Image.open(img_path)
img.save(os.path.abspath("wallpaper.bmp"))

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("wallpaper.bmp"), 3)
