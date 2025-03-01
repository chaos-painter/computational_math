def jacobi(A, b, x0, e, max_iter):
    n = len(A)
    x = x0[:]
    x_vals = []
    for i in range(max_iter):
        xn = x[:]
        for j in range(n):
            sum1 = sum(A[j][k] * x[k] for k in range(n) if k != j)
            xn[j] = (b[j] - sum1) / A[j][j]
            x_vals.append(xn)
        
        if max(abs(xn[j] - x[j]) for j in range(n)) < e:
            return xn
        
        x = xn

    return xn


def gauss_seidel(A, b, x0, e, max_iter):
    n = len(A)
    x = x0[:]

    for i in range(max_iter):
        xn = x[:]
        for j in range(n):
            sum1 = sum(A[j][k] * xn[k] for k in range(j))  
            sum2 = sum(A[j][k] * x[k] for k in range(j + 1, n)) 
            xn[j] = (b[j] - sum1 - sum2) / A[j][j]

        if max(abs(xn[j] - x[j]) for j in range(n)) < e:
            return xn

        x = xn

    return xn


if __name__=="__main__":
    a = [
        [27, 6, -1],
        [1, 1, 54],
        [6, 15, 2]
    ]
    b = [85, 110, 72]
    xn = gauss_seidel(a, b, [85, 110, 72], 0.00001, 5)
    print(xn)