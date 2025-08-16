# Day: 79(Multiple Inheritance)

''' Multiple inheritance is a powerful feature in OOP that allows a class to inherit attributes and methods
    from multiple parent classes '''
class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
         self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer):  # whichever class is mentioned first, after searching within
    def __init__(self,name,dance):          # it will first search within that class
         self.name=name
         self.dance=dance
         
ed1=DancerEmployee("Micheal Jackson","Break-dance")

ed1.show()


# You can check the MRO(Method Resolution Order) of any class by:
print(DancerEmployee.mro())