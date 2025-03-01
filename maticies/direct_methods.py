def gaussian_elimination(a, b):
    n = len(b)
    aug = [a[i] + [b[i]] for i in range(n)]
    
    for i in range(n):
        max_row = i
        max_value = abs(aug[i][i])
        for k in range(i + 1, n):
            if abs(aug[k][i]) > max_value:
                max_row = k
                max_value = abs(aug[k][i])

        aug[i], aug[max_row] = aug[max_row], aug[i]

        for j in range(i + 1, n):
            factor = aug[j][i] / aug[i][i]
            for k in range(i, n + 1):
                aug[j][k] -= factor * aug[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum1 = sum(aug[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (aug[i][-1] - sum1) / aug[i][i]

    return x


def determinant(matrix):
    matrix = [row[:] for row in matrix]
    
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)

    return det


def cramers_rule(a, b):
    a = [row[:] for row in a]
    b = b[:]

    n = len(b)
    det = determinant(a)
    if det == 0:
        raise ValueError("Determinant is zero.")

    x = [0] * n
    for i in range(n):
        a_copy = [row[:] for row in a]
        for j in range(n):
            a_copy[j][i] = b[j]
        x[i] = determinant(a_copy) / det

    return x


def gauss_jordan(a, b):
    n = len(a)
    aug = [ a[i] + [b[i]] for i in range(n) ]

    for i in range(n):
        max_row = i
        max_value = abs(aug[i][i])
        for k in range(i + 1, n):
            if abs(aug[k][i]) > max_value:
                max_row = k
                max_value = abs(aug[k][i])

        aug[i], aug[max_row] = aug[max_row], aug[i]

        pivot = aug[i][i]
        for j in range(len(aug[i])):
            aug[i][j] /= pivot

        for j in range(n):
            if i != j:
                factor = aug[j][i]
                for k in range(len(aug[j])):
                    aug[j][k] -= factor * aug[i][k]

    x = [aug[i][-1] for i in range(n)]

    return x




A = [
        [27, 6, -1],
        [1, 1, 54],
        [6, 15, 2]
    ]
b = [85, 110, 72]

print("Gaussian Elimination:", gaussian_elimination(A, b))
print("Cramer's Rule:", cramers_rule(A, b))
print("Gauss-Jordan Elimination:", gauss_jordan(A, b))
