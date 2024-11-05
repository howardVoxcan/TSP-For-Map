import networkx as nx
import osmnx as ox

ox.config(use_cache=True, log_console=False)

# Hàm nhập tọa độ từ người dùng
def input_coordinates():
    coordinates = []
    n = int(input("Nhập số lượng địa điểm: "))
    for i in range(n):
        coord_type = input(f"Nhập 'a' nếu nhập địa chỉ hoặc 'c' nếu nhập tọa độ cho địa điểm {i + 1}: ").lower()
        if coord_type == 'c':
            lat = float(input("Nhập vĩ độ: "))
            lon = float(input("Nhập kinh độ: "))
            coordinates.append((lat, lon))
        else:
            address = input("Nhập địa chỉ: ")
            location = ox.geocode(address)
            coordinates.append((location[1], location[0]))  # đảo ngược thứ tự
    return coordinates

# Hàm tính tổng khoảng cách của một đường đi
def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Quay lại điểm đầu
    return total_distance

# Thuật toán Nearest Neighbor để tìm đường đi
def tsp_nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    path = [0]  # Bắt đầu từ địa điểm đầu tiên
    total_distance = 0

    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        total_distance += distance_matrix[last][next_city]
        path.append(next_city)
        unvisited.remove(next_city)

    total_distance += distance_matrix[path[-1]][path[0]]  # Quay lại điểm đầu
    path.append(0)
    return path, total_distance

# Hàm chính
coordinates = input_coordinates()

# Xác định ranh giới của tọa độ để tạo đồ thị
latitudes = [coord[0] for coord in coordinates]
longitudes = [coord[1] for coord in coordinates]
bbox = (max(latitudes), min(latitudes), max(longitudes), min(longitudes))

# Tạo đồ thị đường đi trong khu vực xác định
G = ox.graph_from_bbox(*bbox, network_type='all_private')

# Tìm các node gần nhất với tọa độ đã nhập
nodes = [ox.distance.nearest_nodes(G, lon, lat) for lat, lon in coordinates]

# Xây dựng ma trận khoảng cách giữa các điểm
distance_matrix = nx.floyd_warshall_numpy(G, nodelist=nodes)

# Chạy thuật toán
best_path, min_distance = tsp_nearest_neighbor(distance_matrix)

# In kết quả
print("Optimal Path (Nearest Neighbor):", best_path)
print("Minimum Distance:", min_distance / 1000, "km")  # chuyển sang km
