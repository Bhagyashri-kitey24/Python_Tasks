print("Boolean data type")
a=10
b=20
c=a>b
print(c) #it will show the result in the form of true or false 
print(type(c))
print()

print(True + True) # True=1 False=0 so 1+1=2
print(True - False)  # True=1 False=0 so 1-0=1
print(True * False) # True=1 False=0 so 1*0=0


print("--------------")

print("Inteer data type")
a = 2
b = 100
c = 123456789
d = 38563846326424324
print("\n",a,"\n",b,"\n",c,"\n",d,"\n") 
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("---------------")

print("Float data type")
a = 2.0
b = 100.e0
c = 123456789.e1
print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print("---------------")

print("Complex numbers")
a = 2 + 1j # 2 is a real part, 1 is a imaginary part. and "j square=-1" j=square root of -1 this type of representation is called complex number.
b = 100 + 10J
print(a)
print(type(a))
print(b)
print(type(b))

print(a.real) #To know the value of real value
print (b.imag) #To know the value of imaginary part

c= 1.2+5.2j #valid
print(c)
print(type(c))
g= 0B1111+20j #valid , real party can represent in binary, float, octal, hexadecimal but imaginary part should only in decimal form
print(g)
print(type(g))
# x= 15+0B1111j this is Invalid the imaginary part is always in decimal form
print("-----------------------\n")

#tuple: An ordered collection of n values of any type (n >= 0).
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else' # returns a TypeError Supports indexing; immutable
print("-----------------\n")

#list: An ordered collection of n values (n >= 0)
a = [1, 2, 3] 
print(a)
b = ['a', 1, 'python', (1, 2), [1, 2]]
print(b)
b[2] = 'something else' # allowed ,mutable
print(b)
print("-----------------\n")

#set: An unordered collection of unique values. Items must be hashable.
a = {1, 2, 'a'}
print(a)

#dict: An unordered collection of unique key-value pairs; keys must be hashable.
a = {1: 'one',
 2: 'two'}
b = {'a': [1, 2, 3],
 'b': 'a string'}
print(a,b)

x = None
if x is None:
 print('Not a surprise, I just defined x as None.')
print("----------------\n")

print("Converting between datatypes\n")
a = '123' #string
b = int(a) #converted to int
print(type(b))
print("-----------------\n")

#We can also convert sequence or collection types
a = 'hello'
list(a) # ['h', 'e', 'l', 'l', 'o']
set(a) # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')
print(list)
print(set)
print(tuple)

