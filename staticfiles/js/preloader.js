// Make a function that gets rid of the preloader

window.addEventListener('load', () => {
    const preLoader = document.querySelector('.preload');
    preLoader.classList.add('preload-finished');
});