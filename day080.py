# Day: 80(Mulltilevel Inheritance)

''' Multilevel inheritance is a type of inheritance  in OOP where a derived class inherits from another
    derived class '''

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed=breed

    def show_info(self):
        Animal.show_info(self)
        print(f"Breed: {self.breed}")

class Husky(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Husky")    
        self.color=color
    
    def show_info(self):
        Dog.show_info(self)
        print(f"Color: {self.color}")

h1=Husky("Roxy","Grayish")
h1.show_info() 

''' Object of Husky class has access to all the methods and variables of Dog and Animal class. Purpose of
    multi-level inheritance is to reduce repeatation of the same code '''