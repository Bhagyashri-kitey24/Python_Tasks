import itertools
num=[1,7,5,8,7,9,6,5,4,3]
#print(dir(itertools))
for i in itertools.accumulate(num):
    print(i, end=" ")
    
print("----------------------")
     
for i in itertools.count(10,2):
    if i==30:
        break
    else:
        print(i,end="_")
        
print("---------------")
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 3))
print (b) #[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]