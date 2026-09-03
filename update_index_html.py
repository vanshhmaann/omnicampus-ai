# -*- coding: utf-8 -*-
import os

index_path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# YouTube player block
new_player_block = """          <div class="lg:col-span-7 flex flex-col space-y-4">
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
                <button data-yt-url="https://www.youtube.com/watch?v=kCc8FmEb1nY" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">Karpathy Let\'s Build GPT</button>
                <button data-yt-url="https://www.youtube.com/watch?v=jGwO_UgTS7I" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">Stanford CS229 ML</button>
                <button data-yt-url="https://www.youtube.com/watch?v=OQ5jsbhAv_M" class="rag-yt-preset-chip px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-300 border border-slate-700">MIT 6.006 Dynamic Prog</button>
              </div>
            </div>

            <!-- Video Player: Supports both HTML5 and YouTube Embed with Sync Seeking -->
            <div class="glass-card rounded-2xl overflow-hidden p-1.5 border border-slate-800">
              <div class="relative aspect-video bg-slate-900 rounded-xl overflow-hidden">
                <!-- Native HTML5 Video Element -->
                <video id="rag-video-player" controls class="w-full h-full object-cover">
                  <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4">
                  Your browser does not support video playback.
                </video>

                <!-- YouTube Embedded Player Container -->
                <div id="rag-youtube-container" class="hidden w-full h-full">
                  <div id="rag-youtube-iframe-target" class="w-full h-full"></div>
                </div>
              </div>
            </div>"""

# Replace the player column
import re
pattern = r'<div class="lg:col-span-7 flex flex-col space-y-4">.*?</div>\s*</div>\s*</div>'
match = re.search(r'<div class="lg:col-span-7 flex flex-col space-y-4">.*?<video id="rag-video-player".*?</video>\s*</div>\s*</div>', html, re.DOTALL)
if match:
    html = html[:match.start()] + new_player_block + html[match.end():]
    print("Matched and replaced video player block.")
else:
    print("Direct replace fallback")
    html = html.replace('<video id="rag-video-player"', '<!-- Dual --><video id="rag-video-player"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully.")
