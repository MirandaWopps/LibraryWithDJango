// JavaScript for carousel scroll buttons
document.querySelector('.next-btn').addEventListener('click', () => {
    document.querySelector('.carousel').scrollBy({
        left: 300,
        behavior: 'smooth'
    });
});

document.querySelector('.prev-btn').addEventListener('click', () => {
    document.querySelector('.carousel').scrollBy({
        left: -300,
        behavior: 'smooth'
    });
});
