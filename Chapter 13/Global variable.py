x=10 #This is a global variable 
def fun1():
    global x
    print("inside x:",x)
fun1()
print("outside x:",x)