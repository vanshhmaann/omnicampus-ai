// Module 2: Smart Campus "Lost & Found" Semantic Visual Search
const ModuleLostFound = (() => {
  let allItems = [];
  let activeImageBase64 = null;
  let claimingItem = null;

  async function init() {
    setupEventListeners();
    await loadItems();
  }

  function setupEventListeners() {
    // Search input
    const searchInput = document.getElementById('lf-search-input');
    const searchBtn = document.getElementById('lf-search-btn');

    if (searchBtn && searchInput) {
      searchBtn.addEventListener('click', () => performSearch());
      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') performSearch();
      });
    }

    // Category & Type filters
    document.querySelectorAll('.lf-filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.lf-filter-btn').forEach(b => b.classList.remove('bg-indigo-600', 'text-white'));
        btn.classList.add('bg-indigo-600', 'text-white');
        performSearch();
      });
    });

    document.querySelectorAll('.lf-type-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.lf-type-toggle').forEach(b => b.classList.remove('bg-indigo-600', 'text-white'));
        btn.classList.add('bg-indigo-600', 'text-white');
        performSearch();
      });
    });

    // Image dropzone
    const dropzone = document.getElementById('lf-image-dropzone');
    const fileInput = document.getElementById('lf-image-input');

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
          handleImageUpload(e.dataTransfer.files[0]);
        }
      });
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          handleImageUpload(e.target.files[0]);
        }
      });
    }

    // Clear image
    document.getElementById('lf-clear-image-btn')?.addEventListener('click', (e) => {
      e.stopPropagation();
      clearUploadedImage();
    });

    // Report Item Modal
    document.getElementById('lf-open-report-btn')?.addEventListener('click', openReportModal);
    document.getElementById('lf-close-report-btn')?.addEventListener('click', closeReportModal);
    document.getElementById('lf-submit-report-btn')?.addEventListener('click', submitReport);

    // Claim Modal
    document.getElementById('lf-close-claim-btn')?.addEventListener('click', closeClaimModal);
    document.getElementById('lf-submit-claim-btn')?.addEventListener('click', submitClaim);
  }

  function handleImageUpload(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      activeImageBase64 = e.target.result;
      const previewImg = document.getElementById('lf-image-preview');
      const placeholder = document.getElementById('lf-dropzone-placeholder');
      const previewContainer = document.getElementById('lf-preview-container');

      if (previewImg) previewImg.src = activeImageBase64;
      if (placeholder) placeholder.classList.add('hidden');
      if (previewContainer) previewContainer.classList.remove('hidden');

      window.showToast('Visual embedding extracted. Running semantic visual search...', 'info');
      performSearch();
    };
    reader.readAsDataURL(file);
  }

  function clearUploadedImage() {
    activeImageBase64 = null;
    const fileInput = document.getElementById('lf-image-input');
    if (fileInput) fileInput.value = '';
    document.getElementById('lf-preview-container')?.classList.add('hidden');
    document.getElementById('lf-dropzone-placeholder')?.classList.remove('hidden');
    performSearch();
  }

  async function loadItems() {
    try {
      const res = await fetch('/api/lostfound/items');
      const data = await res.json();
      allItems = data.items || [];
      renderItems(allItems);
      renderCampusMapPins(allItems);
    } catch (err) {
      console.error('Failed to fetch lost & found items:', err);
    }
  }

  async function performSearch() {
    const query = document.getElementById('lf-search-input')?.value || '';
    const activeFilterBtn = document.querySelector('.lf-filter-btn.bg-indigo-600');
    const activeTypeBtn = document.querySelector('.lf-type-toggle.bg-indigo-600');

    const category = activeFilterBtn ? activeFilterBtn.getAttribute('data-category') : 'all';
    const itemType = activeTypeBtn ? activeTypeBtn.getAttribute('data-type') : 'all';

    try {
      const res = await fetch('/api/lostfound/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: query,
          category: category,
          itemType: itemType,
          imageBase64: activeImageBase64
        })
      });

      const data = await res.json();
      renderItems(data.results || []);
      renderCampusMapPins(data.results || []);
    } catch (err) {
      console.error('Search failed:', err);
    }
  }

  function renderItems(items) {
    const grid = document.getElementById('lf-items-grid');
    const countBadge = document.getElementById('lf-results-count');

    if (countBadge) countBadge.textContent = `${items.length} Matches`;
    if (!grid) return;

    if (!items.length) {
      grid.innerHTML = `
        <div class="col-span-full py-12 text-center text-slate-400">
          <i data-lucide="package-search" class="w-12 h-12 mx-auto text-slate-600 mb-3"></i>
          <p class="text-base font-semibold text-slate-300">No matching lost & found items located.</p>
          <p class="text-xs text-slate-500 mt-1">Try broadening your semantic keywords or uploading a clearer visual photo.</p>
        </div>
      `;
      lucide.createIcons();
      return;
    }

    grid.innerHTML = items.map(item => {
      const isFound = item.type === 'found';
      const matchScore = item.matchScore || 88;
      
      return `
        <div class="glass-card rounded-2xl overflow-hidden flex flex-col group border border-slate-700/60 hover:border-indigo-500/80 transition-all duration-300">
          <!-- Thumbnail & Badges -->
          <div class="relative h-44 w-full bg-slate-800 overflow-hidden">
            <img src="${item.image}" alt="${item.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=600&auto=format&fit=crop&q=60'">
            
            <div class="absolute top-2.5 left-2.5 flex items-center gap-1.5">
              <span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold tracking-wide uppercase shadow-lg ${
                isFound ? 'bg-emerald-500 text-slate-950' : 'bg-amber-500 text-slate-950'
              }">
                ${item.type}
              </span>
              <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-slate-900/80 backdrop-blur-md text-slate-300 border border-slate-700">
                ${item.category}
              </span>
            </div>

            <div class="absolute top-2.5 right-2.5">
              <span class="flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-black bg-indigo-950/90 backdrop-blur-md text-indigo-300 border border-indigo-500/50 shadow-lg">
                <i data-lucide="sparkles" class="w-3 h-3 text-indigo-400"></i> ${matchScore}% Match
              </span>
            </div>

            <div class="absolute bottom-2 left-2 right-2 flex items-center justify-between text-[11px] text-slate-300 bg-slate-900/80 backdrop-blur-md px-2.5 py-1 rounded-lg border border-slate-800">
              <span class="flex items-center gap-1"><i data-lucide="map-pin" class="w-3 h-3 text-rose-400"></i> ${item.location}</span>
              <span class="font-mono text-[10px] text-slate-400">${item.date}</span>
            </div>
          </div>

          <!-- Content Body -->
          <div class="p-4 flex-1 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between gap-2 mb-1.5">
                <h3 class="font-bold text-sm text-slate-100 group-hover:text-indigo-400 transition-colors line-clamp-1">${item.title}</h3>
                <span class="text-[10px] font-mono text-slate-400">${item.id}</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed mb-3">${item.description}</p>
              
              <!-- Attribute Badges -->
              <div class="flex flex-wrap gap-1 mb-4">
                ${(item.attributes || []).map(attr => `
                  <span class="px-2 py-0.5 rounded bg-slate-800/90 text-slate-300 border border-slate-700 text-[10px] font-medium">${attr}</span>
                `).join('')}
              </div>
            </div>

            <!-- Action footer -->
            <div class="pt-3 border-t border-slate-700/60 flex items-center justify-between">
              <span class="text-[11px] font-medium text-slate-400">
                Status: <strong class="${item.status === 'Claimed' ? 'text-slate-500' : 'text-emerald-400'}">${item.status}</strong>
              </span>
              
              ${item.status === 'Claimed' ? `
                <button disabled class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-500 cursor-not-allowed">
                  Claimed
                </button>
              ` : `
                <button onclick="ModuleLostFound.openClaimModal('${item.id}')" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/30 transition-all duration-200">
                  <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> Verify & Claim
                </button>
              `}
            </div>
          </div>
        </div>
      `;
    }).join('');

    lucide.createIcons();
  }

  function renderCampusMapPins(items) {
    const mapEl = document.getElementById('lf-campus-map-pins');
    if (!mapEl) return;

    mapEl.innerHTML = items.map(item => {
      const coords = item.coordinates || { x: 50, y: 50 };
      const isFound = item.type === 'found';
      return `
        <div style="left: ${coords.x}%; top: ${coords.y}%;" class="absolute transform -translate-x-1/2 -translate-y-1/2 group cursor-pointer" onclick="ModuleLostFound.openClaimModal('${item.id}')">
          <div class="relative flex items-center justify-center">
            <span class="w-3.5 h-3.5 rounded-full ${isFound ? 'bg-emerald-400' : 'bg-amber-400'} animate-ping absolute opacity-75"></span>
            <span class="w-4 h-4 rounded-full ${isFound ? 'bg-emerald-500 border-2 border-slate-900' : 'bg-amber-500 border-2 border-slate-900'} relative shadow-md"></span>
          </div>
          <!-- Tooltip Popover -->
          <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 hidden group-hover:flex flex-col bg-slate-900/95 backdrop-blur-md border border-slate-700 rounded-lg p-2 text-center w-36 shadow-2xl z-20 pointer-events-none">
            <span class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide">${item.type}</span>
            <span class="text-xs font-semibold text-slate-200 line-clamp-1">${item.title}</span>
            <span class="text-[9px] text-slate-400">${item.location}</span>
          </div>
        </div>
      `;
    }).join('');
  }

  function openClaimModal(itemId) {
    const item = allItems.find(i => i.id === itemId);
    if (!item) return;

    claimingItem = item;
    const modal = document.getElementById('lf-claim-modal');
    const titleEl = document.getElementById('lf-claim-item-title');
    const qEl = document.getElementById('lf-claim-security-q');
    const resultBox = document.getElementById('lf-claim-result-box');
    const ansInput = document.getElementById('lf-claim-answer-input');

    if (titleEl) titleEl.textContent = `${item.title} (${item.id})`;
    if (qEl) qEl.textContent = item.securityQuestion || 'Please describe any distinctive markings or internal contents.';
    if (ansInput) ansInput.value = '';
    if (resultBox) resultBox.classList.add('hidden');

    modal?.classList.remove('hidden');
  }

  function closeClaimModal() {
    document.getElementById('lf-claim-modal')?.classList.add('hidden');
    claimingItem = null;
  }

  async function submitClaim() {
    if (!claimingItem) return;
    const ans = document.getElementById('lf-claim-answer-input')?.value.trim();
    if (!ans) {
      window.showToast('Please type your verification response.', 'warning');
      return;
    }

    try {
      const res = await fetch('/api/lostfound/verify-claim', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          itemId: claimingItem.id,
          answer: ans
        })
      });

      const data = await res.json();
      const resultBox = document.getElementById('lf-claim-result-box');
      if (resultBox) {
        resultBox.classList.remove('hidden');
        if (data.verified) {
          resultBox.className = 'p-4 rounded-xl bg-emerald-950/80 border border-emerald-500/40 text-emerald-200 text-xs space-y-2';
          resultBox.innerHTML = `
            <div class="flex items-center gap-2 font-bold text-sm text-emerald-300">
              <i data-lucide="check-circle" class="w-4 h-4"></i> ${data.message}
            </div>
            <div class="p-2.5 bg-slate-900/90 rounded-lg border border-emerald-500/30 flex items-center justify-between font-mono">
              <span>Pickup Token:</span>
              <strong class="text-sm text-emerald-400">${data.pickupToken}</strong>
            </div>
            <p class="text-[11px] text-slate-300">Location: ${data.pickupLocation} • Hours: ${data.claimHours}</p>
          `;
          lucide.createIcons();
          window.showToast('Ownership verified! Pickup token issued.', 'success');
        } else {
          resultBox.className = 'p-3 rounded-xl bg-rose-950/80 border border-rose-500/40 text-rose-200 text-xs';
          resultBox.innerHTML = `<strong>Verification Failed:</strong> ${data.message}`;
        }
      }
    } catch (err) {
      console.error('Claim verification error:', err);
    }
  }

  function openReportModal() {
    document.getElementById('lf-report-modal')?.classList.remove('hidden');
  }

  function closeReportModal() {
    document.getElementById('lf-report-modal')?.classList.add('hidden');
  }

  async function submitReport() {
    const title = document.getElementById('report-title-input')?.value.trim();
    const type = document.getElementById('report-type-select')?.value || 'lost';
    const category = document.getElementById('report-category-select')?.value || 'Personal Items';
    const location = document.getElementById('report-location-input')?.value.trim();
    const color = document.getElementById('report-color-input')?.value.trim();
    const brand = document.getElementById('report-brand-input')?.value.trim();
    const description = document.getElementById('report-desc-input')?.value.trim();
    const securityQuestion = document.getElementById('report-security-input')?.value.trim();

    if (!title || !location || !description) {
      window.showToast('Please fill out all required fields.', 'warning');
      return;
    }

    try {
      const res = await fetch('/api/lostfound/report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title, type, category, location, color, brand, description, securityQuestion
        })
      });

      const data = await res.json();
      if (data.success) {
        window.showToast(data.message, 'success');
        closeReportModal();
        await loadItems();
      }
    } catch (err) {
      console.error('Failed to submit report:', err);
    }
  }

  return {
    init,
    openClaimModal,
    openReportModal
  };
})();

window.ModuleLostFound = ModuleLostFound;
