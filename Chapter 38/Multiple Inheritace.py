class C1:
    Back="Oracle DB & Java"
    def backend(self):
        print("Backend tast implemented using:",self.Back)
class C2:
    Front="HTML , CSS ,JavaScript"
    def frontend(self):
        print("frontend tast implemented using:",self.Front)

class Teamlead(C1,C2): #mutiple Class implemented 
    def show(self):
        print("Dynamic Website created......")
T=Teamlead()
T.backend()       
T.frontend()
T.show()