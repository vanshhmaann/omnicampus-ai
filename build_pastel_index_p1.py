# -*- coding: utf-8 -*-
target = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\index.html"

with open(target, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OmniCampus AI • Unified Academic Intelligence Suite</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0284c7',
              600: '#0369a1',
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- KaTeX for Math -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>

  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- Custom Soft Pastel Styles -->
  <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body class="min-h-screen bg-slate-50 text-slate-900 flex flex-col pb-24 selection:bg-yellow-200 selection:text-slate-900">

  <!-- Minimal Top Header Bar -->
  <header class="sticky top-0 z-40 bg-slate-50/90 backdrop-blur-md border-b border-slate-200/60 px-4 md:px-8 py-3.5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-sky-400 to-indigo-500 flex items-center justify-center text-white shadow-md shadow-sky-500/20">
        <i data-lucide="sparkles" class="w-5 h-5"></i>
      </div>
      <div>
        <div class="flex items-center gap-1.5">
          <h1 class="text-base font-extrabold text-slate-900 tracking-tight">OmniCampus AI</h1>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-sky-100 text-sky-700">v2.2</span>
        </div>
        <p class="text-[11px] text-slate-500 font-medium">Academic Intelligence & Student Companion</p>
      </div>
    </div>

    <!-- Quick Navigation Pills on Desktop -->
    <nav class="hidden lg:flex items-center gap-1.5 p-1 bg-white rounded-full border border-slate-200 shadow-sm">
      <button data-module-target="rag" class="flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-bold bg-yellow-300 text-slate-900 shadow-sm transition-all">
        <i data-lucide="book-open-check" class="w-3.5 h-3.5"></i> Home & Lectures
      </button>
      <button data-module-target="syllabus" class="flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
        <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Schedule
      </button>
      <button data-module-target="roadmap" class="flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
        <i data-lucide="milestone" class="w-3.5 h-3.5"></i> Learning Roadmap
      </button>
      <button data-module-target="lostfound" class="flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
        <i data-lucide="search" class="w-3.5 h-3.5"></i> Lost & Found
      </button>
      <button data-module-target="interview" class="flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all">
        <i data-lucide="users-round" class="w-3.5 h-3.5"></i> Interview Prep
      </button>
    </nav>

    <!-- Top Right Controls -->
    <div class="flex items-center gap-2.5">
      <div id="gemini-status-badge" class="hidden sm:flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
        <span class="w-2 h-2 rounded-full bg-emerald-500 mr-1.5"></span>
        Smart Engine Active
      </div>

      <button id="open-settings-btn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white hover:bg-slate-100 text-slate-700 text-xs font-semibold border border-slate-200 shadow-sm transition-colors">
        <i data-lucide="settings" class="w-3.5 h-3.5 text-slate-600"></i>
        <span>Settings</span>
      </button>
    </div>
  </header>

  <!-- Main Content Container -->
  <main class="flex-1 max-w-6xl mx-auto w-full p-4 md:p-6 lg:p-8 space-y-6">
""")
