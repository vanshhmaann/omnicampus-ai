# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"
with open(target, "a", encoding="utf-8") as f:
    f.write("""
      <!-- ========================================================================= -->
      <!-- MODULE 3: AI MULTI-AGENT INTERVIEW & PLACEMENT PREP -->
      <!-- ========================================================================= -->
      <section id="view-interview" class="hidden space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl border border-slate-800">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">MODULE 3</span>
              <h2 class="text-xl font-bold text-white">AI Multi-Agent Interview & Placement Prep Hub</h2>
            </div>
            <p class="text-xs text-slate-400 mt-1">Simulate real-time multi-agent panel interviews with speech synthesis, live coding IDE, and ATS resume scoring</p>
          </div>

          <div class="flex flex-wrap items-center gap-3">
            <button id="interview-open-resume-btn" class="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
              <i data-lucide="file-text" class="w-3.5 h-3.5 text-indigo-400"></i> Resume ATS Scan
            </button>
            <button id="interview-tts-toggle" class="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
              <i data-lucide="volume-2" class="w-3.5 h-3.5 text-emerald-400"></i> Audio TTS On
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div data-agent-name="Dr. Aris" class="agent-card glass-panel p-4 rounded-2xl border border-slate-700/60 flex items-center gap-3.5 transition-all duration-300">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=60" alt="Dr. Aris" class="w-12 h-12 rounded-full object-cover border-2 border-indigo-500">
              <div class="waveform-container hidden absolute -bottom-1 -right-1 bg-slate-900 rounded-full p-1 border border-indigo-500 flex items-center gap-0.5">
                <div class="waveform-bar bg-indigo-400"></div>
                <div class="waveform-bar bg-indigo-400"></div>
                <div class="waveform-bar bg-indigo-400"></div>
              </div>
            </div>
            <div>
              <h4 class="font-bold text-xs text-white">Dr. Aris</h4>
              <span class="text-[10px] text-indigo-400 font-semibold block">Technical Lead</span>
              <span class="text-[9px] text-slate-400">Algorithms & Complexity</span>
            </div>
          </div>

          <div data-agent-name="Elena Vance" class="agent-card glass-panel p-4 rounded-2xl border border-slate-700/60 flex items-center gap-3.5 transition-all duration-300">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=60" alt="Elena" class="w-12 h-12 rounded-full object-cover border-2 border-pink-500">
              <div class="waveform-container hidden absolute -bottom-1 -right-1 bg-slate-900 rounded-full p-1 border border-pink-500 flex items-center gap-0.5">
                <div class="waveform-bar bg-pink-400"></div>
                <div class="waveform-bar bg-pink-400"></div>
                <div class="waveform-bar bg-pink-400"></div>
              </div>
            </div>
            <div>
              <h4 class="font-bold text-xs text-white">Elena Vance</h4>
              <span class="text-[10px] text-pink-400 font-semibold block">HR & Behavioral Dir.</span>
              <span class="text-[9px] text-slate-400">STAR Method & Culture</span>
            </div>
          </div>

          <div data-agent-name="Marcus Thorne" class="agent-card glass-panel p-4 rounded-2xl border border-slate-700/60 flex items-center gap-3.5 transition-all duration-300">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=60" alt="Marcus" class="w-12 h-12 rounded-full object-cover border-2 border-cyan-500">
              <div class="waveform-container hidden absolute -bottom-1 -right-1 bg-slate-900 rounded-full p-1 border border-cyan-500 flex items-center gap-0.5">
                <div class="waveform-bar bg-cyan-400"></div>
                <div class="waveform-bar bg-cyan-400"></div>
                <div class="waveform-bar bg-cyan-400"></div>
              </div>
            </div>
            <div>
              <h4 class="font-bold text-xs text-white">Marcus Thorne</h4>
              <span class="text-[10px] text-cyan-400 font-semibold block">Principal Architect</span>
              <span class="text-[9px] text-slate-400">Scale & Distributed Systems</span>
            </div>
          </div>

          <div data-agent-name="Samira" class="agent-card glass-panel p-4 rounded-2xl border border-slate-700/60 flex items-center gap-3.5 transition-all duration-300">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=60" alt="Samira" class="w-12 h-12 rounded-full object-cover border-2 border-amber-500">
              <div class="waveform-container hidden absolute -bottom-1 -right-1 bg-slate-900 rounded-full p-1 border border-amber-500 flex items-center gap-0.5">
                <div class="waveform-bar bg-amber-400"></div>
                <div class="waveform-bar bg-amber-400"></div>
                <div class="waveform-bar bg-amber-400"></div>
              </div>
            </div>
            <div>
              <h4 class="font-bold text-xs text-white">Samira</h4>
              <span class="text-[10px] text-amber-400 font-semibold block">Peer Candidate</span>
              <span class="text-[9px] text-slate-400">Collaborative Design</span>
            </div>
          </div>
        </div>

        <div class="glass-panel p-3 rounded-xl border border-slate-800 flex flex-wrap items-center justify-between gap-3 text-xs">
          <div class="flex flex-wrap items-center gap-3">
            <div class="flex items-center gap-2">
              <span class="text-slate-400 font-semibold">Target Position:</span>
              <select id="interview-role-select" class="bg-slate-800 border border-slate-700 text-white rounded-lg px-2.5 py-1 font-semibold outline-none">
                <option value="Senior Full-Stack Engineer">Senior Full-Stack Engineer</option>
                <option value="Distributed Systems Architect">Distributed Systems Architect</option>
                <option value="AI/ML Infrastructure Specialist">AI/ML Infrastructure Specialist</option>
                <option value="Core Data Platform Engineer">Core Data Platform Engineer</option>
              </select>
            </div>

            <div class="flex items-center gap-2">
              <span class="text-slate-400 font-semibold">Difficulty:</span>
              <select id="interview-difficulty-select" class="bg-slate-800 border border-slate-700 text-white rounded-lg px-2.5 py-1 font-semibold outline-none">
                <option value="Senior">Senior (L5)</option>
                <option value="Mid-Level">Mid-Level (L4)</option>
                <option value="Staff Architect">Staff Architect (L6)</option>
                <option value="Junior">Junior / New Grad</option>
              </select>
            </div>
          </div>

          <button id="interview-start-btn" class="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg font-bold shadow-md shadow-indigo-600/30 transition-all flex items-center gap-1.5">
            <i data-lucide="play" class="w-3.5 h-3.5"></i> Start Panel Simulation
          </button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-6 flex flex-col space-y-4">
            <div class="glass-panel p-4 rounded-2xl border border-slate-800 flex-1 flex flex-col justify-between min-h-[460px]">
              <div id="interview-chat-stream" class="flex-1 overflow-y-auto space-y-4 pr-2 max-h-[420px]">
                <div class="text-center py-12 text-slate-400">
                  <i data-lucide="message-square" class="w-10 h-10 mx-auto text-slate-600 mb-2"></i>
                  <p class="text-xs font-semibold text-slate-300">Interview session ready to start.</p>
                  <p class="text-[11px] text-slate-500 mt-0.5">Click 'Start Panel Simulation' to initiate your multi-agent technical interview.</p>
                </div>
              </div>

              <div class="pt-3 border-t border-slate-800 space-y-2">
                <div id="interview-live-critique"></div>
                <div class="flex items-center gap-2">
                  <textarea id="interview-answer-input" rows="2" placeholder="Type your response or click the microphone to speak (Ctrl+Enter to send)..." class="flex-1 bg-slate-900 border border-slate-700/80 rounded-xl p-3 text-xs text-white placeholder:text-slate-500 focus:ring-2 focus:ring-indigo-500 outline-none resize-none"></textarea>
                  <div class="flex flex-col gap-2">
                    <button id="interview-mic-btn" title="Voice Input" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">
                      <i data-lucide="mic" class="w-4 h-4 text-indigo-400"></i>
                    </button>
                    <button id="interview-send-btn" title="Send Answer" class="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white transition-colors">
                      <i data-lucide="send" class="w-4 h-4"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="lg:col-span-6 space-y-4">
            <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                <div class="flex items-center gap-2">
                  <i data-lucide="code-2" class="w-4 h-4 text-indigo-400"></i>
                  <span class="text-xs font-bold text-white">Live Whiteboard Coding IDE</span>
                </div>
                <div class="flex items-center gap-2">
                  <select id="code-lang-select" class="bg-slate-800 border border-slate-700 text-white rounded-lg px-2 py-1 text-[11px] font-mono outline-none">
                    <option value="python">Python 3</option>
                    <option value="javascript">JavaScript (ES6)</option>
                    <option value="cpp">C++ 20</option>
                  </select>
                  <button id="reset-code-btn" class="p-1 rounded bg-slate-800 text-slate-400 hover:text-white" title="Reset Code"><i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i></button>
                </div>
              </div>

              <textarea id="interview-code-editor" class="w-full h-44 bg-slate-950 text-indigo-200 font-mono text-xs p-3 rounded-xl border border-slate-800 focus:ring-1 focus:ring-indigo-500 outline-none leading-relaxed resize-none"></textarea>

              <div class="flex items-center justify-between">
                <span class="text-[10px] text-slate-400 font-mono">Sandboxed Execution</span>
                <button id="run-code-btn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-md shadow-emerald-600/30 transition-all">
                  <i data-lucide="play" class="w-3.5 h-3.5"></i> Run Test Cases
                </button>
              </div>

              <div id="code-output-terminal" class="p-3 bg-slate-950 rounded-xl border border-slate-800/90 text-xs font-mono text-slate-300 min-h-[50px]">
                <span class="text-slate-500">// Ready to compile and run candidate solution</span>
              </div>
            </div>

            <div class="glass-panel p-4 rounded-2xl border border-slate-800">
              <div class="flex items-center justify-between mb-2">
                <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="activity" class="w-3.5 h-3.5 text-pink-400"></i> Competency Performance Matrix
                </h4>
                <span id="interview-overall-score" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/40">76/100</span>
              </div>
              <div class="relative h-48 w-full">
                <canvas id="interview-radar-chart"></canvas>
              </div>
            </div>
          </div>
        </div>
      </section>
""")
