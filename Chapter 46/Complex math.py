import cmath
a = 2 + 3j
# calculating phase using phase function
print(cmath.phase(a)) #0.982793723247329
print(cmath.sin(a)) # prints sin value of a complex number. (9.15449914691143-4.168906959966565j)

print("---Basic complex arithmetic---")
z1 = 3 + 2j
z2 = 2 + 1j

print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
print(z1 / z2)