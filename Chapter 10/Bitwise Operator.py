print("Bitwise Operators")
print()

print("---------------Bitwise NOT----------------")
a= 0b1010
c =~a
print(a) #0b1011

print("---------------Bitwise AND----------------")
a=0b1010
b=0b1100
c=a&b #8
print("Bitwise AND",c)
d=10
e=12
f= d&e #8
print("Bitwise AND",f)

print("---------------Bitwise OR----------------")
a=0b1010
b=0b1100
c=a|b #14
print("Bitwise OR",c)

print("---------------Bitwise XOR (Exclusive OR)----------------")
a=0b1010
b=0b1100
c=a^b
print("Bitwise XOR",c)#6

print("---------------Bitwise Left Shift----------------")
a=0b1010
c= a<<2
print("Bitwise Left Shift",c)#40

print("---------------Bitwise Right Shift----------------")
a=0b1010
c= a>>2 #2
print("Bitwise Right Shift",c)

print("---------------Bitwise Right Shift----------------")

a = 0b001
a &= 0b010
print("AND operation",a)# a = 0b000 ->0
a = 0b001
a |= 0b010
print("OR operation",a)# a = 0b011  ->3
a = 0b001
a <<= 2
print("Left shift operation",a)# a = 0b100  ->4
a = 0b100
a >>= 2
print("Right shift operation",a)# a = 0b001  ->1
a = 0b101
a ^= 0b011
print("XOR operation",a)# a = 0b110  ->6
