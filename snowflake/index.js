const santaImage = "./assets/santa.png";

// nested functions, because i didnt plan this out very well
function snowflake() {
  /**
   * @type {HTMLCanvasElement}
   */
  const canvas = document.getElementById("snowflake");
  const ctx = canvas.getContext("2d");

  const width = window.innerWidth;
  const height = window.innerHeight;

  canvas.width = width;
  canvas.height = height;

  const maxFlakes = 200;
  let flakes = [];

  for (let i = 0; i < maxFlakes; i++) {
    flakes.push({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() * 5 + 2,
      d: Math.random() + 1
    });
  }

  function drawFlakes() {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = "white"
    ctx.beginPath();
    for (let i = 0; i < maxFlakes; i++) {
      const f = flakes[i];
      ctx.moveTo(f.x, f.y);
      ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2, true);
    }
    ctx.fill();
    moveFlakes();
  }

  let angle = 0;

  function moveFlakes() {
    angle += 0.01;
    for (let i = 0; i < maxFlakes; i++) {
      const f = flakes[i];
      f.y += Math.pow(f.d, 2) + 1;
      f.x += Math.sin(angle) * 2;
      if (f.y > height) {
        flakes[i] = { x: Math.random() * width, y: 0, r: f.r, d: f.d };
      }
    }
  }

  drawFlakes();
  setInterval(drawFlakes, 25);
}

function santa() {
  const img = document.createElement("img");
  img.src = santaImage;
  img.style.position = "absolute";
  img.style.top = "0px";
  img.style.left = "0px";
  img.style.width = "200px";
  img.style.height = "200px";
  document.body.appendChild(img);

  // animate it by having santa slide across the screen
  let left = 0;
  let direction = 1;
  setInterval(() => {
    left += direction;
    img.style.left = `${left}px`;
    if (left > window.innerWidth - 200) {
      direction = -1;
    } else if (left < 0) {
      direction = 1;
    }
  }, 5);
}

function merryChrysler() {
  const possibleTexts = [
    "Merry Chrysler",
    "Merry Crisis",
    "Merry Chrimmas",
    "Merry Chrimus",
    "Merry Chrimms",
    "Merry Chrimbus",
    "Merry Chrimb",
    "Merry Chrim",
    "Murry Chrmis"
  ]
  // display merry chrysler in the middle of the canvas, transitioning between red and green text colour
  const h1 = document.createElement("h1");
  h1.innerText = possibleTexts[Math.floor(Math.random() * possibleTexts.length)];
  h1.style.position = "absolute";
  h1.style.top = `${window.innerHeight / 2}px`;
  h1.style.left = `${window.innerWidth / 2}px`;
  h1.style.transform = "translate(-50%, -50%)";
  h1.style.color = "red";
  document.body.appendChild(h1);

  // give it a nice transition
  h1.style.transition = "color 0.5s";

  let red = true;

  setInterval(() => {
    h1.innerText = possibleTexts[Math.floor(Math.random() * possibleTexts.length)];
    if (red) {
      h1.style.color = "green";
    } else {
      h1.style.color = "red";
    }
    red = !red;
  }, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
  snowflake();
  santa();
  merryChrysler();
});