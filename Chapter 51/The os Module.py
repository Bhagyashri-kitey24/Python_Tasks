#print(type(os.listdir("c://"))) #it will show the files and folders of c drive 
import os
# use to make a folder
#os.mkdir("Chapter 51/Folder_1")  

# this will make multiple folders
#os.makedirs("Folder1/folder2")  

#it will rename the file 
#os.rename("Folder_1.txt","Its_file.txt")    

# remove a directory
#os.rmdir('Chapter 51/Folder_1')

# get current directory
# print(os.getcwd()) 

# to check if the given path exists
path = 'Chapter 51/Folder_1.txt'
print(os.path.exists(path)) #True 