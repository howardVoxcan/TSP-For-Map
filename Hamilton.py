from utils import print_hamilton_circuit

def find_hamilton_circuit(i, n, adj, cost, circuit, is_free, total_cost, min_cost, best_circuit):
    """Tìm tất cả chu trình Hamilton và ghi nhận chu trình ngắn nhất."""
    if i > n:
        if adj[circuit[n]][circuit[1]]:  # Kiểm tra xem có cạnh từ cuối về đầu
            total_cost += cost[circuit[n]][circuit[1]]
            if total_cost < min_cost[0]:  # Cập nhật chu trình tối ưu
                min_cost[0] = total_cost
                best_circuit[:] = circuit[1:n+1] + [circuit[1]]
        return

    for v in range(1, n + 1):
        if is_free[v] and adj[circuit[i - 1]][v]:  # Kiểm tra cạnh hợp lệ
            circuit[i] = v
            is_free[v] = False
            find_hamilton_circuit(i + 1, n, adj, cost, circuit, is_free, total_cost + cost[circuit[i-1]][v], min_cost, best_circuit)
            is_free[v] = True
