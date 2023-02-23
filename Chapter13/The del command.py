#The command del v removes the variable from its scope
l=[1,2,5,6,7,3]
del l[2] #it will delete 5  because it is on l index 2
print(l)

l1=[1,2,5,8,9,0,6,7,3]
del l1[-1] #it will delete 3  because it is on -1  index of l1
print(l1) #it will print [1, 2, 5, 8, 9, 0, 6, 7]
del l1[-1] #it will delete 3  because it is on -1  index of l1
print(l1) #it will print [1, 2, 5, 8, 9, 0, 6]

x = [0, 1, 2, 3, 4]
del x[1:3]
print(x) #[0, 3, 4]