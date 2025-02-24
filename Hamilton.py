import sys

def enter():
    n, m = map(int, input().split())
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u][v] += 1
        adj[v][u] += 1
        deg[u] += 1
        deg[v] += 1
    
    return n, adj, deg

def check_hamilton_graph(n, deg):
    return all(deg[u] >= 2 for u in range(1, n + 1))

def print_hamilton_circuit(n, circuit):
    print(" ".join(map(str, circuit[1:n+1])) + f" {circuit[1]}")

def find_hamilton_circuit(i, n, adj, circuit, is_free):
    for v in range(1, n + 1):
        if is_free[v] and adj[circuit[i - 1]][v]:
            circuit[i] = v
            if i < n:
                is_free[v] = False
                find_hamilton_circuit(i + 1, n, adj, circuit, is_free)
                is_free[v] = True
            elif adj[v][circuit[1]]:
                print_hamilton_circuit(n, circuit)

def solution(n, adj, deg):
    is_free = [True] * (n + 1)
    circuit = [0] * (n + 1)
    circuit[1] = 1
    
    if not check_hamilton_graph(n, deg):
        print(0)
    else:
        find_hamilton_circuit(2, n, adj, circuit, is_free)

def main():
    n, adj, deg = enter()
    solution(n, adj, deg)
    
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
