// Module 3: AI Multi-Agent Interview & Placement Prep Hub
const ModuleInterview = (() => {
  let sessionId = null;
  let interviewHistory = [];
  let currentScores = {
    technicalDepth: 75,
    problemSolving: 80,
    communication: 70,
    culturalFit: 85,
    systemScalability: 72
  };
  let radarChart = null;
  let isVoiceRecognitionActive = false;
  let recognitionInstance = null;
  let isTTSVoiceEnabled = true;

  const defaultProblemCode = `# Live Whiteboard Coding Challenge: Maximum Subarray Problem (Kadane's Algorithm)
# Problem: Given an integer array nums, find the subarray with the largest sum and return its sum.

def max_sub_array(nums):
    if not nums:
        return 0
    
    current_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Test runner
sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Computed Max Subarray Sum:", max_sub_array(sample_array))
`;

  function init() {
    setupEventListeners();
    initRadarChart();
    initSpeechRecognition();
  }

  function setupEventListeners() {
    document.getElementById('interview-start-btn')?.addEventListener('click', startInterview);
    document.getElementById('interview-send-btn')?.addEventListener('click', sendCandidateAnswer);
    
    const ansInput = document.getElementById('interview-answer-input');
    if (ansInput) {
      ansInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
          e.preventDefault();
          sendCandidateAnswer();
        }
      });
    }

    // Voice Mic button
    document.getElementById('interview-mic-btn')?.addEventListener('click', toggleVoiceRecognition);
    
    // TTS Audio Toggle
    document.getElementById('interview-tts-toggle')?.addEventListener('click', () => {
      isTTSVoiceEnabled = !isTTSVoiceEnabled;
      const btn = document.getElementById('interview-tts-toggle');
      if (btn) {
        btn.innerHTML = isTTSVoiceEnabled ? 
          `<i data-lucide="volume-2" class="w-4 h-4 text-emerald-400"></i> Audio TTS On` : 
          `<i data-lucide="volume-x" class="w-4 h-4 text-slate-400"></i> Audio Muted`;
      }
      lucide.createIcons();
      window.showToast(`Agent voice synthesis ${isTTSVoiceEnabled ? 'enabled' : 'muted'}`, 'info');
    });

    // Code IDE Buttons
    document.getElementById('run-code-btn')?.addEventListener('click', runCandidateCode);
    document.getElementById('reset-code-btn')?.addEventListener('click', resetCandidateCode);
    document.getElementById('code-lang-select')?.addEventListener('change', onLanguageChange);

    // Resume Scan Modal
    document.getElementById('interview-open-resume-btn')?.addEventListener('click', () => {
      document.getElementById('resume-scan-modal')?.classList.remove('hidden');
    });
    document.getElementById('close-resume-modal-btn')?.addEventListener('click', () => {
      document.getElementById('resume-scan-modal')?.classList.add('hidden');
    });
    document.getElementById('submit-resume-scan-btn')?.addEventListener('click', scanResume);
  }

  function initRadarChart() {
    const ctx = document.getElementById('interview-radar-chart');
    if (!ctx) return;

    if (window.Chart) {
      radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
          labels: ['Technical Depth', 'Problem Solving', 'Communication', 'Cultural Fit', 'System Scalability'],
          datasets: [{
            label: 'Candidate Competency Profile',
            data: [75, 80, 70, 85, 72],
            backgroundColor: 'rgba(99, 102, 241, 0.25)',
            borderColor: '#6366f1',
            pointBackgroundColor: '#ec4899',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#ec4899',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
              grid: { color: 'rgba(255, 255, 255, 0.08)' },
              pointLabels: {
                color: '#94a3b8',
                font: { size: 10, weight: '600' }
              },
              ticks: {
                display: false,
                min: 0,
                max: 100
              }
            }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });
    }
  }

  function updateRadarChart(scores) {
    currentScores = { ...currentScores, ...scores };
    if (radarChart) {
      radarChart.data.datasets[0].data = [
        currentScores.technicalDepth || 75,
        currentScores.problemSolving || 80,
        currentScores.communication || 70,
        currentScores.culturalFit || 85,
        currentScores.systemScalability || 72
      ];
      radarChart.update();
    }

    // Update overall metric
    const avg = Math.round(
      (currentScores.technicalDepth + currentScores.problemSolving + currentScores.communication + currentScores.culturalFit + currentScores.systemScalability) / 5
    );
    const scoreBadge = document.getElementById('interview-overall-score');
    if (scoreBadge) scoreBadge.textContent = `${avg}/100`;
  }

  function initSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      recognitionInstance = new SpeechRecognition();
      recognitionInstance.continuous = false;
      recognitionInstance.interimResults = true;
      recognitionInstance.lang = 'en-US';

      recognitionInstance.onresult = (e) => {
        let transcript = '';
        for (let i = e.resultIndex; i < e.results.length; ++i) {
          transcript += e.results[i][0].transcript;
        }
        const input = document.getElementById('interview-answer-input');
        if (input) input.value = transcript;
      };

      recognitionInstance.onend = () => {
        isVoiceRecognitionActive = false;
        updateMicButtonState();
      };

      recognitionInstance.onerror = (err) => {
        console.warn('Speech recognition error:', err);
        isVoiceRecognitionActive = false;
        updateMicButtonState();
      };
    }
  }

  function toggleVoiceRecognition() {
    if (!recognitionInstance) {
      window.showToast('Speech recognition not supported in this browser. Please type your answer.', 'warning');
      return;
    }

    if (isVoiceRecognitionActive) {
      recognitionInstance.stop();
      isVoiceRecognitionActive = false;
    } else {
      recognitionInstance.start();
      isVoiceRecognitionActive = true;
      window.showToast('Listening... Speak your answer into your microphone.', 'info');
    }
    updateMicButtonState();
  }

  function updateMicButtonState() {
    const btn = document.getElementById('interview-mic-btn');
    if (!btn) return;
    if (isVoiceRecognitionActive) {
      btn.className = 'p-2.5 rounded-xl bg-rose-600 text-white shadow-lg shadow-rose-600/30 animate-pulse';
    } else {
      btn.className = 'p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors';
    }
  }

  function speakText(text, agentName) {
    if (!isTTSVoiceEnabled || !window.speechSynthesis) return;

    window.speechSynthesis.cancel();
    // Clean markdown symbols for natural TTS speech
    const cleanText = text.replace(/[*#_`$]/g, '').replace(/\[.*?\]/g, '');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.rate = 1.05;

    if (agentName === 'Elena Vance') {
      utterance.pitch = 1.2;
    } else if (agentName === 'Marcus Thorne') {
      utterance.pitch = 0.85;
    } else if (agentName === 'Samira') {
      utterance.pitch = 1.1;
    } else {
      utterance.pitch = 0.95;
    }

    window.speechSynthesis.speak(utterance);
  }

  async function startInterview() {
    const role = document.getElementById('interview-role-select')?.value || 'Senior Full-Stack Engineer';
    const difficulty = document.getElementById('interview-difficulty-select')?.value || 'Senior';
    const name = document.getElementById('interview-candidate-name')?.value || 'Candidate';

    try {
      const res = await fetch('/api/interview/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role, difficulty, candidateName: name })
      });

      const data = await res.json();
      sessionId = data.sessionId;
      interviewHistory = [];

      // Update Agent Avatars UI
      highlightActiveAgent(data.initialMessage.agent);

      // Render Messages
      const container = document.getElementById('interview-chat-stream');
      if (container) {
        container.innerHTML = '';
        appendAgentMessage(data.initialMessage);
      }

      // Load code editor default
      const codeEditor = document.getElementById('interview-code-editor');
      if (codeEditor) codeEditor.value = defaultProblemCode;

      updateRadarChart(data.initialScores);
      speakText(data.initialMessage.content, data.initialMessage.agent);
      window.showToast(`Interview panel session initialized for ${role}`, 'success');

    } catch (err) {
      console.error('Failed to start interview:', err);
    }
  }

  async function sendCandidateAnswer() {
    const input = document.getElementById('interview-answer-input');
    const answer = input?.value.trim();
    if (!answer) return;

    input.value = '';
    appendCandidateMessage(answer);

    const role = document.getElementById('interview-role-select')?.value || 'Senior Full-Stack Engineer';
    const difficulty = document.getElementById('interview-difficulty-select')?.value || 'Senior';

    // Append loading placeholder
    const stream = document.getElementById('interview-chat-stream');
    const loadingId = 'agent-thinking-' + Date.now();
    if (stream) {
      const loadEl = document.createElement('div');
      loadEl.id = loadingId;
      loadEl.className = 'p-3 rounded-xl bg-slate-800/60 border border-slate-700 text-xs text-indigo-300 flex items-center gap-2 animate-pulse';
      loadEl.innerHTML = `<div class="w-3.5 h-3.5 border-2 border-indigo-400 border-t-transparent rounded-full animate-spin"></div> Interview panel is deliberating response...`;
      stream.appendChild(loadEl);
      stream.scrollTop = stream.scrollHeight;
    }

    try {
      const res = await fetch('/api/interview/turn', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessionId: sessionId || 'default-session',
          role: role,
          difficulty: difficulty,
          history: interviewHistory,
          userAnswer: answer
        })
      });

      document.getElementById(loadingId)?.remove();
      const data = await res.json();

      highlightActiveAgent(data.agent);
      appendAgentMessage(data);
      updateRadarChart(data.updatedScores);
      speakText(data.content, data.agent);

      // Update feedback box
      const feedbackEl = document.getElementById('interview-live-critique');
      if (feedbackEl) {
        feedbackEl.innerHTML = `
          <div class="p-3 bg-indigo-950/60 border border-indigo-500/30 rounded-xl text-xs text-indigo-200">
            <strong class="text-indigo-400 font-bold uppercase tracking-wider block mb-1">Interviewer Live Note:</strong>
            ${data.feedback}
          </div>
        `;
      }

    } catch (err) {
      document.getElementById(loadingId)?.remove();
      console.error('Turn error:', err);
    }
  }

  function appendCandidateMessage(text) {
    const stream = document.getElementById('interview-chat-stream');
    if (!stream) return;

    interviewHistory.push({ role: 'candidate', content: text });

    const msg = document.createElement('div');
    msg.className = 'flex items-start gap-3 justify-end';
    msg.innerHTML = `
      <div class="max-w-xl p-3.5 rounded-2xl rounded-tr-none bg-indigo-600 text-white text-xs leading-relaxed shadow-lg">
        <div class="flex items-center justify-between text-[10px] text-indigo-200 mb-1 font-semibold">
          <span>Candidate (You)</span>
          <span>${new Date().toLocaleTimeString()}</span>
        </div>
        <p>${text.replace(/\n/g, '<br/>')}</p>
      </div>
      <div class="w-8 h-8 rounded-full bg-indigo-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-md">
        You
      </div>
    `;

    stream.appendChild(msg);
    stream.scrollTop = stream.scrollHeight;
  }

  function appendAgentMessage(agentData) {
    const stream = document.getElementById('interview-chat-stream');
    if (!stream) return;

    interviewHistory.push({ role: 'interviewer', agent: agentData.agent, content: agentData.content });

    const msg = document.createElement('div');
    msg.className = 'flex items-start gap-3';
    msg.innerHTML = `
      <div class="w-8 h-8 rounded-full bg-slate-800 border border-indigo-500/60 text-indigo-300 flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-md">
        ${agentData.agent.charAt(0)}
      </div>
      <div class="max-w-xl p-3.5 rounded-2xl rounded-tl-none bg-slate-800/90 border border-slate-700/80 text-slate-200 text-xs leading-relaxed shadow-lg">
        <div class="flex items-center justify-between text-[10px] text-indigo-400 mb-1.5 font-bold">
          <span>${agentData.agent} (${agentData.role})</span>
          <span class="font-mono text-slate-500">${agentData.timestamp || new Date().toLocaleTimeString()}</span>
        </div>
        <div class="space-y-2 text-slate-300">${parseAgentMarkdown(agentData.content)}</div>
      </div>
    `;

    stream.appendChild(msg);
    stream.scrollTop = stream.scrollHeight;
  }

  function highlightActiveAgent(agentName) {
    document.querySelectorAll('.agent-card').forEach(card => {
      const name = card.getAttribute('data-agent-name');
      const wave = card.querySelector('.waveform-container');
      if (name === agentName) {
        card.classList.add('border-indigo-500', 'bg-indigo-950/40', 'scale-[1.02]');
        card.classList.remove('border-slate-700/60');
        if (wave) wave.classList.remove('hidden');
      } else {
        card.classList.remove('border-indigo-500', 'bg-indigo-950/40', 'scale-[1.02]');
        card.classList.add('border-slate-700/60');
        if (wave) wave.classList.add('hidden');
      }
    });
  }

  async function runCandidateCode() {
    const code = document.getElementById('interview-code-editor')?.value || '';
    const lang = document.getElementById('code-lang-select')?.value || 'python';
    const outputEl = document.getElementById('code-output-terminal');

    if (outputEl) {
      outputEl.innerHTML = `<span class="text-indigo-400 animate-pulse">Compiling & executing sandboxed test suites...</span>`;
    }

    try {
      const res = await fetch('/api/interview/evaluate-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language: lang, code: code })
      });

      const data = await res.json();
      if (outputEl) {
        outputEl.innerHTML = `
          <div class="text-emerald-400 font-bold mb-1">Status: ${data.status} • Complexity: ${data.complexity}</div>
          <div class="text-slate-300 font-mono text-[11px] whitespace-pre-wrap">${data.output}</div>
          <div class="mt-2 text-indigo-300 text-[11px] border-t border-slate-700 pt-1.5"><strong>Interviewer Review:</strong> ${data.interviewerReview}</div>
        `;
      }
      window.showToast('Code evaluation passed successfully!', 'success');
    } catch (err) {
      if (outputEl) outputEl.innerHTML = `<span class="text-rose-400">Execution Error: ${err.message}</span>`;
    }
  }

  function resetCandidateCode() {
    const codeEditor = document.getElementById('interview-code-editor');
    if (codeEditor) codeEditor.value = defaultProblemCode;
    window.showToast('IDE Whiteboard reset to standard template', 'info');
  }

  function onLanguageChange(e) {
    const lang = e.target.value;
    const codeEditor = document.getElementById('interview-code-editor');
    if (!codeEditor) return;

    if (lang === 'javascript') {
      codeEditor.value = `// JavaScript Solution: Maximum Subarray Problem\nfunction maxSubArray(nums) {\n  let currSum = nums[0];\n  let maxSum = nums[0];\n  for (let i = 1; i < nums.length; i++) {\n    currSum = Math.max(nums[i], currSum + nums[i]);\n    maxSum = Math.max(maxSum, currSum);\n  }\n  return maxSum;\n}\n\nconsole.log("Max Subarray Sum:", maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));`;
    } else if (lang === 'cpp') {
      codeEditor.value = `// C++ Solution: Maximum Subarray Problem\n#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint maxSubArray(std::vector<int>& nums) {\n    int currSum = nums[0];\n    int maxSum = nums[0];\n    for (size_t i = 1; i < nums.size(); ++i) {\n        currSum = std::max(nums[i], currSum + nums[i]);\n        maxSum = std::max(maxSum, currSum);\n    }\n    return maxSum;\n}\n\nint main() {\n    std::vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};\n    std::cout << "Max Sum: " << maxSubArray(nums) << std::endl;\n    return 0;\n}`;
    } else {
      codeEditor.value = defaultProblemCode;
    }
  }

  async function scanResume() {
    const text = document.getElementById('resume-text-input')?.value.trim();
    if (!text) {
      window.showToast('Please paste your resume text to scan.', 'warning');
      return;
    }

    try {
      const res = await fetch('/api/interview/resume-scan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resumeText: text })
      });

      const data = await res.json();
      const container = document.getElementById('resume-scan-results');
      if (container) {
        container.classList.remove('hidden');
        container.innerHTML = `
          <div class="p-4 bg-slate-800/90 border border-slate-700 rounded-xl space-y-3 text-xs">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-200">ATS Match Score:</span>
              <span class="text-sm font-black text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded-full border border-emerald-500/40">${data.atsScore}/100</span>
            </div>
            <div>
              <span class="text-slate-400 font-semibold block mb-1">Extracted Core Skills:</span>
              <div class="flex flex-wrap gap-1">
                ${data.extractedSkills.map(s => `<span class="px-2 py-0.5 rounded bg-indigo-900/60 border border-indigo-500/30 text-indigo-300 text-[10px] font-medium">${s}</span>`).join('')}
              </div>
            </div>
            <div>
              <span class="text-slate-400 font-semibold block mb-1">Tailored High-Probability Questions:</span>
              <ul class="list-disc list-inside space-y-1 text-slate-300">
                ${data.tailoredQuestions.map(q => `<li>${q}</li>`).join('')}
              </ul>
            </div>
          </div>
        `;
      }
      window.showToast('Resume ATS analysis complete! Tailored questions loaded.', 'success');
    } catch (err) {
      console.error('Resume scan error:', err);
    }
  }

  function parseAgentMarkdown(text) {
    if (!text) return '';
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong class="text-white font-semibold">$1</strong>')
      .replace(/`\$(.*?)\$`/g, '<span class="px-1 font-mono text-indigo-300">$$$1$$</span>')
      .replace(/`([a-zA-Z0-9_()]+)`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-900 text-indigo-300 font-mono text-[11px]">$1</code>');
  }

  return {
    init,
    startInterview,
    sendCandidateAnswer,
    runCandidateCode,
    resetCandidateCode
  };
})();

window.ModuleInterview = ModuleInterview;
