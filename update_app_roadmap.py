# -*- coding: utf-8 -*-
import os, json

app_path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\app.py"

with open(app_path, "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

# Replace status modules list
code = code.replace(
    "'4. Handwritten Diagram & Equation-to-Code Engine'",
    "'4. AI Interactive Learning Roadmap & Knowledge Graph (Generated from Syllabus)'"
).replace(
    '"4. Handwritten Diagram & Equation-to-Code Engine"',
    '"4. AI Interactive Learning Roadmap & Knowledge Graph (Generated from Syllabus)"'
)

# Roadmap API Code
roadmap_endpoint_code = """
class RoadmapGenerateRequest(BaseModel):
    courseName: Optional[str] = "Distributed Cloud Architectures"
    syllabusText: Optional[str] = ""
    pacingMode: Optional[str] = "semester" # 'semester', 'sprint', 'crash'

@app.post("/api/syllabus/generate-roadmap")
@app.post("/api/roadmap/generate")
async def generate_roadmap(req: RoadmapGenerateRequest):
    sample = load_json_data("sample_syllabus.json", {})
    roadmap = sample.get("roadmap", {})
    
    if req.courseName and req.courseName != "Course":
        roadmap["courseTitle"] = req.courseName
        
    # Recalculate hours based on pacing mode
    pacing = req.pacingMode or "semester"
    multiplier = 1.0
    if pacing == "sprint":
        multiplier = 0.75
    elif pacing == "crash":
        multiplier = 0.45
        
    for phase in roadmap.get("phases", []):
        for node in phase.get("nodes", []):
            node["hours"] = max(2, round(node.get("hours", 6) * multiplier))
            
    return {
        "success": True,
        "pacingMode": pacing,
        "roadmap": roadmap,
        "message": f"Generated interactive learning roadmap for '{roadmap.get('courseTitle')}' across {len(roadmap.get('phases', []))} phases."
    }

@app.post("/api/roadmap/update-node")
async def update_roadmap_node(req: Dict[str, Any]):
    node_id = req.get("nodeId")
    status = req.get("status", "In Progress")
    sample = load_json_data("sample_syllabus.json", {})
    roadmap = sample.get("roadmap", {})
    
    found = False
    mastered_count = 0
    total_nodes = 0
    
    for phase in roadmap.get("phases", []):
        for node in phase.get("nodes", []):
            total_nodes += 1
            if node.get("id") == node_id:
                node["status"] = status
                found = True
            if node.get("status") == "Mastered":
                mastered_count += 1
                
    mastery_percent = round((mastered_count / max(1, total_nodes)) * 100)
    roadmap["currentMasteryPercent"] = mastery_percent
    sample["roadmap"] = roadmap
    
    path = os.path.join(DATA_DIR, "sample_syllabus.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sample, f, indent=2)
        
    return {
        "success": True,
        "nodeId": node_id,
        "newStatus": status,
        "masteryPercent": mastery_percent
    }
"""

# Replace diagram endpoint with roadmap endpoint
if "/api/diagram/convert" in code:
    import re
    code = re.sub(r'@app\.post\("/api/diagram/convert"\)[\s\S]*?(?=@app\.post\("/api/syllabus/upload-pdf"|app\.mount\()', roadmap_endpoint_code + "\n\n", code)
else:
    # Append before app.mount
    idx = code.find("app.mount(")
    if idx != -1:
        code = code[:idx] + roadmap_endpoint_code + "\n" + code[idx:]
    else:
        code += "\n" + roadmap_endpoint_code

with open(app_path, "w", encoding="utf-8") as f:
    f.write(code)

print("app.py updated with Roadmap endpoints.")
