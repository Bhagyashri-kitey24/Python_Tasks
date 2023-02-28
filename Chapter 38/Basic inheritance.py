#Inheritance 
class Father:
    def lands(self):
        print("Having 50 ekar Lands")

class Son (Father):
    def money(self):
        print("Having 10 lakhs money")

s=Son()
s.lands() # accessing the property of Father class using child class object
s.money()

#output:
#Having 50 ekar Lands
#Having 10 lakhs money

