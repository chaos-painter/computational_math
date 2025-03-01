from integration import trapezoidal, simpsons13, simpsons38 
import numpy as np

#TASK 1
print("TASK 1")

def func(x):
  return x**3

print(f"Trapezoidal:  {trapezoidal(0, 1, func, 5)}")
print("\n")


#TASK 2
print("TASK 2")

def func(x):
  return np.sqrt(np.cos(x))

print("Simpsons 1/3:")
print(f"(i) {simpsons13(0, np.pi, np.sin, 11)}")
print(f"(i) {simpsons13(0, np.pi/2, func, 9)}")
print("\n")


#TASK 3
print("TASK 3")

def func(x):
  return 1/(1+x**3)


print("Simpsons 3/8:")
print(f"(i) {simpsons38(0, 9, func, 201)}")
print(f"(i) {simpsons38(0, np.pi/2, np.sin, 201)}")
print("\n")


#TASK 4
print("TASK 4")

def func(x):
  return 1/(1+x)


print("Trapezoidal:")
print(f"(i) {trapezoidal(0, 1, func, 1000)}")

print("Simpsons 3/8:")
print(f"(i) {simpsons13(0, 1, func, 1000)}")

print("Simpsons 3/8:")
print(f"(i) {simpsons38(0, 1, func, 1002)}")
print("\n")
