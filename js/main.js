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

// ===== 背景音樂播放器 =====
// 瀏覽器會阻擋完全沒有互動就自動播放有聲音的內容,
// 因此改為「使用者第一次與網頁互動時(點擊/捲動/按鍵)自動開始播放」,
// 這樣既符合瀏覽器政策,體驗上也幾乎等同於「一進站就播放」。
// 播放鍵仍保留,使用者隨時可以手動暫停/重新播放。
function initBgmPlayer() {
  const btn = document.getElementById('bgmToggle');
  const audio = document.getElementById('bgmAudio');
  if (!btn || !audio) return;

  const STORAGE_KEY = 'fangxin_bgm_playing';
  let autoplayAttempted = false;

  function setPlayingState(playing) {
    btn.classList.toggle('is-playing', playing);
    btn.setAttribute('aria-label', playing ? '暫停背景音樂' : '播放背景音樂');
  }

  // 使用者手動按播放鍵
  btn.addEventListener('click', () => {
    if (audio.paused) {
      audio.play().then(() => {
        setPlayingState(true);
        sessionStorage.setItem(STORAGE_KEY, '1');
      }).catch(() => {});
    } else {
      audio.pause();
      setPlayingState(false);
      sessionStorage.setItem(STORAGE_KEY, '0');
    }
  });

  // 使用者若明確按過暫停,就不要再自動幫他播放
  function userHasPaused() {
    return sessionStorage.getItem(STORAGE_KEY) === '0';
  }

  // 第一次互動(點擊/捲動/按鍵/觸控)時嘗試自動播放
  function tryAutoplayOnFirstInteraction() {
    if (autoplayAttempted || userHasPaused() || !audio.paused) return;
    autoplayAttempted = true;
    audio.play().then(() => {
      setPlayingState(true);
      sessionStorage.setItem(STORAGE_KEY, '1');
    }).catch(() => {
      // 少數情況仍可能被擋下,使用者可自行按播放鍵
      autoplayAttempted = false;
    });
  }

  // 第一次「有效使用者手勢」時嘗試自動播放
  // 注意:scroll(捲動)不算瀏覽器認可的使用者手勢,不能用來觸發帶聲音的播放,
  // 用它來觸發只會讓瀏覽器擋下嘗試、又白白耗掉唯一一次機會,故不列入
  const interactionEvents = ['click', 'keydown', 'touchend', 'pointerdown'];
  interactionEvents.forEach(evt => {
    window.addEventListener(evt, tryAutoplayOnFirstInteraction, { once: true, passive: true });
  });

  // 如果本次瀏覽已經在其他頁面播放過,切換頁面時延續播放狀態
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
