print(" Simple Mathematical Operators")
print() 
 
print("---------------Division-----------------") 
a, b, c, d, e = 3, 2, 2.0, -3, 10
x=a / b  #1.5
print("Division=",x)
x1=a / c  #1.5
print("Division=",x1)
x2=d / b # -1.5 
print("Division=",x2)
x3=b / a # 0.66666666666
print("Division=",x3)
x4=d / e # -0.3
print("Division=",x4)


print("----------------Addition-----------------")
a=5
b=5
c = a+b
a +=b  # a +=b  is (equivalent to a = a + b)
print("addition of a and b:",c)
print("addition of a and b:",a)
import operator 
n1,n2=1,2
sum = operator.add(n1,n2)
print("addition of a and b:",sum)

print("--------------Exponentiation-------------")
a=4
b=2
c= a**b #it will give the power of 4
print("Exponential of 4 is:",c) #16
import math
d=math.pow(a, b) # = 16.0 (always float; does not allow complex results)
print("exponential result:",d) #16.0

print("--------------Trigonometric Functions-------------")
a, b = 1, 2
import math
c=math.sin(a) # returns the sine of 'a' in radians
print("sign value of a:",c)# Out: 0.8414709848078965
d=math.cosh(b) # returns the inverse hyperbolic cosine of 'b' in radians
print("cos value of a:",d)# Out: 3.7621956910836314

print("--------------Inplace Operations-------------")
a= 10
print(a)
a +=1 # increment the variable in place
print(a)
a -= 1 #decrement the variable in place
print(a)
a *= 2 # multiply the variable in place
print(a)
a /= 2 #divide the variable in place
print(a)
a //= 3 #floor divide the variable in place # Python 3
print(a)
a %= 3 # return the modulus of the variable in place
print(a)
a **= 2 #  raise to a power in place
print(a)

print("--------------Subtraction-------------")
# Using the "-" operator:
a, b = 5,2 
c= b - a # = 1
print("subtract:",c)# = 1
import operator # contains 2 argument arithmetic functions
d= operator.sub(b, a) # = 1
print("subtract:",d)

print("--------------multiplication-------------")
a, b = 2, 3
c= a * b # = 6
print("multiplication",c)
import operator
d=operator.mul(a, b) # = 6
print("multiplication",d)

print("--------------Modulus-------------")
a=3 % 4 # 3
b=10 % 2 # 0
c=6 % 4 #2
print("Modulus",a)
print("Modulus",b)
print("Modulus",c) 

import operator
a=operator.mod(3 , 4) # 3
b=operator.mod(10 , 2) # 0
c=operator.mod(6 , 4) # 
print("Modulus",a)
print("Modulus",b)
print("Modulus",c)
