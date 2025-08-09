# Day: 74(Method Overriding)

''' Method overriding is a powerful feature in OOP, which allows you to redefine a method of parent
    class in a child class. The method in the child class is said to override the method in the parent class '''

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    
    def area(self):               # Area method of AREA class overriden by area method of CIRCLE class
        return 3.14 * super().area() # or instead of this you can also use self.radius **2 
        
s1= Shape(5,5)
print(s1.area())

c1= Circle(7)
print(c1.area())