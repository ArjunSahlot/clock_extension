import os
import sys
import zipfile
import urllib.request
from tkinter import Tk
from tkinter.filedialog import askdirectory
Tk().withdraw()

print("Choose installation location.")
dir = askdirectory()
tmp = os.path.join(dir, "tmp")
file = "clock_extension-main"
print("Installing...")
urllib.request.urlretrieve("https://github.com/ArjunSahlot/clock_extension/archive/main.zip", tmp)

print("Unzipping")
with zipfile.ZipFile(tmp, 'r') as zip:
    zip.extractall(dir)

print("Cleaning up")
final = os.path.join(dir, file.split("-")[0]
os.rename(os.path.join(dir, file), final))

print("Done!")
