def matrix_chain_order(p):
    """
    Computes the optimal order of scalar multiplications using DP.
    p: List of dimensions where Matrix i has dimension p[i-1] x p[i]
    """
    n = len(p) - 1
    # m[i][j] stores minimum number of scalar multiplications
    m = [[0] * (n + 1) for _ in range(n + 1)]
    # s[i][j] stores the optimal split point k
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    """Prints optimal parenthesization of matrices"""
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# --- Main Execution ---
# Matrices: A1(10x30), A2(30x5), A3(5x60), A4(60x10)
p = [10, 30, 5, 60, 10]
n = len(p) - 1

m, s = matrix_chain_order(p)

print(f"Dimensions: {p}")
print(f"Minimum number of scalar multiplications: {m[1][n]}")
print("Optimal Parenthesization: ", end="")
print_optimal_parens(s, 1, n)
print()