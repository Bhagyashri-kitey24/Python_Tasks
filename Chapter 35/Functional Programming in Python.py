print("----------------Lambda Function ----------------")

#def sq(a):
   # return a*a
#num=[2,3,4,5,6,7,8,9]
#square= list(map(sq,num))
#print(square)

num=[2,3,4,5,6,7,8,9]
square= list(map(lambda x:x*x, num))
print(square) #[4, 9, 16, 25, 36, 49, 64, 81]
print()

print("----------------Map Function ----------------")
num=[1,5,8,16]
num=list(map(int,num))
num[2]=num[2]+1
print(num[2]) #o/p=9 it will add 1 in 8 which is on index position 2 
print()

print("----------------Reduce Function ----------------")
from functools import reduce
list1=[1,2,3,4]
num= reduce[lambda x,y:x+y , list1]
print(num) #10

print("----------------Filter Function ----------------")
lst=[1,2,3,4,5,6,7,8,9,10]
def is_gretter_5(num):
    return num>5
gr_than_5=list(filter(is_gretter_5,lst))
print(gr_than_5) #[6, 7, 8, 9, 10]