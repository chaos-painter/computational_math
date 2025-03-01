import matplotlib.pyplot as plt
from curve_fitting import best_fit

x = [1, 2, 3, 4, 5]
y = [1.8, 5.1, 8.9, 14.1, 19.8]

fitting_func = best_fit(x, y) 

# print(f"Fitted Line: y = {a:.2f} + {b:.2f}x + {c:.2f}x^2")


x_fit = [i for i in range(0, 10, 1)]
y_fit = [fitting_func(x_val) for x_val in x_fit]

plt.scatter(x, y, color='blue', label='Original Data')

plt.plot(x_fit, y_fit, color='red', label='Quadratic fit')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
