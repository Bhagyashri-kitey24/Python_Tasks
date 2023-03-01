import json
#read json file.
file= open("Chapter 49/Post.json","r")
a=file.read()
final_data=json.loads(a)

print(final_data) #print all data which is present in json file.