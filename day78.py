# Day: 78(Single Inheritance)

''' Single inheritance is the most common type of inheritance where a child class inherits the properties
    and behavioirs from it's single parent class.'''

class Animal:
    def __init__(self,animal,sound):
        self.animal=animal
        self.sound=sound

    def make_sound(self):
        return f"{self.animal} makes a sound {self.sound}!"
    
class Cat(Animal):
    def __init__(self, animal, sound, species,):
        super().__init__(animal,sound)
        self.species=species
    
    def make_sound(self):
        return f"{self.animal} {self.sound } MEOW !!!"

    def hungry(self):
        return f"{self.species} Pursssss !!!"
    
a1= Animal("Dog","Woof")

c1= Cat("Russian","Dog","Woof")
        
print(a1.make_sound())
print(c1.make_sound())