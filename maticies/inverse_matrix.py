def inverse(a):
    n = len(a)

    id = [[float(i == j) for j in range(n)] for i in range(n)]
    aug = [a[i] + id[i] for i in range(n)]

    for i in range(n):
        max_row = i
        max_value = abs(aug[i][i])
        for k in range(i + 1, n):
            if abs(aug[k][i]) > max_value:
                max_value = abs(aug[k][i])
                max_row = k
        
        aug[i], aug[max_row] = aug[max_row], aug[i]
        pivot = aug[i][i]

        for j in range(len(aug[i])):
            aug[i][j] /= pivot
        
        for j in range(n):
            if i != j:
                factor = aug[j][i]
                for k in range(len(aug[j])):
                    aug[j][k] -= factor * aug[i][k]

    inverse = [row[n:] for row in aug]

    return inverse


A = [[1, 1/2],
     [1/2, 1/3]]

for i in range(len(A)):
    print(inverse(A)[i])
