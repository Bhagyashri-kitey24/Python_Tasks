#String Formating

me="Bhagyashri"
a=" This is %s" %me #This is Bhagyashri
print(a)

#named indexes:
txt1="welcome to{fname}{lname}".format(fname="WsCube",lname="Tech") # welcome toWardha Maharashtra

#numbered indexes:
txt2="welcome to{0}{1}".format("Wardha","Maharashtra")#welcome toWardha Maharashtra

#empty placeholder:
txt3="welcome to {} {}".format("Wardha","Maharashtra")#welcome to Wardha Maharashtra
print(txt1)
print(txt2)
print(txt3)

print("---Padding and truncating strings, combined---")
a="hello"
b= "world"
print(a+" "+b)