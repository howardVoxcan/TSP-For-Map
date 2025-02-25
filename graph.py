def read_graph():
    """Đọc dữ liệu đầu vào và khởi tạo ma trận kề, ma trận chi phí, bậc ra của đỉnh."""
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

def is_hamiltonian_graph(n, deg):
    """Kiểm tra xem đồ thị có đủ điều kiện để tồn tại chu trình Hamilton hay không."""
    return all(deg[u] >= 1 for u in range(1, n + 1))
