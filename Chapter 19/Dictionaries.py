print("------Accessing dictionary elements usig index number------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
print(dict1["01"])
print(dict1["02"])
print(dict1["03"])
print(dict1["04"])
print(dict1["05"])
print(dict1["06"])

print("------Iterating Over a Dictionary------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
for key in dict1:
 print(key, dict1[key])
 
print("-------Accessing keys and values-------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
print(dict1.keys()) #dict_keys(['01', '02', '03', '04', '05', '06'])

print("---------Creating an ordered dictionary--------")
from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4

for key in d:
 print(key, d[key])# Outputs "first 1", "second 2", "third 3", "last 4"
 
print("--------Dictionary Operation-------")
print("------update()------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
dict1.update({"07":"Darsh"})
print(dict1) #{'01': 'bhagi', '02': 'appu', '03': 'sanji', '04': 'dami', '05': 'dipa', '06': 'ishu', '07': 'Darsh'}

print("------__len__()------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
a=dict1.__len__() # this will find length of number of pair
print("dict1 contain",a,"Pairs") #dict1 contain 6 Pairs

print("------clear------")
dict1={"01":"bhagi","02":"appu","03":"sanji","04":"dami","05":"dipa","06":"ishu"}
dict1.clear()
print("after clear operation",dict1)

