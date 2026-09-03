# -*- coding: utf-8 -*-
path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\app.py"

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Put import re at top
code = "import re\n" + code

# Also put import re inside ingest_youtube
code = code.replace("async def ingest_youtube(req: YouTubeIngestRequest):", "async def ingest_youtube(req: YouTubeIngestRequest):\n    import re")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed import re in app.py.")
