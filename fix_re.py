# -*- coding: utf-8 -*-
path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\app.py"

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Add import re at top
if "import re" not in text:
    text = "import re\n" + text

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Added import re to app.py successfully.")
