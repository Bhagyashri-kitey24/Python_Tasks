# List comprehensions are utilized to generate lists from other lists by applying functions to each element in the list. 

# List Comprehensions
# offers a shorter syntax when you want to create a new list based on the values of anexisting list.

lst=[i for i in range(100) if i%3==0]
print(lst) #it will print multiples of 3 upto 100

# Dictionary Comprehensions
dict1={i:f"item{i}" for i in range (5)} #it will return all key values upto 20 ,for example o/p={0: 'item0'}......to....{99: 'item99'}
print(dict1) #{0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4'}
dict2={value:key for key,value in dict1.items()} #it will return reverse the dict1
print(dict2) #{'item0': 0, 'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4}

# set Comprehensions
subjects= {"sub1","sub2","sub1","sub2","sub3","sub1"}
print(subjects) #{'sub1', 'sub2', 'sub3'}

# Generator Comprehensions
evens=(i for i in range(100)if i%2==0)
print(evens)#at 0x000001FB8D854040>

for item in evens :
    print(item)

# Changing Types in a List
# Convert a list of strings to integers.
items = ["1","2","3","4"]
print([int(item) for item in items])# Out: [1, 2, 3, 4]

# Convert a list of strings to float.
items = ["1","2","3","4"]
print(map(float, items))# Out:[1.0, 2.0, 3.0, 4.0]
