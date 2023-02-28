# Tuple is a immutable list of values

print("-----------built-in tuple functions-----------")
tup1 = ('a', 'b', 'c', 'd', 'e', 'f')
print(tup1)
tup2 = (1, 2, 3, 4, 5,)
print(tup2)


print("-----------length of tuple-----------")
print(len(tup1)) #6

print("-----------max and min of a tuple-----------")
print(max(tup1)) #f
print(min(tup1)) #a

print("----------- convert a list into tuple-----------")
l1 = [1, 2, 3, 4, 5]
print(l1) #[1, 2, 3, 4, 5]
from_list = tuple(l1)
print(from_list) #(1, 2, 3, 4, 5)

print("-----------concatenating tuples-----------")
tup3 = tup1 + tup2
print(tup3) #('a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5)

print("-----------Accessing elements of tuple using index-----------")
print(tup1[0]) #a
print(tup1[1]) #b
print(tup1[3]) #d
print(tup1[5]) #f

print("-----------using negative indexes-----------")
print(tup1[-1]) #f
print(tup1[-2]) #e
print(tup1[-3]) #d
print(tup1[-5]) #b

print("-----------using range-----------")
print(tup1[2::-1]) #('c', 'b', 'a') it will start from index 2 and reverse from 2 to start

print("-----------reversing elements of a tuple-----------")
print(tup1[::-1])
print(reversed(tup1)) #('f', 'e', 'd', 'c', 'b', 'a')