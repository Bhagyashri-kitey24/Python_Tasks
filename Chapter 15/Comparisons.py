print("----------Chain Comparisons---------------")
a,b,c= 10,5,2 
if a > b > c:   # it is similar to "a>b and b>c"
    print("A is biggest")
    
print("------------Comparison by `is` vs `==`-------------")
a = 'Python is fun!'
b = 'Python is fun!'
print(a == b) # returns True
print(a is b) # returns True

print("------------Greater than or less than-------------")
print(12 > 4) # True
print(12 < 4) # False
print(1 < 4) # True

print("------------Not equals to-------------")
print(12 != 1) # True
print(12 != '12') # True
print('12' != '12') # False

print("------------equals to-------------")
print(12 == 1) # False
print(12 == '12') # False
print('12' == '12') # True
print(12 == 12) # True
