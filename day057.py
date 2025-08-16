# Day: 57(Classes and Objects)

class enemy:
    grade= "regular"
    weapon= "pistol"
    age= 35
    def info(self):
        print(f"It is a {self.grade} enemy. It has {self.weapon} as a weapon. It's age is {self.age}")
    
e1= enemy()
e1.grade= "Heavy"
e1.weapon= "Machine gun"
e1.info()           # The value for age wasnt specifically provided for e1 object so it retains
                        # the one provided from enemy class
                        
                        
# The self keyword refers to the object that on which the method is being called
# For example: If you have another object like e1 say e2

e2= enemy()
e2.grade="ninja"
e2.weapon="Katana"
e2.info()  # The self keyword here refers to the object e2, and earlier when we called "e1.info()", it
            # referred to e1, in simple words it refers to the object that is being called at the moment
              # by the method (it will always be a single method because only one object can be called
                # at the moment)

