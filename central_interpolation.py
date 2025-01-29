import pandas as pd

def central_differences(y):
  size = len(y)
  cent_diffs = []
  diffs = y
  for i in range(size - 1):
      if len(diffs) > 2:
        diffs = [(diffs[j+1] - diffs[j-1]) / 2 for j in range(1, len(diffs) - 1)]
        cent_diffs.append(diffs)
  return cent_diffs

def build_table(x, y, cent_diffs):
  table = pd.DataFrame({'x': x, 'f(x)': y})
  cent_diffs = central_differences(y)

  for i, diffs in enumerate(cent_diffs):
      table[f'Δ^{i+1}f'] = ['-' for _ in range(i)] + diffs + ['-' for _ in range(len(x) - i - 1)]

  return table

def central_interpolation(x, y, x_val):
  h = x[1] - x[0]
  cent_diffs = central_differences(y)
  p = (x_val - x[-1]) / h
  
  interpolation = y[-1]
  p_product = 1
  for i in range(len(cent_diffs)):
      p_product *= p + i
      print(cent_diffs)
      interpolation += (p_product * cent_diffs[i][0])
  
  return interpolation


y = [2, 4, 6, 8]
x = [1, 2, 3, 4]

interpolation = central_interpolation(x, y, 2.5)
print(interpolation)
