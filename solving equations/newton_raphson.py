import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2

def derivative(f, x, h=0.00001):
    return (f(x + h) - f(x - h)) / (2 * h)

def plot(x_vals, iterations):
    plt.figure(figsize=(10, 10))
    plt.scatter(iterations, x_vals, color='red')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.show()

def newton_raphson(f, max_iterations):
    x = float(input("Input x0: "))
    e = float(input("Input tolerance: "))
    x_vals = []
    iterations = []
    for i in range(max_iterations):
        df = derivative(f, x)
        
        if df == 0:
            print("Provide a functino whose derviative isn't zero.")
            return

        xn = x - f(x) / df
        x_vals.append(x)
        iterations.append(i + 1)
        if abs(xn - x) < e:
            print(xn)
            plot(x_vals, iterations)   
            print(x_vals[4])
            return
        x = xn
    plot(x_vals, iterations)
    print("Root not found.")

    return


newton_raphson(f, 1000)
