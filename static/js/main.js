// static/js/main.js

// --- Konami Code Easter Egg with Keyboard "Character Collector" Game v2 ---
document.addEventListener('DOMContentLoaded', () => {
    const konamiCode = [
        'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
        'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'
    ];
    let konamiIndex = 0;
    let matrixInterval = null;
    let isGameActive = false;

    // MOVED: alphabet is now in the main scope so our keydown listener can access it
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    const konamiOverlay = document.getElementById('konami-overlay');
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    const gameInfo = document.getElementById('game-info');

    let score = 0;
    let targets = [];

    const startMatrix = () => {
        isGameActive = true;
        score = 0;
        targets = [];
        gameInfo.innerText = "Score: 0";
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const fontSize = 20;
        const columns = Math.floor(canvas.width / fontSize);
        const rainDrops = Array.from({ length: columns }).fill(1);

        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.font = fontSize + 'px monospace';
            ctx.fillStyle = '#04D9FF';
            for (let i = 0; i < rainDrops.length; i++) {
                const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
                ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    rainDrops[i] = 0;
                }
                rainDrops[i]++;
            }
            if (Math.random() < 0.03) {
                targets.push({
                    char: alphabet.charAt(Math.floor(Math.random() * alphabet.length)),
                    x: Math.floor(Math.random() * columns) * fontSize,
                    y: 0
                });
            }
            ctx.fillStyle = '#F472B6';
            targets = targets.filter(target => {
                ctx.fillText(target.char, target.x, target.y);
                target.y += fontSize;
                return target.y < canvas.height;
            });
        };
        if (matrixInterval) clearInterval(matrixInterval);
        matrixInterval = setInterval(draw, 50);
    };

    const stopMatrix = () => {
        isGameActive = false;
        if (matrixInterval) clearInterval(matrixInterval);
        matrixInterval = null;
    };

    document.addEventListener('keydown', (event) => {
        if (isGameActive) {
            const keyPressed = event.key.toUpperCase();
            let hit = false;
            
            // Only process valid alphanumeric keys for the game
            if (alphabet.includes(keyPressed)) {
                for (let i = targets.length - 1; i >= 0; i--) {
                    if (targets[i].char === keyPressed) {
                        targets.splice(i, 1);
                        score += 10;
                        hit = true;
                        break;
                    }
                }

                // NEW: If it was a valid key but didn't hit anything, apply a penalty.
                if (!hit) {
                    score -= 5;
                }
                
                gameInfo.innerText = `Score: ${score}`;
            }
            
            if (hit) return;
        }

        // Konami Code Logic
        if (event.key === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                konamiOverlay.classList.remove('hidden');
                startMatrix();
                konamiIndex = 0;
            }
        } else {
            konamiIndex = 0;
        }
    });

    konamiOverlay.addEventListener('click', () => {
        konamiOverlay.classList.add('hidden');
        stopMatrix();
    });
});