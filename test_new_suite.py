# -*- coding: utf-8 -*-
import requests, time

base = "http://127.0.0.1:8000"
time.sleep(1)

tests = []

# 1. Server Status
try:
    r = requests.get(f"{base}/api/status", timeout=5)
    tests.append(("GET /api/status", r.status_code == 200, str(r.json().get("system"))))
except Exception as e:
    tests.append(("GET /api/status", False, str(e)))

# 2. Frontend HTML
try:
    r = requests.get(f"{base}/", timeout=5)
    has_roadmap = "AI Interactive Learning Roadmap" in r.text
    has_no_diagram = "Handwritten Diagram" not in r.text
    tests.append(("GET / (index.html with Roadmap)", r.status_code == 200 and has_roadmap and has_no_diagram, f"{len(r.text)} bytes"))
except Exception as e:
    tests.append(("GET /", False, str(e)))

# 3. Module 1: Lecture RAG & YouTube
try:
    r = requests.get(f"{base}/api/rag/lectures", timeout=5)
    tests.append(("Module 1: Lecture RAG", r.status_code == 200 and len(r.json().get("lectures", [])) > 0, f"{len(r.json().get('lectures', []))} lectures"))
except Exception as e:
    tests.append(("Module 1: Lecture RAG", False, str(e)))

# 4. Module 2: Lost & Found
try:
    r = requests.get(f"{base}/api/lostfound/items", timeout=5)
    tests.append(("Module 2: Lost & Found", r.status_code == 200, f"{len(r.json().get('items', []))} catalog items"))
except Exception as e:
    tests.append(("Module 2: Lost & Found", False, str(e)))

# 5. Module 3: Interview Prep
try:
    r = requests.post(f"{base}/api/interview/start", json={"role": "Senior Full-Stack Engineer", "difficulty": "Senior", "candidateName": "Alex"}, timeout=5)
    tests.append(("Module 3: Interview Start", r.status_code == 200 and "sessionId" in r.json(), r.json().get("sessionId")))
except Exception as e:
    tests.append(("Module 3: Interview Start", False, str(e)))

# 6. Module 4: Roadmap Generation & Node Update (NEW)
try:
    r = requests.post(f"{base}/api/roadmap/generate", json={"courseName": "CS 8803 Distributed Cloud", "pacingMode": "semester"}, timeout=5)
    phases_count = len(r.json().get("roadmap", {}).get("phases", []))
    
    # Update node status
    r2 = requests.post(f"{base}/api/roadmap/update-node", json={"nodeId": "node-101", "status": "Mastered"}, timeout=5)
    
    tests.append(("Module 4: AI Learning Roadmap API", r.status_code == 200 and r2.status_code == 200 and phases_count > 0, f"{phases_count} phases, Mastery: {r2.json().get('masteryPercent')}%"))
except Exception as e:
    tests.append(("Module 4: AI Learning Roadmap API", False, str(e)))

# 7. Module 5: Syllabus & ICS Export
try:
    r = requests.post(f"{base}/api/syllabus/parse", json={"syllabusText": "CS 8803 Cloud Systems", "courseName": "Cloud Systems", "term": "Fall 2026"}, timeout=5)
    sample_milestones = [{"date": "2026-10-26", "title": "Midterm Exam", "type": "Exam", "weight": "20%", "stressLevel": "Critical"}]
    r2 = requests.post(f"{base}/api/syllabus/export-ics", json={"courseCode": "CS8803", "milestones": sample_milestones}, timeout=5)
    tests.append(("Module 5: Syllabus & ICS Export", r.status_code == 200 and "BEGIN:VCALENDAR" in r2.text, f"ICS: {len(r2.text)} bytes"))
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
    print("\n>>> ALL 5 MODULES INCLUDING SYLLABUS ROADMAP OPERATIONAL! <<<")
else:
    print("\n>>> SOME TESTS FAILED <<<")
