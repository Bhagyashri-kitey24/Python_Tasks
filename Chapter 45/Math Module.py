import math
#rounding
x = 1.55
y = -1.55

print("-------round-------")
# round to the nearest integer
print(round(x)) # 2
print(round(y)) #-2

print("------floor------")
# get the largest integer less than x
print(math.floor(x)) # 1
print(math.floor(y)) # -2

print("------ceil------")
# get the smallest integer greater than x
print(math.ceil(x)) # 2
print(math.ceil(y)) # -1

print("------trunc------")
# drop fractional part of x
print(math.trunc(x)) # 1, equivalent to math.floor for positive numbers
print(math.trunc(y)) # -1, equivalent to math.ceil for negative numbers

print("------pow------")
# calculating power
print(math.pow(2, 10))

print("------Logarithms------")
#gives the natural (base e) logarithm of x.
print(math.log(x)) # 0.4382549309311553
print(math.log(math.e)) # 1.0
print(math.log(1)) # 0.0
print(math.log(100))#4.605170185988092

print("------Constants------")
from math import pi, e
# constants
print(math.pi)#3.141592653589793
print(math.e) #2.718281828459045
