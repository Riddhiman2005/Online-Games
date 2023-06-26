var canvas = document.getElementById("snake");
var context = canvas.getContext("2d");

var game = {
  score: 0,
  highScore: 0,
  fps: 8,
  over: false,
  message: null,
  level: 1,
  maxLevel: 3,

  start: function () {
    game.over = false;
    game.message = null;
    game.score = 0;
    game.fps = 8;
    snake.init();
    food.set();
    game.level = 1;
  },

  stop: function () {
    game.over = true;
    game.message = "TAP TO PLAY";
    if (game.score > game.highScore) {
      game.highScore = game.score;
    }
  },

  drawBox: function (x, y, size, color) {
    context.fillStyle = color;
    context.beginPath();
    context.moveTo(x - size / 2, y - size / 2);
    context.lineTo(x + size / 2, y - size / 2);
    context.lineTo(x + size / 2, y + size / 2);
    context.lineTo(x - size / 2, y + size / 2);
    context.closePath();
    context.fill();
  },

  drawScore: function () {
    context.fillStyle = "#ddd";
    context.font = "36px Impact, Arial, sans-serif";
    context.textAlign = "center";
    context.fillText(
      "Score: " + game.score,
      canvas.width / 2,
      canvas.height * 0.9
    );
    context.fillText(
      "High Score: " + game.highScore,
      canvas.width / 2,
      canvas.height * 0.95
    );
  },

  drawMessage: function () {
    if (game.message !== null) {
      context.fillStyle = "#fff";
      context.font = (canvas.height / 10) + "px Impact, Arial, sans-serif";
      context.textAlign = "center";
      context.fillText(game.message, canvas.width / 2, canvas.height / 2);
    }
  },

  resetCanvas: function () {
    context.clearRect(0, 0, canvas.width, canvas.height);
  },

  levelComplete: function () {
    game.level++;
    if (game.level > game.maxLevel) {
      game.stop();
    } else {
      game.message =
        "Level " +
        game.level +
        " Complete! Next Level: " +
        (game.level + 1);
      setTimeout(function () {
        food.set();
        snake.init();
        game.message = null;
      }, 2000);
    }
  },
};

var snake = {
  size: canvas.width / 40,
  x: null,
  y: null,
  color: "#0F0",
  direction: "left",
  sections: [],

 init: function() {
  snake.sections = [];
  snake.direction = 'left';
  snake.x = canvas.width / 2 + snake.size / 2;
  snake.y = canvas.height / 2 + snake.size / 2;
  for (var i = snake.x + (5 * snake.size); i >= snake.x; i -= snake.size) {
    snake.sections.push(i + ',' + snake.y);
  }
},

  move: function () {
    var head;
    var tail;

    snake.sections.pop();
    head = snake.getNextSection();
    snake.sections.unshift(head);

    if (snake.isCollision(head)) {
      game.stop();
      return;
    }

    if (snake.eatsFood(head)) {
      game.score++;
      snake.sections.push(tail);
      food.set();
    }

    if (snake.eatsPowerUp(head)) {
      game.score += 5;
      powerUp.set();
    }

    if (snake.hitsObstacle(head)) {
      game.stop();
      return;
    }

    if (snake.sections.length > game.level + 5) {
      snake.sections.pop();
    }
  },

  getNextSection: function () {
    var head = snake.sections[0].split(",");
    var nx = parseInt(head[0]);
    var ny = parseInt(head[1]);

    switch (snake.direction) {
      case "up":
        ny -= snake.size;
        break;
      case "down":
        ny += snake.size;
        break;
      case "left":
        nx -= snake.size;
        break;
      case "right":
        nx += snake.size;
        break;
    }

    return nx + "," + ny;
  },

  draw: function () {
    for (var i = 0; i < snake.sections.length; i++) {
      snake.drawSection(snake.sections[i].split(","));
    }
  },

  drawSection: function (section) {
    game.drawBox(
      parseInt(section[0]),
      parseInt(section[1]),
      snake.size,
      snake.color
    );
  },

  isCollision: function (section) {
    var head = section.split(",");
    var nx = parseInt(head[0]);
    var ny = parseInt(head[1]);

    return (
      nx < snake.size / 2 ||
      nx > canvas.width ||
      ny < snake.size / 2 ||
      ny > canvas.height ||
      snake.sections.indexOf(section) >= 0
    );
  },

  eatsFood: function (head) {
    var foodPos = food.getPosition();
    return head === foodPos;
  },

  eatsPowerUp: function (head) {
    var powerUpPos = powerUp.getPosition();
    return head === powerUpPos;
  },

  hitsObstacle: function (head) {
    for (var i = 0; i < obstacle.positions.length; i++) {
      if (head === obstacle.positions[i]) {
        return true;
      }
    }
    return false;
  },

  setDirection: function (newDirection) {
    if (
      snake.direction === "up" &&
      newDirection === "down" ||
      snake.direction === "down" &&
      newDirection === "up" ||
      snake.direction === "left" &&
      newDirection === "right" ||
      snake.direction === "right" &&
      newDirection === "left"
    ) {
      return;
    }
    snake.direction = newDirection;
  },
};

