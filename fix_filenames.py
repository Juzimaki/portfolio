import os
import re

# Folder containing images
images_folder = "images"

# Get all files in the images folder
for filename in os.listdir(images_folder):
    old_path = os.path.join(images_folder, filename)
    new_filename = filename.lower()
    new_path = os.path.join(images_folder, new_filename)
    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"Renamed {filename} -> {new_filename}")

# Update all HTML files in the current folder
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace any occurrence of 'images/filename' with lowercase
    def replace_match(match):
        return f"images/{match.group(1).lower()}"

    content = re.sub(r'images/([a-zA-Z0-9._-]+)', replace_match, content)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {html_file}")

print("\n✅ All images and HTML references are now lowercase!")
