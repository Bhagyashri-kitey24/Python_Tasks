# this module is use to disassemble the function and show the bytecode

def fun(name):
    return "hello,"+ name + "!!!!"
fun('Bhagi')

import dis  
dis.dis(fun)

