# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"

with open(target, "a", encoding="utf-8") as f:
    f.write("""
    <!-- ========================================================================= -->
    <!-- MODULE 1: HOME & LECTURE RAG COMPANION (MATCHING SCREEN 1) -->
    <!-- ========================================================================= -->
    <section id="view-rag" class="space-y-6">
      
      <!-- HERO BANNER CARD (EXACTLY MATCHING SCREEN 1) -->
      <div class="card-pastel-blue p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 relative overflow-hidden">
        <div class="max-w-md space-y-4 z-10">
          <h2 class="text-2xl md:text-3xl font-extrabold text-slate-900 leading-tight">
            Take a look to your courses & track your progress
          </h2>
          <button onclick="window.switchModule('roadmap')" class="btn-yellow px-6 py-2.5 text-sm font-bold flex items-center gap-2">
            <span>Go to Roadmap</span> <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>

        <!-- 3D Book Graphic Illustration -->
        <div class="relative w-36 h-36 md:w-44 md:h-44 flex-shrink-0 flex items-center justify-center">
          <div class="absolute inset-0 bg-white/40 rounded-full blur-xl"></div>
          <div class="relative flex flex-col items-center gap-1">
            <div class="w-24 h-5 rounded-lg bg-pink-400 shadow-md transform -rotate-6"></div>
            <div class="w-28 h-6 rounded-lg bg-indigo-500 shadow-md transform rotate-3"></div>
            <div class="w-32 h-7 rounded-lg bg-amber-400 shadow-md transform -rotate-2"></div>
            <div class="w-36 h-8 rounded-lg bg-cyan-400 shadow-md transform rotate-1 flex items-center justify-center text-white text-xs font-bold">
              OmniCampus AI
            </div>
          </div>
        </div>
      </div>

      <!-- Feature Pill Banner -->
      <div onclick="window.switchModule('interview')" class="card-white p-4 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-2xl bg-amber-100 flex items-center justify-center text-amber-700">
            <i data-lucide="award" class="w-5 h-5"></i>
          </div>
          <div>
            <h4 class="font-bold text-xs text-slate-900">Go to Placement Hub & Interview Simulation</h4>
            <p class="text-[11px] text-slate-500">Practice live multi-agent technical & HR mock panels</p>
          </div>
        </div>
        <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i>
      </div>

      <!-- YouTube Link Ingestion Bar -->
      <div class="card-white p-5 space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <i data-lucide="youtube" class="w-4 h-4 text-rose-500"></i> Import Any YouTube Lecture Video
          </span>
          <span class="text-[10px] text-slate-400 font-mono">Auto-extracts timestamps & slides</span>
        </div>

        <div class="flex items-center gap-2">
          <div class="relative flex-1">
            <i data-lucide="link" class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 transform -translate-y-1/2"></i>
            <input id="rag-yt-url-input" type="text" placeholder="Paste YouTube link (e.g. https://www.youtube.com/watch?v=kCc8FmEb1nY)..." class="w-full bg-slate-50 border border-slate-200 rounded-full pl-10 pr-4 py-2.5 text-xs text-slate-900 placeholder:text-slate-400 focus:ring-2 focus:ring-sky-400 focus:bg-white outline-none">
          </div>
          <button id="rag-yt-import-btn" class="btn-yellow px-5 py-2.5 text-xs font-bold flex items-center gap-1.5">
            <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Ingest Video
          </button>
        </div>

        <!-- Quick Presets -->
        <div class="flex flex-wrap items-center gap-1.5 pt-1">
          <span class="text-[10px] text-slate-400 font-semibold">Quick Presets:</span>
          <button data-yt-url="https://www.youtube.com/watch?v=aircAruvnKk" class="rag-yt-preset-chip px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-[11px] font-medium text-slate-700 transition-colors">3Blue1Brown Neural Nets</button>
          <button data-yt-url="https://www.youtube.com/watch?v=kCc8FmEb1nY" class="rag-yt-preset-chip px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-[11px] font-medium text-slate-700 transition-colors">Karpathy GPT from Scratch</button>
          <button data-yt-url="https://www.youtube.com/watch?v=jGwO_UgTS7I" class="rag-yt-preset-chip px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-[11px] font-medium text-slate-700 transition-colors">Stanford CS229 ML</button>
        </div>
      </div>

      <!-- Main Video & Synchronized Companion Workspace -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-7 space-y-4">
          <div class="card-white overflow-hidden p-2">
            <div class="relative aspect-video bg-slate-900 rounded-2xl overflow-hidden shadow-inner">
              <video id="rag-video-player" controls class="w-full h-full object-cover">
                <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4">
                Your browser does not support video playback.
              </video>
              <div id="rag-youtube-container" class="hidden w-full h-full">
                <div id="rag-youtube-iframe-target" class="w-full h-full"></div>
              </div>
            </div>
          </div>

          <div class="card-white p-4">
            <div class="flex items-center justify-between mb-3">
              <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="presentation" class="w-3.5 h-3.5 text-sky-600"></i> Synchronized Slide Decks
              </h4>
              <span class="text-[11px] text-sky-600 font-semibold">Click any slide to jump video</span>
            </div>
            <div id="rag-slides-strip" class="flex gap-3 overflow-x-auto pb-1"></div>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-4">
          <div class="card-white p-1.5 flex items-center justify-between">
            <button data-rag-tab="qa" class="px-3.5 py-1.5 rounded-full text-xs font-bold bg-yellow-300 text-slate-900 shadow-sm flex items-center gap-1">
              <i data-lucide="message-square" class="w-3 h-3"></i> Q&A
            </button>
            <button data-rag-tab="flashcards" class="px-3 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1">
              <i data-lucide="layers" class="w-3 h-3"></i> Flashcards
            </button>
            <button data-rag-tab="quiz" class="px-3 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1">
              <i data-lucide="check-square" class="w-3 h-3"></i> Quiz
            </button>
            <button data-rag-tab="summary" class="px-3 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1">
              <i data-lucide="file-text" class="w-3 h-3"></i> Summary
            </button>
          </div>

          <!-- Tab 1: Q&A -->
          <div id="rag-tab-view-qa" class="card-white p-4 flex flex-col justify-between space-y-4 min-h-[400px]">
            <div id="rag-qa-scroll-area" class="flex-1 overflow-y-auto space-y-3 pr-1 max-h-[340px]">
              <div id="rag-chat-placeholder" class="text-center py-8 text-slate-500">
                <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-600 flex items-center justify-center mx-auto mb-2.5">
                  <i data-lucide="bot" class="w-6 h-6"></i>
                </div>
                <h4 class="font-bold text-sm text-slate-800">Ask Anything About This Lecture</h4>
                <p class="text-xs text-slate-500 mt-0.5 max-w-xs mx-auto">Multimodal retrieval pinpoints exact video timestamps and slide diagrams.</p>
              </div>

              <div id="rag-answer-container" class="hidden space-y-3">
                <div id="rag-answer-content" class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 text-xs text-slate-800 leading-relaxed"></div>
                <div>
                  <h5 class="text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-2 flex items-center gap-1">
                    <i data-lucide="pin" class="w-3 h-3 text-sky-600"></i> Pinpointed Citations
                  </h5>
                  <div id="rag-citations-list" class="space-y-2"></div>
                </div>
              </div>
            </div>

            <div class="space-y-2 pt-2 border-t border-slate-100">
              <div class="flex items-center gap-2">
                <input id="rag-query-input" type="text" placeholder="Ask a question across audio, video & slides..." class="flex-1 bg-slate-50 border border-slate-200 rounded-full px-4 py-2 text-xs text-slate-900 placeholder:text-slate-400 focus:ring-2 focus:ring-sky-400 focus:bg-white outline-none">
                <button id="rag-ask-btn" class="btn-yellow px-4 py-2 text-xs font-bold flex items-center gap-1">
                  <span>Ask</span> <i data-lucide="send" class="w-3 h-3"></i>
                </button>
              </div>
            </div>
          </div>

          <!-- Tab 2: Flashcards -->
          <div id="rag-tab-view-flashcards" class="hidden card-white p-5 min-h-[400px] flex flex-col justify-between">
            <div class="flex items-center justify-between pb-2 border-b border-slate-100">
              <span id="flashcard-diff-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">Easy</span>
              <span id="flashcard-counter" class="text-xs font-mono text-slate-400">1 / 4</span>
            </div>

            <div class="my-4 perspective-1000">
              <div id="flashcard-card-el" class="relative w-full h-52 transform-style-3d transition-transform duration-500 cursor-pointer">
                <div class="absolute inset-0 card-pastel-blue p-6 flex flex-col justify-between backface-hidden shadow-md">
                  <span class="text-[11px] font-bold text-sky-800 uppercase tracking-wider">Question</span>
                  <p id="flashcard-front-text" class="text-sm font-bold text-slate-900 leading-relaxed text-center my-auto">Loading question...</p>
                  <span class="text-[10px] text-sky-700 text-center">Tap to flip card</span>
                </div>
                <div class="absolute inset-0 card-pastel-purple p-6 flex flex-col justify-between backface-hidden rotate-y-180 shadow-md">
                  <span class="text-[11px] font-bold text-purple-800 uppercase tracking-wider">Answer</span>
                  <p id="flashcard-back-text" class="text-xs font-semibold text-slate-900 leading-relaxed text-center my-auto">Loading answer...</p>
                  <span class="text-[10px] text-purple-700 text-center">Tap to flip back</span>
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between pt-2 border-t border-slate-100">
              <button id="flashcard-prev-btn" class="p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700"><i data-lucide="chevron-left" class="w-4 h-4"></i></button>
              <div class="flex items-center gap-2">
                <button id="flashcard-flip-btn" class="px-4 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 text-xs font-bold text-slate-700">Flip</button>
                <button id="flashcard-mark-mastered-btn" class="px-4 py-1.5 rounded-full bg-emerald-100 hover:bg-emerald-200 text-xs font-bold text-emerald-800">Mastered ✓</button>
              </div>
              <button id="flashcard-next-btn" class="p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700"><i data-lucide="chevron-right" class="w-4 h-4"></i></button>
            </div>
          </div>

          <!-- Tab 3: Quiz -->
          <div id="rag-tab-view-quiz" class="hidden card-white p-5 min-h-[400px] overflow-y-auto max-h-[420px]">
            <div id="rag-quiz-container" class="space-y-4"></div>
          </div>

          <!-- Tab 4: Summary -->
          <div id="rag-tab-view-summary" class="hidden card-white p-5 min-h-[400px] overflow-y-auto max-h-[420px]">
            <div id="rag-summary-content"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- MODULE 5: SCHEDULE & SYLLABUS OPTIMIZER (MATCHING SCREEN 2) -->
    <!-- ========================================================================= -->
    <section id="view-syllabus" class="hidden space-y-6">
      
      <!-- SCHEDULE HEADER & HORIZONTAL WEEK PICKER (SCREEN 2) -->
      <div class="card-white p-6 space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight">Schedule</h2>
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-sky-100 text-sky-800">Fall 2026</span>
          </div>

          <div class="flex items-center gap-2">
            <button id="syllabus-export-ics-btn" class="btn-yellow px-4 py-2 text-xs font-bold flex items-center gap-1.5">
              <i data-lucide="download" class="w-3.5 h-3.5"></i> Export .ICS
            </button>
          </div>
        </div>

        <!-- This Week Section Header -->
        <div class="flex items-center justify-between pt-1">
          <span class="text-xs font-bold text-slate-800">This week</span>
          <span class="text-xs font-semibold text-slate-400 cursor-pointer hover:text-slate-600">See all</span>
        </div>

        <!-- HORIZONTAL DATE PICKER STRIP (SCREEN 2) -->
        <div class="flex items-center justify-between gap-1 overflow-x-auto py-1">
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Sun</span>
            <span class="text-xs font-bold text-slate-700">04</span>
          </div>
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Mon</span>
            <span class="text-xs font-bold text-slate-700">05</span>
          </div>
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Tue</span>
            <span class="text-xs font-bold text-slate-700">06</span>
          </div>
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Wed</span>
            <span class="text-xs font-bold text-slate-700">07</span>
          </div>
          <div class="date-pill date-pill-active flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-sky-700 font-bold uppercase">Thu</span>
            <span class="text-xs font-extrabold text-sky-900">08</span>
          </div>
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Fri</span>
            <span class="text-xs font-bold text-slate-700">09</span>
          </div>
          <div class="date-pill flex flex-col items-center gap-0.5">
            <span class="text-[10px] text-slate-400 font-semibold uppercase">Sat</span>
            <span class="text-xs font-bold text-slate-700">10</span>
          </div>
        </div>
      </div>

      <!-- TIMELINE SCHEDULE & PDF IMPORT GRID -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Time Blocks (Styled identically to Screen 2) -->
        <div class="lg:col-span-8 card-white p-6 space-y-4">
          <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Today's Class Schedule & Study Blocks</h3>

          <div class="space-y-3 font-medium text-xs">
            <!-- 9:00am -->
            <div class="flex items-center gap-4">
              <span class="w-16 font-mono text-slate-400 font-semibold">9:00am</span>
              <div class="flex-1 timeline-block-blue p-3.5 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-sky-900 text-sm">Basic Mathematics & Asynchronous I/O</h4>
                  <p class="text-[11px] text-sky-700 font-mono mt-0.5">9:00am - 9:45am • Science Hall 102</p>
                </div>
                <span class="px-2.5 py-1 rounded-full bg-white/80 text-sky-800 text-[10px] font-bold">Lecture</span>
              </div>
            </div>

            <!-- 11:00am -->
            <div class="flex items-center gap-4">
              <span class="w-16 font-mono text-slate-400 font-semibold">11:00am</span>
              <div class="flex-1 timeline-block-cyan p-3.5 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-cyan-900 text-sm">English Grammar & Technical Writing</h4>
                  <p class="text-[11px] text-cyan-700 font-mono mt-0.5">11:00am - 11:45am • Online Live</p>
                </div>
                <span class="px-2.5 py-1 rounded-full bg-white/80 text-cyan-800 text-[10px] font-bold">Discussion</span>
              </div>
            </div>

            <!-- 1:00pm -->
            <div class="flex items-center gap-4">
              <span class="w-16 font-mono text-slate-400 font-semibold">1:00pm</span>
              <div class="flex-1 timeline-block-yellow p-3.5 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-amber-900 text-sm">Science & Distributed Consensus Proofs</h4>
                  <p class="text-[11px] text-amber-800 font-mono mt-0.5">1:00pm - 2:15pm • Lab Tower 4</p>
                </div>
                <span class="px-2.5 py-1 rounded-full bg-white/80 text-amber-900 text-[10px] font-bold">Lab</span>
              </div>
            </div>

            <!-- 3:00pm -->
            <div class="flex items-center gap-4">
              <span class="w-16 font-mono text-slate-400 font-semibold">3:00pm</span>
              <div class="flex-1 timeline-block-purple p-3.5 flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-purple-900 text-sm">World History & Computing Architecture Evolution</h4>
                  <p class="text-[11px] text-purple-800 font-mono mt-0.5">3:00pm - 4:15pm • Auditorium B</p>
                </div>
                <span class="px-2.5 py-1 rounded-full bg-white/80 text-purple-900 text-[10px] font-bold">Seminar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Syllabus PDF Dropzone -->
        <div class="lg:col-span-4 space-y-4">
          <div class="card-white p-5 space-y-3">
            <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
              <i data-lucide="file-up" class="w-4 h-4 text-sky-600"></i> Import Course Syllabus (PDF)
            </h4>

            <input id="syllabus-pdf-input" type="file" accept=".pdf,.txt" class="hidden">
            <div id="syllabus-pdf-dropzone" class="border-2 border-dashed border-sky-200 hover:border-sky-500 rounded-2xl p-5 text-center cursor-pointer transition-all bg-sky-50/50 hover:bg-sky-50">
              <i data-lucide="file-text" class="w-8 h-8 text-sky-500 mx-auto mb-2"></i>
              <p class="text-xs font-bold text-slate-800">Drop syllabus PDF here</p>
              <p class="text-[10px] text-slate-500 mt-0.5">Extracts deadlines, grading weights, and roadmap</p>
            </div>
          </div>

          <!-- Grading Weight Card -->
          <div class="card-white p-5 space-y-3">
            <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
              <i data-lucide="pie-chart" class="w-4 h-4 text-amber-500"></i> Grading Weight Distribution
            </h4>
            <div id="syllabus-weights-bar" class="w-full h-3 rounded-full overflow-hidden flex bg-slate-100"></div>
            <div id="syllabus-weights-container" class="space-y-1.5"></div>
          </div>
        </div>
      </div>
    </section>
""")
