document.addEventListener('DOMContentLoaded', function() {
    let timer;
    let timeLeft;
    let isPaused = false;

    const timeInput = document.getElementById('timeInput');
    const display = document.getElementById('display');
    const startButton = document.getElementById('startButton');
    const pauseButton = document.getElementById('pauseButton');
    const resetButton = document.getElementById('resetButton');

    startButton.addEventListener('click', startTimer);
    pauseButton.addEventListener('click', pauseTimer);
    resetButton.addEventListener('click', resetTimer);

    function startTimer() {
        if (timer) clearInterval(timer);
        if (!isPaused) {
            timeLeft = parseInt(timeInput.value);
        }
        isPaused = false;
        timer = setInterval(updateTimer, 1000);
    }

    function pauseTimer() {
        isPaused = true;
        clearInterval(timer);
    }

    function resetTimer() {
        clearInterval(timer);
        timeLeft = 0;
        display.textContent = '00:00';
        timeInput.value = '';
    }

    function updateTimer() {
        if (timeLeft <= 0) {
            clearInterval(timer);
            alert('时间到！');
            return;
        }
        timeLeft--;
        display.textContent = formatTime(timeLeft);
    }

    function formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }
});