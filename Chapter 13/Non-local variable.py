""" The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
    Use the keyword nonlocal to declare that the variable is not local.
"""
def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1()) #it will print hello

