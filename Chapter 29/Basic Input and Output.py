#read the file
f= open ("Chapter 29/file.txt","r")
content= f.read() #Hello......i am in text file This is Bhagyashri.........
print(content)

a= open ("Chapter 29/file.txt","r")
content1= a.read(6) #Hello
print(content1)

print("----inline-----")
print("#it will print character by character")

b= open ("Chapter 29/file.txt","r")
content= b.read(5) 
for line in content: #it will print character by character. like h e l l o  
    print(line)
        
print("#it will print line by line")
c= open ("Chapter 29/file.txt","r")
for line in c: #it will print line by line. 
    print(line, end=" ")    

print("\n")
f.close()
print("----------Printing a string without a newline at the end----------")
print("Hello, ", end="\n")
print("World!")

a=1
b=2
c=3
print(a,b,c,end="||")
print(a,b,c) # 1 2 3||1 2 3

print()

print(a,b,c,end=" ")
print(a,b,c) #1 2 3 1 2 3

print("----------readline()----------")
abc= open ("Chapter 29/file.txt","r")
print(abc.readline()) #print one line
print(abc.readline()) #print another one line

print("----------readlines()----------")
var= open ("Chapter 29/file.txt","r")
print(var.readlines()) #print list of lines 
#['Hello......i am in text file\n', 'This is Bhagyashri.........']
