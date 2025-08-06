# Day: 69(Class Methods)

# Classes arae used to make built-in data types

class Employee:
    company="apple"
    def __init__(self,name):
        self.name=name
    
    def showinfo(self):
        print(f"The name of the employee is {self.name} and their company name is: {self.company}")
        
    @classmethod
    def change_company(cls,new_company):   #Without the @classmethod decorator it won't work
        cls.company=new_company

''' In methods, the first parameter(self) which they get is an instance, but in class methods the first
    parameter is the class instead of a variable.
    A class method is a method that is bound to the class, not the object (instance).
    It can access and modify class variables, but not instance variables (unless instances are passed manually).
    It is marked with a @classmethod decorator. 
    cls and self are not restricted keywords, but using them is a good practice. '''

e1= Employee("Ali")

e1.showinfo()

e1.company="tesla"
e1.showinfo()