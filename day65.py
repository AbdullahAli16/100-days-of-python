<<<<<<< HEAD
# Day: 65(Static Methods)

''' Static Methods are methods that belong to a class instead of the objects of a class. They are defined
    using the decorator @staticmethod'''
class Math:
    def __init__(self,num):
        self.num=num
        
    def add(self,b):            # Usual method for objects
        return self.num+b
    
    @staticmethod
    def substract(a,b):         # Static Method
        return a-b

math1=Math(6)

print(math1.num)
print(math1.substract(2,4))   # Objects can still access them, but they are not specifically required
                                # to access this method like usual methods
print(Math.substract(6,3))  # As you can see I don't necessarily need a object of the math class
                                # to access the substract method, I can call it by the class itself
                                
                        
'''  So the answer to the question, "Is self keyword necessary for making a method in the class?"
=======
# Day: 65(Static Methods)

''' Static Methods are methods that belong to a class instead of the objects of a class. They are defined
    using the decorator @staticmethod'''
class Math:
    def __init__(self,num):
        self.num=num
        
    def add(self,b):            # Usual method for objects
        return self.num+b
    
    @staticmethod
    def substract(a,b):         # Static Method
        return a-b

math1=Math(6)

print(math1.num)
print(math1.substract(2,4))   # Objects can still access them, but they are not specifically required
                                # to access this method like usual methods
print(Math.substract(6,3))  # As you can see I don't necessarily need a object of the math class
                                # to access the substract method, I can call it by the class itself
                                
                        
'''  So the answer to the question, "Is self keyword necessary for making a method in the class?"
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
    is "No, because we can make static methods that don't have access to the objects (self)"  '''