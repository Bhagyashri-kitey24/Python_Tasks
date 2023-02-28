import os
# print(dir(os)) 
#print(os.getcwd()) #it will show current working directory

"""f= open ("Chapter 29/file.txt","r")
cont=f.read()
print(cont)""" 

#print(type(os.listdir("c://"))) #it will show the files and folders of c drive 
#os.mkdir("Folder_name") # use to make a folder 
#os.makedirs("Folder1/folder2")  # this will make multiple folders
#os.rename("file.txt","Its_file.txt")

#If the given path exists 
# #to check if the given path exists
path = 'Chapter 29/file.txt'
print(os.path.exists(path)) #True
