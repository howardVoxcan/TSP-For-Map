# TSP Using Hamiltonian cycle

## 📌 Introduction
This program finds the shortest Hamiltonian cycle in a directed graph using a backtracking algorithm. A Hamiltonian cycle is a cycle that visits every vertex exactly once and returns to the starting point.

## 🛠 Directory Structure
```
hamilton_path/
│── main.py              # Run the main program
│── graph.py             # Handle input and graph processing
│── Hamilton.py          # Find the Hamiltonian cycle
│── utils.py             # Utility functions
│── README.md            # User guide
```

## ⚙ Installation and Running
### 1️⃣ Install Python Environment
The program runs on **Python 3.x**. If you don't have Python installed, download it from [python.org](https://www.python.org/).

### 2️⃣ Clone Repository
```sh
git clone <repository-link>
cd hamilton_path
```

### 3️⃣ Run the Program
```sh
python main.py
```

## 📥 Input
- The first line contains two integers:
  - `n`: Number of vertices
  - `m`: Number of edges (default is `n * (n - 1)`, meaning every vertex is connected in one direction)
- The next `m` lines each contain three integers:
  - `u`: Start vertex
  - `v`: End vertex
  - `c`: Cost from `u` to `v`

### 📝 Example Input
```
4 12
1 2 10
1 3 15
1 4 20
2 1 10
2 3 35
2 4 25
3 1 15
3 2 35
3 4 30
4 1 20
4 2 25
4 3 30
```

## 📤 Output
The program prints the shortest Hamiltonian cycle.

### 📝 Example Output
```
1 2 4 3 1 - Cost: 65
```
If there is no valid Hamiltonian cycle, the program outputs `0`.

## 🏗 How It Works
1. **`graph.py`**: Reads input data and validates the graph.
2. **`hamilton.py`**: Uses recursion to find all Hamiltonian cycles and selects the shortest one.
3. **`utils.py`**: Supports result printing.
4. **`main.py`**: Coordinates the entire program.

## 📌 Notes
- The program uses **backtracking**, so it may take a long time if the number of vertices is too large.
- You can optimize the algorithm using **branch and bound** or **dynamic programming**.
