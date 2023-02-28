import json
d={'course_name':'python',
'fees': '15000' 
}
f=json.dumps(d) #It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. 
print(type(f))
print(f)

print("---------------------------------------------")
import json
a='{"course_name":"python","fees": "15000", "duration":"2month"}'
b=json.loads(a)   # loads() method allows us to convert a JSON string into an equivalent python object (dictionary).
print(type(b))
print(b)

for i in b:
    print(i,b[i])


