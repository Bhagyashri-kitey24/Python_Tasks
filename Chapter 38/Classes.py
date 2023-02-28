#class and object 
class Employee:
    name ="Ramya"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

#creat object
a= Employee() 
b= Employee()

b.name="Nayannya"
b.occupation="Software Tester"
a.info()
b.info()
    
