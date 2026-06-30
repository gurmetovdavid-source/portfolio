document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('js-enabled');

  // Mobile menu
  const menuBtn = document.createElement('button');
  menuBtn.className = 'mobile-menu-btn';
  menuBtn.innerHTML = '☰';
  menuBtn.setAttribute('aria-label', 'Open menu');
  const headerInner = document.querySelector('.dental-header-inner');
  const nav = document.querySelector('.dental-nav');
  headerInner.insertBefore(menuBtn, nav.nextSibling);

  menuBtn.setAttribute('aria-expanded', 'false');

  menuBtn.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    menuBtn.innerHTML = isOpen ? '✕' : '☰';
    menuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    menuBtn.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
  });

  document.querySelectorAll('.dental-nav a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      menuBtn.innerHTML = '☰';
      menuBtn.setAttribute('aria-expanded', 'false');
      menuBtn.setAttribute('aria-label', 'Open menu');
    });
  });

  // Appointment form
  const form = document.getElementById('appointmentForm');
  const modal = document.getElementById('successModal');
  const closeModal = document.getElementById('closeModal');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    const data = Object.fromEntries(new FormData(form).entries());
    console.log('Appointment request:', data);
    modal.classList.add('active');
    form.reset();
  });

  closeModal.addEventListener('click', () => {
    modal.classList.remove('active');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });

  // Scroll reveal animations
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal, .stagger-children').forEach(el => observer.observe(el));
});
