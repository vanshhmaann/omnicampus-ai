# -*- coding: utf-8 -*-
import os

path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\app.py"
with open(path, "rb") as f:
    b = f.read()

# Filter out non-ascii bytes
clean_chars = []
for byte in b:
    if byte < 128:
        clean_chars.append(chr(byte))
    else:
        clean_chars.append(" ")

clean_text = "".join(clean_chars)
with open(path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n" + clean_text)

print("app.py ascii-cleaned successfully.")
