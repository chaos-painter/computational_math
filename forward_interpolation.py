def forward_differences(y):
  size = len(y)
  forward_diffs = []
  diffs = y
  for _ in range(size-1):
    diffs = [diffs[j + 1] - diffs[j] for j in range(len(diffs) - 1)]
    forward_diffs.append(diffs)
  return forward_diffs

def factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n - 1)
    
def build_table(diffs, x):
    print("Forward Differences Table")
    
    num_rows = len(x)  
    num_cols = len(diffs) + 1
    
    table = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        table[i][0] = str(x[i])

    for col in range(1, num_cols):
        for row in range(num_rows - col):
            table[row][col] = str(round(diffs[col - 1][row], 3))

    for row in table:
        print("\t".join(row))

def newton_forward_interpolation(x, y, x_val):
    forward_diffs = forward_differences(y)
    h = x[1] - x[0]
    
    u = (x_val - x[0]) / h

    interpolation = y[0]
    u_product = 1
    
    for i in range(1, len(forward_diffs) + 1):  
        u_product *= (u - (i - 1))  
        interpolation += (u_product * forward_diffs[i - 1][0]) / factorial(i)

    return interpolation







  
  
