from linear_methods import gauss_seidel
import numpy as np
import math

def basic_sums(x,y):
  sumx = sum(x)
  sumy = sum(y)
  sumxy = sum(x_val*y_val for x_val, y_val in zip(x, y))
  sumx2 = sum(x_val**2 for x_val in x)

  return sumx, sumy, sumxy, sumx2


def least_squares_linear(x, y):
  n = len(x)
  sumx, sumy, sumxy, sumx2 = basic_sums(x,y)

  a = [
    [ n, sumx ],
    [ sumx, sumx2 ]
    ]
  b = [sumy, sumxy]
  coefficients = gauss_seidel(a, b, [0,0], 0.000001, 100000)
  print(coefficients)

  def f(x_val):
    return coefficients[0] + coefficients[1]*x_val

  return coefficients, f


def least_squares_parabola(x, y):
  n = len(x)
  sumx, sumy, sumxy, sumx2 = basic_sums(x,y)
  sumx3 = sum(x_val**3 for x_val in x)
  sumx4 = sum(x_val**4 for x_val in x)
  sumx2y = sum(x_val*x_val*y_val for x_val, y_val in zip(x, y))

  a = [
    [ n, sumx, sumx2 ],
    [ sumx, sumx2, sumx3 ],
    [ sumx2, sumx3, sumx4 ]
    ]
  b = [sumy, sumxy, sumx2y]

  coefficients = gauss_seidel(a, b, [ n, sumx, sumx2 ], 0.000001, 100000)

  def f(x_val):
    return coefficients[0] + coefficients[1] * x_val + coefficients[2] * math.pow(x_val, 2)

  return coefficients, f


def least_squares_ax_bx2(x, y):
  n = len(x)
  sumx, sumy, sumxy, sumx2 = basic_sums(x,y)
  sumY = sum(y_val/x_val for x_val, y_val in zip(x, y))

  a = [
    [ n, sumx ],
    [ sumx, sumx2 ],
    ]
  b = [sumY, sumy]

  coefficients = gauss_seidel(a, b, [ 0, 0 ], 0.000001, 100000)

  def f(x_val):
    return coefficients[0] * x_val + coefficients[1] * math.pow(x_val, 2)
  
  return coefficients, f


def least_squares_hyperbolic(x, y):
  n = len(x)
  sumY = sum(x_val*y_val for x_val, y_val in zip(x,y))
  sumX = sum(x_val**2 for x_val in x)
  sumX2 = sum(x_val**4 for x_val in x)
  sumXY = sum(x_val*x_val*x_val*y_val for x_val, y_val in zip(x,y))

  a = [
    [ n, sumX ],
    [ sumX, sumX2 ],
    ]
  b = [sumY, sumXY]

  coefficients = gauss_seidel(a, b, [ 0, 0 ], 0.000001, 100000)

  def f(x_val):
    return coefficients[0] * x_val + coefficients[1] / x_val
  
  return coefficients, f


def least_squares_exponential(x, y):
  n = len(x)
  sumx, sumy, sumxy, sumx2 = basic_sums(x,y)
  sumY = sum(math.log(y_val) for y_val in y)
  sumYx = sum(math.log(y_val)*x_val for x_val, y_val in zip(x, y))

  a = [
    [ n, sumx ],
    [ sumx, sumx2 ],
    ]
  b = [sumY, sumYx]

  coefficients = gauss_seidel(a, b, [ 0, 0 ], 0.000001, 100000)

  def f(x_val):
    return math.pow(math.e, coefficients[0]) * math.pow(math.e, coefficients[1]*x_val)

  return coefficients, f
  # return math.pow(math.e, coefficients[0]), coefficients[1]


def best_fit(x, y):
  _, funcs = zip(
    least_squares_linear(x, y),
    least_squares_parabola(x, y),
    least_squares_exponential(x, y),
    least_squares_hyperbolic(x, y)
  )

  est_list = [[] for _ in funcs]

  if 0 in x:
    funcs = funcs[:-1]
    est_list = est_list[:-1]
  
  for x_val in x:
        for i, f in enumerate(funcs):
            est_list[i].append(f(x_val))
    
  rmse = [sum((y_val - y_est_val)**2 for y_val, y_est_val in zip(y, y_est)) for y_est in est_list ]

  best_fit = rmse.index(min(rmse))

  return funcs[best_fit]

  
if __name__ == "__main__":
  x = [77, 100, 185, 239, 285]
  y = [2.4, 3.4, 7.0, 11.1, 19.6]
  # coeff = np.polyfit(x, y, 1)

  # # def func(x):
  # #   return coeff[0]*x**3 + coeff[1]*x**2 + coeff[2]*x + coeff[3]
  
  # print(coeff)
  coeff, f = least_squares_exponential(x,y)
  print(coeff)

    

  
    