# Decorator is use too change the function of update the function.
# Decorator takes another funcation as an argument and returns the new function that modify the behaviour of original function, the new function often consider as a decorated function.
# Decorator modify the function
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

hello()
#output:
#Good Morning
#Hello World
#Thanks for using this function