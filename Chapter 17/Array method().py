from array import *

stu_roll= array('i',[1,2,3,4,5,6])

print("-------print all elements of array--------")
for i in stu_roll:
 print(i)
 
print("-------Append any value to the array using append()method--------")
stu_roll= array('i',[1,2,3,4,5,6])
stu_roll.append(7) #[1,2,3,4,5,6,7] it will append the element at the end
print(stu_roll)

print("-------Insert value in an array using insert() method--------")
stu_roll= array('i',[1,2,3,4,5,6,7])
stu_roll.insert(2,8) #[1,2,8,3,4,5,6,7] it will insert 8 on 2nd index
print(stu_roll)

print("-------Extend python array using extend() method--------")
arr1= array('i',[1,2,3,4,5])
arr2= array('i',[6,7,8,9,10])
arr1.extend(arr2) #it will extend arr1 and arr2
print(arr1) #[1,2,3,4,5,6,7,8,9,10] 

print("-------Add items from list into array using fromlist() method--------")
arr1 = array('i', [1,2,3,4,5])
lst=[11,12,13]
arr1.fromlist(lst) #[1, 2, 3, 4, 5, 11, 12, 13]) it will add list into the array
print(arr1)

print("-------Remove any array element using remove()method--------")
arr1= array('i',[1,2,8,3,4,5])
arr1.remove(8) #it will remove 8 from array
print(arr1) #[1, 2, 3, 4, 5]

print("-------Remove last array element using pop() method--------")
arr1= array('i',[1,2,8,3,4,5])
arr1.pop() #it will Remove last array element using pop() 
print(arr1) #[1, 2, 3, 4]

print("-------Fetch any element through its index using index()method--------")
arr1 = array('i', [1,2,3,4,4,5])
print(arr1.index(5)) #it will return the index of element 5.  o/p= 5
print(arr1.index(2)) #it will return the index of element 2.  o/p= 1
print(arr1.index(4)) #it will return the index of element 4.  o/p= 3

print("-------Reverse a python array using reverse() method--------")
arr1 = array('i', [1,2,3,4,5])
arr1.reverse() #it will return reversed of arr1 
print(arr1)    #o/p=[5, 4, 3, 2, 1]

print("-------Get array buer information through buer_info() method--------")
arr1 = array('i', [1,2,3,4,5])
print(arr1.buffer_info()) #(2429614275696, 5) This method provides you the array buffer start address in memory and number of elements in array.


print("-------Check for number of occurrences of an element using count() method--------")
arr1 = array('i', [1,7,3,3,7,6,7,8,7,8,7,9])
print(arr1.count(3)) #2 it will return number of occurances of element so 3 is occure 2 times
print(arr1.count(7)) #5 it will return number of occurances of element so 7 is occure 5 times

print("-------Convert array to a python list with same elements using tolist() method--------")
arr1 = array('i', [1,2,3,4,5])
c = arr1.tolist() #it will convert the arry into the list
print(c) # [1, 2, 3, 4, 5]




