import os
print(" reading a file line by line")
c= open ("Chapter 30/file1.txt","r")
for line in c: #it will print line by line. 
    print(line, end=" ")    

print("")
    
# # reading from a file using readline() function
# f1 = open("Chapter 30/file1.txt", "r")
# for line in f1:
#     line = f1.readline()
#     print(line)

    
# # getting the full contents of a file
# content = f1.read()
# print(content)


print("writing to a file")
f2 = open("Chapter 30/file1.txt", "w")
f2.write("The contents of this file are written using File I/O functions in python\n")
print("\n")
list_of_lines = ["hello",
                  "welcom",
                  "to", 
                  "shubhchintak Technology",
                  "Mumbai"]
f2.writelines(list_of_lines)


# f3 = open("Chapter-30/file2.txt", "r")
# content = f3.read()
# print(content)

print("checking whether a file or path exists or not using os module")
print(os.path.isfile('Chapter-30/file1.txt'))
print(os.path.isfile('Chapter 30/file1.txt'))