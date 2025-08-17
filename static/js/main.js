// --- Konami Code Easter Egg ---
document.addEventListener('DOMContentLoaded', () => {
    const konamiCode = [
        'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
        'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
        'b', 'a'
    ];
    let konamiIndex = 0;

    const konamiOverlay = document.getElementById('konami-overlay');
    const konamiText = document.getElementById('konami-text');

    document.addEventListener('keydown', (event) => {
        if (event.key === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                // Code entered successfully
                konamiOverlay.classList.remove('hidden');
                konamiText.classList.add('konami-active');
                konamiIndex = 0; // Reset for next time
            }
        } else {
            konamiIndex = 0; // Reset if wrong key is pressed
        }
    });

    // Hide the overlay when it's clicked
    konamiOverlay.addEventListener('click', () => {
        konamiOverlay.classList.add('hidden');
        konamiText.classList.remove('konami-active');
    });
});