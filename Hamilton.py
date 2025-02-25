import sys

def enter():
    n, m = map(int, input().split())
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)  # Bậc ra của từng đỉnh

    for _ in range(m):
        u, v, c = map(int, input().split())
        adj[u][v] += 1  # Chỉ xét cạnh có hướng từ u -> v
        cost[u][v] = c
        deg[u] += 1  # Tăng bậc ra của u

    return n, adj, cost, deg

def check_hamilton_graph(n, deg):
    return all(deg[u] >= 1 for u in range(1, n + 1))  # Mỗi đỉnh có ít nhất 1 cung ra

def print_hamilton_circuit(n, circuit, cost):
    total_cost = sum(cost[circuit[i]][circuit[i+1]] for i in range(1, n)) + cost[circuit[n]][circuit[1]]
    print(" ".join(map(str, circuit[1:n+1])) + f" {circuit[1]} - Cost: {total_cost}")

def find_hamilton_circuit(i, n, adj, cost, circuit, is_free):
    if i > n:
        if adj[circuit[n]][circuit[1]]:  # Kiểm tra xem có cung đi từ đỉnh cuối về đỉnh đầu không
            print_hamilton_circuit(n, circuit, cost)
        return

    for v in range(1, n + 1):
        if is_free[v] and adj[circuit[i - 1]][v]:  # Chỉ xét cung đi có hướng từ `circuit[i-1] -> v`
            circuit[i] = v
            is_free[v] = False
            find_hamilton_circuit(i + 1, n, adj, cost, circuit, is_free)
            is_free[v] = True

def solution(n, adj, cost, deg):
    is_free = [True] * (n + 1)
    circuit = [0] * (n + 1)
    circuit[1] = 1  # Bắt đầu từ đỉnh 1
    is_free[1] = False

    if not check_hamilton_graph(n, deg):
        print(0)
    else:
        find_hamilton_circuit(2, n, adj, cost, circuit, is_free)

def main():
    n, adj, cost, deg = enter()
    solution(n, adj, cost, deg)

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()