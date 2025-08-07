# Day: 72(super() keyword)

''' super() keyword is used to call the methods of parent class in child class. For example: '''

class Parent:
    def parent_method(self):
        print("This is the parent method")

class child(Parent):
    def child_method(self):
        print("This is the child method")
        super().parent_method() # We can use this method to access the methods that are defined in parent class

child_obj=child()
child_obj.child_method()

''' But if the parent class and child class have the same name for a method, then the object of the child
    class will first execute it's own function with that name, so only when the child class has no such
    method with the given name will it call the parent class function '''

# You can also access the parent class constructor if you want. For example:

class Employeee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class Developer(Employeee):
    def __init__(self, name, id, lang):
        super().__init__(name, id) # Here the constructor of Developer class has all the attributes, which
        self.lang=lang              # the constructor of Employee has and it can also add ones of its own

d2=Developer("Ali",26,"Python")

print(d2.name)
print(d2.id)
print(d2.lang)