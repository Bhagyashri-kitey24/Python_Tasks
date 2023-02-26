#creat list
lst=[1, 2, 3, 4, 5]
print(lst)

print("-----append----")
a = [1, 2, 3, 4, 5]
# Append values 6, 7, and 7 to the list
a.append(6)
a.append(7)
a.append(8)
print(a) #output will be [1, 2, 3, 4, 5, 6, 7, 8]

# Appending a list to another list
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9]
a.append(b) 
print(a)# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9]]
print(a[8]) # Returns: [8,9]

print("-----extend----")
#extend(enumerable) – extends the list by appending elements from another enumerable.
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]
a.extend(b)# Extend list by appending all elements from b
print(a) #[1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

print("-----Index----")
a = [1, 2, 3, 4, 5, 6, 7, 7]
print(a.index(2)) #it will return the index of element 2 that is index->1
print(a.index(1)) #it will return the index of element 1 that is index->0

print("-----insert----")
a = [1, 2, 3, 4, 5, 6, 7]
a.insert(0,0) #it will add 0 into 0 index
print(a) #[0, 1, 2, 3, 4, 5, 6, 7]
a.insert(6,8) #it will add 8 into 6 index
print(a) #[0, 1, 2, 3, 4, 5, 8, 6, 7]

print("-----pop----")
a = [1, 2, 3, 4, 5, 6, 7]
print(a.pop(2)) #it will pop 3 from index 2
print(a) #[1, 2, 4, 5, 6, 7]

print("-----remove----")
a = [1, 2, 3, 4, 5, 6, 7]
a.remove(2) #it will remove element 2
print(a) #[1, 3, 4, 5, 6, 7]

print("-----reverse----")
a = [1, 2, 3, 4, 5, 6, 7]
a.reverse() #it will reverse the list
print(a) #[7, 6, 5, 4, 3, 2, 1]

print("-----count----")
a = [1, 2, 3, 4, 5, 6, 7]
print(a.count(2)) #counts the number of occurrences of some value in the list. o/p= 1

print("-----clear----")
a = [1, 2, 3, 4, 5, 6, 7]
a.clear() #it will clear the list
print(a)

print("-----Replication----")
b = ["Bhagi"] * 3 #multiplying an existing list by an integer
print(b) #['Bhagi', 'Bhagi', 'Bhagi']

print("-----Element deletion----")
#it is possible to delete multiple elements in the list using the del keyword and slicenotation:
a = list(range(10))
del a[::2]
print(a)# a = [1, 3, 5, 7, 9]
del a[-1]
print(a)# a = [1, 3, 5, 7]
del a[:]
print(a)# a = []

print("-----Copying----")
import copy
old_list=[1,2,3,4]
new_list = copy.copy(old_list) 
print(new_list) #new_list=[1,2,3,4]

print("------------- Accessing list values ------------")
lst = [1, 2, 3, 4]
print(lst[0]) # 1
print(lst[1]) # 2

print("------------- Accessing list values ------------")
lst = [1, 2, 3, 4]
print(lst[0]) # 1
print(lst[1]) # 2
print(lst[-1]) # 4
print(lst[-2]) # 3

print("------------- Checking if list is empty ------------")
lst = []
if not lst:
 print("list is empty")


print("------------- Iterating over a list ------------")
my_list = ['bhagi', 'appu', 'dami']
for item in my_list:
 print(item)
 
print("------------- Checking whether an item is in a list ------------")
lst = ['test', 'twest', 'tweast', 'treast']
print('test' in lst) # Out: True
print('toast' in lst) #False

print("------------- concatenate and merge lists ------------")
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
res = lst1 + lst2
print(res)

print("------------- printing length of list ------------")
print(len(res))

print("------------- # Comparing lists ------------")
l1 = [1,2,3]
l2 = [2,5,-1]
print(l1 < l2)

print("------------- initializing a list to a fixed number of elements ------------")
listt = [1] * 10
print(listt)

name = ["Ishika"]*5
print(name)


