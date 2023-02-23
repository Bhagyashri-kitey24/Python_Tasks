#collectiontypes hold multiple values.

#List 
print("List\n")
int_list = [1, 2, 3]
string_list = ['abc', 'defghi']
print(int_list)
print(string_list)
print("------------------\n")

mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]] #A list can contain another list as its element.

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) # Alice
print(names[2]) # Craig
print(names[-1]) # Eric
print(names[-4]) # Bob

names[0] = 'Ann' #conver alice to ann
print(names)

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia") #it will append means add sia at last after eric
print(names)

names.insert(1, "Nikki") #add a new element to list at a specific index L.insert(index, object)

print(names)

names.remove("Bob")
print(names) # Outputs ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']
print("-----------------------\n")

#Count length of list
lst=[11,25,12,45,13,26,57,89,85,16,12]
print(len(lst))

a = [1, 1, 1, 2, 3, 4]
print(a.count(1)) #count occurrence of any item in list

#Reverse the list
print(a.reverse())
[4, 3, 2, 1, 1, 1]
# or
print(a[::-1])
[4, 3, 2, 1, 1, 1]
print("------X-------")

#Tuples
print("tuple\n")
ip_address = ('10.20.30.40', 8080)
print(ip_address) #Tuples are represented with parentheses instead of square brackets

one_member_tuple = ('Only member',)
print(one_member_tuple)
print("---------X---------\n")

#Dictionary
#A dictionary in Python is a collection of key-value pairs.
print("Dictionaries\n")

stud_info = {
 '1': 'lucky',
 '2': 'krishna',
 '3': 'liana',
 '4': 'divisha'
}
print(stud_info)
roll = stud_info['2'] #To get a value, refer to it by its key
print(roll)
print("---------X---------\n")

#set
#A set is a collection of elements with no repeats and without insertion order but sorted order. 
print("set")

first_names = {'Adam', 'Beth', 'Charlie'} #Defining a set is very similar to defining a dictionary:
print(first_names)

# we can build a set using an existing list:
my_list = [1,2,3]
my_set = set(my_list)
print(my_set )

print("---------X-------")