var food = {
  size: null,
  x: null,
  y: null,
  color: "#0F0",

  set: function () {
    food.size = snake.size;
    food.x =
      Math.floor(Math.random() * (canvas.width / snake.size)) *
      snake.size;
    food.y =
      Math.floor(Math.random() * (canvas.height / snake.size)) *
      snake.size;
  },

  getPosition: function () {
    return food.x + "," + food.y;
  },

  draw: function () {
    game.drawBox(food.x, food.y, food.size, food.color);
  },
};

var obstacle = {
  size: null,
  positions: [],
  color: "#F00",

  generate: function () {
    obstacle.size = snake.size;
    obstacle.positions = [];
    var numObstacles = Math.floor(Math.random() * 4) + 1;

    for (var i = 0; i < numObstacles; i++) {
      var x =
        Math.floor(Math.random() * (canvas.width / snake.size)) *
        snake.size;
      var y =
        Math.floor(Math.random() * (canvas.height / snake.size)) *
        snake.size;
      var position = x + "," + y;

      if (
        position !== food.getPosition() &&
        snake.sections.indexOf(position) === -1
      ) {
        obstacle.positions.push(position);
      }
    }
  },

  draw: function () {
    for (var i = 0; i < obstacle.positions.length; i++) {
      var pos = obstacle.positions[i].split(",");
      game.drawBox(
        parseInt(pos[0]),
        parseInt(pos[1]),
        obstacle.size,
        obstacle.color
      );
    }
  },
};

var powerUp = {
  size: null,
  x: null,
  y: null,
  color: "#FF0",
  active: false,

  set: function () {
    powerUp.size = snake.size;
    powerUp.x =
      Math.floor(Math.random() * (canvas.width / snake.size)) *
      snake.size;
    powerUp.y =
      Math.floor(Math.random() * (canvas.height / snake.size)) *
      snake.size;
    powerUp.active = true;

    setTimeout(function () {
      powerUp.active = false;
      setTimeout(function () {
        powerUp.set();
      }, 5000);
    }, 10000);
  },

  getPosition: function () {
    return powerUp.x + "," + powerUp.y;
  },

  draw: function () {
    if (powerUp.active) {
      game.drawBox(powerUp.x, powerUp.y, powerUp.size, powerUp.color);
    }
  },
};

var keys = {
  up: [38, 75, 87],
  down: [40, 74, 83],
  left: [37, 65, 72],
  right: [39, 68, 76],
  start_game: [13, 32],
};

Object.prototype.getKey = function (value) {
  for (var key in this) {
    if (
      this[key] instanceof Array &&
      this[key].indexOf(value) >= 0
    ) {
      return key;
    }
  }
  return null;
};

function isTouchDevice() {
  return "ontouchstart" in document.documentElement;
}

if (isTouchDevice()) {
  addEventListener("touchstart", handleEvent, false);
} else {
  addEventListener("keydown", function (e) {
    var lastKey = keys.getKey(e.keyCode);
    if (
      ["up", "down", "left", "right"].indexOf(lastKey) >= 0 &&
      lastKey != inverseDirection[snake.direction]
    ) {
      snake.setDirection(lastKey);
    } else if (
      ["start_game"].indexOf(lastKey) >= 0 &&
      game.over
    ) {
      game.start();
    }
  }, false);
  addEventListener("click", handleEvent, false);
}

function handleEvent(e) {
  e.stopPropagation();

  if (game.over) {
    game.start();
  }

  if (snake.direction === "left") {
    snake.setDirection("down");
  } else if (snake.direction === "down") {
    snake.setDirection("right");
  } else if (snake.direction === "right") {
    snake.setDirection("up");
  } else if (snake.direction === "up") {
    snake.setDirection("left");
  }
}

var requestAnimationFrame =
  window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.oRequestAnimationFrame ||
  window.msRequestAnimationFrame ||
  function (callback) {
    window.setTimeout(callback, 1000 / 60);
  };

function loop() {
  if (game.over) {
    game.drawMessage();
  } else {
    game.resetCanvas();
    game.drawScore();
    snake.move();
    food.draw();
    obstacle.draw();
    powerUp.draw();
    snake.draw();
  }
  setTimeout(function () {
    requestAnimationFrame(loop);
  }, 1000 / game.fps);
}

requestAnimationFrame(loop);
