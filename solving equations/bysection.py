import math
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x + 1

def plot(x_vals, iterations):
    plt.figure(figsize=(10, 10))
    plt.scatter(iterations, x_vals, color='red')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.show()

def bisection(f, max_iterations):
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    
    if f(a) * f(b) >= 0:
        print("Change a and b so that f(a) * f(b) < 0\n")
        return
    
    e = float(input("Input tolerance: "))
    
    x_vals = []
    y_vals = []
    iterations = []
    
    for i in range(max_iterations):
        if abs(b - a) < e:
            x = (a + b) / 2
            x_vals.append(x)
            y_vals.append(f(x))
            iterations.append(i + 1)
            break
        
        x = (a + b) / 2
        x_vals.append(x)
        y_vals.append(f(x))
        iterations.append(i + 1)
        
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
    
    print(x)
    plt.figure(figsize=(10, 10))
    plt.scatter(iterations, x_vals, color='red')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.show()

bisection(f, 1000)
