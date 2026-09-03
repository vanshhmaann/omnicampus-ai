# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"

with open(target, "a", encoding="utf-8") as f:
    f.write("""
    <!-- ========================================================================= -->
    <!-- MODULE 4: AI LEARNING ROADMAP & KNOWLEDGE GRAPH -->
    <!-- ========================================================================= -->
    <section id="view-roadmap" class="hidden space-y-6">
      
      <!-- Direct Syllabus Upload & Builder Card -->
      <div class="card-white p-6 space-y-4">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-100 text-sky-800">MODULE 4</span>
              <h2 class="text-xl font-extrabold text-slate-900 tracking-tight">AI Interactive Learning Roadmap</h2>
            </div>
            <p id="roadmap-course-title" class="text-xs text-sky-700 font-semibold mt-1">CS 8803: Distributed Cloud Architectures & Resiliency</p>
          </div>

          <!-- Pacing Mode Switcher & Export -->
          <div class="flex flex-wrap items-center gap-2.5">
            <div class="flex items-center gap-1 p-1 bg-slate-100 rounded-full border border-slate-200 text-xs font-medium">
              <button data-pacing="semester" class="roadmap-pacing-btn px-3 py-1 rounded-full font-bold bg-yellow-300 text-slate-900 shadow-sm">15-Wk Semester</button>
              <button data-pacing="sprint" class="roadmap-pacing-btn px-3 py-1 rounded-full font-semibold text-slate-600 hover:text-slate-900">6-Wk Sprint</button>
              <button data-pacing="crash" class="roadmap-pacing-btn px-3 py-1 rounded-full font-semibold text-slate-600 hover:text-slate-900">14-Day Crash</button>
            </div>

            <button id="roadmap-export-md-btn" class="btn-yellow px-4 py-1.5 text-xs font-bold flex items-center gap-1.5">
              <i data-lucide="download" class="w-3.5 h-3.5"></i> Export Checklist
            </button>
          </div>
        </div>

        <!-- DIRECT SYLLABUS UPLOAD BOX -->
        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 pt-3 border-t border-slate-100">
          <div class="md:col-span-6">
            <input id="roadmap-pdf-input" type="file" accept=".pdf,.txt" class="hidden">
            <div id="roadmap-pdf-dropzone" class="border-2 border-dashed border-sky-200 hover:border-sky-500 rounded-2xl p-4 text-center cursor-pointer transition-all bg-sky-50/50 hover:bg-sky-50">
              <i data-lucide="file-up" class="w-6 h-6 text-sky-600 mx-auto mb-1"></i>
              <p class="text-xs font-bold text-slate-800">Upload Your Syllabus (PDF / TXT)</p>
              <p class="text-[10px] text-slate-500 mt-0.5">Drag & drop or click to upload your course syllabus</p>
            </div>
          </div>

          <div class="md:col-span-6 flex flex-col justify-between space-y-2">
            <div class="flex items-center gap-2">
              <input id="roadmap-paste-text-input" type="text" placeholder="Or paste course name / topic outline text..." class="flex-1 bg-slate-50 border border-slate-200 rounded-full px-4 py-2 text-xs text-slate-900 placeholder:text-slate-400 outline-none focus:ring-2 focus:ring-sky-400">
              <button id="roadmap-paste-submit-btn" class="btn-yellow px-4 py-2 text-xs font-bold flex items-center gap-1">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Generate
              </button>
            </div>

            <div class="flex flex-wrap items-center gap-1.5 text-[10px]">
              <span class="text-slate-400 font-semibold">Quick Presets:</span>
              <button data-course="ml" class="roadmap-preset-chip px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-sky-800 font-semibold">Deep Learning & LLMs</button>
              <button data-course="cloud" class="roadmap-preset-chip px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-indigo-800 font-semibold">Distributed Cloud</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Mastery Progress Card -->
      <div class="card-white p-5 space-y-2">
        <div class="flex items-center justify-between text-xs font-bold text-slate-800">
          <div class="flex items-center gap-1.5">
            <i data-lucide="compass" class="w-4 h-4 text-sky-600"></i>
            <span>Curriculum Mastery Progression</span>
          </div>
          <div class="flex items-center gap-3 text-[11px] font-mono">
            <span>Estimated Time: <strong id="roadmap-total-hours" class="text-sky-700">85 hrs</strong></span>
            <span>Mastery: <strong id="roadmap-mastery-percent" class="text-emerald-700">25%</strong></span>
          </div>
        </div>
        <div class="w-full h-3 rounded-full bg-slate-100 overflow-hidden">
          <div id="roadmap-progress-bar" style="width: 25%;" class="h-full bg-gradient-to-r from-sky-400 via-indigo-500 to-emerald-400 rounded-full transition-all duration-500"></div>
        </div>
      </div>

      <!-- Roadmap Nodes Tree -->
      <div class="card-white p-6">
        <div id="roadmap-phases-tree" class="space-y-6"></div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- MODULE 2: SMART CAMPUS "LOST & FOUND" -->
    <!-- ========================================================================= -->
    <section id="view-lostfound" class="hidden space-y-6">
      <div class="card-white p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-100 text-purple-800">MODULE 2</span>
            <h2 class="text-xl font-extrabold text-slate-900 tracking-tight">Smart Campus "Lost & Found" Search</h2>
          </div>
          <p class="text-xs text-slate-500 mt-1">Multi-modal visual match & natural language semantic search across campus</p>
        </div>

        <button id="lf-open-report-btn" class="btn-yellow px-5 py-2.5 text-xs font-bold flex items-center gap-1.5">
          <i data-lucide="plus-circle" class="w-4 h-4"></i> Report Lost/Found Item
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-8 space-y-4">
          <div class="card-white p-2 flex items-center gap-2">
            <i data-lucide="search" class="w-4 h-4 text-slate-400 ml-3"></i>
            <input id="lf-search-input" type="text" placeholder="Describe lost/found item (e.g. 'navy blue Hydro Flask near library')..." class="flex-1 bg-transparent text-xs text-slate-900 placeholder:text-slate-400 outline-none px-2">
            <button id="lf-search-btn" class="btn-yellow px-4 py-2 text-xs font-bold">Search</button>
          </div>

          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-1 p-1 bg-white rounded-full border border-slate-200 text-xs">
              <button data-type="all" class="lf-type-toggle px-3 py-1 rounded-full font-bold bg-yellow-300 text-slate-900">All</button>
              <button data-type="lost" class="lf-type-toggle px-3 py-1 rounded-full font-semibold text-slate-600 hover:text-slate-900">Lost</button>
              <button data-type="found" class="lf-type-toggle px-3 py-1 rounded-full font-semibold text-slate-600 hover:text-slate-900">Found</button>
            </div>

            <div class="flex flex-wrap items-center gap-1 text-xs">
              <button data-category="all" class="lf-filter-btn px-3 py-1 rounded-full font-bold bg-yellow-300 text-slate-900">All Categories</button>
              <button data-category="Electronics" class="lf-filter-btn px-2.5 py-1 rounded-full font-medium text-slate-600 hover:bg-slate-100">Electronics</button>
              <button data-category="Personal Items" class="lf-filter-btn px-2.5 py-1 rounded-full font-medium text-slate-600 hover:bg-slate-100">Personal</button>
              <button data-category="Wallets & IDs" class="lf-filter-btn px-2.5 py-1 rounded-full font-medium text-slate-600 hover:bg-slate-100">Wallets & IDs</button>
            </div>
          </div>

          <div id="lf-items-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
        </div>

        <div class="lg:col-span-4 space-y-4">
          <div class="card-white p-5 space-y-3">
            <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
              <i data-lucide="camera" class="w-4 h-4 text-sky-600"></i> Visual Match Dropzone
            </h4>
            <input id="lf-image-input" type="file" accept="image/*" class="hidden">
            <div id="lf-image-dropzone" class="border-2 border-dashed border-sky-200 hover:border-sky-500 rounded-2xl p-4 text-center cursor-pointer transition-all bg-sky-50/50 hover:bg-sky-50">
              <div id="lf-dropzone-placeholder" class="py-3">
                <i data-lucide="upload-cloud" class="w-8 h-8 text-sky-500 mx-auto mb-1.5"></i>
                <p class="text-xs font-bold text-slate-800">Drop photo of lost item</p>
                <p class="text-[10px] text-slate-400 mt-0.5">JPG, PNG, WebP • Auto visual match</p>
              </div>
              <div id="lf-preview-container" class="hidden relative">
                <img id="lf-image-preview" src="" alt="Preview" class="w-full h-32 object-cover rounded-xl">
                <button id="lf-clear-image-btn" class="absolute top-2 right-2 bg-slate-900/80 text-white p-1 rounded-lg text-xs font-bold">Clear</button>
              </div>
            </div>
          </div>

          <div class="card-white p-5 space-y-3">
            <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
              <i data-lucide="map" class="w-4 h-4 text-rose-500"></i> Campus Geo-Locator Map
            </h4>
            <div class="relative w-full h-60 bg-slate-100 rounded-2xl border border-slate-200 overflow-hidden">
              <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#0284c7 1px, transparent 1px); background-size: 16px 16px;"></div>
              <span class="absolute top-3 left-3 text-[10px] font-bold text-slate-500 uppercase">Science Library</span>
              <span class="absolute top-3 right-3 text-[10px] font-bold text-slate-500 uppercase">Dining Commons</span>
              <span class="absolute bottom-3 left-3 text-[10px] font-bold text-slate-500 uppercase">Engineering Tower</span>
              <span class="absolute bottom-3 right-3 text-[10px] font-bold text-slate-500 uppercase">Student Center</span>
              <div id="lf-campus-map-pins"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- MODULE 3: AI MULTI-AGENT INTERVIEW PREP -->
    <!-- ========================================================================= -->
    <section id="view-interview" class="hidden space-y-6">
      <div class="card-white p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-pink-100 text-pink-800">MODULE 3</span>
            <h2 class="text-xl font-extrabold text-slate-900 tracking-tight">AI Multi-Agent Interview & Placement Prep Hub</h2>
          </div>
          <p class="text-xs text-slate-500 mt-1">Multi-agent panel interview simulation with speech synthesis, live coding IDE, and radar scorecards</p>
        </div>

        <div class="flex items-center gap-2">
          <button id="interview-open-resume-btn" class="px-4 py-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold transition-colors">
            <i data-lucide="file-text" class="w-3.5 h-3.5 inline mr-1"></i> Resume ATS Scan
          </button>
          <button id="interview-tts-toggle" class="btn-yellow px-4 py-2 text-xs font-bold">
            <i data-lucide="volume-2" class="w-3.5 h-3.5 inline mr-1"></i> Audio TTS On
          </button>
        </div>
      </div>

      <!-- Agent Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        <div data-agent-name="Dr. Aris" class="card-white p-4 flex items-center gap-3 transition-all">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=60" alt="Dr. Aris" class="w-11 h-11 rounded-full object-cover border-2 border-sky-400">
          <div>
            <h4 class="font-bold text-xs text-slate-900">Dr. Aris</h4>
            <span class="text-[10px] text-sky-700 font-bold block">Technical Lead</span>
            <span class="text-[9px] text-slate-500">Algorithms & Proofs</span>
          </div>
        </div>

        <div data-agent-name="Elena Vance" class="card-white p-4 flex items-center gap-3 transition-all">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=60" alt="Elena" class="w-11 h-11 rounded-full object-cover border-2 border-pink-400">
          <div>
            <h4 class="font-bold text-xs text-slate-900">Elena Vance</h4>
            <span class="text-[10px] text-pink-700 font-bold block">HR & Culture</span>
            <span class="text-[9px] text-slate-500">STAR Method</span>
          </div>
        </div>

        <div data-agent-name="Marcus Thorne" class="card-white p-4 flex items-center gap-3 transition-all">
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=60" alt="Marcus" class="w-11 h-11 rounded-full object-cover border-2 border-cyan-400">
          <div>
            <h4 class="font-bold text-xs text-slate-900">Marcus Thorne</h4>
            <span class="text-[10px] text-cyan-700 font-bold block">Principal Architect</span>
            <span class="text-[9px] text-slate-500">System Scaling</span>
          </div>
        </div>

        <div data-agent-name="Samira" class="card-white p-4 flex items-center gap-3 transition-all">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=60" alt="Samira" class="w-11 h-11 rounded-full object-cover border-2 border-amber-400">
          <div>
            <h4 class="font-bold text-xs text-slate-900">Samira</h4>
            <span class="text-[10px] text-amber-700 font-bold block">Peer Candidate</span>
            <span class="text-[9px] text-slate-500">Collaborative Design</span>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-6 card-white p-5 flex flex-col justify-between min-h-[440px]">
          <div id="interview-chat-stream" class="flex-1 overflow-y-auto space-y-4 pr-1 max-h-[380px]">
            <div class="text-center py-12 text-slate-500">
              <i data-lucide="message-square" class="w-10 h-10 mx-auto text-slate-300 mb-2"></i>
              <p class="text-xs font-bold text-slate-800">Interview simulation ready.</p>
              <button id="interview-start-btn" class="btn-yellow px-5 py-2 text-xs font-bold mt-3">Start Panel Simulation</button>
            </div>
          </div>

          <div class="pt-3 border-t border-slate-100 flex items-center gap-2">
            <textarea id="interview-answer-input" rows="2" placeholder="Type response or click mic to speak..." class="flex-1 bg-slate-50 border border-slate-200 rounded-2xl p-3 text-xs text-slate-900 placeholder:text-slate-400 outline-none resize-none"></textarea>
            <button id="interview-mic-btn" class="p-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700"><i data-lucide="mic" class="w-4 h-4"></i></button>
            <button id="interview-send-btn" class="btn-yellow p-3 text-xs font-bold"><i data-lucide="send" class="w-4 h-4"></i></button>
          </div>
        </div>

        <div class="lg:col-span-6 space-y-4">
          <div class="card-white p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-800">Live Whiteboard IDE</span>
              <button id="run-code-btn" class="btn-yellow px-4 py-1 text-xs font-bold flex items-center gap-1">
                <i data-lucide="play" class="w-3.5 h-3.5"></i> Run Code
              </button>
            </div>
            <textarea id="interview-code-editor" class="w-full h-40 bg-slate-900 text-sky-300 font-mono text-xs p-3 rounded-2xl outline-none leading-relaxed resize-none"></textarea>
            <div id="code-output-terminal" class="p-3 bg-slate-900 rounded-2xl text-xs font-mono text-slate-300 min-h-[40px]">
              <span class="text-slate-500">// Terminal output</span>
            </div>
          </div>

          <div class="card-white p-5">
            <div class="flex items-center justify-between mb-2">
              <h4 class="text-xs font-bold text-slate-800">Performance Radar</h4>
              <span id="interview-overall-score" class="px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">76/100</span>
            </div>
            <div class="relative h-44 w-full">
              <canvas id="interview-radar-chart"></canvas>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- FLOATING BOTTOM NAVIGATION DOCK (MATCHING SCREENSHOT) -->
  <div class="fixed bottom-4 left-1/2 transform -translate-x-1/2 z-50 floating-dock px-3 py-2 flex items-center gap-2 shadow-2xl">
    <button data-module-target="rag" title="Home & Lectures" class="p-3 rounded-full dock-item-active transition-all">
      <i data-lucide="home" class="w-5 h-5"></i>
    </button>
    <button data-module-target="syllabus" title="Schedule & Syllabus" class="p-3 rounded-full text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
      <i data-lucide="calendar" class="w-5 h-5"></i>
    </button>
    <button data-module-target="roadmap" title="Learning Roadmap" class="p-3 rounded-full text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
      <i data-lucide="milestone" class="w-5 h-5"></i>
    </button>
    <button data-module-target="lostfound" title="Lost & Found" class="p-3 rounded-full text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
      <i data-lucide="search" class="w-5 h-5"></i>
    </button>
    <button data-module-target="interview" title="Interview Prep" class="p-3 rounded-full text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
      <i data-lucide="users-round" class="w-5 h-5"></i>
    </button>
  </div>

  <!-- Slide-Over Node Inspector Drawer -->
  <div id="node-drawer-backdrop" class="hidden fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm transition-opacity"></div>
  <div id="roadmap-node-drawer" class="fixed top-0 right-0 z-50 h-full w-full max-w-md bg-white border-l border-slate-200 p-6 shadow-2xl transform translate-x-full transition-transform duration-300 overflow-y-auto flex flex-col justify-between">
    <div class="space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <div>
          <span id="node-drawer-type" class="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase bg-sky-100 text-sky-800">Concept</span>
          <h3 id="node-drawer-title" class="text-base font-bold text-slate-900 mt-1">Topic Details</h3>
        </div>
        <button id="close-node-drawer-btn" class="text-slate-400 hover:text-slate-600 text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div class="flex items-center justify-between p-3 rounded-2xl bg-slate-50 border border-slate-100">
          <span id="node-drawer-hours" class="font-bold text-sky-700">8 Estimated Hours</span>
          <select id="node-status-select" class="bg-white border border-slate-200 text-slate-800 rounded-full px-3 py-1 outline-none font-bold">
            <option value="Not Started">Not Started</option>
            <option value="In Progress">In Progress</option>
            <option value="Mastered">Mastered</option>
          </select>
        </div>

        <div>
          <span class="text-slate-500 font-bold block mb-1">Overview:</span>
          <p id="node-drawer-desc" class="text-slate-700 leading-relaxed bg-slate-50 p-3.5 rounded-2xl border border-slate-100"></p>
        </div>

        <div>
          <span class="text-slate-500 font-bold block mb-1">Key Learning Objectives:</span>
          <ul id="node-drawer-objectives" class="space-y-1.5 p-3.5 rounded-2xl bg-slate-50 border border-slate-100"></ul>
        </div>

        <div>
          <span class="text-slate-500 font-bold block mb-1">Curated Resources:</span>
          <div id="node-drawer-resources" class="space-y-1.5"></div>
        </div>

        <div>
          <span class="text-slate-500 font-bold block mb-1">Hands-on Practice:</span>
          <div class="p-3.5 bg-yellow-50 border border-yellow-200 rounded-2xl text-slate-800 text-xs">
            <p id="node-drawer-task"></p>
          </div>
        </div>
      </div>
    </div>

    <div class="pt-4 border-t border-slate-100">
      <button onclick="ModuleRoadmap.closeNodeDrawer()" class="w-full py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold rounded-full transition-colors">
        Close Inspector
      </button>
    </div>
  </div>

  <!-- Settings Modal -->
  <div id="settings-modal" class="hidden fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="card-white max-w-md w-full p-6 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <div class="flex items-center gap-2">
          <i data-lucide="settings" class="w-5 h-5 text-sky-600"></i>
          <h3 class="font-bold text-base text-slate-900">Settings</h3>
        </div>
        <button id="close-settings-btn" class="text-slate-400 hover:text-slate-600 text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="font-bold text-slate-700 block mb-1">Google Gemini API Key (Optional BYOK):</label>
          <input id="gemini-api-key-input" type="password" placeholder="AIzaSy..." class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-slate-900 font-mono text-xs focus:ring-2 focus:ring-sky-400 outline-none">
        </div>

        <div>
          <label class="font-bold text-slate-700 block mb-1">Preferred Model Architecture:</label>
          <select id="gemini-model-select" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-slate-900 text-xs outline-none font-semibold">
            <option value="gemini-1.5-flash">Gemini 1.5 Flash (Ultra-Fast Multimodal)</option>
            <option value="gemini-1.5-pro">Gemini 1.5 Pro (Deep Reasoning)</option>
            <option value="gemini-2.0-flash">Gemini 2.0 Flash</option>
          </select>
        </div>
      </div>

      <div class="pt-3 border-t border-slate-100 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('settings-modal').classList.add('hidden')" class="px-4 py-2 rounded-full bg-slate-100 text-slate-700 text-xs font-bold">Cancel</button>
        <button id="save-settings-btn" class="btn-yellow px-5 py-2 text-xs font-bold">Save Settings</button>
      </div>
    </div>
  </div>

  <!-- Lost & Found Claim & Report Modals -->
  <div id="lf-claim-modal" class="hidden fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="card-white max-w-md w-full p-6 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 class="font-bold text-sm text-slate-900">Item Ownership Verification</h3>
        <button id="lf-close-claim-btn" class="text-slate-400 hover:text-slate-600 text-xl font-bold">&times;</button>
      </div>
      <div class="space-y-3 text-xs">
        <p id="lf-claim-item-title" class="text-sky-700 font-bold text-sm"></p>
        <div class="p-3 bg-amber-50 rounded-2xl border border-amber-200">
          <p id="lf-claim-security-q" class="text-slate-800 font-medium"></p>
        </div>
        <textarea id="lf-claim-answer-input" rows="2" placeholder="Describe identifying marks..." class="w-full bg-slate-50 border border-slate-200 rounded-2xl p-2.5 text-slate-900 text-xs outline-none resize-none"></textarea>
      </div>
      <div class="pt-3 border-t border-slate-100 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('lf-claim-modal').classList.add('hidden')" class="px-4 py-2 rounded-full bg-slate-100 text-slate-700 text-xs font-bold">Cancel</button>
        <button id="lf-submit-claim-btn" class="btn-yellow px-5 py-2 text-xs font-bold">Verify & Unlock</button>
      </div>
    </div>
  </div>

  <div id="lf-report-modal" class="hidden fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="card-white max-w-lg w-full p-6 space-y-4 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 class="font-bold text-sm text-slate-900">Register Lost / Found Item</h3>
        <button id="lf-close-report-btn" class="text-slate-400 hover:text-slate-600 text-xl font-bold">&times;</button>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="md:col-span-2">
          <label class="font-bold text-slate-700 block mb-1">Item Title *</label>
          <input id="report-title-input" type="text" placeholder="e.g. Sony WH-1000XM5" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
        </div>
        <div>
          <label class="font-bold text-slate-700 block mb-1">Type *</label>
          <select id="report-type-select" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
            <option value="lost">Lost</option>
            <option value="found">Found</option>
          </select>
        </div>
        <div>
          <label class="font-bold text-slate-700 block mb-1">Category *</label>
          <select id="report-category-select" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
            <option value="Electronics">Electronics</option>
            <option value="Personal Items">Personal Items</option>
            <option value="Wallets & IDs">Wallets & IDs</option>
          </select>
        </div>
        <div>
          <label class="font-bold text-slate-700 block mb-1">Campus Location *</label>
          <input id="report-location-input" type="text" placeholder="Library 3rd Floor" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
        </div>
        <div>
          <label class="font-bold text-slate-700 block mb-1">Color / Brand</label>
          <input id="report-color-input" type="text" placeholder="Navy Blue" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
        </div>
        <div class="md:col-span-2">
          <label class="font-bold text-slate-700 block mb-1">Description *</label>
          <textarea id="report-desc-input" rows="2" placeholder="Distinct stickers or scratches..." class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none resize-none"></textarea>
        </div>
        <div class="md:col-span-2">
          <label class="font-bold text-slate-700 block mb-1">Security Question *</label>
          <input id="report-security-input" type="text" placeholder="What is written on the sticker or lock screen?" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-900 outline-none">
        </div>
      </div>
      <div class="pt-3 border-t border-slate-100 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('lf-report-modal').classList.add('hidden')" class="px-4 py-2 rounded-full bg-slate-100 text-slate-700 text-xs font-bold">Cancel</button>
        <button id="lf-submit-report-btn" class="btn-yellow px-5 py-2 text-xs font-bold">Publish Item</button>
      </div>
    </div>
  </div>

  <div id="resume-scan-modal" class="hidden fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="card-white max-w-lg w-full p-6 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 class="font-bold text-sm text-slate-900">ATS Resume Scanner</h3>
        <button id="close-resume-modal-btn" class="text-slate-400 hover:text-slate-600 text-xl font-bold">&times;</button>
      </div>
      <textarea id="resume-text-input" rows="5" placeholder="Paste your resume markdown / plain text..." class="w-full bg-slate-50 border border-slate-200 rounded-2xl p-3 text-slate-900 text-xs font-mono outline-none resize-none"></textarea>
      <div id="resume-scan-results" class="hidden"></div>
      <div class="pt-3 border-t border-slate-100 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('resume-scan-modal').classList.add('hidden')" class="px-4 py-2 rounded-full bg-slate-100 text-slate-700 text-xs font-bold">Close</button>
        <button id="submit-resume-scan-btn" class="btn-yellow px-5 py-2 text-xs font-bold">Analyze Resume</button>
      </div>
    </div>
  </div>

  <div id="toast-container" class="fixed top-6 right-6 z-50 flex flex-col gap-2 max-w-sm w-full pointer-events-none"></div>

  <!-- Scripts -->
  <script src="/static/js/app.js"></script>
  <script src="/static/js/module_rag.js"></script>
  <script src="/static/js/module_lostfound.js"></script>
  <script src="/static/js/module_interview.js"></script>
  <script src="/static/js/module_roadmap.js"></script>
  <script src="/static/js/module_syllabus.js"></script>
</body>
</html>
""")
