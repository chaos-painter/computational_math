def backward_differences(y):
    size = len(y)
    back_diffs = []
    diffs = y
    for _ in range(size - 1):
        diffs = [diffs[j] - diffs[j - 1] for j in range(len(diffs) - 1, 0, -1)]
        back_diffs.append(diffs)
    print(back_diffs)
    return back_diffs


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def forward_differences_table(y):
    size = len(y)
    table = [y[:]]
    
    for _ in range(1, size):
        table.append([table[-1][i + 1] - table[-1][i] for i in range(len(table[-1]) - 1)])
    
    print("Forward Difference Table:")
    for row in table:
        print("\t".join(map(str, row)))
    
    return table

def newton_backward_interpolation(x, y, x_val):
    back_diffs = backward_differences(y)
    p = (x_val - x[-1])
    
    interpolation = y[-1]
    p_product = 1
    for i in range(len(back_diffs)):
        p_product *= p + i
        interpolation += (p_product * back_diffs[i][0]) / factorial(i + 1)
    
    return interpolation


y = [2, 4, 6, 8]
x = [1, 2, 3, 4]

interpolation = newton_backward_interpolation(x, y, 2.5)
print(interpolation)

