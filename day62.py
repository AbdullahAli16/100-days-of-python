# Day: 62(Access Modifiers)

# Public variables and methods can be accessed outside the class

# Private variables and methods can only be accessed inside the class 

# Protected variables and methods can only be accessed within the class and within the sub-class

class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age
        print("Oye geo goe")
        
s1= Student("Ali",52)
print(s1._name)                     # All the methods(member functions) and variables in python are by 
print(s1._age)                          # default "public"

class Employee:
    def __init__(self,name,id):         # In python there is no specific private access modifier, but there 
        self.__name=name                    # is a convention has been established to indicate that a variable
        self.__id=id                            # or method should be considered should be considered private
        print("Ghulam aya ghulam aya")              # by naming it with a double underscore like, __name
        
e1= Employee("Ali",666)
print(e1.__name)               # The access is blocked by python if you try to access the private                      
                                     # method or variable just like any other private variable but,
print(e1._Employee__name)                    # you can still access them by using this syntax

# This syntax above is called "Name mangling" in python, name mangling is basically a technique used to
#  protect class-private and superclass-private attributes from being accidently overwritten by sub classes
#    because it is possible that by mistake we overwrite the __name which was supposed to be private.

# Nothing related to access modiefiers is  enforced in python, and it ultimately depends on your workspace 
#  but whenever you declare a variable using '__' convention, python would not let you directly access it,
#   unless you use the "Name mangling" method.