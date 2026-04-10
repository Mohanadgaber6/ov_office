// ========================
// OV_OFFICE - script.js
// Google Sheets Integration
// ========================

// ============================================================
// ⚠️ ضع هنا رابط Google Apps Script بعد النشر
// تعليمات في ملف: google_apps_script.gs
// ============================================================
const GOOGLE_SHEET_URL = 'https://script.google.com/macros/s/AKfycbyz79DtWi5kHLX4fbOHnyRF7JC86ayIvMUbz5Bs8zjDWK_p_Rjkd-OAUoTYa823wFh2/exec'; // ← ضع الـ URL هنا


// ---- NAVBAR scroll effect ----
const navbar       = document.getElementById('navbar');
const scrollTopBtn = document.getElementById('scrollTop');

window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
    scrollTopBtn.classList.add('show');
  } else {
    navbar.classList.remove('scrolled');
    scrollTopBtn.classList.remove('show');
  }
}, { passive: true });

scrollTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ---- HAMBURGER menu ----
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    navLinks.classList.remove('open');
  });
});

// ---- SCROLL ANIMATIONS ----
const fadeEls = document.querySelectorAll(
  '.section-badge, .section-title, .about-body, .goal-box, .big-circle-card, ' +
  '.why-item, .srv-card, .srv-detail-content, .srv-detail-title-card, ' +
  '.ci-item, .contact-form-wrap, .contact-info h3, .pkg-card'
);

fadeEls.forEach(el => el.classList.add('fade-up'));

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

fadeEls.forEach(el => observer.observe(el));

// Stagger delays
document.querySelectorAll('.why-item').forEach((item, i) => {
  item.style.transitionDelay = `${i * 80}ms`;
});
document.querySelectorAll('.srv-card').forEach((card, i) => {
  card.style.transitionDelay = `${i * 70}ms`;
});
document.querySelectorAll('.pkg-card').forEach((card, i) => {
  card.style.transitionDelay = `${i * 100}ms`;
});

// ---- CONTACT FORM ----
const form        = document.getElementById('contactForm');
const formSuccess = document.getElementById('formSuccess');
const submitBtn   = document.getElementById('submit-btn');
const btnText     = submitBtn.querySelector('.btn-text');

function validateForm() {
  let valid = true;
  ['f-name', 'f-phone', 'f-service'].forEach(id => {
    const el = document.getElementById(id);
    if (!el.value.trim()) {
      el.classList.add('error');
      el.addEventListener('input', () => el.classList.remove('error'), { once: true });
      valid = false;
    }
  });
  return valid;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (!validateForm()) return;

  // حالة التحميل
  btnText.textContent = '...جاري الإرسال';
  submitBtn.disabled = true;

  const now     = new Date();
  const payload = {
    name:    document.getElementById('f-name').value.trim(),
    phone:   document.getElementById('f-phone').value.trim(),
    email:   document.getElementById('f-email').value.trim() || '—',
    service: document.getElementById('f-service').value,
    message: document.getElementById('f-message').value.trim() || '—',
    date:    now.toLocaleDateString('ar-SA'),
    time:    now.toLocaleTimeString('ar-SA'),
  };

  // ---- إرسال إلى Google Sheets ----
  let saved = false;
  if (GOOGLE_SHEET_URL !== 'YOUR_GOOGLE_APPS_SCRIPT_URL') {
    try {
      const res = await fetch(GOOGLE_SHEET_URL, {
        method: 'POST',
        mode:   'no-cors',          // Google Apps Script يتطلب no-cors
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      saved = true;
    } catch (err) {
      console.error('خطأ في الإرسال:', err);
    }
  }

  // إعادة تعيين الزر
  btnText.textContent = 'إرسال الطلب';
  submitBtn.disabled  = false;

  // إظهار رسالة النجاح
  form.style.display = 'none';
  formSuccess.classList.add('show');
  form.reset();
});

// ---- ACTIVE NAV on scroll ----
const sections   = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 90) current = sec.getAttribute('id');
  });
  navAnchors.forEach(a => {
    a.style.color = a.getAttribute('href') === `#${current}` ? 'var(--teal-light)' : '';
  });
}, { passive: true });
