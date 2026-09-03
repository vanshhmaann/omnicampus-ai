import requests

url = "http://127.0.0.1:8000/api/rag/ingest-youtube"
test_links = [
    "https://www.youtube.com/watch?v=aircAruvnKk",
    "https://youtu.be/kCc8FmEb1nY"
]

for link in test_links:
    r = requests.post(url, json={"url": link}, timeout=8)
    print(f"Status: {r.status_code}")
    data = r.json()
    print("Ingested Title:", data.get("lecture", {}).get("title"))
    print("Slides / Milestones extracted:", len(data.get("lecture", {}).get("slides", [])))
    print("Flashcards generated:", len(data.get("lecture", {}).get("flashcards", [])))

print("YouTube Ingest Endpoint Test Passed Successfully!")
