# Day: 58(Constructors)

# The usual way:
class Person:
    name="Ali"
    age=28
    def info(self):
        print(f"Hello, my name is {self.name} and I' am {self.age} years old.")
        
person_1= Person()
person_1.info()

# Now the same thing using constructors:
class Another_Person:
    def __init__(self, naam, umar):        # Predefined keyword for constructor
        self.name= naam
        self.age= umar
        print(f"By constructor: Another person's name is {self.name} and their age is {self.age}")
        
    def info(self):
        print(f"Another person's name is {self.name} and their age is {self.age}")
        
Another_person_1= Another_Person()   # Will give an error because it needs its 2 required arguments

# In this constructor method in total 3 arguments are required, the obvious ones are name and age
#  for the parameters 'naam' and 'umar' ,but the argument for the self parameter is the object itself
#   so whenever we create an object the content in the constructor will execute automatically.

# If nothing is assigned to the constructor it always returns 'None'.

Another_person_2= Another_Person("Maheen",80)

# Two types of constructors:
    # 1- Parameterized constructor:
    # (Example: The constructor of Another_person class is parameterized constructor because it accepts
    #  arguments along with self)
    # 2- Default constructor: It doesn't take any arguments except the self argument
    #  (Example: The constructor of Another_person class but without name and age argument)