// ===== 共用工具:載入 CMS 管理的 JSON 內容 =====
async function loadJSON(path) {
  try {
    const res = await fetch(path, { cache: 'no-store' });
    if (!res.ok) throw new Error('無法載入內容: ' + path);
    return await res.json();
  } catch (err) {
    console.error(err);
    return null;
  }
}

// ===== 手機版導覽選單開關 =====
function initNavToggle() {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (!toggle || !links) return;
  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
  });
  links.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => links.classList.remove('open'));
  });
}

// ===== 目前頁面導覽列反白 =====
function markActiveNav() {
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === current) a.classList.add('active');
  });
}

// ===== 捲動出現動畫 =====
function initRevealOnScroll() {
  const items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || items.length === 0) {
    items.forEach(el => el.classList.add('visible'));
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  items.forEach(el => observer.observe(el));
}

// ===== 背景音樂播放器(手動播放鍵,不自動播放) =====
function initBgmPlayer() {
  const btn = document.getElementById('bgmToggle');
  const audio = document.getElementById('bgmAudio');
  if (!btn || !audio) return;

  // 記住使用者在本次瀏覽中的播放狀態(跨頁面),但絕不自動播放,需使用者主動按過一次
  const STORAGE_KEY = 'fangxin_bgm_playing';

  function setPlayingState(playing) {
    btn.classList.toggle('is-playing', playing);
    btn.setAttribute('aria-label', playing ? '暫停背景音樂' : '播放背景音樂');
  }

  btn.addEventListener('click', () => {
    if (audio.paused) {
      audio.play().then(() => {
        setPlayingState(true);
        sessionStorage.setItem(STORAGE_KEY, '1');
      }).catch(() => {
        // 瀏覽器阻擋自動播放等情況
      });
    } else {
      audio.pause();
      setPlayingState(false);
      sessionStorage.setItem(STORAGE_KEY, '0');
    }
  });

  // 只有使用者「這次瀏覽中已經手動按過播放」,切換頁面才延續播放狀態
  if (sessionStorage.getItem(STORAGE_KEY) === '1') {
    audio.play().then(() => setPlayingState(true)).catch(() => setPlayingState(false));
  } else {
    setPlayingState(false);
  }
}

// ===== 頁尾年份自動帶入 =====
function initFooterYear() {
  const el = document.getElementById('footerYear');
  if (el) el.textContent = new Date().getFullYear();
}

document.addEventListener('DOMContentLoaded', () => {
  initNavToggle();
  markActiveNav();
  initRevealOnScroll();
  initBgmPlayer();
  initFooterYear();
});
