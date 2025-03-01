from differentiation import first_derivative, second_derivative
from interpolation.forward_interpolation import newton_forward_interpolation



#TASK 1
print("TASK 1")


x0 = 20
x = [0, 5, 10, 15]
y = [3, 14, 69, 228]
y0 = newton_forward_interpolation(x, y, x0)

x.append(x0)
y.append(y0)

print(f"1st Derivative at {x0}: {first_derivative(x, y, 0)}")


#TASK 3
print("TASK 3")


x0 = 1.5
x = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y = [3.375, 7.000, 13.625, 24.000, 38.875, 59.000]

print(f"1st Derivative at {x0}: {first_derivative(x, y, x0)}")
print(f"2nd Derivative at {x0}: {second_derivative(x, y, x0)}")
print("\n")




#TASK 4
# print("TASK 4")


# x0 = 1.1
# x = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# y = [0, 0.128, 0.544, 1.296, 2.432, 4.000]



# for i in range(1, len(x)-1, 2):
#   x1 = 1.1
#   y0 = newton_forward_interpolation(x, y, x0)
#   x.insert(i, x1)
#   y.insert(i, y0)
#   x1 += 0.2


# fd, sd = derivatives(x, y, x0)

# print(f"1st Derivative at {x0}: {fd}")
# print(f"2nd Derivative at {x0}: {sd}")
# print("\n")



#TASK 5
print("TASK 5")


x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
y = [1.000, 1.025, 1.049, 1.072, 1.095, 1.118, 1.140]


x0=1.05
x1=1.25
x2=1.15


print(f"1st Derivative at {x0}: {first_derivative(x, y, x0)}")
print(f"2nd Derivative at {x0}: {second_derivative(x, y, x0)}")

print(f"1st Derivative at {x1}: {first_derivative(x, y, x1)}")
print(f"2nd Derivative at {x1}: {second_derivative(x, y, x1)}")

print(f"1st Derivative at {x2}: {first_derivative(x, y, x2)}")
print(f"2nd Derivative at {x2}: {second_derivative(x, y, x2)}")
print("\n")