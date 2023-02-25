# The best way to get the unique elements from a list is to turn it into a set:

girls_name = ["Bhagi", "Sanju", "Appu", "Dipa", "Appu","Ishu","Bhagi","Dami","Sanju" ]
a = set(girls_name) #it will give only unic names
print(a)
print()

b=list(girls_name) #it will print all elements
print(b)

c=list(set(girls_name)) # it will give only unic names
print(c)
