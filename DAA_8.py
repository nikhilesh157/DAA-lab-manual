import heapq
from itertools import permutations

INF = float('inf')

def reduce_matrix(mat):
    """Reduce matrix and return reduction cost"""
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min and row_min != INF:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min and col_min != INF:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost

def tsp_brute_force(cost, n):
    """Brute force implementation for TSP optimal path verification"""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        c = sum(cost[path[i]][path[i+1]] for i in range(n))
        if c < best_cost:
            best_cost = c
            best_path = path
    return best_path, best_cost

# --- Main Execution ---
# 5-City Cost Matrix (0-indexed: 0=A, 1=B, 2=C, 3=D, 4=E)
cost_matrix = [
    [INF, 20,  30,  10,  11],
    [15,  INF, 16,  4,   2],
    [3,   5,   INF, 2,   4],
    [19,  6,   18,  INF, 3],
    [16,  4,   7,   16,  INF]
]

n = len(cost_matrix)
city_names = ['A', 'B', 'C', 'D', 'E']

best_path, min_cost = tsp_brute_force(cost_matrix, n)
path_str = " -> ".join(city_names[i] for i in best_path)

print(f"Optimal TSP Tour: {path_str}")
print(f"Minimum Tour Cost: {min_cost}")