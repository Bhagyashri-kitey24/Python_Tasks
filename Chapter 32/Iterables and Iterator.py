"""
iterables= __iter__ this is the type of object which gives iterators
iterators = it has defined next() method 
iteration= means go to the next element then next then next and so on or The process of iterating an object and fetching its next elements
generators= iterators --> it is a iterator which can define once
"""
print("----------generators---------")
def gen(n):
    for i in range (n):
        yield i
print(gen(10000000)) #generate the object at some location, o/p <generator object gen at 0x0000026CDBFC42B0>
for i in gen(10):
    print(i) 

print("---generator object---")    
ob1= gen(1000)
print(next(ob1))#0
print(next(ob1))#1
print(next(ob1))#2
print(next(ob1))#3
print(next(ob1))#4

print("-------Iterating over entire iterable-------")
s = {1, 2, 3}
for a in s:# get every element in s
 print (a) # prints 1, then 2, then 3
# copy into list
l1 = list(s) # l1 = [1, 2, 3]
# use list comprehension
l2 = [a * 2 for a in s if a > 2] # l2 = [6]
print(l2)

