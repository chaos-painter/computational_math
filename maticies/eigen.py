def qr_decomposition(a):
    n = len(a)
    q = [[0.0] * n for _ in range(n)]
    r = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = [a[i][j] for i in range(n)]
        for i in range(j):
            r[i][j] = sum(q[i][k] * a[k][j] for k in range(n))
            v = [v[k] - r[i][j] * q[i][k] for k in range(n)]
        r[j][j] = sum(v[k] ** 2 for k in range(n)) ** 0.5
        q[j] = [v[k] / r[j][j] for k in range(n)]

    q_transpose = [[q[i][j] for i in range(n)] for j in range(n)]

    return q_transpose, r


def matrix_multiply(a, b):
    n = len(a)
    result = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
    return result


def qr_algorithm(a, e, max_iter=1000):
    n = len(a)
    q_total = [[float(i == j) for j in range(n)] for i in range(n)]

    for _ in range(max_iter):
        q, r = qr_decomposition(a)
        a = matrix_multiply(r, q)
        q_total = matrix_multiply(q_total, q)
        if all(abs(a[i][j]) < e for i in range(1, n) for j in range(i)):
            return a, q_total

    raise ValueError("QR Algorithm failed.")


def eigenvalues(a, e):
    diag_matrix, _ = qr_algorithm(a, e)
    return [diag_matrix[i][i] for i in range(len(diag_matrix))]


def eigenvectors(a, e):
    _, q_total = qr_algorithm(a, e)
    return q_total



a = [[5, 4], [1, 2]]
e = float(input("Enter tolerance: "))


eigenvalues_result = eigenvalues(a, e)
eigenvectors_result = eigenvectors(a, e)

print("Eigenvalues:", eigenvalues_result)
print("Eigenvectors:")
for row in eigenvectors_result:
    print(row)

