// Module 1: Multimodal Lecture & Research Companion (RAG) - with YouTube Link Integration
const ModuleRAG = (() => {
  let currentLectures = [];
  let selectedLecture = null;
  let currentFlashcardIndex = 0;
  let quizAnswers = {};
  let ytPlayer = null;
  let isYTAPIReady = false;

  async function init() {
    setupYouTubeAPI();
    setupEventListeners();
    await loadLectures();
  }

  function setupYouTubeAPI() {
    // Load YouTube IFrame API script dynamically
    if (!window.YT) {
      const tag = document.createElement('script');
      tag.src = 'https://www.youtube.com/iframe_api';
      const firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      window.onYouTubeIframeAPIReady = () => {
        isYTAPIReady = true;
        console.log('YouTube IFrame API Ready');
        if (selectedLecture && selectedLecture.videoType === 'youtube') {
          initOrLoadYTPlayer(selectedLecture.youtubeId);
        }
      };
    } else if (window.YT && window.YT.Player) {
      isYTAPIReady = true;
    }
  }

  function setupEventListeners() {
    // Lecture select dropdown
    const lectureSelect = document.getElementById('rag-lecture-select');
    if (lectureSelect) {
      lectureSelect.addEventListener('change', (e) => {
        const lec = currentLectures.find(l => l.id === e.target.value);
        if (lec) selectLecture(lec);
      });
    }

    // YouTube Import Button & Input
    const ytImportBtn = document.getElementById('rag-yt-import-btn');
    const ytInput = document.getElementById('rag-yt-url-input');
    if (ytImportBtn && ytInput) {
      ytImportBtn.addEventListener('click', () => importYouTubeVideo());
      ytInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          importYouTubeVideo();
        }
      });
    }

    // YouTube Preset Chips
    document.querySelectorAll('.rag-yt-preset-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const url = chip.getAttribute('data-yt-url');
        if (ytInput) {
          ytInput.value = url;
          importYouTubeVideo();
        }
      });
    });

    // Ask RAG Q&A
    const askBtn = document.getElementById('rag-ask-btn');
    const queryInput = document.getElementById('rag-query-input');
    if (askBtn && queryInput) {
      askBtn.addEventListener('click', () => submitQuery());
      queryInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          submitQuery();
        }
      });
    }

    // Prompt suggestion chips
    document.querySelectorAll('.rag-prompt-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const text = chip.getAttribute('data-prompt');
        if (queryInput) {
          queryInput.value = text;
          submitQuery();
        }
      });
    });

    // Flashcard navigation
    document.getElementById('flashcard-flip-btn')?.addEventListener('click', flipFlashcard);
    document.getElementById('flashcard-card-el')?.addEventListener('click', flipFlashcard);
    document.getElementById('flashcard-prev-btn')?.addEventListener('click', prevFlashcard);
    document.getElementById('flashcard-next-btn')?.addEventListener('click', nextFlashcard);
    document.getElementById('flashcard-mark-mastered-btn')?.addEventListener('click', toggleMastery);

    // Summary tab toggles
    document.querySelectorAll('[data-rag-tab]').forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-rag-tab');
        switchRAGTab(target);
      });
    });
  }

  async function loadLectures() {
    try {
      const res = await fetch('/api/rag/lectures');
      const data = await res.json();
      currentLectures = data.lectures || [];
      
      const select = document.getElementById('rag-lecture-select');
      if (select) {
        select.innerHTML = currentLectures.map(l => 
          `<option value="${l.id}">${l.course ? l.course + ' - ' : ''}${l.title}</option>`
        ).join('');
      }

      if (currentLectures.length > 0) {
        selectLecture(currentLectures[0]);
      }
    } catch (err) {
      console.error('Failed to load lectures:', err);
    }
  }

  function selectLecture(lecture) {
    selectedLecture = lecture;
    currentFlashcardIndex = 0;
    quizAnswers = {};

    // Update Header and Metadata
    const titleEl = document.getElementById('rag-lecture-title');
    const metaEl = document.getElementById('rag-lecture-meta');
    if (titleEl) titleEl.textContent = lecture.title;
    if (metaEl) metaEl.textContent = `${lecture.course} • ${lecture.instructor} • Duration: ${lecture.duration}`;

    // Switch Player View: YouTube iframe vs Standard Video
    const html5Video = document.getElementById('rag-video-player');
    const ytContainer = document.getElementById('rag-youtube-container');

    if (lecture.videoType === 'youtube' && lecture.youtubeId) {
      if (html5Video) {
        html5Video.pause();
        html5Video.classList.add('hidden');
      }
      if (ytContainer) {
        ytContainer.classList.remove('hidden');
        initOrLoadYTPlayer(lecture.youtubeId);
      }
    } else {
      if (ytContainer) {
        ytContainer.classList.add('hidden');
        if (ytPlayer && ytPlayer.pauseVideo) ytPlayer.pauseVideo();
      }
      if (html5Video) {
        html5Video.classList.remove('hidden');
        html5Video.src = lecture.videoUrl;
      }
    }

    // Render Slide Preview Strip
    renderSlideStrip(lecture.slides || []);

    // Render Flashcards, Quiz, Summary
    renderFlashcard();
    renderQuiz(lecture.quiz || []);
    renderSummary(lecture);
  }

  function initOrLoadYTPlayer(videoId) {
    if (!isYTAPIReady && window.YT && window.YT.Player) {
      isYTAPIReady = true;
    }

    if (!isYTAPIReady) {
      // If YT API not ready yet, load directly via standard responsive iframe
      const container = document.getElementById('rag-youtube-iframe-target');
      if (container) {
        container.innerHTML = `<iframe id="yt-direct-iframe" class="w-full h-full rounded-xl" src="https://www.youtube.com/embed/${videoId}?enablejsapi=1&autoplay=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
      }
      return;
    }

    if (ytPlayer && ytPlayer.loadVideoById) {
      try {
        ytPlayer.loadVideoById(videoId);
      } catch (e) {
        console.warn('Error loading video on existing player:', e);
      }
    } else {
      const container = document.getElementById('rag-youtube-iframe-target');
      if (container) {
        container.innerHTML = `<div id="yt-player-embed" class="w-full h-full"></div>`;
        try {
          ytPlayer = new YT.Player('yt-player-embed', {
            height: '100%',
            width: '100%',
            videoId: videoId,
            playerVars: {
              playsinline: 1,
              modestbranding: 1,
              rel: 0
            },
            events: {
              onReady: (event) => {
                console.log('YouTube Player Ready for video:', videoId);
              }
            }
          });
        } catch (err) {
          console.warn('YT.Player init fallback:', err);
        }
      }
    }
  }

  async function importYouTubeVideo() {
    const input = document.getElementById('rag-yt-url-input');
    const url = input?.value.trim();
    if (!url) {
      window.showToast('Please paste a valid YouTube video URL.', 'warning');
      return;
    }

    window.showToast('Importing YouTube lecture & generating multimodal transcript timeline...', 'info');

    try {
      const res = await fetch('/api/rag/ingest-youtube', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
      });

      const data = await res.json();
      if (data.success && data.lecture) {
        currentLectures.unshift(data.lecture);
        
        // Update Select Dropdown
        const select = document.getElementById('rag-lecture-select');
        if (select) {
          select.innerHTML = currentLectures.map(l => 
            `<option value="${l.id}">${l.course ? l.course + ' - ' : ''}${l.title}</option>`
          ).join('');
          select.value = data.lecture.id;
        }

        selectLecture(data.lecture);
        window.showToast(data.message, 'success');
        if (input) input.value = '';
      } else {
        window.showToast('Failed to ingest YouTube video.', 'error');
      }
    } catch (err) {
      console.error('YouTube import error:', err);
      window.showToast(`YouTube import error: ${err.message}`, 'error');
    }
  }

  function renderSlideStrip(slides) {
    const strip = document.getElementById('rag-slides-strip');
    if (!strip) return;

    strip.innerHTML = slides.map(s => `
      <div onclick="ModuleRAG.seekToTimestamp('${s.timestamp}', ${s.page})" class="flex-shrink-0 w-48 bg-slate-850 border border-slate-700/60 hover:border-indigo-500 rounded-xl p-3 cursor-pointer transition-all duration-200 group">
        <div class="flex items-center justify-between text-xs text-indigo-400 font-semibold mb-1">
          <span>Slide ${s.page}</span>
          <span class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-[10px] group-hover:bg-indigo-600 group-hover:text-white">${s.timestamp}</span>
        </div>
        <h4 class="text-xs font-bold text-slate-200 line-clamp-2 mb-1">${s.title}</h4>
        <p class="text-[11px] text-slate-400 line-clamp-2">${s.excerpt}</p>
      </div>
    `).join('');
  }

  function seekToTimestamp(ts, pageNumber) {
    const parts = ts.split(':').map(Number);
    let seconds = 0;
    if (parts.length === 2) {
      seconds = parts[0] * 60 + parts[1];
    } else if (parts.length === 3) {
      seconds = parts[0] * 3600 + parts[1] * 60 + parts[2];
    }

    if (selectedLecture && selectedLecture.videoType === 'youtube') {
      if (ytPlayer && ytPlayer.seekTo) {
        try {
          ytPlayer.seekTo(seconds, true);
          ytPlayer.playVideo();
        } catch (e) {
          console.warn('ytPlayer.seekTo exception:', e);
        }
      } else {
        // Fallback for iframe postMessage
        const iframe = document.querySelector('#rag-youtube-iframe-target iframe');
        if (iframe && iframe.contentWindow) {
          iframe.contentWindow.postMessage(JSON.stringify({
            event: 'command',
            func: 'seekTo',
            args: [seconds, true]
          }), '*');
        }
      }
    } else {
      const video = document.getElementById('rag-video-player');
      if (video) {
        video.currentTime = seconds;
        video.play();
      }
    }

    window.showToast(`Seeked lecture to timestamp [${ts}] (Topic ${pageNumber})`, 'info');
  }

  async function submitQuery() {
    const queryInput = document.getElementById('rag-query-input');
    const query = queryInput?.value.trim();
    if (!query) return;

    const answerContainer = document.getElementById('rag-answer-container');
    const placeholder = document.getElementById('rag-chat-placeholder');
    const contentBox = document.getElementById('rag-answer-content');
    const citationsBox = document.getElementById('rag-citations-list');

    if (placeholder) placeholder.classList.add('hidden');
    if (answerContainer) answerContainer.classList.remove('hidden');

    if (contentBox) {
      contentBox.innerHTML = `
        <div class="flex items-center gap-3 text-indigo-400 py-4">
          <div class="w-5 h-5 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin"></div>
          <span class="text-sm font-medium">Synthesizing multimodal retrieval across video transcript & slide decks...</span>
        </div>
      `;
    }

    try {
      const res = await fetch('/api/rag/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          lectureId: selectedLecture?.id || 'lec-cs6501',
          query: query
        })
      });

      const data = await res.json();
      
      if (contentBox) {
        contentBox.innerHTML = parseMarkdownAndLaTeX(data.answer);
      }

      if (citationsBox) {
        citationsBox.innerHTML = (data.citations || []).map(c => `
          <div onclick="ModuleRAG.seekToTimestamp('${c.timestamp}', ${c.page})" class="p-3 bg-slate-800/80 border border-slate-700 hover:border-indigo-500 rounded-xl cursor-pointer transition-all duration-200 group">
            <div class="flex items-center justify-between text-xs mb-1">
              <span class="font-bold text-indigo-400 group-hover:text-indigo-300 flex items-center gap-1.5">
                <i data-lucide="play-circle" class="w-3.5 h-3.5"></i> ${c.source}
              </span>
              <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                ${c.confidence} match
              </span>
            </div>
            <p class="text-xs text-slate-300 italic">"${c.excerpt}"</p>
            <div class="mt-2 text-[10px] font-mono text-indigo-300 flex items-center gap-1">
              <span>Timestamp: [${c.timestamp}]</span> • <span>Click to Jump Video</span>
            </div>
          </div>
        `).join('');
        lucide.createIcons();
      }

    } catch (err) {
      if (contentBox) {
        contentBox.innerHTML = `<p class="text-rose-400">Error processing lecture retrieval query: ${err.message}</p>`;
      }
    }
  }

  function renderFlashcard() {
    const cards = selectedLecture?.flashcards || [];
    const cardEl = document.getElementById('flashcard-card-el');
    const frontEl = document.getElementById('flashcard-front-text');
    const backEl = document.getElementById('flashcard-back-text');
    const countEl = document.getElementById('flashcard-counter');
    const diffBadge = document.getElementById('flashcard-diff-badge');

    if (!cards.length) return;
    const card = cards[currentFlashcardIndex];

    if (frontEl) frontEl.textContent = card.front;
    if (backEl) backEl.textContent = card.back;
    if (countEl) countEl.textContent = `${currentFlashcardIndex + 1} / ${cards.length}`;
    
    if (diffBadge) {
      diffBadge.textContent = card.difficulty;
      diffBadge.className = `px-2 py-0.5 rounded-full text-xs font-semibold ${
        card.difficulty === 'Easy' ? 'bg-emerald-500/20 text-emerald-300' :
        card.difficulty === 'Medium' ? 'bg-amber-500/20 text-amber-300' :
        'bg-rose-500/20 text-rose-300'
      }`;
    }

    if (cardEl) cardEl.classList.remove('rotate-y-180');
  }

  function flipFlashcard() {
    document.getElementById('flashcard-card-el')?.classList.toggle('rotate-y-180');
  }

  function prevFlashcard() {
    const cards = selectedLecture?.flashcards || [];
    if (!cards.length) return;
    currentFlashcardIndex = (currentFlashcardIndex - 1 + cards.length) % cards.length;
    renderFlashcard();
  }

  function nextFlashcard() {
    const cards = selectedLecture?.flashcards || [];
    if (!cards.length) return;
    currentFlashcardIndex = (currentFlashcardIndex + 1) % cards.length;
    renderFlashcard();
  }

  function toggleMastery() {
    const cards = selectedLecture?.flashcards || [];
    if (!cards.length) return;
    cards[currentFlashcardIndex].mastered = !cards[currentFlashcardIndex].mastered;
    window.showToast(`Card marked as ${cards[currentFlashcardIndex].mastered ? 'Mastered 🎉' : 'Needs Review 📚'}`, 'success');
  }

  function renderQuiz(quizItems) {
    const container = document.getElementById('rag-quiz-container');
    if (!container) return;

    if (!quizItems || !quizItems.length) {
      container.innerHTML = '<p class="text-slate-400 text-sm">No quiz items generated yet.</p>';
      return;
    }

    container.innerHTML = quizItems.map((q, idx) => `
      <div class="p-4 bg-slate-800/80 border border-slate-700/60 rounded-xl mb-4">
        <div class="flex items-center gap-2 mb-2">
          <span class="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center text-xs font-bold">Q${idx + 1}</span>
          <h4 class="font-semibold text-slate-200 text-sm">${q.question}</h4>
        </div>
        <div class="space-y-2 mt-3">
          ${q.options.map((opt, optIdx) => `
            <label class="flex items-center gap-3 p-2.5 rounded-lg border border-slate-700 hover:bg-slate-700/50 cursor-pointer text-xs text-slate-300 transition-colors">
              <input type="radio" name="quiz-q-${idx}" value="${optIdx}" onchange="ModuleRAG.onQuizSelect(${idx}, ${optIdx}, ${q.correctIndex})" class="text-indigo-600 focus:ring-indigo-500">
              <span>${opt}</span>
            </label>
          `).join('')}
        </div>
        <div id="quiz-explanation-${idx}" class="mt-3 p-3 rounded-lg bg-indigo-950/60 border border-indigo-500/30 text-xs text-indigo-200 hidden">
          <strong>Explanation:</strong> ${q.explanation}
        </div>
      </div>
    `).join('');
  }

  function onQuizSelect(qIdx, selectedOpt, correctOpt) {
    const expEl = document.getElementById(`quiz-explanation-${qIdx}`);
    if (expEl) {
      expEl.classList.remove('hidden');
      if (selectedOpt === correctOpt) {
        expEl.className = 'mt-3 p-3 rounded-lg bg-emerald-950/60 border border-emerald-500/30 text-xs text-emerald-200';
        expEl.innerHTML = `<strong>Correct! 🎉</strong> ${selectedLecture.quiz[qIdx].explanation}`;
      } else {
        expEl.className = 'mt-3 p-3 rounded-lg bg-rose-950/60 border border-rose-500/30 text-xs text-rose-200';
        expEl.innerHTML = `<strong>Incorrect.</strong> ${selectedLecture.quiz[qIdx].explanation}`;
      }
    }
  }

  function renderSummary(lecture) {
    const summaryBox = document.getElementById('rag-summary-content');
    if (!summaryBox) return;

    summaryBox.innerHTML = `
      <div class="space-y-4 text-sm text-slate-300 leading-relaxed">
        <div class="p-4 bg-slate-800/80 border border-slate-700/60 rounded-xl">
          <h4 class="font-bold text-indigo-400 text-xs uppercase tracking-wider mb-1.5 flex items-center gap-2">
            <i data-lucide="book-open" class="w-4 h-4"></i> Comprehensive Abstract
          </h4>
          <p>${lecture.summary}</p>
        </div>
        <div class="p-4 bg-slate-800/80 border border-slate-700/60 rounded-xl">
          <h4 class="font-bold text-amber-400 text-xs uppercase tracking-wider mb-2 flex items-center gap-2">
            <i data-lucide="zap" class="w-4 h-4"></i> Key Multimodal Highlights
          </h4>
          <ul class="list-disc list-inside space-y-1.5 text-xs text-slate-300">
            <li>Interactive video synchronized with ${lecture.slides ? lecture.slides.length : 6} topic milestones.</li>
            <li>Clicking citations in Q&A seeks the video player automatically to that timestamp.</li>
            <li>Spaced repetition flashcards and AI test questions generated for active recall.</li>
          </ul>
        </div>
      </div>
    `;
    lucide.createIcons();
  }

  function switchRAGTab(tabName) {
    document.querySelectorAll('[data-rag-tab]').forEach(t => {
      if (t.getAttribute('data-rag-tab') === tabName) {
        t.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 text-white shadow-sm';
      } else {
        t.className = 'px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-slate-200 hover:bg-slate-800';
      }
    });

    ['qa', 'flashcards', 'quiz', 'summary'].forEach(view => {
      const el = document.getElementById(`rag-tab-view-${view}`);
      if (el) {
        if (view === tabName) el.classList.remove('hidden');
        else el.classList.add('hidden');
      }
    });
    lucide.createIcons();
  }

  function parseMarkdownAndLaTeX(text) {
    if (!text) return '';
    let parsed = text
      .replace(/### (.*?)\n/g, '<h3 class="text-base font-bold text-indigo-300 mt-3 mb-1.5">$1</h3>')
      .replace(/\*\*(.*?)\*\*/g, '<strong class="text-white font-semibold">$1</strong>')
      .replace(/`\[(.*?)\]`/g, '<span class="inline-flex items-center px-1.5 py-0.5 rounded bg-indigo-900/60 border border-indigo-500/30 text-indigo-300 font-mono text-xs cursor-pointer hover:bg-indigo-800" onclick="ModuleRAG.seekToTimestamp(\'$1\', 1)">[$1]</span>')
      .replace(/\n\n/g, '<br/><br/>');

    if (window.katex) {
      parsed = parsed.replace(/\$\$(.*?)\$\$/g, (match, expr) => {
        try {
          return `<div class="my-2 p-2 bg-slate-900/90 rounded-lg text-center overflow-x-auto">${katex.renderToString(expr, { displayMode: true, throwOnError: false })}</div>`;
        } catch (e) {
          return match;
        }
      });
      parsed = parsed.replace(/\$(.*?)\$/g, (match, expr) => {
        try {
          return `<span class="inline-block px-1 font-mono text-indigo-300">${katex.renderToString(expr, { displayMode: false, throwOnError: false })}</span>`;
        } catch (e) {
          return match;
        }
      });
    }

    return parsed;
  }

  return {
    init,
    seekToTimestamp,
    importYouTubeVideo,
    onQuizSelect,
    switchRAGTab
  };
})();

window.ModuleRAG = ModuleRAG;
