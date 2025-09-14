import os

# Path to your images folder
images_path = os.path.join(os.getcwd(), "images")

# Collect all files in the images folder
if not os.path.exists(images_path):
    print("⚠️ The 'images' folder does not exist in your project.")
    exit()

image_files = set(os.listdir(images_path))

# Look through index.html for image references
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("🔎 Checking for missing images...\n")
missing = False
for file in image_files:
    if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
        if file not in html:
            print(f"⚠️ '{file}' is in the folder but not used in index.html")

# Look for image names in the HTML that might not exist
import re
matches = re.findall(r'images/([a-zA-Z0-9._-]+)', html)
for match in matches:
    if match not in image_files:
        print(f"❌ '{match}' is referenced in HTML but not found in images folder")
        missing = True

if not missing:
    print("✅ All images are correctly linked!")
