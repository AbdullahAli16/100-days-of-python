# Day: 66(Instance variables VS Class variables)

class Employee:
    company="Apple"
    def __init__(self,name,raise_amount):
        self.name=name                      # Both of these  are instance variables meaning, each object of
        self.raise_amount=raise_amount       #  Employee class will have it's own name and raise_amount
        
    def info(self):
        print(f"The name of the employee is {self.name}")
    
e1=Employee("Arham",0.2)

e1.info()           # Method 1    (Ultimately changes into method 2 further at backend)
Employee.info(e1)   # Method 2


print(e1.company)

'''Note (Read Carefully):
Instance and class variables may look similar since both can be accessed and even overwritten from an
object, but the key difference lies in how they're stored and shared. Instance variables are unique to
each object — each time you create a new object, it gets its own copy. Changing it in one object does
not affect others. Class variables are shared across all instances — they are created once at the class
level. If you change the class variable using the class name (e.g., ClassName.var = value), it changes for
all objects that haven't overridden it individually. If you assign a class variable using
an object (e.g., obj.var = value), it creates or modifies an instancevariable with the same name, hiding
the class variable for that object only.
A good example could be no_of_employees in employee class, you will make this variable a class variable
instead of a instance variable'''