# 🏓 Pong Game – Python & Turtle

A classic two-player Pong game built with Python's `turtle` module, using Object-Oriented Programming principles.

---

## 📖 Project Overview

A faithful recreation of the arcade classic Pong. Two players compete on the same keyboard — one controlling the left paddle, the other the right. The ball speeds up with every successful hit, making each rally more intense.

---

## 🚀 Key Features

- 🎮 **Two-Player Local Multiplayer** – both players share the same keyboard
- ⚡ **Dynamic Difficulty** – ball accelerates with each paddle hit
- 🏆 **Live Scoreboard** – scores update in real time on screen
- 🔄 **Automatic Ball Reset** – ball resets to center after each point
- 🧱 **Wall & Paddle Collision Detection** – smooth and responsive bouncing

---

## 🛠️ Technologies Used

- **Python 3** – game logic and OOP structure
- **Turtle** – graphics and animation
- **OOP** – separate classes for Ball, Paddle, and Scoreboard

---

## 📂 Project Structure
```
/Pong_Game
├── main.py         # Game loop, collision detection, score tracking
├── ball.py         # Ball class – movement and bouncing
├── paddle.py       # Paddle class – position and controls
├── scoreboard.py   # Scoreboard class – score display and updates


---

## 🧠 How It Works

- The ball starts in the center and moves diagonally
- Each time a paddle returns the ball, `time.sleep()` decreases — the ball moves faster
- If the ball passes a paddle and crosses the screen edge, the opponent scores a point and the ball resets
- The game runs indefinitely until the window is closed
