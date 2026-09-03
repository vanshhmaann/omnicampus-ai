# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"
with open(target, "a", encoding="utf-8") as f:
    f.write("""
      <!-- ========================================================================= -->
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
        </div>

        <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-2">
          <div class="flex items-center justify-between text-xs">
            <div class="flex items-center gap-2">
              <i data-lucide="compass" class="w-4 h-4 text-cyan-400"></i>
              <span class="font-bold text-slate-200">Curriculum Mastery Progression</span>
            </div>
            <div class="flex items-center gap-4 text-[11px] font-mono">
              <span>Estimated Time: <strong id="roadmap-total-hours" class="text-indigo-400">85 hrs</strong></span>
              <span>Mastery: <strong id="roadmap-mastery-percent" class="text-emerald-400">25%</strong></span>
            </div>
          </div>
          <div class="w-full h-2.5 rounded-full bg-slate-800 overflow-hidden">
            <div id="roadmap-progress-bar" style="width: 25%;" class="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400 rounded-full transition-all duration-500"></div>
          </div>
        </div>

        <div class="glass-panel p-6 rounded-2xl border border-slate-800">
          <div id="roadmap-phases-tree" class="space-y-6"></div>
        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- MODULE 5: PDF SYLLABUS-TO-CALENDAR STUDY OPTIMIZER -->
      <!-- ========================================================================= -->
      <section id="view-syllabus" class="hidden space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl border border-slate-800">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">MODULE 5</span>
              <h2 class="text-xl font-bold text-white">PDF Syllabus-to-Calendar Study Optimizer</h2>
            </div>
            <p id="syllabus-course-meta" class="text-xs text-slate-400 mt-1">CS 8803-SYS • Prof. Elena Rostova • Fall 2026</p>
          </div>

          <div class="flex items-center gap-3">
            <button id="syllabus-generate-roadmap-btn" class="flex items-center gap-1.5 px-3.5 py-2.5 bg-gradient-to-r from-cyan-600 to-indigo-600 hover:from-cyan-500 hover:to-indigo-500 text-white rounded-xl text-xs font-bold shadow-lg shadow-cyan-500/20 transition-all">
              <i data-lucide="milestone" class="w-4 h-4"></i> View Visual Roadmap
            </button>
            <button id="syllabus-export-ics-btn" class="flex items-center gap-1.5 px-4 py-2.5 bg-gradient-to-r from-amber-500 to-indigo-600 hover:from-amber-600 hover:to-indigo-700 text-white rounded-xl text-xs font-bold shadow-lg shadow-amber-500/20 transition-all">
              <i data-lucide="download" class="w-4 h-4"></i> Export .ICS
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-4 space-y-4">
            <div class="glass-panel p-4 rounded-2xl border border-slate-800">
              <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <i data-lucide="file-up" class="w-3.5 h-3.5 text-indigo-400"></i> Import Course Syllabus (PDF)
              </h4>

              <input id="syllabus-pdf-input" type="file" accept=".pdf,.txt" class="hidden">
              <div id="syllabus-pdf-dropzone" class="border-2 border-dashed border-slate-700 hover:border-indigo-500 rounded-xl p-4 text-center cursor-pointer transition-all">
                <i data-lucide="file-text" class="w-8 h-8 text-indigo-400 mx-auto mb-2"></i>
                <p class="text-xs font-semibold text-slate-300">Drop syllabus PDF here</p>
                <p class="text-[10px] text-slate-500 mt-0.5">Auto-generates Learning Roadmap & Study Schedule</p>
              </div>
            </div>

            <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-3">
              <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="pie-chart" class="w-3.5 h-3.5 text-amber-400"></i> Grading Weight Distribution
              </h4>

              <div id="syllabus-weights-bar" class="w-full h-3 rounded-full overflow-hidden flex bg-slate-800"></div>
              <div id="syllabus-weights-container" class="space-y-1.5"></div>
            </div>
          </div>

          <div class="lg:col-span-8 space-y-4">
            <div class="glass-panel p-1.5 rounded-xl flex items-center justify-between border border-slate-800">
              <div class="flex items-center gap-1">
                <button data-syllabus-view="calendar" class="syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-sm flex items-center gap-1.5">
                  <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Calendar
                </button>
                <button data-syllabus-view="gantt" class="syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                  <i data-lucide="bar-chart-2" class="w-3.5 h-3.5"></i> Gantt Timeline
                </button>
                <button data-syllabus-view="kanban" class="syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                  <i data-lucide="columns" class="w-3.5 h-3.5"></i> Kanban Board
                </button>
                <button data-syllabus-view="sprints" class="syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                  <i data-lucide="zap" class="w-3.5 h-3.5"></i> Spaced Study Sprints
                </button>
              </div>
              <span class="text-[11px] text-slate-400 hidden sm:inline">Fall 2026 Timeline</span>
            </div>

            <div id="syllabus-view-panel-calendar" class="glass-panel p-4 rounded-2xl border border-slate-800">
              <div id="syllabus-calendar-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3"></div>
            </div>

            <div id="syllabus-view-panel-gantt" class="hidden glass-panel p-4 rounded-2xl border border-slate-800">
              <div id="syllabus-gantt-container" class="space-y-1"></div>
            </div>

            <div id="syllabus-view-panel-kanban" class="hidden glass-panel p-4 rounded-2xl border border-slate-800">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800">
                  <h5 class="text-xs font-bold text-slate-400 mb-2 flex items-center justify-between">
                    <span>TO STUDY</span> <span class="text-[10px] bg-slate-800 px-1.5 rounded">Backlog</span>
                  </h5>
                  <div id="kanban-col-todo" class="space-y-2"></div>
                </div>

                <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800">
                  <h5 class="text-xs font-bold text-amber-400 mb-2 flex items-center justify-between">
                    <span>IN PROGRESS</span> <span class="text-[10px] bg-amber-950 px-1.5 rounded">Active</span>
                  </h5>
                  <div id="kanban-col-inprogress" class="space-y-2"></div>
                </div>

                <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800">
                  <h5 class="text-xs font-bold text-emerald-400 mb-2 flex items-center justify-between">
                    <span>EXAM READY</span> <span class="text-[10px] bg-emerald-950 px-1.5 rounded">Mastered</span>
                  </h5>
                  <div id="kanban-col-done" class="space-y-2"></div>
                </div>
              </div>
            </div>

            <div id="syllabus-view-panel-sprints" class="hidden glass-panel p-4 rounded-2xl border border-slate-800">
              <div id="syllabus-sprints-container"></div>
            </div>

            <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="flame" class="w-3.5 h-3.5 text-rose-400"></i> Workload & Exam Stress Heatmap
                </h4>
                <span class="text-[10px] text-slate-400">Identifies Conflicting Spikes</span>
              </div>
              <div id="syllabus-burnout-heatmap" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5"></div>
            </div>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Slide-Over Node Inspector Drawer (for Module 4 Roadmap) -->
  <div id="node-drawer-backdrop" class="hidden fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-sm transition-opacity"></div>
  <div id="roadmap-node-drawer" class="fixed top-0 right-0 z-50 h-full w-full max-w-md bg-slate-900 border-l border-slate-800 p-6 shadow-2xl transform translate-x-full transition-transform duration-300 overflow-y-auto flex flex-col justify-between">
    <div class="space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
          <span id="node-drawer-type" class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-indigo-950 text-indigo-300 border border-indigo-500/30">Concept</span>
          <h3 id="node-drawer-title" class="text-base font-bold text-white mt-1">Topic Details</h3>
        </div>
        <button id="close-node-drawer-btn" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <span class="text-slate-400 font-semibold block mb-1">Status & Pacing:</span>
          <div class="flex items-center justify-between p-2.5 rounded-xl bg-slate-800 border border-slate-700">
            <span id="node-drawer-hours" class="font-mono text-indigo-300">8 Estimated Hours</span>
            <select id="node-status-select" class="bg-slate-900 border border-slate-700 text-white rounded-lg px-2 py-1 outline-none font-semibold">
              <option value="Not Started">Not Started</option>
              <option value="In Progress">In Progress</option>
              <option value="Mastered">Mastered</option>
            </select>
          </div>
        </div>

        <div>
          <span class="text-slate-400 font-semibold block mb-1">Overview:</span>
          <p id="node-drawer-desc" class="text-slate-300 leading-relaxed bg-slate-950 p-3 rounded-xl border border-slate-800"></p>
        </div>

        <div>
          <span class="text-slate-400 font-semibold block mb-1">Key Learning Objectives:</span>
          <ul id="node-drawer-objectives" class="space-y-1.5 p-3 rounded-xl bg-slate-950 border border-slate-800"></ul>
        </div>

        <div>
          <span class="text-slate-400 font-semibold block mb-1">Recommended Curated Resources:</span>
          <div id="node-drawer-resources" class="space-y-1.5"></div>
        </div>

        <div>
          <span class="text-slate-400 font-semibold block mb-1">Hands-on Practice Task:</span>
          <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-xl text-indigo-200 text-xs">
            <p id="node-drawer-task"></p>
          </div>
        </div>
      </div>
    </div>

    <div class="pt-4 border-t border-slate-800">
      <button onclick="ModuleRoadmap.closeNodeDrawer()" class="w-full py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-xl transition-colors">
        Close Inspector
      </button>
    </div>
  </div>

  <!-- Global Modals -->
  <div id="settings-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="glass-panel-glow max-w-md w-full rounded-2xl p-6 space-y-4 border border-indigo-500/30">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <i data-lucide="key" class="w-5 h-5 text-indigo-400"></i>
          <h3 class="font-bold text-base text-white">AI Engine & Gemini Settings</h3>
        </div>
        <button id="close-settings-btn" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="font-semibold text-slate-300 block mb-1">Google Gemini API Key (Optional BYOK):</label>
          <input id="gemini-api-key-input" type="password" placeholder="AIzaSy..." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-white font-mono text-xs focus:ring-2 focus:ring-indigo-500 outline-none">
          <p class="text-[10px] text-slate-500 mt-1">If left blank, OmniCampus operates on high-fidelity intelligent local engines.</p>
        </div>

        <div>
          <label class="font-semibold text-slate-300 block mb-1">Preferred Model Architecture:</label>
          <select id="gemini-model-select" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-white text-xs outline-none">
            <option value="gemini-1.5-flash">Gemini 1.5 Flash (Ultra-Fast Multimodal)</option>
            <option value="gemini-1.5-pro">Gemini 1.5 Pro (Deep Reasoning)</option>
            <option value="gemini-2.0-flash">Gemini 2.0 Flash</option>
          </select>
        </div>
      </div>

      <div class="pt-3 border-t border-slate-800 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('settings-modal').classList.add('hidden')" class="px-3 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold">Cancel</button>
        <button id="save-settings-btn" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md">Save Configuration</button>
      </div>
    </div>
  </div>

  <div id="lf-claim-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="glass-panel max-w-md w-full rounded-2xl p-6 space-y-4 border border-indigo-500/40 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <i data-lucide="shield-check" class="w-5 h-5 text-emerald-400"></i>
          <h3 class="font-bold text-sm text-white">Item Ownership Verification Challenge</h3>
        </div>
        <button id="lf-close-claim-btn" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <span class="text-slate-400 font-semibold block">Target Item:</span>
          <p id="lf-claim-item-title" class="text-indigo-300 font-bold text-sm mt-0.5"></p>
        </div>

        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <span class="text-[11px] text-amber-400 font-bold uppercase tracking-wider block mb-1">Security Question:</span>
          <p id="lf-claim-security-q" class="text-slate-200"></p>
        </div>

        <div>
          <label class="text-slate-300 font-semibold block mb-1">Your Identifying Answer:</label>
          <textarea id="lf-claim-answer-input" rows="2" placeholder="Describe the sticker, exact numbers, lock screen name, or distinct scratch marks..." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 text-white text-xs focus:ring-2 focus:ring-indigo-500 outline-none resize-none"></textarea>
        </div>

        <div id="lf-claim-result-box" class="hidden"></div>
      </div>

      <div class="pt-3 border-t border-slate-800 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('lf-claim-modal').classList.add('hidden')" class="px-3 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold">Cancel</button>
        <button id="lf-submit-claim-btn" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md">Verify & Generate Locker Code</button>
      </div>
    </div>
  </div>

  <div id="lf-report-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="glass-panel max-w-lg w-full rounded-2xl p-6 space-y-4 border border-slate-700 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <i data-lucide="plus-circle" class="w-5 h-5 text-indigo-400"></i>
          <h3 class="font-bold text-sm text-white">Register Lost or Found Item</h3>
        </div>
        <button id="lf-close-report-btn" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="md:col-span-2">
          <label class="text-slate-300 font-semibold block mb-1">Item Title / Name *</label>
          <input id="report-title-input" type="text" placeholder="e.g. Sony WH-1000XM5 Headphones" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
        </div>

        <div>
          <label class="text-slate-300 font-semibold block mb-1">Report Type *</label>
          <select id="report-type-select" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
            <option value="lost">Lost (I lost this item)</option>
            <option value="found">Found (I found this item)</option>
          </select>
        </div>

        <div>
          <label class="text-slate-300 font-semibold block mb-1">Category *</label>
          <select id="report-category-select" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
            <option value="Electronics">Electronics</option>
            <option value="Personal Items">Personal Items</option>
            <option value="Wallets & IDs">Wallets & IDs</option>
            <option value="Laptops">Laptops</option>
            <option value="Stationery & Tools">Stationery & Tools</option>
          </select>
        </div>

        <div>
          <label class="text-slate-300 font-semibold block mb-1">Location on Campus *</label>
          <input id="report-location-input" type="text" placeholder="e.g. Library 3rd Floor Desk 12" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
        </div>

        <div>
          <label class="text-slate-300 font-semibold block mb-1">Color / Brand</label>
          <input id="report-color-input" type="text" placeholder="e.g. Navy Blue / Sony" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
        </div>

        <div class="md:col-span-2">
          <label class="text-slate-300 font-semibold block mb-1">Detailed Description *</label>
          <textarea id="report-desc-input" rows="2" placeholder="Describe condition, attached keychains, distinct scratches or stickers..." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none resize-none"></textarea>
        </div>

        <div class="md:col-span-2">
          <label class="text-slate-300 font-semibold block mb-1">Ownership Security Verification Question *</label>
          <input id="report-security-input" type="text" placeholder="e.g. What is written on the inner label or lock screen?" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2 text-white outline-none">
        </div>
      </div>

      <div class="pt-3 border-t border-slate-800 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('lf-report-modal').classList.add('hidden')" class="px-3 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold">Cancel</button>
        <button id="lf-submit-report-btn" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md">Publish Item</button>
      </div>
    </div>
  </div>

  <div id="resume-scan-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="glass-panel max-w-lg w-full rounded-2xl p-6 space-y-4 border border-slate-700 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2">
          <i data-lucide="scan-line" class="w-5 h-5 text-indigo-400"></i>
          <h3 class="font-bold text-sm text-white">ATS Resume Scanner & Question Tailor</h3>
        </div>
        <button id="close-resume-modal-btn" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="text-slate-300 font-semibold block mb-1">Paste Resume Text / Summary:</label>
          <textarea id="resume-text-input" rows="5" placeholder="Paste your resume markdown or plain text here (Experience, Projects, Education, Skills)..." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white text-xs font-mono focus:ring-2 focus:ring-indigo-500 outline-none leading-relaxed resize-none"></textarea>
        </div>

        <div id="resume-scan-results" class="hidden"></div>
      </div>

      <div class="pt-3 border-t border-slate-800 flex items-center justify-end gap-2">
        <button onclick="document.getElementById('resume-scan-modal').classList.add('hidden')" class="px-3 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-semibold">Close</button>
        <button id="submit-resume-scan-btn" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md">Analyze Resume & Generate Questions</button>
      </div>
    </div>
  </div>

  <div id="toast-container" class="fixed bottom-6 right-6 z-50 flex flex-col gap-2 max-w-sm w-full pointer-events-none"></div>

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
