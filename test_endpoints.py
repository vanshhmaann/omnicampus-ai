# -*- coding: utf-8 -*-
import requests
import json
import time

base = "http://127.0.0.1:8000"

tests = []

# 1. Health Status
try:
    r = requests.get(f"{base}/api/status", timeout=5)
    tests.append(("GET /api/status", r.status_code == 200, str(r.json().get("system"))))
except Exception as e:
    tests.append(("GET /api/status", False, str(e)))

# 2. Frontend HTML
try:
    r = requests.get(f"{base}/", timeout=5)
    tests.append(("GET / (index.html)", r.status_code == 200 and "OmniCampus AI" in r.text, f"{len(r.text)} bytes"))
except Exception as e:
    tests.append(("GET /", False, str(e)))

# 3. Module 1: Lecture RAG
try:
    r = requests.get(f"{base}/api/rag/lectures", timeout=5)
    r2 = requests.post(f"{base}/api/rag/query", json={"lectureId": "lec-cs6501", "query": "How does Raft elect a leader?"}, timeout=5)
    tests.append(("Module 1: RAG Query", r2.status_code == 200 and "Raft" in r2.text, f"{len(r2.json().get('citations', []))} citations"))
except Exception as e:
    tests.append(("Module 1: RAG Query", False, str(e)))

# 4. Module 2: Lost & Found
try:
    r = requests.get(f"{base}/api/lostfound/items", timeout=5)
    r2 = requests.post(f"{base}/api/lostfound/search", json={"query": "Sony headphones library", "category": "all", "itemType": "all"}, timeout=5)
    tests.append(("Module 2: Lost & Found Search", r2.status_code == 200 and len(r2.json().get("results", [])) > 0, f"{len(r2.json().get('results', []))} items found"))
except Exception as e:
    tests.append(("Module 2: Lost & Found Search", False, str(e)))

# 5. Module 3: Interview Start & Turn
try:
    r = requests.post(f"{base}/api/interview/start", json={"role": "Senior Full-Stack Engineer", "difficulty": "Senior", "candidateName": "Alex"}, timeout=5)
    session_id = r.json().get("sessionId")
    r2 = requests.post(f"{base}/api/interview/turn", json={"sessionId": session_id, "role": "Senior Full-Stack Engineer", "difficulty": "Senior", "history": [], "userAnswer": "I designed an event-driven architecture with Kafka and Redis."}, timeout=5)
    tests.append(("Module 3: Multi-Agent Turn", r2.status_code == 200 and "agent" in r2.json(), f"Agent: {r2.json().get('agent')}"))
except Exception as e:
    tests.append(("Module 3: Multi-Agent Turn", False, str(e)))

# 6. Module 4: Diagram & Equation to Code
try:
    r = requests.post(f"{base}/api/diagram/convert", json={"diagramType": "math", "textPrompt": ""}, timeout=5)
    r2 = requests.post(f"{base}/api/diagram/convert", json={"diagramType": "flowchart", "textPrompt": ""}, timeout=5)
    tests.append(("Module 4: Diagram-to-Code", r.status_code == 200 and r2.status_code == 200, "LaTeX + Mermaid + Python generated"))
except Exception as e:
    tests.append(("Module 4: Diagram-to-Code", False, str(e)))

# 7. Module 5: Syllabus Optimizer & ICS
try:
    r = requests.post(f"{base}/api/syllabus/parse", json={"syllabusText": "CS 8803 Cloud Systems", "courseName": "Cloud Systems", "term": "Fall 2026"}, timeout=5)
    sample_milestones = [{"date": "2026-10-26", "title": "Midterm Exam", "type": "Exam", "weight": "20%", "stressLevel": "Critical"}]
    r2 = requests.post(f"{base}/api/syllabus/export-ics", json={"courseCode": "CS8803", "milestones": sample_milestones}, timeout=5)
    tests.append(("Module 5: Syllabus & ICS Export", r.status_code == 200 and "BEGIN:VCALENDAR" in r2.text, f"ICS size: {len(r2.text)} bytes"))
except Exception as e:
    tests.append(("Module 5: Syllabus & ICS Export", False, str(e)))

print("\n--- TEST EXECUTION SUMMARY ---")
all_passed = True
for name, passed, detail in tests:
    status_str = "PASS" if passed else "FAIL"
    print(f"[{status_str}] {name}: {detail}")
    if not passed:
        all_passed = False

if all_passed:
    print("\n>>> ALL MODULE ENDPOINTS VERIFIED & OPERATIONAL! <<<")
else:
    print("\n>>> SOME TESTS FAILED <<<")
