import matplotlib.pyplot as plt
from curve_fitting import best_fit

x = [6, 7, 7, 8, 8, 8, 9, 9, 10]
y = [5, 5, 4, 5, 4, 3, 4, 3, 3]

fitting_func = best_fit(x, y) 

x_fit = [i for i in range(0, 12, 1)]
y_fit = [fitting_func(x_val) for x_val in x_fit]

plt.scatter(x, y, color='blue', label='Original Data')

plt.plot(x_fit, y_fit, color='red', label='Quadratic fit')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
