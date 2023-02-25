print("--------AND--------")
x = True
y = True
z = x and y # z = True
print(z)

x = True
y = False
z = x and y # z = False
print(z)

x = False
y = True
z = x and y # z = False
print(z)

x = False
y = False
z = x and y # z = False
print(z)

x = 1
y = 1
z = x and y # z = y, so z = 1, see `and` and `or` are not guaranteed to be a boolean -->1
print(z)

x = 0
y = 1
z = x and y # z = x, so z = 0 (see above) -->0
print(z)

x = 1
y = 0
z = x and y # z = y, so z = 0 (see above) -->0
print(z)

x = 0
y = 0
z = x and y # z = x, so z = 0 (see above) -->0
print(z)

print("--------OR--------")
x = True
y = True
z = x or y # z = True
print(z)

x = True
y = False
z = x or y # z = True
print(z)

x = False
y = True
z = x or y # z = True
print(z)

x = False
y = False
z = x or y # z = False
print(z)

x = 1
y = 1
z = x or y # z = x, so z = 1, see `and` and `or` are not guaranteed to be a boolean -->1
print(z)

x = 1
y = 0
z = x or y # z = x, so z = 1 (see above) -->1
print(z)

x = 0
y = 1
z = x or y # z = y, so z = 1 (see above) -->1
print(z)

x = 0
y = 0
z = x or y # z = y, so z = 0 (see above) -->0
print(z)

print("--------OR--------")
x = True
y = not x # y = False
print(y)

x = False
y = not x # y = True
print(y)
