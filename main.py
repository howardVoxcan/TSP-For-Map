import sys
from graph import read_graph, is_hamiltonian_graph
from hamilton import find_hamilton_circuit
from utils import print_hamilton_circuit

def main():
    n, adj, cost, deg = read_graph()
    
    if not is_hamiltonian_graph(n, deg):
        print(0)
        return

    min_cost = [float('inf')]  # Dùng list để giữ giá trị tối thiểu (vì Python không hỗ trợ tham chiếu biến kiểu int)
    best_circuit = []

    is_free = [True] * (n + 1)
    circuit = [0] * (n + 1)
    circuit[1] = 1  # Bắt đầu từ đỉnh 1
    is_free[1] = False

    find_hamilton_circuit(2, n, adj, cost, circuit, is_free, 0, min_cost, best_circuit)

    print_hamilton_circuit(best_circuit, min_cost[0])

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
