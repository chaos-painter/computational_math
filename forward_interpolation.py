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

def newton_forward_interpolation(x, y, x_val):
  forward_diffs = forward_differences(y)
  p = (x_val - x[0])
  
  interpolation = y[0]
  p_product = 1
  for i in range(len(forward_diffs)):
      p_product *= (p - i)
      interpolation += (p_product * forward_diffs[i][0]) / factorial(i + 1)
  
  return interpolation


y = [2, 4, 6, 8]
x = [1, 2, 3]
interpolation = newton_forward_interpolation(x, y, 2.5)
print(interpolation)


  
  
