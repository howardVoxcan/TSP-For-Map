def print_hamilton_circuit(best_circuit, min_cost):
    """In chu trình Hamilton ngắn nhất tìm được."""
    if min_cost < float('inf'):
        print(" ".join(map(str, best_circuit)) + f" - Cost: {min_cost}")
    else:
        print(0)
