path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\app.py"
with open(path, "r", encoding="latin-1") as f:
    text = f.read()

# Replace any unicode characters with clean ASCII equivalents in python source
replacements = {
    "\x97": " - ",
    "\xb7": " * ",
    "?": " ^ ",
    "·": " * ",
    "?": "floor(",
    "?": ")",
    "—": " - ",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n" + text)

print("Rewritten with clean UTF-8.")
