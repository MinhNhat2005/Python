"""
There are three numeric types in Python:
-  int
-  float
-  complex
"""
x = 1    # int
y = 2.5  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print("---------------------")

# int (trong python không giới hạn độ dài)
x = 0
y = 194721472189742817
z = -33250932988247219748297
print(type(x))
print(type(y))
print(type(z))
print("---------------------")

# float
x = 1.12
y = 0.5
z = -23429.327492492749
print(type(x))
print(type(y))
print(type(z))
print("---------------------")

x = 12e3
y = 2374E3324
z = -23429.327492e492749
print(x)
print(type(x))
print(type(y))
print(type(z))
print("---------------------")

# complex
x = 3+6j
y = 3j
z = -5j
print(x)
print(type(x))
print(type(y))
print(type(z))
print("---------------------")

# ép kiểu 
x = 1  # int
y = 2.5 # float
z = 4+4j

a = float(x)
b = int(y)
c = complex(x)
d = complex(z)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("---------------------")

# Random Number (số ngẫu nhiên)
import random
print(random.randrange(1, 100))