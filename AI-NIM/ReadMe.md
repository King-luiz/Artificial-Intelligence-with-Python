
# 🧠 Nim Game with Q-Learning AI

A Python implementation of the **Nim game** with a self-learning **AI agent** powered by **Q-learning**.
The project demonstrates reinforcement learning principles, where the AI learns to play optimally through self-play.

---

## 🎮 Overview

This project simulates the classic **Nim Game**, a mathematical strategy game where players take turns removing objects from heaps.
In this version, **the player who removes the last object loses** (a misère version of Nim).

An **AI agent** (NimAI) uses **Q-learning** — a model-free reinforcement learning algorithm — to learn optimal strategies through thousands of self-play simulations.

---

## 🧩 Features

* ✅ Fully functional **Nim game engine**
* 🤖 **AI agent** that learns from experience
* 🧠 **Q-learning algorithm** implemented from scratch
* 🔁 **Self-training loop** for AI improvement
* 👤 Human vs. AI **interactive gameplay**
* 🧮 Configurable **learning rate (alpha)** and **exploration rate (epsilon)**

---

## 📚 How It Works

1. **Game Setup:**

   * Four piles: `[1, 3, 5, 7]`
   * Two players take turns removing 1 or more objects from a single pile.
   * The player who takes the **last object loses**.

2. **AI Training (Reinforcement Learning):**

   * The AI plays against itself for a number of games (`train(n)`).
   * Each game updates the Q-table (state-action values).
   * Rewards are assigned:

     * `+1` for winning
     * `-1` for losing
     * `0` for intermediate moves

3. **Gameplay:**

   * After training, you can play against the AI.
   * The AI uses **epsilon-greedy strategy**:

     * Explores random moves with probability ε (epsilon)
     * Chooses the best-known move otherwise

---

## ⚙️ Installation & Setup

### Prerequisites

Ensure you have **Python 3.7+** installed.

### Steps

```bash
# Clone this repository
git clone https://github.com/King-luiz/nim-ai-game.git

# Navigate to the project directory
cd nim-ai-game

# Run the program
python nim.py
```

---

## 🧠 Training the AI

You can modify the number of training games in the script:

```python
# Number of self-play games
n = 1000
ai = train(n)
```

Increasing `n` improves AI performance but takes longer.

---

## 🎮 Playing the Game

After training, you’ll play against the AI directly in the terminal:

```bash
python main.py
```

Example gameplay:

```
Training 1000 games...
Done training.
Piles:
  Pile 0: 1
  Pile 1: 3
  Pile 2: 5
  Pile 3: 7

Your turn.
Choose a pile: 2
How many to remove: 3

AI's turn.
AI chose to take 1 from pile 3.
...
Game over.
Winner: 1 (player who took the last object loses)
```

---

## 🧪 Project Structure

```
nim-ai-game/
│
├── nim.py         # Core Nim game logic and Q-learning AI
├── main.py        # Entry point to train and play the game
└── README.md      # Project documentation
```

---

## 🧮 Key Classes & Functions

### `class Nim`

Handles the game state, rules, and player moves.

* `available_actions(piles)` → Returns possible actions.
* `move(action)` → Applies a move and switches players.

### `class NimAI`

Implements the Q-learning algorithm.

* `get_q_value(state, action)`
* `update_q_value(state, action, old_q, reward, future_rewards)`
* `choose_action(state, epsilon=True)` → Chooses best or random move.

### Helper Functions

* `train(n)` → Trains the AI by self-play.
* `play(ai)` → Human vs AI gameplay session.

---

## 🧩 Concepts Applied

* **Q-Learning Algorithm:**
  ( Q(s, a) ← Q(s, a) + α[(r + γ * max_{a’} Q(s’, a’)) - Q(s, a)] )

* **Epsilon-Greedy Policy:**
  Balances exploration (trying new moves) and exploitation (using learned best moves).

* **Reinforcement Learning (RL):**
  AI learns optimal strategies through rewards and penalties over multiple episodes.

---

## 🧑‍💻 Author

**Lewins Mureithi Nderitu**
* ** 📧 Email: [mureithilewins@gmail.com](mailto:mureithilewins@gmail.com)
* ** 📞 Contact: +254 112876340
* ** 💻 GitHub: [King-luiz](https://github.com/King-luiz)

---

## 🏁 License

This project is open-source and available under the **MIT License**.

---
