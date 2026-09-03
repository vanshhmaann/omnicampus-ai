// Module 4: AI Interactive Learning Roadmap & Knowledge Graph (with Direct Syllabus Upload)
const ModuleRoadmap = (() => {
  let activeRoadmap = null;
  let activeNode = null;
  let currentPacing = 'semester'; // 'semester', 'sprint', 'crash'

  async function init() {
    setupEventListeners();
    await loadInitialRoadmap();
  }

  function setupEventListeners() {
    // Direct Syllabus Upload Dropzone in Roadmap View
    const dropzone = document.getElementById('roadmap-pdf-dropzone');
    const fileInput = document.getElementById('roadmap-pdf-input');

    if (dropzone && fileInput) {
      dropzone.addEventListener('click', () => fileInput.click());
      dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('border-cyan-500', 'bg-cyan-950/20');
      });
      dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('border-cyan-500', 'bg-cyan-950/20');
      });
      dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('border-cyan-500', 'bg-cyan-950/20');
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
          uploadSyllabusFromRoadmap(e.dataTransfer.files[0]);
        }
      });
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          uploadSyllabusFromRoadmap(e.target.files[0]);
        }
      });
    }

    // Direct Syllabus Text Paste Button
    const pasteBtn = document.getElementById('roadmap-paste-submit-btn');
    const pasteInput = document.getElementById('roadmap-paste-text-input');
    if (pasteBtn && pasteInput) {
      pasteBtn.addEventListener('click', () => {
        const text = pasteInput.value.trim();
        if (text) {
          generateRoadmapFromText(text);
        } else {
          window.showToast('Please paste course syllabus or topic list text.', 'warning');
        }
      });
    }

    // Preset Curriculum Buttons
    document.querySelectorAll('.roadmap-preset-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const course = chip.getAttribute('data-course');
        loadPresetRoadmap(course);
      });
    });

    // Pacing Mode Switcher
    document.querySelectorAll('.roadmap-pacing-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const pacing = btn.getAttribute('data-pacing');
        setPacingMode(pacing);
      });
    });

    // Close Node Inspector Drawer
    document.getElementById('close-node-drawer-btn')?.addEventListener('click', closeNodeDrawer);
    document.getElementById('node-drawer-backdrop')?.addEventListener('click', closeNodeDrawer);

    // Node Status Toggle in Drawer
    document.getElementById('node-status-select')?.addEventListener('change', onNodeStatusChange);

    // Export Roadmap Markdown
    document.getElementById('roadmap-export-md-btn')?.addEventListener('click', exportRoadmapMarkdown);
  }

  async function uploadSyllabusFromRoadmap(file) {
    const formData = new FormData();
    formData.append('file', file);

    window.showToast(`Analyzing "${file.name}" & constructing AI Learning Roadmap...`, 'info');

    try {
      const res = await fetch('/api/syllabus/upload-pdf', {
        method: 'POST',
        body: formData
      });

      const data = await res.json();
      if (data.parsedSyllabus) {
        loadRoadmapFromSyllabus(data.parsedSyllabus);
        window.showToast(`Roadmap generated successfully from "${file.name}"!`, 'success');
      } else {
        window.showToast('Failed to parse syllabus. Loading dynamic fallback roadmap.', 'warning');
        generateRoadmapFromText(file.name);
      }
    } catch (err) {
      console.error('Roadmap PDF upload error:', err);
      window.showToast(`Upload error: ${err.message}`, 'error');
    }
  }

  async function generateRoadmapFromText(text) {
    window.showToast('Generating AI Learning Roadmap from text...', 'info');
    try {
      const res = await fetch('/api/roadmap/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          courseName: text.slice(0, 45),
          syllabusText: text,
          pacingMode: currentPacing
        })
      });
      const data = await res.json();
      if (data.success && data.roadmap) {
        activeRoadmap = data.roadmap;
        activeRoadmap.courseTitle = text.length > 50 ? `${text.slice(0, 45)}...` : text;
        renderRoadmap(activeRoadmap);
        window.showToast(`Learning Roadmap generated!`, 'success');
      }
    } catch (err) {
      console.error('Error generating roadmap from text:', err);
    }
  }

  function loadPresetRoadmap(presetKey) {
    const presets = {
      'ml': {
        title: 'CS 7641: Deep Learning & Generative LLMs',
        phases: [
          {
            phaseNumber: 1,
            title: 'Phase 1: Deep Learning Fundamentals & Backprop',
            weeks: 'Weeks 1-3',
            nodes: [
              {
                id: 'ml-101',
                title: 'Computational Graphs & Autograd',
                type: 'Concept',
                status: 'Mastered',
                hours: 8,
                difficulty: 'Foundational',
                description: 'Reverse-mode automatic differentiation, Jacobian vector products, and loss landscape geometry.',
                learningObjectives: ['Implement backward pass for linear and activation layers from scratch', 'Debug vanishing/exploding gradient dynamics'],
                resources: [{'title': 'Calculus on Computational Graphs (Olah)', 'type': 'Article', 'url': 'https://colah.github.io/posts/2015-08-Backprop/'}],
                practiceTask: 'Build micrograd-style reverse-mode autodiff engine in pure Python.'
              },
              {
                id: 'ml-102',
                title: 'Stochastic Optimizers & Momentum',
                type: 'Lab',
                status: 'In Progress',
                hours: 6,
                difficulty: 'Intermediate',
                description: 'SGD with Nesterov momentum, AdamW weight decay decoupling, and learning rate warmup schedules.',
                learningObjectives: ['Derive exponential moving averages for first and second gradient moments', 'Tune cosine annealing learning rate schedules'],
                resources: [{'title': 'Adam: A Method for Stochastic Optimization (Kingma & Ba)', 'type': 'Paper', 'url': 'https://arxiv.org/abs/1412.6980'}],
                practiceTask: 'Implement AdamW optimizer and benchmark convergence against vanilla SGD.'
              }
            ]
          },
          {
            phaseNumber: 2,
            title: 'Phase 2: Transformer Architecture & Attention Mechanisms',
            weeks: 'Weeks 4-8',
            nodes: [
              {
                id: 'ml-201',
                title: 'Scaled Dot-Product & Multi-Head Attention',
                type: 'Core Milestone',
                status: 'In Progress',
                hours: 14,
                difficulty: 'Advanced',
                description: 'Query-Key-Value projections, causal masking for autoregressive modeling, and Rotary Position Embeddings (RoPE).',
                learningObjectives: ['Implement multi-head self-attention with tensor broadcasting in PyTorch', 'Derive softmax scaling factor 1/sqrt(d_k)'],
                resources: [{'title': 'Attention Is All You Need (Vaswani et al.)', 'type': 'Paper', 'url': 'https://arxiv.org/abs/1706.03762'}],
                practiceTask: 'Implement complete GPT-2 Transformer decoder block from scratch.'
              }
            ]
          },
          {
            phaseNumber: 3,
            title: 'Phase 3: Scaling, Quantization & Capstone LLM Deployment',
            weeks: 'Weeks 9-15',
            nodes: [
              {
                id: 'ml-301',
                title: 'FlashAttention & KV-Cache Inference',
                type: 'Capstone Lab',
                status: 'Not Started',
                hours: 16,
                difficulty: 'Mastery',
                description: 'IO-aware exact attention tiling, SRAM memory hierarchy optimization, and continuous batching in vLLM.',
                learningObjectives: ['Profile memory bandwidth bottlenecks during autoregressive token generation', 'Implement past_key_values tensor caching'],
                resources: [{'title': 'FlashAttention Paper (Dao et al.)', 'type': 'Paper', 'url': 'https://arxiv.org/abs/2205.14135'}],
                practiceTask: 'Benchmark token generation throughput with and without KV-cache on consumer GPU.'
              }
            ]
          }
        ]
      },
      'cloud': {
        title: 'CS 8803: Distributed Cloud Architectures & Resiliency',
        phases: null // Loads default sample syllabus
      }
    };

    if (presetKey === 'ml' && presets['ml']) {
      activeRoadmap = {
        courseTitle: presets['ml'].title,
        totalEstimatedHours: 70,
        currentMasteryPercent: 30,
        phases: presets['ml'].phases
      };
      renderRoadmap(activeRoadmap);
      window.showToast(`Loaded Roadmap for ${presets['ml'].title}`, 'success');
    } else {
      loadInitialRoadmap();
    }
  }

  async function loadInitialRoadmap() {
    try {
      const res = await fetch('/api/roadmap/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pacingMode: currentPacing })
      });
      const data = await res.json();
      if (data.success && data.roadmap) {
        activeRoadmap = data.roadmap;
        renderRoadmap(activeRoadmap);
      }
    } catch (err) {
      console.error('Failed to load initial roadmap:', err);
    }
  }

  function renderRoadmap(roadmap) {
    if (!roadmap) return;

    // Header Metadata
    const titleEl = document.getElementById('roadmap-course-title');
    const hoursEl = document.getElementById('roadmap-total-hours');
    const progressEl = document.getElementById('roadmap-mastery-percent');
    const progressBar = document.getElementById('roadmap-progress-bar');

    if (titleEl) titleEl.textContent = roadmap.courseTitle || 'Curriculum Roadmap';
    
    // Calculate total hours and mastery
    let totalHours = 0;
    let totalNodes = 0;
    let masteredNodes = 0;

    (roadmap.phases || []).forEach(phase => {
      (phase.nodes || []).forEach(node => {
        totalHours += node.hours || 0;
        totalNodes++;
        if (node.status === 'Mastered') masteredNodes++;
      });
    });

    const masteryPercent = totalNodes > 0 ? Math.round((masteredNodes / totalNodes) * 100) : 0;

    if (hoursEl) hoursEl.textContent = `${totalHours} hrs`;
    if (progressEl) progressEl.textContent = `${masteryPercent}%`;
    if (progressBar) progressBar.style.width = `${masteryPercent}%`;

    // Render Phases and Nodes Tree
    const treeContainer = document.getElementById('roadmap-phases-tree');
    if (!treeContainer) return;

    treeContainer.innerHTML = (roadmap.phases || []).map((phase, pIdx) => {
      return `
        <div class="relative mb-8 last:mb-0">
          <!-- Phase Header Card -->
          <div class="flex items-center gap-3 mb-4">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-cyan-500 to-indigo-600 flex items-center justify-center text-white font-bold text-sm shadow-lg shadow-cyan-500/25">
              ${phase.phaseNumber}
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h3 class="text-sm font-bold text-white">${phase.title}</h3>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-slate-800 text-cyan-300 border border-slate-700">
                  ${phase.weeks}
                </span>
              </div>
              <p class="text-[11px] text-slate-400">Phase Milestones & Core Competencies</p>
            </div>
          </div>

          <!-- Nodes Grid for Phase -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pl-4 md:pl-6 border-l-2 border-slate-800 relative">
            ${(phase.nodes || []).map(node => {
              const statusColors = {
                'Mastered': 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
                'In Progress': 'bg-amber-500/20 text-amber-300 border-amber-500/40',
                'Not Started': 'bg-slate-800 text-slate-400 border-slate-700'
              };

              const statusIcons = {
                'Mastered': 'check-circle-2',
                'In Progress': 'clock',
                'Not Started': 'circle'
              };

              return `
                <div onclick="ModuleRoadmap.openNodeDrawer('${node.id}')" class="glass-card rounded-2xl p-4 border border-slate-700/70 hover:border-cyan-500/80 cursor-pointer transition-all duration-200 group flex flex-col justify-between">
                  <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                      <span class="px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-slate-900 border border-slate-800 text-cyan-400">
                        ${node.type}
                      </span>
                      <span class="flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold border ${statusColors[node.status] || statusColors['Not Started']}">
                        <i data-lucide="${statusIcons[node.status] || 'circle'}" class="w-3 h-3"></i> ${node.status}
                      </span>
                    </div>

                    <h4 class="text-xs font-bold text-slate-100 group-hover:text-cyan-300 transition-colors line-clamp-1 mb-1.5">${node.title}</h4>
                    <p class="text-[11px] text-slate-400 line-clamp-2 leading-relaxed mb-3">${node.description}</p>
                  </div>

                  <div class="pt-2 border-t border-slate-700/60 flex items-center justify-between text-[10px] text-slate-400">
                    <span class="flex items-center gap-1"><i data-lucide="clock" class="w-3 h-3 text-cyan-400"></i> ${node.hours} hrs</span>
                    <span class="font-semibold text-slate-300">${node.difficulty}</span>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }).join('');

    lucide.createIcons();
  }

  function openNodeDrawer(nodeId) {
    if (!activeRoadmap) return;

    let targetNode = null;
    (activeRoadmap.phases || []).forEach(phase => {
      (phase.nodes || []).forEach(node => {
        if (node.id === nodeId) targetNode = node;
      });
    });

    if (!targetNode) return;
    activeNode = targetNode;

    const drawer = document.getElementById('roadmap-node-drawer');
    const backdrop = document.getElementById('node-drawer-backdrop');
    
    // Fill Drawer Content
    document.getElementById('node-drawer-title').textContent = targetNode.title;
    document.getElementById('node-drawer-type').textContent = targetNode.type;
    document.getElementById('node-drawer-hours').textContent = `${targetNode.hours} Estimated Hours`;
    document.getElementById('node-drawer-desc').textContent = targetNode.description;
    document.getElementById('node-drawer-task').textContent = targetNode.practiceTask || 'Complete review exercises.';

    const statusSelect = document.getElementById('node-status-select');
    if (statusSelect) statusSelect.value = targetNode.status;

    // Objectives List
    const objList = document.getElementById('node-drawer-objectives');
    if (objList) {
      objList.innerHTML = (targetNode.learningObjectives || []).map(obj => `
        <li class="flex items-start gap-2 text-xs text-slate-300">
          <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400 flex-shrink-0 mt-0.5"></i>
          <span>${obj}</span>
        </li>
      `).join('');
    }

    // Resources List
    const resList = document.getElementById('node-drawer-resources');
    if (resList) {
      resList.innerHTML = (targetNode.resources || []).map(r => `
        <a href="${r.url}" target="_blank" class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-cyan-500 text-xs transition-colors group">
          <div class="flex items-center gap-2">
            <i data-lucide="${r.type === 'Paper' ? 'file-text' : r.type === 'Video' ? 'play-circle' : 'external-link'}" class="w-4 h-4 text-cyan-400"></i>
            <span class="text-slate-200 group-hover:text-cyan-300 font-medium">${r.title}</span>
          </div>
          <span class="px-2 py-0.5 rounded bg-slate-800 text-[10px] text-slate-400 font-mono">${r.type}</span>
        </a>
      `).join('');
    }

    lucide.createIcons();
    drawer?.classList.remove('translate-x-full');
    backdrop?.classList.remove('hidden');
  }

  function closeNodeDrawer() {
    document.getElementById('roadmap-node-drawer')?.classList.add('translate-x-full');
    document.getElementById('node-drawer-backdrop')?.classList.add('hidden');
    activeNode = null;
  }

  async function onNodeStatusChange(e) {
    if (!activeNode) return;
    const newStatus = e.target.value;
    activeNode.status = newStatus;

    try {
      const res = await fetch('/api/roadmap/update-node', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nodeId: activeNode.id,
          status: newStatus
        })
      });

      const data = await res.json();
      if (data.success) {
        renderRoadmap(activeRoadmap);
        window.showToast(`Updated '${activeNode.title}' to ${newStatus}`, 'success');
      }
    } catch (err) {
      console.error('Failed to update node status:', err);
    }
  }

  async function setPacingMode(pacing) {
    currentPacing = pacing;
    document.querySelectorAll('.roadmap-pacing-btn').forEach(btn => {
      if (btn.getAttribute('data-pacing') === pacing) {
        btn.classList.add('bg-indigo-600', 'text-white');
        btn.classList.remove('text-slate-400', 'hover:text-white');
      } else {
        btn.classList.remove('bg-indigo-600', 'text-white');
        btn.classList.add('text-slate-400', 'hover:text-white');
      }
    });

    try {
      const res = await fetch('/api/roadmap/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pacingMode: pacing })
      });
      const data = await res.json();
      if (data.success && data.roadmap) {
        activeRoadmap = data.roadmap;
        renderRoadmap(activeRoadmap);
        window.showToast(`Pacing updated to ${pacing.toUpperCase()} mode`, 'info');
      }
    } catch (err) {
      console.error('Error changing pacing:', err);
    }
  }

  function loadRoadmapFromSyllabus(syllabus) {
    if (!syllabus) return;
    if (syllabus.roadmap) {
      activeRoadmap = syllabus.roadmap;
    } else {
      activeRoadmap = {
        courseTitle: syllabus.courseName || syllabus.courseCode || 'Curriculum Roadmap',
        totalEstimatedHours: 75,
        currentMasteryPercent: 0,
        phases: [
          {
            phaseNumber: 1,
            title: 'Phase 1: Core Fundamentals & Course Kickoff',
            weeks: 'Weeks 1-4',
            nodes: (syllabus.milestones || []).slice(0, 3).map((m, idx) => ({
              id: `dyn-node-${idx}`,
              title: m.title,
              type: m.type,
              status: 'Not Started',
              hours: 8,
              difficulty: 'Foundational',
              description: `Study module covering ${m.title} with milestone due on ${m.date}.`,
              learningObjectives: ['Master fundamental theory and complete lab implementations'],
              resources: [{'title': `${syllabus.courseCode || 'Course'} Lecture Series`, 'type': 'Video', 'url': '#'}],
              practiceTask: `Complete ${m.title} assignment problem sets.`
            }))
          },
          {
            phaseNumber: 2,
            title: 'Phase 2: Midterm Synthesis & Core Projects',
            weeks: 'Weeks 5-9',
            nodes: (syllabus.milestones || []).slice(3, 6).map((m, idx) => ({
              id: `dyn-node-p2-${idx}`,
              title: m.title,
              type: m.type,
              status: 'Not Started',
              hours: 12,
              difficulty: 'Advanced',
              description: `Advanced preparation and project development for ${m.title}.`,
              learningObjectives: ['In-depth problem solving and system scaling'],
              resources: [{'title': 'Midterm High-Yield Exam Guide', 'type': 'Doc', 'url': '#'}],
              practiceTask: 'Review past midterms and complete timed mock tests.'
            }))
          },
          {
            phaseNumber: 3,
            title: 'Phase 3: Final Capstone Project & Mastery',
            weeks: 'Weeks 10-15',
            nodes: (syllabus.milestones || []).slice(6).map((m, idx) => ({
              id: `dyn-node-p3-${idx}`,
              title: m.title,
              type: m.type,
              status: 'Not Started',
              hours: 16,
              difficulty: 'Mastery',
              description: `Capstone project demo, retrospective, and final evaluation.`,
              learningObjectives: ['Deliver production capstone solution and achieve comprehensive mastery'],
              resources: [{'title': 'Capstone Defense Rubric', 'type': 'Doc', 'url': '#'}],
              practiceTask: 'Complete capstone testing and code freeze.'
            }))
          }
        ]
      };
    }

    renderRoadmap(activeRoadmap);
    window.switchModule('roadmap');
    window.showToast(`AI Learning Roadmap generated for ${activeRoadmap.courseTitle}!`, 'success');
  }

  function exportRoadmapMarkdown() {
    if (!activeRoadmap) return;

    let md = `# Learning Roadmap: ${activeRoadmap.courseTitle}\n\n`;
    md += `**Overall Mastery**: ${activeRoadmap.currentMasteryPercent || 0}%\n\n---\n\n`;

    (activeRoadmap.phases || []).forEach(p => {
      md += `## ${p.title} (${p.weeks})\n\n`;
      (p.nodes || []).forEach(n => {
        const check = n.status === 'Mastered' ? '[x]' : '[ ]';
        md += `- ${check} **${n.title}** (${n.hours} hrs) - Status: *${n.status}*\n`;
        md += `  - *Description*: ${n.description}\n`;
        md += `  - *Practice Task*: ${n.practiceTask}\n\n`;
      });
    });

    const blob = new Blob([md], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${(activeRoadmap.courseTitle || 'Course').replace(/[^a-zA-Z0-9]/g, '_')}_Roadmap.md`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);

    window.showToast('Roadmap checklist exported as Markdown!', 'success');
  }

  return {
    init,
    openNodeDrawer,
    closeNodeDrawer,
    setPacingMode,
    loadRoadmapFromSyllabus,
    exportRoadmapMarkdown
  };
})();

window.ModuleRoadmap = ModuleRoadmap;
