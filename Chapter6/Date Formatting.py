from datetime import datetime
print("To show date and time")
dt=datetime.today() #it will show current date and time
print(dt)
print()

#Outputting datetime object to string
newd1 = dt.strftime("%B,%d,%Y") 
print(newd1)
print()

newd1 = dt.strftime("%d,%b,%Y") 
print(newd1)
print()

newd1 = dt.strftime("%d,%m,%Y") 
print(newd1)
print()

newd1 = dt.strftime("%H:%M:%S") 
print(newd1)
print()

newd1 = dt.strftime("%I:%M:%S") 
print(newd1)
print()

#Parsing string to datetime object
from datetime import datetime
datetime_string = 'Feb 20 2023, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_string, datetime_string_format)

