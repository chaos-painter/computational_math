import math
import matplotlib.pyplot as plt

def f(x):
    return x*math.log(x, 10) - 1.2

def plot(x_vals, iterations):
    plt.figure(figsize=(10, 10))
    plt.scatter(iterations, x_vals, color='red')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.show()

def false_position(f, max_iterations):
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return
    
    e = float(input("Input tolerance: "))
    x_vals = []
    iterations = []

    for i in range(max_iterations):
        x = b - (f(b)*(b-a))/(f(b)-f(a))
        x_vals.append(x)
        iterations.append(i + 1)

        if f(x) == 0 or abs(f(x)) < e:
            print(x)
            plot(x_vals, iterations)
            return
        
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
    print("Root not found.")
    plot(x_vals, iterations)
    
print(math.log(100, 10))
false_position(f, 1000)