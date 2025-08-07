# Day: 71(dir,__dict__ and help method)

''' When you are dealing with a new class, or an unknown class you can use these three functions on it's
   objects to figure out what is that class capable of doing. '''

# Using dir:

x= [1,2,3]
print(dir(x))    # This returns a list of all the attributes and functions available for that object

# This can be useful for discovering what you can do with an object

# You can print an attribute or a function to know about it

print(x.__reduce__)

# using the __dict__ attribute:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
person1= person("Abdullah",81)

print(person1.__dict__)  # Returns a dictionary of the object's attributes along with
                            #the values assigned to them

# using the help() method:

print(help(person1))

''' help() function is used to get help documentation for an object, including a
description of it's attributes and methods. '''