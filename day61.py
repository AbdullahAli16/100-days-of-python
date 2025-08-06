# Day: 61(Inheritance)

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showinfo(self):
        print(f"The employee id is: {self.id} and their name is: {self.name}")

class Programmer(Employee):          # Child class of Employee (It will have all the attributes and methods
    def showrole(self):
        print("Developer nigga hai sala")                                   # of the Employee class but also of its own )
    
e1= Employee("Aliyan",420)
e1.showinfo()

e2= Programmer("Ali",120)
e2.showinfo()
e2.showrole()

