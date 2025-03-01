import math
import matplotlib.pyplot as plt
import sympy as sym

x = sym.symbols('x')
f_sym = x**2 - 4*x - 4
solutions = sym.solve(f_sym, x)
solution = solutions[0]


def g(x_value):
  return float(solution.subs(x, x_value))


def plot(x_vals, iterations):
    plt.figure(figsize=(10, 10))
    plt.scatter(iterations, x_vals, color='red')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.show()


def iteration(g, max_iterations):
    x = float(input("Input x0: "))
    e = float(input("Input tolerance: "))
    x_vals = []
    iterations = []
    
    for i in range(max_iterations):
        xn = g(x)
        x_vals.append(x)
        iterations.append(i + 1)
        
        if abs(xn - x) < e: 
            print(xn)
            plot(x_vals, iterations)
            return
        x = xn
    
    print("Root not found.")
    plot(x_vals, iterations)
    return

iteration(g, 1000)
