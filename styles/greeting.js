(() => {
  const lines = [
    "Hi there!",
    "I'm Ian Sequeira",
    "An AI Engineer",
    "Let's connect!",
    ];

  const el = document.getElementById("typing");
  if (!el) return;

  let lineIndex = 0;
  let charIndex = 0;
  let deleting = false;

  const TYPE_SPEED = 90;
  const DELETE_SPEED = 50;
  const HOLD_AFTER_TYPE = 1200;

  function loop() {
    const text = lines[lineIndex];

    if (!deleting) {
      el.textContent = text.slice(0, ++charIndex);

      if (charIndex === text.length) {
        setTimeout(() => deleting = true, HOLD_AFTER_TYPE);
      }
    } else {
      el.textContent = text.slice(0, --charIndex);

      if (charIndex === 0) {
        deleting = false;
        lineIndex = (lineIndex + 1) % lines.length;
      }
    }

    setTimeout(loop, deleting ? DELETE_SPEED : TYPE_SPEED);
  }

  loop();
})();