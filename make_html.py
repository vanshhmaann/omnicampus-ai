# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"
with open(target, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OmniCampus AI • Unified Academic Intelligence Suite</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body class="min-h-screen bg-slate-950 text-slate-100 flex flex-col selection:bg-indigo-500 selection:text-white">

  <!-- Top Navigation Bar -->
  <header class="glass-panel sticky top-0 z-40 border-b border-slate-800/80 px-6 py-3.5 flex items-center justify-between">
    <div class="flex items-center gap-3.5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center shadow-lg shadow-indigo-500/25">
        <i data-lucide="sparkles" class="w-5 h-5 text-white"></i>
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-base font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-200 to-indigo-300 bg-clip-text text-transparent">
            OmniCampus AI
          </h1>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
            v2.1
          </span>
        </div>
        <p class="text-[11px] text-slate-400 font-medium">Unified Multimodal Campus Intelligence Suite</p>
      </div>
    </div>

    <!-- Quick Module Navigation Switcher -->
    <nav class="hidden lg:flex items-center gap-1.5 p-1 bg-slate-900/80 rounded-xl border border-slate-800">
      <button data-module-target="rag" class="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-md transition-all">
        <i data-lucide="book-open-check" class="w-3.5 h-3.5"></i> Lecture RAG
      </button>
      <button data-module-target="lostfound" class="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
        <i data-lucide="search" class="w-3.5 h-3.5"></i> Lost & Found
      </button>
      <button data-module-target="interview" class="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
        <i data-lucide="users-round" class="w-3.5 h-3.5"></i> Interview Prep
      </button>
      <button data-module-target="roadmap" class="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
        <i data-lucide="milestone" class="w-3.5 h-3.5"></i> Learning Roadmap
      </button>
      <button data-module-target="syllabus" class="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
        <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Syllabus Optimizer
      </button>
    </nav>

    <!-- Right Controls: Status, Gemini Key, Theme -->
    <div class="flex items-center gap-3">
      <div id="gemini-status-badge" class="hidden sm:flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
        <span class="w-2 h-2 rounded-full bg-indigo-400 mr-1.5"></span>
        Local Smart Simulation
      </div>

      <button id="open-settings-btn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
        <i data-lucide="settings-2" class="w-3.5 h-3.5 text-indigo-400"></i>
        <span>API Key</span>
      </button>

      <button onclick="toggleTheme()" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors" title="Toggle Dark/Light Mode">
        <i id="theme-toggle-icon" data-lucide="sun" class="w-4 h-4"></i>
      </button>
    </div>
  </header>

  <!-- Main Application Body -->
  <div class="flex-1 flex overflow-hidden">
    <!-- Left Icon Sidebar -->
    <aside class="w-16 md:w-20 bg-slate-900/60 border-r border-slate-800/80 flex flex-col items-center py-5 justify-between flex-shrink-0">
      <div class="flex flex-col items-center gap-4">
        <button data-module-target="rag" title="Multimodal Lecture RAG" class="p-3 rounded-2xl bg-indigo-600 text-white shadow-lg shadow-indigo-600/30 transition-all">
          <i data-lucide="book-open-check" class="w-5 h-5"></i>
        </button>
        <button data-module-target="lostfound" title="Lost & Found Visual Search" class="p-3 rounded-2xl text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
          <i data-lucide="search" class="w-5 h-5"></i>
        </button>
        <button data-module-target="interview" title="Multi-Agent Interview Prep" class="p-3 rounded-2xl text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
          <i data-lucide="users-round" class="w-5 h-5"></i>
        </button>
        <button data-module-target="roadmap" title="AI Learning Roadmap" class="p-3 rounded-2xl text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
          <i data-lucide="milestone" class="w-5 h-5"></i>
        </button>
        <button data-module-target="syllabus" title="Syllabus to Calendar Optimizer" class="p-3 rounded-2xl text-slate-400 hover:text-white hover:bg-slate-800 transition-all">
          <i data-lucide="calendar-check" class="w-5 h-5"></i>
        </button>
      </div>
      <div class="flex flex-col items-center gap-3 text-slate-500 text-xs font-mono">
        <span>5/5</span>
        <i data-lucide="cpu" class="w-4 h-4 text-indigo-400"></i>
      </div>
    </aside>

    <!-- Main Workspace -->
    <main class="flex-1 overflow-y-auto p-4 md:p-6 lg:p-8 max-w-7xl mx-auto w-full">
""")
