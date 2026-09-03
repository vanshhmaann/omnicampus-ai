// OmniCampus AI - Core App Controller & State Manager
const AppState = {
  activeModule: 'rag',
  theme: localStorage.getItem('omnicampus_theme') || 'dark',
  geminiKey: localStorage.getItem('omnicampus_gemini_key') || '',
  geminiModel: localStorage.getItem('omnicampus_gemini_model') || 'gemini-1.5-flash',
  isOnline: true
};

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

function initApp() {
  lucide.createIcons();
  applyTheme(AppState.theme);
  setupNavigation();
  setupSettingsModal();
  checkBackendHealth();

  // Initialize all individual modules
  if (window.ModuleRAG) window.ModuleRAG.init();
  if (window.ModuleLostFound) window.ModuleLostFound.init();
  if (window.ModuleInterview) window.ModuleInterview.init();
  if (window.ModuleRoadmap) window.ModuleRoadmap.init();
  if (window.ModuleSyllabus) window.ModuleSyllabus.init();

  // Keyboard shortcut: Ctrl+K or Cmd+K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openCommandPalette();
    }
  });
}

function setupNavigation() {
  const navButtons = document.querySelectorAll('[data-module-target]');
  navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-module-target');
      switchModule(target);
    });
  });
}

function switchModule(moduleName) {
  AppState.activeModule = moduleName;

  // Update navigation buttons active state
  document.querySelectorAll('[data-module-target]').forEach(btn => {
    const target = btn.getAttribute('data-module-target');
    if (target === moduleName) {
      btn.classList.add('bg-indigo-600', 'text-white', 'shadow-lg', 'shadow-indigo-500/25');
      btn.classList.remove('text-slate-400', 'hover:bg-slate-800/60', 'hover:text-slate-200');
    } else {
      btn.classList.remove('bg-indigo-600', 'text-white', 'shadow-lg', 'shadow-indigo-500/25');
      btn.classList.add('text-slate-400', 'hover:bg-slate-800/60', 'hover:text-slate-200');
    }
  });

  // Toggle view containers
  const views = ['rag', 'lostfound', 'interview', 'roadmap', 'syllabus'];
  views.forEach(v => {
    const el = document.getElementById(`view-${v}`);
    if (el) {
      if (v === moduleName) {
        el.classList.remove('hidden');
        el.classList.add('animate-fadeIn');
      } else {
        el.classList.add('hidden');
        el.classList.remove('animate-fadeIn');
      }
    }
  });

  lucide.createIcons();
}

function applyTheme(theme) {
  AppState.theme = theme;
  localStorage.setItem('omnicampus_theme', theme);
  if (theme === 'light') {
    document.body.classList.add('light-mode');
    document.getElementById('theme-toggle-icon')?.setAttribute('data-lucide', 'moon');
  } else {
    document.body.classList.remove('light-mode');
    document.getElementById('theme-toggle-icon')?.setAttribute('data-lucide', 'sun');
  }
  lucide.createIcons();
}

function toggleTheme() {
  const newTheme = AppState.theme === 'dark' ? 'light' : 'dark';
  applyTheme(newTheme);
  showToast(`Switched to ${newTheme} mode`, 'info');
}

function setupSettingsModal() {
  const modal = document.getElementById('settings-modal');
  const openBtn = document.getElementById('open-settings-btn');
  const closeBtn = document.getElementById('close-settings-btn');
  const saveBtn = document.getElementById('save-settings-btn');
  const keyInput = document.getElementById('gemini-api-key-input');
  const modelSelect = document.getElementById('gemini-model-select');

  if (openBtn) {
    openBtn.addEventListener('click', () => {
      if (keyInput) keyInput.value = AppState.geminiKey;
      if (modelSelect) modelSelect.value = AppState.geminiModel;
      modal?.classList.remove('hidden');
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', () => modal?.classList.add('hidden'));
  }

  if (saveBtn) {
    saveBtn.addEventListener('click', () => {
      const key = keyInput?.value.trim() || '';
      const model = modelSelect?.value || 'gemini-1.5-flash';
      AppState.geminiKey = key;
      AppState.geminiModel = model;
      localStorage.setItem('omnicampus_gemini_key', key);
      localStorage.setItem('omnicampus_gemini_model', model);
      
      const badge = document.getElementById('gemini-status-badge');
      if (badge) {
        if (key) {
          badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse mr-1.5"></span> Gemini Live API`;
          badge.className = 'flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        } else {
          badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-indigo-400 mr-1.5"></span> Local Intelligent Simulation`;
          badge.className = 'flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30';
        }
      }

      modal?.classList.add('hidden');
      showToast('AI Settings updated successfully!', 'success');
    });
  }
}

async function checkBackendHealth() {
  try {
    const res = await fetch('/api/status');
    if (res.ok) {
      const data = await res.json();
      console.log('OmniCampus AI Backend connected:', data);
    }
  } catch (err) {
    console.warn('Backend running in local client mode:', err);
  }
}

function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  const colors = {
    info: 'bg-slate-800 text-white border-slate-700',
    success: 'bg-emerald-950 text-emerald-200 border-emerald-600/50',
    warning: 'bg-amber-950 text-amber-200 border-amber-600/50',
    error: 'bg-rose-950 text-rose-200 border-rose-600/50'
  };

  const icons = {
    info: 'info',
    success: 'check-circle-2',
    warning: 'alert-triangle',
    error: 'alert-circle'
  };

  toast.className = `flex items-center gap-3 px-4 py-3 rounded-xl border shadow-2xl backdrop-blur-md transition-all transform duration-300 translate-y-2 opacity-0 text-sm font-medium ${colors[type] || colors.info}`;
  toast.innerHTML = `
    <i data-lucide="${icons[type] || 'info'}" class="w-5 h-5 flex-shrink-0"></i>
    <span class="flex-1">${message}</span>
    <button onclick="this.parentElement.remove()" class="text-slate-400 hover:text-white">&times;</button>
  `;

  container.appendChild(toast);
  lucide.createIcons();

  requestAnimationFrame(() => {
    toast.classList.remove('translate-y-2', 'opacity-0');
  });

  setTimeout(() => {
    toast.classList.add('translate-y-2', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function openCommandPalette() {
  showToast('Quick Jump: Switch modules using sidebar tabs or 1-5 keys!', 'info');
}

window.AppState = AppState;
window.switchModule = switchModule;
window.toggleTheme = toggleTheme;
window.showToast = showToast;
