from forward_interpolation import newton_forward_interpolation, forward_differences, build_table

# task 1
print("TASK 1")
x = [ 10, 20, 30, 40 ]
y = [ 1.1, 2.0, 4.4, 7.9]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
interpolation = newton_forward_interpolation(x, y, 15)
print(interpolation)
print("\n")

# task 2
print("TASK 2")
x = [ 0, 1, 2, 3, 4 ]
y = [ 1.0, 1.5, 2.2, 3.1, 4.6 ]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
print(forward_diffs[2][0])
interpolation = newton_forward_interpolation(x, y, 1.5)
print(interpolation)
print("\n")

# task 2
print("TASK 3")
def func(x):
  return x**3 + x**2 - 2*x + 1
x = [ 0, 1, 2, 3, 4, 5 ]
y = [func(x_val) for x_val in x]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
interpolation = newton_forward_interpolation(x, y, 6)
print(interpolation)
print(f"Value by substitution: {func(6)}")
print("\n")

# task 4
print("TASK 4")
def func(x):
  return x**3 + 5*x - 7
x = [ -1, 0, 1, 2, 3, 4, 5 ]
y = [func(x_val) for x_val in x]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
interpolation = newton_forward_interpolation(x, y, 6)
print(interpolation)

print(f"Value by substitution: {func(6)}")
print("\n")


#task 5
print("TASK 5")
x = [ -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ]
y = [ 2.6, 3.0, 3.4, 4.28, 7.08, 14.2, 29.0 ]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
interpolation1 = newton_forward_interpolation(x, y, -0.4)
interpolation2 = newton_forward_interpolation(x, y, -0.6)
interpolation3 = newton_forward_interpolation(x, y, 1.2)
interpolation4 = newton_forward_interpolation(x, y, 1.4)
y.extend([interpolation3, interpolation4])
y = [interpolation2, interpolation1] + y

x.extend([1.2, 1.4])
x = [-0.6, -0.4] + x

print(y)
print(x)


print("\n")


#task 6
print("TASK 6")
x = [ 2, 3, 4, 5 ]
y = [ 45.0, 49.2, 54.1, 63.2 ]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
# missing_point = 3
# missing = forward_diffs[missing_point-2][0] + forward_diffs[missing_point-2][1] + y[missing_point-1]

interpolation = newton_forward_interpolation(x, y, 6)

# print(missing)
print(interpolation)
print("\n")


#task 7
print("TASK 7")
x = [ 1, 2, 3, 4, 5 ]

def func(x):
  product = 1
  for i in range(16):
    if i % 2 != 0:
      product *= (2*x + i)
  return product

y = [func(x_val) for x_val in x]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
print(forward_diffs[3][0])
interpolation = newton_forward_interpolation(x, y, 4.5)

print(interpolation)


#task 8
print("TASK 8")
x = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
н = [1, -1, 1, -1, 1]

def func(x):
  product = 1
  for i in range(19):
    if i % 2 != 0:
      product *= (2*x + i)
  return product

y = [func(x_val) for x_val in x]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
print(forward_diffs[3][0])
interpolation = newton_forward_interpolation(x, y, 4.5)

print(interpolation)



#task 9
print("TASK 9")
x = [ 1, 2, 3, 4, 5 ]

def func(x):
  product = 1
  for i in range(19):
    if i % 2 != 0:
      product *= (2*x + i)
  return product

y = [func(x_val) for x_val in x]

forward_diffs = forward_differences(y)
build_table(forward_diffs, x)
print(forward_diffs[3][0])
interpolation = newton_forward_interpolation(x, y, 4.5)

print(interpolation)





