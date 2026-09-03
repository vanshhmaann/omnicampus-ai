// Module 5: PDF Syllabus-to-Calendar Study Optimizer & Roadmap Trigger
const ModuleSyllabus = (() => {
  let currentSyllabus = null;
  let activeView = 'calendar'; // 'calendar', 'gantt', 'kanban', 'sprints'

  async function init() {
    setupEventListeners();
    await loadSampleSyllabus();
  }

  function setupEventListeners() {
    // PDF Upload Dropzone
    const dropzone = document.getElementById('syllabus-pdf-dropzone');
    const fileInput = document.getElementById('syllabus-pdf-input');

    if (dropzone && fileInput) {
      dropzone.addEventListener('click', () => fileInput.click());
      dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('border-indigo-500', 'bg-indigo-950/20');
      });
      dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('border-indigo-500', 'bg-indigo-950/20');
      });
      dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('border-indigo-500', 'bg-indigo-950/20');
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
          uploadSyllabusPDF(e.dataTransfer.files[0]);
        }
      });
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          uploadSyllabusPDF(e.target.files[0]);
        }
      });
    }

    // View Toggles (Calendar, Gantt, Kanban, Sprints)
    document.querySelectorAll('.syllabus-view-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const view = tab.getAttribute('data-syllabus-view');
        switchSyllabusView(view);
      });
    });

    // 1-Click .ICS Export
    document.getElementById('syllabus-export-ics-btn')?.addEventListener('click', exportICSFile);

    // Direct Roadmap Generation Button
    document.getElementById('syllabus-generate-roadmap-btn')?.addEventListener('click', () => {
      if (currentSyllabus && window.ModuleRoadmap) {
        window.ModuleRoadmap.loadRoadmapFromSyllabus(currentSyllabus);
      } else {
        window.switchModule('roadmap');
      }
    });
  }

  async function loadSampleSyllabus() {
    try {
      const res = await fetch('/static/data/sample_syllabus.json');
      const data = await res.json();
      currentSyllabus = data;
      renderSyllabusDashboard(currentSyllabus);
    } catch (err) {
      console.error('Failed to load sample syllabus:', err);
    }
  }

  async function uploadSyllabusPDF(file) {
    const formData = new FormData();
    formData.append('file', file);

    window.showToast(`Uploading & parsing "${file.name}" with PyPDF...`, 'info');

    try {
      const res = await fetch('/api/syllabus/upload-pdf', {
        method: 'POST',
        body: formData
      });

      const data = await res.json();
      currentSyllabus = data.parsedSyllabus;
      renderSyllabusDashboard(currentSyllabus);
      
      // Auto trigger roadmap update
      if (window.ModuleRoadmap) {
        window.ModuleRoadmap.loadRoadmapFromSyllabus(currentSyllabus);
      }

      window.showToast(`Parsed ${data.pagesCount} syllabus pages! Extracted deadlines and generated Learning Roadmap.`, 'success');
    } catch (err) {
      console.error('PDF upload error:', err);
      window.showToast(`Syllabus upload error: ${err.message}`, 'error');
    }
  }

  function renderSyllabusDashboard(s) {
    if (!s) return;

    // Render Header Info
    const titleEl = document.getElementById('syllabus-course-title');
    const metaEl = document.getElementById('syllabus-course-meta');
    if (titleEl) titleEl.textContent = `${s.courseCode}: ${s.courseName}`;
    if (metaEl) metaEl.textContent = `${s.instructor} • ${s.term} • ${s.creditHours} Credit Hours`;

    // Render Grading Weights Bar & Badges
    renderGradingWeights(s.weights || []);

    // Render Burnout & Stress Heatmap
    renderBurnoutHeatmap(s.milestones || []);

    // Render Active Sub-View (Calendar / Gantt / Kanban / Sprints)
    renderCalendarView(s.milestones || []);
    renderGanttView(s.milestones || []);
    renderKanbanView(s.milestones || []);
    renderStudySprints(s.studyPlan || []);
  }

  function renderGradingWeights(weights) {
    const container = document.getElementById('syllabus-weights-container');
    const bar = document.getElementById('syllabus-weights-bar');

    if (bar) {
      bar.innerHTML = weights.map(w => `
        <div style="width: ${w.percent}%; background-color: ${w.color};" class="h-full relative group transition-all duration-300">
          <div class="hidden group-hover:block absolute -top-8 left-1/2 transform -translate-x-1/2 bg-slate-900 text-white text-[10px] px-2 py-0.5 rounded shadow whitespace-nowrap z-10">
            ${w.name}: ${w.percent}%
          </div>
        </div>
      `).join('');
    }

    if (container) {
      container.innerHTML = weights.map(w => `
        <div class="flex items-center justify-between p-2 rounded-lg bg-slate-800/60 border border-slate-700/60 text-xs">
          <div class="flex items-center gap-2">
            <span style="background-color: ${w.color};" class="w-2.5 h-2.5 rounded-full"></span>
            <span class="text-slate-300 font-medium">${w.name}</span>
          </div>
          <span class="font-bold text-slate-100 font-mono">${w.percent}%</span>
        </div>
      `).join('');
    }
  }

  function renderBurnoutHeatmap(milestones) {
    const container = document.getElementById('syllabus-burnout-heatmap');
    if (!container) return;

    container.innerHTML = milestones.map(m => {
      const stressColors = {
        'Low': 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
        'Medium': 'bg-amber-500/20 text-amber-300 border-amber-500/40',
        'High': 'bg-orange-500/20 text-orange-300 border-orange-500/40',
        'Critical': 'bg-rose-500/20 text-rose-300 border-rose-500/40 animate-pulse'
      };

      return `
        <div class="flex items-center justify-between p-2.5 bg-slate-800/80 border border-slate-700/60 rounded-xl text-xs">
          <div class="flex items-center gap-3">
            <span class="w-7 h-7 rounded-lg bg-slate-700 text-indigo-300 flex items-center justify-center font-bold text-[11px]">W${m.week}</span>
            <div>
              <h4 class="font-semibold text-slate-200">${m.title}</h4>
              <p class="text-[10px] text-slate-400 font-mono">${m.date} • ${m.type} ${m.weight ? '(' + m.weight + ')' : ''}</p>
            </div>
          </div>
          <span class="px-2 py-0.5 rounded-full border text-[10px] font-bold ${stressColors[m.stressLevel] || stressColors['Low']}">
            ${m.stressLevel} Stress
          </span>
        </div>
      `;
    }).join('');
  }

  function renderCalendarView(milestones) {
    const grid = document.getElementById('syllabus-calendar-grid');
    if (!grid) return;

    grid.innerHTML = milestones.map(m => `
      <div class="p-3 bg-slate-800/90 border border-slate-700/70 rounded-xl flex flex-col justify-between hover:border-indigo-500 transition-colors">
        <div>
          <div class="flex items-center justify-between text-[11px] mb-1.5">
            <span class="font-bold text-indigo-400">Week ${m.week}</span>
            <span class="font-mono text-[10px] text-slate-400 bg-slate-900 px-1.5 py-0.5 rounded">${m.date}</span>
          </div>
          <h4 class="font-semibold text-xs text-slate-100 mb-1">${m.title}</h4>
          <span class="inline-block px-2 py-0.5 rounded bg-slate-700 text-slate-300 text-[10px] font-medium">${m.type}</span>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-700/60 flex items-center justify-between text-[10px]">
          <span class="text-slate-400">Weight: <strong>${m.weight || 'N/A'}</strong></span>
          <span class="text-indigo-300 font-semibold">${m.status.toUpperCase()}</span>
        </div>
      </div>
    `).join('');
  }

  function renderGanttView(milestones) {
    const container = document.getElementById('syllabus-gantt-container');
    if (!container) return;

    container.innerHTML = milestones.map((m, idx) => {
      const leftOffset = (idx / milestones.length) * 80;
      return `
        <div class="p-2 border-b border-slate-800 flex items-center gap-4 text-xs">
          <div class="w-36 text-slate-300 font-medium truncate">${m.title}</div>
          <div class="flex-1 bg-slate-800/80 h-7 rounded-lg relative overflow-hidden flex items-center">
            <div style="left: ${leftOffset}%; width: 22%;" class="absolute h-5 rounded bg-gradient-to-r from-indigo-500 to-purple-600 shadow-md flex items-center px-2 text-[10px] font-bold text-white whitespace-nowrap">
              ${m.type} (W${m.week})
            </div>
          </div>
          <div class="w-20 text-right font-mono text-[11px] text-slate-400">${m.date.slice(5)}</div>
        </div>
      `;
    }).join('');
  }

  function renderKanbanView(milestones) {
    const todoCol = document.getElementById('kanban-col-todo');
    const inProgCol = document.getElementById('kanban-col-inprogress');
    const doneCol = document.getElementById('kanban-col-done');

    const todoItems = milestones.filter(m => m.status === 'todo');
    const inProgItems = milestones.filter(m => m.status === 'in-progress');
    const doneItems = milestones.filter(m => m.status === 'completed');

    const renderCard = (m) => `
      <div class="p-3 bg-slate-800 border border-slate-700 rounded-xl mb-2.5 shadow-sm hover:border-indigo-500 transition-colors cursor-grab">
        <div class="flex items-center justify-between text-[10px] text-slate-400 mb-1">
          <span class="font-bold text-indigo-400">W${m.week}</span>
          <span>${m.date}</span>
        </div>
        <h4 class="font-semibold text-xs text-slate-200 mb-1">${m.title}</h4>
        <div class="flex items-center justify-between mt-2 pt-1 border-t border-slate-700/60 text-[10px] text-slate-400">
          <span>${m.type}</span>
          <span class="font-bold text-amber-400">${m.weight || ''}</span>
        </div>
      </div>
    `;

    if (todoCol) todoCol.innerHTML = todoItems.map(renderCard).join('') || '<p class="text-xs text-slate-500 p-2">No tasks</p>';
    if (inProgCol) inProgCol.innerHTML = inProgItems.map(renderCard).join('') || '<p class="text-xs text-slate-500 p-2">No tasks</p>';
    if (doneCol) doneCol.innerHTML = doneItems.map(renderCard).join('') || '<p class="text-xs text-slate-500 p-2">No tasks</p>';
  }

  function renderStudySprints(plans) {
    const container = document.getElementById('syllabus-sprints-container');
    if (!container) return;

    container.innerHTML = plans.map(p => `
      <div class="p-4 bg-slate-800/80 border border-slate-700/60 rounded-2xl mb-4">
        <div class="flex items-center justify-between pb-2 border-b border-slate-700/60 mb-3">
          <div>
            <h4 class="font-bold text-sm text-indigo-300">${p.targetMilestone}</h4>
            <span class="text-xs text-slate-400">Target Exam / Deadline: <strong>${p.targetDate}</strong></span>
          </div>
          <span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-950 text-indigo-300 border border-indigo-500/40">
            Backward Planning Active
          </span>
        </div>

        <div class="space-y-2">
          ${p.sprints.map(s => `
            <div class="flex items-center justify-between p-2.5 bg-slate-900/70 border border-slate-800 rounded-xl text-xs">
              <div class="flex items-center gap-3">
                <span class="px-2 py-0.5 rounded bg-indigo-600/30 text-indigo-300 font-mono font-bold text-[10px]">${s.day}</span>
                <span class="text-slate-200">${s.topic}</span>
              </div>
              <div class="flex items-center gap-3">
                <span class="text-[11px] text-slate-400 font-mono"><i data-lucide="clock" class="w-3 h-3 inline mr-1"></i>${s.hours} hrs</span>
                <input type="checkbox" ${s.completed ? 'checked' : ''} class="rounded text-indigo-600 focus:ring-indigo-500 cursor-pointer">
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `).join('');

    lucide.createIcons();
  }

  function switchSyllabusView(viewName) {
    activeView = viewName;
    document.querySelectorAll('.syllabus-view-tab').forEach(t => {
      if (t.getAttribute('data-syllabus-view') === viewName) {
        t.className = 'syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-sm';
      } else {
        t.className = 'syllabus-view-tab px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800';
      }
    });

    ['calendar', 'gantt', 'kanban', 'sprints'].forEach(v => {
      const el = document.getElementById(`syllabus-view-panel-${v}`);
      if (el) {
        if (v === viewName) el.classList.remove('hidden');
        else el.classList.add('hidden');
      }
    });
  }

  async function exportICSFile() {
    if (!currentSyllabus) return;

    try {
      const res = await fetch('/api/syllabus/export-ics', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          courseCode: currentSyllabus.courseCode || 'CS8803',
          milestones: currentSyllabus.milestones || []
        })
      });

      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${currentSyllabus.courseCode}_study_schedule.ics`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);

      window.showToast('iCalendar (.ics) downloaded! Ready to import into Google Calendar / Outlook / Apple Calendar.', 'success');
    } catch (err) {
      console.error('ICS download failed:', err);
    }
  }

  return {
    init,
    exportICSFile,
    switchSyllabusView
  };
})();

window.ModuleSyllabus = ModuleSyllabus;
