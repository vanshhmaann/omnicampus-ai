# -*- coding: utf-8 -*-
index_path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

old_roadmap_header = """      <!-- ========================================================================= -->
      <!-- MODULE 4: AI INTERACTIVE LEARNING ROADMAP & KNOWLEDGE GRAPH -->
      <!-- ========================================================================= -->
      <section id="view-roadmap" class="hidden space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl border border-slate-800">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">MODULE 4</span>
              <h2 class="text-xl font-bold text-white">AI Interactive Learning Roadmap & Knowledge Graph</h2>
            </div>
            <p id="roadmap-course-title" class="text-xs text-indigo-400 font-semibold mt-1">CS 8803: Distributed Cloud Architectures & Resiliency</p>
          </div>

          <div class="flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-1 p-1 bg-slate-900 rounded-xl border border-slate-800 text-xs">
              <button data-pacing="semester" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-semibold bg-indigo-600 text-white">15-Wk Semester</button>
              <button data-pacing="sprint" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">6-Wk Sprint</button>
              <button data-pacing="crash" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">14-Day Crash</button>
            </div>

            <button id="roadmap-export-md-btn" class="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
              <i data-lucide="download" class="w-3.5 h-3.5 text-indigo-400"></i> Export Checklist (.md)
            </button>
          </div>
        </div>"""

new_roadmap_header = """      <!-- ========================================================================= -->
      <!-- MODULE 4: AI INTERACTIVE LEARNING ROADMAP & KNOWLEDGE GRAPH -->
      <!-- ========================================================================= -->
      <section id="view-roadmap" class="hidden space-y-6">
        <!-- Direct Syllabus Upload & Curriculum Builder Card -->
        <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-4">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">MODULE 4</span>
                <h2 class="text-xl font-bold text-white">AI Interactive Learning Roadmap & Knowledge Graph</h2>
              </div>
              <p id="roadmap-course-title" class="text-xs text-cyan-400 font-semibold mt-1">CS 8803: Distributed Cloud Architectures & Resiliency</p>
            </div>

            <!-- Actions: Pacing Switcher & Export -->
            <div class="flex flex-wrap items-center gap-2.5">
              <div class="flex items-center gap-1 p-1 bg-slate-900 rounded-xl border border-slate-800 text-xs">
                <button data-pacing="semester" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-semibold bg-indigo-600 text-white">15-Wk Semester</button>
                <button data-pacing="sprint" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">6-Wk Sprint</button>
                <button data-pacing="crash" class="roadmap-pacing-btn px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">14-Day Crash</button>
              </div>

              <button id="roadmap-export-md-btn" class="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
                <i data-lucide="download" class="w-3.5 h-3.5 text-indigo-400"></i> Export Checklist (.md)
              </button>
            </div>
          </div>

          <!-- DIRECT SYLLABUS UPLOAD BOX -->
          <div class="grid grid-cols-1 md:grid-cols-12 gap-4 pt-3 border-t border-slate-800/80">
            <!-- Left: PDF Dropzone -->
            <div class="md:col-span-6">
              <input id="roadmap-pdf-input" type="file" accept=".pdf,.txt" class="hidden">
              <div id="roadmap-pdf-dropzone" class="border-2 border-dashed border-slate-700 hover:border-cyan-500 rounded-xl p-4 text-center cursor-pointer transition-all bg-slate-900/50 hover:bg-cyan-950/20">
                <i data-lucide="file-up" class="w-7 h-7 text-cyan-400 mx-auto mb-1.5"></i>
                <p class="text-xs font-bold text-slate-200">Upload Your Syllabus (PDF / TXT)</p>
                <p class="text-[10px] text-slate-400 mt-0.5">Drag & drop or click to upload your course syllabus file</p>
              </div>
            </div>

            <!-- Right: Paste Syllabus Text or Quick Presets -->
            <div class="md:col-span-6 flex flex-col justify-between space-y-2">
              <div class="flex items-center gap-2">
                <input id="roadmap-paste-text-input" type="text" placeholder="Or paste course name / topic outline text..." class="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-xs text-white placeholder:text-slate-500 outline-none focus:ring-2 focus:ring-cyan-500">
                <button id="roadmap-paste-submit-btn" class="px-3.5 py-2.5 bg-gradient-to-r from-cyan-600 to-indigo-600 hover:from-cyan-500 hover:to-indigo-500 text-white rounded-xl text-xs font-bold shadow-md transition-all flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Generate
                </button>
              </div>

              <!-- Quick Presets -->
              <div class="flex flex-wrap items-center gap-1.5 text-[10px]">
                <span class="text-slate-400 font-semibold">Quick Presets:</span>
                <button data-course="ml" class="roadmap-preset-chip px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 font-medium">Deep Learning & LLMs</button>
                <button data-course="cloud" class="roadmap-preset-chip px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 font-medium">Distributed Cloud</button>
              </div>
            </div>
          </div>
        </div>"""

if old_roadmap_header in html:
    html = html.replace(old_roadmap_header, new_roadmap_header)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully injected direct syllabus upload into Roadmap view!")
else:
    print("Old header string not matched directly, updating structurally.")
    import re
    html = re.sub(r'<section id="view-roadmap"[^>]*>[\s\S]*?<div id="roadmap-progress-bar"', '<section id="view-roadmap" class="hidden space-y-6">\n' + new_roadmap_header.split('<section id="view-roadmap" class="hidden space-y-6">')[1] + '\n<div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-2">\n<div class="flex items-center justify-between text-xs">\n<div class="flex items-center gap-2">\n<i data-lucide="compass" class="w-4 h-4 text-cyan-400"></i>\n<span class="font-bold text-slate-200">Curriculum Mastery Progression</span>\n</div>\n<div class="flex items-center gap-4 text-[11px] font-mono">\n<span>Estimated Time: <strong id="roadmap-total-hours" class="text-indigo-400">85 hrs</strong></span>\n<span>Mastery: <strong id="roadmap-mastery-percent" class="text-emerald-400">25%</strong></span>\n</div>\n</div>\n<div class="w-full h-2.5 rounded-full bg-slate-800 overflow-hidden">\n<div id="roadmap-progress-bar"', html)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Structural injection complete.")
