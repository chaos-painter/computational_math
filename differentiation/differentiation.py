from interpolation.forward_interpolation import forward_differences

def first_derivative(x_vals, y_vals, x0):
  diffs = forward_differences(y_vals)
  # print(diffs)
  step = x_vals[1] - x_vals[0]
  # print(step)

  start = x_vals.index(x0)
  # print(start)
  relevant_diffs = []
  for row in diffs:
    if len(row) > start:
      relevant_diffs.append(row[start])
    else:
       relevant_diffs.append(0)
    
  # print(relevant_diffs)  
  diff_sum = sum(((-1)**(i)*relevant_diffs[i])/(i+1) for i in range(1, len(relevant_diffs)))
  # print(diff_sum)

  derivative = (relevant_diffs[0] + diff_sum) / step
  return derivative


def second_derivative(x_vals, y_vals, x0):
  coefficients = [ 1, 1, 11/12, 5/6, 137/180 ]
  diffs = forward_differences(y_vals)

  step = x_vals[1] - x_vals[0]

  start = x_vals.index(x0)

  relevant_diffs = []
  for row in diffs:
    if len(row) > start:
      relevant_diffs.append(row[start])
    else:
       relevant_diffs.append(0)
    

  diff_sum = sum(((-1)**(i+1)*relevant_diffs[i])*coefficients[i-1] for i in range(1, len(relevant_diffs)))


  derivative = (diff_sum) / step**2
  return derivative




def first_derivative_any(x_vals, y_vals, x0):
  diffs = forward_differences(y_vals)
  # print(diffs)
  step = x_vals[1] - x_vals[0]
  # print(step)
  t = (x0-1)/step
  start = x_vals.index(x0)
  # print(start)
   
  coefficients = [
        1,
        (2 * t - 1) / 2, 
        (3 * t**2 - 6 * t + 2) / 6,
        (4 * t**3 - 18 * t**2 + 22 * t - 6) / 24,  
    ]

  diff_sum = sum((coefficients[i] * diffs[i][0]) for i in range(1, len(diffs)) )
  derivative = (diffs[0][0] + diff_sum) / 1.2
  return derivative


if __name__ == "__main__":
  x = [0, 2, 3, 4, 7, 8]
  y = [4, 26, 58, 112, 466, 922]
  print(first_derivative_any(x, y, 6))

