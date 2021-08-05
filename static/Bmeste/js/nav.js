const toggleBtn = document.querySelector('.navbar_toggleBtn');
const nav = document.querySelector('.site-nav');
const mask = document.querySelector('.mask');

toggleBtn.addEventListener('click', () => {
    nav.classList.toggle('active');
    mask.classList.toggle('active');
});