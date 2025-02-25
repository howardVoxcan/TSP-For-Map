def read_graph():
    n, m = map(int, input().split())
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1) 

    for _ in range(m):
        u, v, c = map(int, input().split())
        adj[u][v] += 1 
        cost[u][v] = c
        deg[u] += 1 

    return n, adj, cost, deg

def is_hamiltonian_graph(n, deg):
    return all(deg[u] >= 1 for u in range(1, n + 1))
