
# Maze Solver 🧩

This project implements a **Maze Solver** in Python using **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** strategies.  
The program takes in a maze defined in a `.txt` file and finds a path from the start point **A** to the goal **B**.  
It can also generate and display a visual solution as an image.

---

## 📌 Features
- Reads maze layout from a text file
- Validates maze (only one start `A` and one goal `B`)
- Uses **DFS (Stack Frontier)** or **BFS (Queue Frontier)** to find paths
- Prints maze solution in the terminal
- Exports a visual representation (`maze.png`) with:
  - 🟥 Start point (A)  
  - 🟩 Goal point (B)  
  - ⭐ Path solution  
  - 🔲 Walls and explored nodes

---

## 🛠 Requirements
- Python 3.x  
- [Pillow](https://pypi.org/project/pillow/) library for image generation  

Install dependencies:
```bash
python -m pip install pillow
````

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/maze-solver.git
cd maze-solver
```

2. Create a maze file, e.g. `maze.txt`:

```
##########
#A     #B#
# ####   #
#        #
##########
```

3. Run the solver:

```bash
python maze.py maze.txt
```

4. Output:

   * Solution printed in terminal
   * Image saved as **maze.png**
   * Image automatically opened in your default viewer

---

## 📷 Example

Terminal Output:

```
Maze:
A   █████
*   █   B
*   █    
****     
█████████
```

Generated Image:
➡️ `maze.png` will show start, goal, explored paths, and solution.

---

## 📂 Project Structure

```
maze-solver/
│-- maze.py        # Main program
│-- maze.txt       # Example maze input
│-- maze.png       # Generated solution image
│-- README.md      # Documentation
```

---

## 👨‍💻 Author

**Lewins Mureithi Nderitu**

* 📧 Email: [mureithilewins@gmail.com](mailto:mureithilewins@gmail.com)
* 📱 Phone: +254 112876340
* 🌍 GitHub: [King-luiz](https://github.com/King-luiz)

---

## 📝 License

This project is open-source and available under the **MIT License**.
---

👉 Do you want me to also add a **section explaining DFS vs BFS** (since your code has both `StackFrontier` and `QueueFrontier`)? That could make your repo look more professional.
```
