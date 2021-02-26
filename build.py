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

<<<<<<< HEAD
print("Cleaning up")
final = os.path.join(dir, file.split("-")[0]
os.rename(os.path.join(dir, file), final))
=======
os.rename(os.path.join(dir, file), os.path.join(dir, file.split("-")[0]))
>>>>>>> df548bb3cff6c79c521eecf010146838104f22af
os.remove(os.path.join(tmp))

with open(os.path.join(final, "requirements.txt"), "r") as f:
    packages = f.read().split("
")

if sys.platform == "windows":
    cmd = "pip install "
else:
    cmd = "pip3 install "

print("Installing packages")
for package in packages:
    if "n" in input(f"Install" + package + "? [y/n] ").lower():
        continue
    os.system(cmd.format(package))

print("Done!")
