#list function
color=["red","black","voilet",2,"indigo","pink",54,56,"white","green","gray"]
print(color)

num=[1,8,2,5,7,9,6,3]
num.sort() #[1, 2, 3, 5, 6, 7, 8, 9]
num.reverse() # [9, 8, 7, 6, 5, 3, 2, 1]
print(num)

#Lists as arguments are just another variable:
def func(myList):
     for item in myList:
        print(item)
func([1,2,3,5,7])        