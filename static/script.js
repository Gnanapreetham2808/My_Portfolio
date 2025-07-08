// Toggle light/dark mode
function toggleMode() {
  document.body.classList.toggle("light-mode");
}

// Animate on scroll
const fadeIns = document.querySelectorAll('.fade-in, .slide-in, .scale-in');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animationPlayState = 'running';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeIns.forEach(el => {
  el.style.animationPlayState = 'paused';
  observer.observe(el);
});
