x=10 #This is a global variable 
def fun1():
    global x
    y= x+2  # Y This is a local variable 
    print("inside x:",x)
    print("inside y:",y)
fun1()
print("outside x:",x)
#print("outside y:",y) this will not run outside of the function
