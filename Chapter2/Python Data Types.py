print("String Data Type\n")
a_str = 'Hello World'
print(a_str) #output will be whole string. Hello World
print(a_str[0]) #output will be first character. H
print(a_str[0:5]) #output will be first five characters. Hello
print("-----------X---------\n")

print("set data type")
#Sets - They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed
a = set('abracadabra')
print(a) # unique letters in a
a.add('z')
print(a)

#Frozen Sets - They are immutable and new elements cannot added after its defined.
b = frozenset('asdfagsa')
print(b)
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)
print("---------X--------\n")

print("Numbers data type\n")
int_num = 10 #int value
float_num = 10.2 #float value
complex_num = 3.14j #complex value
print("\n",int_num,"\n",float_num,"\n",complex_num)
print(type(int_num),type(float_num),type(complex_num))
print("---------X---------\n")

print(" List Data Type") 
print()
list = [123,'abcd',10.2,'d'] #can be an array of any data type or single data type.
list1 = ['hello','world']
print(list) #will output whole list. [123,'abcd',10.2,'d']
print(list[0:2]) #will output first two element of list. [123,'abcd']
print(list1 * 2) #will gave list1 two times. ['hello','world','hello','world']
print(list + list1) #will gave concatenation of both the lists.
print("------------X------------\n")

print("Dictionary Data Type\n")
dic={'name':'red','age':10}
print(dic) #will output all the key-value pairs. {'name':'red','age':10}
print(dic['name']) #will output only value with 'name' key. 'red'
print(dic.values()) #will output list of values in dic. ['red',10]
print(dic.keys()) #will output list of keys. ['name','age']
print("----------X---------\n")

print("Tuple Data Type\n")
tuple = (123,'hello')
tuple1 = ('world')
print(tuple) #will output whole tuple. (123,'hello')
print(tuple[0]) #will output first value. (123)
print(tuple + tuple1) #will output (123,'hello','world')

