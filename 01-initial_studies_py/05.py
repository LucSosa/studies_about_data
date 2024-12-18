# %%
def hello():
    print("Hello World!")

hello()

# %%
def sumTen(x):
    result = x + 10
    return result

y = sumTen(100)
print(y)

# %%
def sumTwoNumbers(a, b):
    return a + b

print(sumTwoNumbers(10, 10))
print(sumTwoNumbers(a = 1, b = 2))

# %%
def operation(op, *num):
    total = 0
    
    if op == "soma":
        for i in num:
            total += i
    
    elif op == "mult":
        total=1
        for i in num:
            total *= i
    
    return total

operation("mult",1,2,3,4,5,6,7,8,9,10)

# %%
file = open("arquivo.txt", 'a')
file.write("Testando")
file.close()

# %%
file = open("arquivo.txt", "r")
content = file.read()
file.close()

print(content)
print(type(content))

# %%
file = open("arquivo.txt", "r")
lines = file.read()
file.close()

print(lines)

# %%
with open("arquivo.txt", "r") as file:
    content = file.read()

print(content)

# %%
import math
math.sqrt(49)

math.pi
math.e

from math import pi, e
print(pi)
print(e)

# %%
import pandas as pd
# %%
