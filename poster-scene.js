const canvas = document.getElementById("scene");
const ctx = canvas.getContext("2d");
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

// Background gradient
const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
gradient.addColorStop(0, "#111");
gradient.addColorStop(1, "#333");
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, canvas.width, canvas.height);

// Comic-style edges
ctx.strokeStyle = "#ff00ff";
ctx.lineWidth = 12;
ctx.beginPath();
ctx.moveTo(10, 20);
ctx.lineTo(canvas.width - 20, 10);
ctx.lineTo(canvas.width - 10, canvas.height - 20);
ctx.lineTo(20, canvas.height - 10);
ctx.closePath();
ctx.stroke();

// Building on fire (aerial-diagonal)
ctx.save();
ctx.translate(260, 260);
ctx.rotate(-0.25);
ctx.fillStyle = "#444";
ctx.fillRect(-80, -40, 200, 260);
ctx.restore();

// Windows
ctx.fillStyle = "#222";
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 4; j++) {
    ctx.fillRect(220 + j * 40, 280 + i * 60, 25, 35);
  }
}

// Flames
ctx.fillStyle = "orange";
for (let i = 0; i < 20; i++) {
  ctx.beginPath();
  const x = 240 + Math.random() * 140;
  const y = 320 + Math.random() * 180;
  ctx.moveTo(x, y);
  ctx.quadraticCurveTo(x - 10, y - 30, x, y - 50);
  ctx.quadraticCurveTo(x + 10, y - 30, x, y);
  ctx.fill();
}

// Firetrucks
function drawTruck(x, y, angle) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle);
  ctx.fillStyle = "red";
  ctx.fillRect(-60, -25, 120, 50);
  ctx.fillStyle = "white";
  ctx.fillRect(-40, -15, 80, 30);
  ctx.fillStyle = "black";
  ctx.fillRect(-55, 15, 20, 10);
  ctx.fillRect(35, 15, 20, 10);
  ctx.restore();
}

drawTruck(140, 620, -0.3);
drawTruck(420, 660, -0.1);

// Ladder truck ladder
ctx.strokeStyle = "silver";
ctx.lineWidth = 4;
ctx.beginPath();
ctx.moveTo(420, 660);
ctx.lineTo(320, 420);
ctx.stroke();

// Firefighters
function drawFirefighter(x, y) {
  ctx.fillStyle = "yellow";
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI * 2);
  ctx.fill();

  ctx.strokeStyle = "orange";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(x, y + 10);
  ctx.lineTo(x, y + 30);
  ctx.moveTo(x, y + 30);
  ctx.lineTo(x - 8, y + 45);
  ctx.moveTo(x, y + 30);
  ctx.lineTo(x + 8, y + 45);
  ctx.moveTo(x, y + 18);
  ctx.lineTo(x - 10, y + 25);
  ctx.moveTo(x, y + 18);
  ctx.lineTo(x + 10, y + 25);
  ctx.stroke();
}

for (let i = 0; i < 6; i++) {
  drawFirefighter(180 + i * 40, 700 - i * 20);
}

// Water spray
ctx.strokeStyle = "cyan";
ctx.lineWidth = 3;
for (let i = 0; i < 6; i++) {
  ctx.beginPath();
  const sx = 180 + i * 40;
  const sy = 700 - i * 20;
  const ex = 260 + i * 20;
  const ey = 420 + i * 10;
  ctx.moveTo(sx, sy);
  ctx.quadraticCurveTo((sx + ex) / 2, sy - 60, ex, ey);
  ctx.stroke();
}

// Colorful comic edges
const colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff"];
for (let i = 0; i < 5; i++) {
  ctx.strokeStyle = colors[i];
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(10 + i * 5, 10 + i * 5);
  ctx.lineTo(canvas.width - 10 - i * 5, 10 + i * 5);
  ctx.lineTo(canvas.width - 10 - i * 5, canvas.height - 10 - i * 5);
  ctx.lineTo(10 + i * 5, canvas.height - 10 - i * 5);
  ctx.closePath();
  ctx.stroke();
}
