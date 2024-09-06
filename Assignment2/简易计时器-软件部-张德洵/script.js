let startTime;
let lastPause;
let timerInterval;
let elapsed = 0;

function startTimer() {
  if (!startTime) {
    startTime = new Date().getTime() - elapsed;
    lastPause = null;
  }
  if (!timerInterval) {
    if (lastPause) {
        startTime += new Date().getTime() - lastPause;
        lastPause = null;
    }
    timerInterval = setInterval(() => {
      elapsed = new Date().getTime() - startTime;
      updateTimerDisplay();
    }, 10);
  }
}

function pauseTimer() {
  clearInterval(timerInterval);
  timerInterval = null;
  lastPause = new Date().getTime();
}

function resetTimer() {
  clearInterval(timerInterval);
  timerInterval = null;
  startTime = null;
  elapsed = 0;
  updateTimerDisplay();
}

function updateTimerDisplay() {
  let time = new Date(elapsed);
  let hours = time.getUTCHours().toString().padStart(2, '0');
  let minutes = time.getUTCMinutes().toString().padStart(2, '0');
  let seconds = time.getUTCSeconds().toString().padStart(2, '0');
  document.getElementById('timer').textContent = `${hours}:${minutes}:${seconds}`;
}