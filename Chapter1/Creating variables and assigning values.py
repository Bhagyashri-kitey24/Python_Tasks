#Creating variables and assigning values

#integer value
a=10 
_b=10021142 #variable can be start with special symbol but python only support underscore special symbol.
print(a,_b) 
#floating point
pi= 3.14
print(pi)
#string 
Name="Bhagyashri" # any value which is written in " " double or ' ' quotes python will consider it as string value

#boolean
q=True
print(q)

# Empty value or null data type
x = None
print(x)

#Variable assignment

a=1
print(a)

a,b,c,d=1,2,3,4
print(a,b,c,d)

a, b, _ = 1, 2, 3
print(a, b) #This dummy variable can have any name, but it is conventional to use the underscore (_) for assigning unwanted values:

x = y = z = 1 # all three names a, b and c refer to same int object with value 1
print(x, y, z)

x = y = [7, 8, 9] # x and y refer to the same list object just created, [7, 8, 9]
x = [13, 8, 9] # x now refers to a different list object just created, [13, 8, 9]
print(y) # y still refers to the list it was first assigned
# Output: [7, 8, 9]

x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7, 8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y) 

x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print (x[2])

print (x[2][1]) #it will print the value of 2 index of x[2] =4


""""a, b, c = 1, 2
=> Traceback (most recent call last):
=> File "name.py", line N, in <module>
=> a, b, c = 1, 2
=> ValueError: need more than 2 values to unpack

a, b = 1, 2, 3
=> Traceback (most recent call last):
=> File "name.py", line N, in <module>
=> a, b = 1, 2, 3
=> ValueError: too many values to unpack"""

x = True # valid
print(x)
_y = True # valid
print(_y)
 
""" 9x = False # starts with numeral variable can't start with digit
=> SyntaxError: invalid syntax 
 $y = False # starts with symbol
=> SyntaxError: invalid syntax ,
python only allow _ special symbol"""

roll_no=401
name="Ram"
perc=98.99
fees=53206
Pass_or_fail=True

print("\n Roll no. is:",roll_no ,"\n Name is:",name,"\n Percentage is:",perc,"\n fees:",fees,"\n Pass or Fail:",Pass_or_fail)
print("Roll no. is:",type(roll_no),"Name is:",type(name),"Percentage is:",type(perc),"fees:",type(fees),"Pass or Fail:",type(Pass_or_fail))
print(type(roll_no),type(name),type(perc),type(fees),type(Pass_or_fail))

