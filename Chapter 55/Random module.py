import random
n= random.randint(2,8)
print(n) #it will print random value from 2 to 8

n= random.randrange(2,8)
print(n) #it will print random value from 2 to 7

l=[1,2,8,9,10]
lc=random.choice(l)
print(lc)


b= random.random()
print(b) #it will print random float value between 0 to 1


l=[5,8,9,7,5,6,1]
c= random.shuffle(l) #shuffle the list element
print(l)

u= random.uniform(3,9)
print(u) #float value