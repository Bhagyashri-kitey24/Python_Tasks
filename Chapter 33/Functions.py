# function is a block of code that performs the specific task
#example of function
def greet(): # created the function
 print("Hello")
greet() #function calling

print("---------- Defining a function with an arbitrary number of arguments ----------")
def func(*args): #* expands the list
     # args will be a tuple containing all values that are passed in
 for i in args:
    print(i)
func(1, 2, 3) # Calling it with 3 arguments
print()

print("---------- function arguments and parameter passing ----------")
def isgreater(a,b):
    if (a>=b):
        print("first number is greater or equal")
    else:
        print("second number is greater")
a=9
b=5
isgreater(a,b)

print()
print("Default argument")
def average(a=9,b=1):
    print("the average is :",(a+b)/2)
average()  
print()

print("required argument")
def average(a,b=1): 
    print(" required argument example :",(a+b)/2)
average(a=2)  # you must have to give the valuue of a it is required

print("variable length argument")
def average(*numbers): 
    sum=0
    for i in numbers:
        sum=sum+i
    print(" average is :",sum/len(numbers))    
average(5,6,7)  
  
    
print()    
print("----------  Lambda (Inline/Anonymous) Functions ----------")
greet_me = lambda: "Hello" #The lambda keyword creates an inline function that contains a single expression.
print(greet_me) 





