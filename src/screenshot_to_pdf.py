import time
import pyautogui
from PIL import Image
import os
from pathlib import Path

try:
    total = int(input("How many screenshots do you want to take? "))
except ValueError:
    print("Please enter a valid number.")
    exit()

print("You have 10 seconds to prepare before screenshots start...")
time.sleep(10)

desktop_path = Path.home() / "Desktop"
screenshot_dir = desktop_path / "ScreenshotToPDF"
os.makedirs(screenshot_dir, exist_ok=True)

screenshot_files = []

print(f"→ Taking {total} screenshots. Pressing Right Arrow, waiting 30ms, then capturing...")

for i in range(1, total + 1):
    screenshot = pyautogui.screenshot()
    filename = screenshot_dir / f"shot_{i:03}.png"
    screenshot.save(filename)
    screenshot_files.append(str(filename))
    print(f"[+] Screenshot {i} saved.")
    pyautogui.press("right")           
    time.sleep(0.06)                  

if screenshot_files:
    images = [Image.open(f).convert('RGB') for f in screenshot_files]
    pdf_path = screenshot_dir / "screenshots_combined.pdf"
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f"[✓] PDF saved at '{pdf_path}'")
    
    os.system(f'open "{screenshot_dir}"')
else:
    print("[x] No screenshots were taken.")