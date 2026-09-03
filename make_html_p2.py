# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"
with open(target, "a", encoding="utf-8") as f:
    f.write("""
      <!-- ========================================================================= -->
      <!-- MODULE 1: MULTIMODAL LECTURE & RESEARCH COMPANION (RAG) -->
      <!-- ========================================================================= -->
      <section id="view-rag" class="space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl border border-slate-800">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">MODULE 1</span>
              <h2 class="text-xl font-bold text-white">Multimodal Lecture & Research Companion (RAG)</h2>
            </div>
            <p id="rag-lecture-meta" class="text-xs text-slate-400 mt-1">CS 6501 • Prof. Alan Kay • Duration: 48:15</p>
          </div>

          <div class="flex items-center gap-3">
            <label class="text-xs text-slate-400 font-medium">Select Lecture:</label>
            <select id="rag-lecture-select" class="bg-slate-800 border border-slate-700 text-slate-200 text-xs font-semibold rounded-xl px-3 py-2 focus:ring-2 focus:ring-indigo-500 outline-none">
            </select>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-7 flex flex-col space-y-4">
            <!-- YouTube URL Import Input Bar -->
            <div class="glass-panel p-3.5 rounded-2xl border border-slate-800 space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="youtube" class="w-4 h-4 text-rose-500"></i> Import Any YouTube Lecture
                </span>
                <span class="text-[10px] text-slate-400 font-mono">Auto-extracts timestamps & topics</span>
              </div>

              <div class="flex items-center gap-2">
                <div class="relative flex-1">
                  <i data-lucide="link" class="w-3.5 h-3.5 text-slate-500 absolute left-3 top-1/2 transform -translate-y-1/2"></i>
                  <input id="rag-yt-url-input" type="text" placeholder="Paste YouTube link (e.g. https://www.youtube.com/watch?v=kCc8FmEb1nY)..." class="w-full bg-slate-900 border border-slate-700/80 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder:text-slate-500 focus:ring-2 focus:ring-rose-500 outline-none">
                </div>
                <button id="rag-yt-import-btn" class="px-4 py-2 bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-500 hover:to-pink-500 text-white rounded-xl text-xs font-bold shadow-md shadow-rose-600/30 transition-all flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Ingest Video
                </button>
              </div>

              <!-- Quick Presets -->
              <div class="flex flex-wrap items-center gap-1.5 pt-1">
                <span class="text-[10px] text-slate-400 font-semibold">Quick Presets:</span>
                <button data-yt-url="https://www.youtube.com/watch?v=aircAruvnKk" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">3Blue1Brown Neural Nets</button>
                <button data-yt-url="https://www.youtube.com/watch?v=kCc8FmEb1nY" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">Karpathy Let's Build GPT</button>
                <button data-yt-url="https://www.youtube.com/watch?v=jGwO_UgTS7I" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">Stanford CS229 ML</button>
                <button data-yt-url="https://www.youtube.com/watch?v=OQ5jsbhAv_M" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">MIT 6.006 Dynamic Prog</button>
              </div>
            </div>

            <!-- Video Player -->
            <div class="glass-card rounded-2xl overflow-hidden p-1.5 border border-slate-800">
              <div class="relative aspect-video bg-slate-900 rounded-xl overflow-hidden">
                <video id="rag-video-player" controls class="w-full h-full object-cover">
                  <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4">
                  Your browser does not support video playback.
                </video>
                <div id="rag-youtube-container" class="hidden w-full h-full">
                  <div id="rag-youtube-iframe-target" class="w-full h-full"></div>
                </div>
              </div>
            </div>

            <div>
              <div class="flex items-center justify-between mb-2">
                <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="presentation" class="w-3.5 h-3.5 text-indigo-400"></i> Synchronized Slide Decks
                </h4>
                <span class="text-[11px] text-indigo-400">Click any slide to jump video</span>
              </div>
              <div id="rag-slides-strip" class="flex gap-3 overflow-x-auto pb-2"></div>
            </div>
          </div>

          <div class="lg:col-span-5 flex flex-col space-y-4">
            <div class="glass-panel p-1.5 rounded-xl flex items-center justify-between border border-slate-800">
              <button data-rag-tab="qa" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-sm flex items-center gap-1.5">
                <i data-lucide="message-square" class="w-3.5 h-3.5"></i> Q&A
              </button>
              <button data-rag-tab="flashcards" class="px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                <i data-lucide="layers" class="w-3.5 h-3.5"></i> Flashcards
              </button>
              <button data-rag-tab="quiz" class="px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                <i data-lucide="check-square" class="w-3.5 h-3.5"></i> Quiz
              </button>
              <button data-rag-tab="summary" class="px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800 flex items-center gap-1.5">
                <i data-lucide="file-text" class="w-3.5 h-3.5"></i> Summary
              </button>
            </div>

            <div id="rag-tab-view-qa" class="glass-panel p-4 rounded-2xl border border-slate-800 flex-1 flex flex-col justify-between space-y-4 min-h-[420px]">
              <div id="rag-qa-scroll-area" class="flex-1 overflow-y-auto space-y-3 pr-1 max-h-[380px]">
                <div id="rag-chat-placeholder" class="text-center py-8 text-slate-400">
                  <div class="w-12 h-12 rounded-2xl bg-indigo-900/30 text-indigo-400 flex items-center justify-center mx-auto mb-3 border border-indigo-500/20">
                    <i data-lucide="bot" class="w-6 h-6"></i>
                  </div>
                  <h4 class="font-bold text-sm text-slate-200">Ask Anything About This Lecture</h4>
                  <p class="text-xs text-slate-400 mt-1 max-w-xs mx-auto">Multimodal citations will pinpoint exact timestamps and slide diagrams in the video.</p>
                </div>

                <div id="rag-answer-container" class="hidden space-y-4">
                  <div id="rag-answer-content" class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 text-xs text-slate-200 leading-relaxed"></div>
                  <div>
                    <h5 class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2 flex items-center gap-1">
                      <i data-lucide="pin" class="w-3 h-3 text-indigo-400"></i> Pinpointed Multimodal Citations
                    </h5>
                    <div id="rag-citations-list" class="space-y-2"></div>
                  </div>
                </div>
              </div>

              <div class="space-y-2 pt-2 border-t border-slate-800/80">
                <div class="flex flex-wrap gap-1.5">
                  <button data-prompt="How does Raft elect a leader and prevent split votes?" class="rag-prompt-chip px-2.5 py-1 rounded-lg text-[11px] bg-slate-800/90 hover:bg-indigo-950 text-indigo-300 border border-indigo-500/30 text-left truncate max-w-full">
                    ⚡ How does Raft elect a leader?
                  </button>
                  <button data-prompt="What is the formula and rationale for Scaled Dot-Product Attention?" class="rag-prompt-chip px-2.5 py-1 rounded-lg text-[11px] bg-slate-800/90 hover:bg-indigo-950 text-indigo-300 border border-indigo-500/30 text-left truncate max-w-full">
                    📐 Attention scaling factor formula
                  </button>
                </div>

                <div class="flex items-center gap-2">
                  <input id="rag-query-input" type="text" placeholder="Ask a question across lecture audio, video & slides..." class="flex-1 bg-slate-900 border border-slate-700/80 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder:text-slate-500 focus:ring-2 focus:ring-indigo-500 outline-none">
                  <button id="rag-ask-btn" class="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold shadow-md shadow-indigo-600/30 transition-all flex items-center gap-1.5">
                    <span>Ask</span> <i data-lucide="send" class="w-3.5 h-3.5"></i>
                  </button>
                </div>
              </div>
            </div>

            <div id="rag-tab-view-flashcards" class="hidden glass-panel p-5 rounded-2xl border border-slate-800 min-h-[420px] flex flex-col justify-between">
              <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                  <span id="flashcard-diff-badge" class="px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300">Easy</span>
                  <span id="flashcard-counter" class="text-xs font-mono text-slate-400">1 / 4</span>
                </div>
                <span class="text-[11px] text-slate-400">Click card to flip</span>
              </div>

              <div class="my-6 perspective-1000">
                <div id="flashcard-card-el" class="relative w-full h-56 transform-style-3d transition-transform duration-500 cursor-pointer">
                  <div class="absolute inset-0 bg-gradient-to-br from-slate-900 to-slate-800 border border-indigo-500/40 rounded-2xl p-6 flex flex-col justify-between backface-hidden shadow-2xl">
                    <span class="text-[11px] font-bold text-indigo-400 uppercase tracking-wider">Question</span>
                    <p id="flashcard-front-text" class="text-sm font-semibold text-white leading-relaxed text-center my-auto">Loading question...</p>
                    <span class="text-[10px] text-slate-500 text-center">Tap to flip</span>
                  </div>
                  <div class="absolute inset-0 bg-gradient-to-br from-indigo-950 to-slate-900 border border-purple-500/40 rounded-2xl p-6 flex flex-col justify-between backface-hidden rotate-y-180 shadow-2xl">
                    <span class="text-[11px] font-bold text-pink-400 uppercase tracking-wider">Answer & Concept</span>
                    <p id="flashcard-back-text" class="text-xs text-slate-200 leading-relaxed text-center my-auto">Loading answer...</p>
                    <span class="text-[10px] text-indigo-300 text-center">Tap to flip back</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                <button id="flashcard-prev-btn" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300"><i data-lucide="chevron-left" class="w-4 h-4"></i></button>
                <div class="flex items-center gap-2">
                  <button id="flashcard-flip-btn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200">Flip</button>
                  <button id="flashcard-mark-mastered-btn" class="px-3 py-1.5 rounded-xl bg-emerald-600/30 hover:bg-emerald-600 text-xs font-semibold text-emerald-200 border border-emerald-500/40">Mastered ✓</button>
                </div>
                <button id="flashcard-next-btn" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300"><i data-lucide="chevron-right" class="w-4 h-4"></i></button>
              </div>
            </div>

            <div id="rag-tab-view-quiz" class="hidden glass-panel p-5 rounded-2xl border border-slate-800 min-h-[420px] overflow-y-auto max-h-[440px]">
              <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
                <h4 class="font-bold text-sm text-slate-200">AI Knowledge Check</h4>
                <span class="text-xs text-indigo-400 font-semibold">Immediate Rationale</span>
              </div>
              <div id="rag-quiz-container" class="space-y-4"></div>
            </div>

            <div id="rag-tab-view-summary" class="hidden glass-panel p-5 rounded-2xl border border-slate-800 min-h-[420px] overflow-y-auto max-h-[440px]">
              <div id="rag-summary-content"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- MODULE 2: SMART CAMPUS "LOST & FOUND" SEMANTIC VISUAL SEARCH -->
      <!-- ========================================================================= -->
      <section id="view-lostfound" class="hidden space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl border border-slate-800">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">MODULE 2</span>
              <h2 class="text-xl font-bold text-white">Smart Campus "Lost & Found" Semantic Visual Search</h2>
            </div>
            <p class="text-xs text-slate-400 mt-1">Multi-modal vector search across uploaded photos, semantic descriptions, and campus geo-coordinates</p>
          </div>

          <div class="flex items-center gap-3">
            <button id="lf-open-report-btn" class="flex items-center gap-1.5 px-4 py-2.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white rounded-xl text-xs font-bold shadow-lg shadow-indigo-600/25 transition-all">
              <i data-lucide="plus-circle" class="w-4 h-4"></i> Report Lost/Found Item
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-8 space-y-4">
            <div class="flex items-center gap-2 p-2 glass-panel rounded-2xl border border-slate-800">
              <div class="pl-3 text-slate-400">
                <i data-lucide="search" class="w-4 h-4"></i>
              </div>
              <input id="lf-search-input" type="text" placeholder="Describe lost/found item (e.g. 'navy blue Hydro Flask with NASA sticker near student commons')..." class="flex-1 bg-transparent text-xs text-white placeholder:text-slate-500 outline-none px-2">
              <button id="lf-search-btn" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold transition-all shadow-md">
                Search
              </button>
            </div>

            <div class="flex flex-wrap items-center justify-between gap-3">
              <div class="flex items-center gap-1 p-1 bg-slate-900 rounded-xl border border-slate-800 text-xs">
                <button data-type="all" class="lf-type-toggle px-3 py-1 rounded-lg font-semibold bg-indigo-600 text-white">All</button>
                <button data-type="lost" class="lf-type-toggle px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">Lost</button>
                <button data-type="found" class="lf-type-toggle px-3 py-1 rounded-lg font-medium text-slate-400 hover:text-white">Found</button>
              </div>

              <div class="flex flex-wrap items-center gap-1.5 text-xs">
                <button data-category="all" class="lf-filter-btn px-3 py-1 rounded-lg font-semibold bg-indigo-600 text-white">All Categories</button>
                <button data-category="Electronics" class="lf-filter-btn px-2.5 py-1 rounded-lg font-medium text-slate-400 hover:bg-slate-800 hover:text-white">Electronics</button>
                <button data-category="Personal Items" class="lf-filter-btn px-2.5 py-1 rounded-lg font-medium text-slate-400 hover:bg-slate-800 hover:text-white">Personal</button>
                <button data-category="Wallets & IDs" class="lf-filter-btn px-2.5 py-1 rounded-lg font-medium text-slate-400 hover:bg-slate-800 hover:text-white">Wallets & IDs</button>
                <button data-category="Laptops" class="lf-filter-btn px-2.5 py-1 rounded-lg font-medium text-slate-400 hover:bg-slate-800 hover:text-white">Laptops</button>
              </div>
            </div>

            <div>
              <div class="flex items-center justify-between mb-3">
                <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Semantic Visual Matches</h4>
                <span id="lf-results-count" class="text-xs font-mono text-indigo-400 font-bold">5 Matches</span>
              </div>
              <div id="lf-items-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4"></div>
            </div>
          </div>

          <div class="lg:col-span-4 space-y-4">
            <div class="glass-panel p-4 rounded-2xl border border-slate-800">
              <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <i data-lucide="camera" class="w-3.5 h-3.5 text-indigo-400"></i> Visual Match Dropzone
              </h4>

              <input id="lf-image-input" type="file" accept="image/*" class="hidden">
              <div id="lf-image-dropzone" class="border-2 border-dashed border-slate-700 hover:border-indigo-500 rounded-xl p-4 text-center cursor-pointer transition-all duration-200">
                <div id="lf-dropzone-placeholder" class="py-4">
                  <i data-lucide="upload-cloud" class="w-8 h-8 text-indigo-400 mx-auto mb-2"></i>
                  <p class="text-xs font-semibold text-slate-300">Drop photo of lost item</p>
                  <p class="text-[10px] text-slate-500 mt-0.5">JPG, PNG, WebP • Auto-extracts visual embeddings</p>
                </div>

                <div id="lf-preview-container" class="hidden relative">
                  <img id="lf-image-preview" src="" alt="Preview" class="w-full h-32 object-cover rounded-lg">
                  <button id="lf-clear-image-btn" class="absolute top-2 right-2 bg-slate-900/90 text-rose-400 p-1.5 rounded-lg text-xs font-bold hover:bg-slate-900">
                    &times; Clear
                  </button>
                </div>
              </div>
            </div>

            <div class="glass-panel p-4 rounded-2xl border border-slate-800">
              <div class="flex items-center justify-between mb-3">
                <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="map" class="w-3.5 h-3.5 text-rose-400"></i> Campus Geo-Locator Map
                </h4>
                <span class="text-[10px] text-slate-400 font-mono">Live Pins</span>
              </div>

              <div class="relative w-full h-64 bg-slate-900 rounded-xl border border-slate-800 overflow-hidden">
                <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#6366f1 1px, transparent 1px); background-size: 16px 16px;"></div>
                <span class="absolute top-4 left-4 text-[10px] font-bold text-slate-500 font-mono uppercase">Science Library</span>
                <span class="absolute top-4 right-4 text-[10px] font-bold text-slate-500 font-mono uppercase">Dining Commons</span>
                <span class="absolute bottom-4 left-4 text-[10px] font-bold text-slate-500 font-mono uppercase">Engineering Tower</span>
                <span class="absolute bottom-4 right-4 text-[10px] font-bold text-slate-500 font-mono uppercase">Recreation Center</span>
                <span class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-[11px] font-extrabold text-indigo-500/40 uppercase tracking-widest pointer-events-none">Central Campus Quad</span>
                <div id="lf-campus-map-pins"></div>
              </div>
            </div>
          </div>
        </div>
      </section>
""")
