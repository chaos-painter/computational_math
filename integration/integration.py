import numpy as np
import math

def trapezoidal(x1, x2, func, chunks):
  delta = (x2-x1) / chunks
  x = [x1 + delta*i for i in range(chunks+1)]
  y = [func(x_val) for x_val in x]
  integral = sum((y[i] + y[i+1]) for i in range(len(y)-1)) / 2 * delta
  return integral


def simpsons13(x1, x2, func, chunks):
  if chunks % 2 != 0:
    chunks += 1
  delta = (x2-x1) / chunks
  x = [x1 + delta*i for i in range(chunks+1)]
  y = [func(x_val) for x_val in x]
  integral = sum(y[i] + 4*y[i+1] + y[i+2] for i in range(0, len(y)-2, 2)) / 3 * delta
  return integral


def simpsons38(x1, x2, func, chunks):
  if chunks % 3 != 0:
    remainder = chunks % 3
    chunks 
    raise ValueError("The number of chunks should be divisible by 3.")
  delta = (x2-x1) / chunks
  x = [x1 + delta*i for i in range(chunks+1)]
  y = [func(x_val) for x_val in x]
  integral = sum(y[i] + 3*y[i+1] + 3*y[i+2] + y[i+3] for i in range(0, len(y)-3, 3)) / 8 * delta * 3
  return integral


def func(x):
  return 1 / (1+x**2)


if __name__ == "__main__":
  x1 = 0
  x2 = 1
  print(trapezoidal(x1, x2, func, 1000))
  print(simpsons13(x1, x2, func, 1000))
  print(simpsons38(x1, x2, func, 6))




