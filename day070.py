# Day: 70(Class Methods as Alternative Constructors)

'''You might be wondering, what is the use for this ???

    Well, in some cases we might need to handle data in different formats at the same time, like:'''


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def forstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

p1= Person("Ali",52)

print(p1.name)
print(p1.age)

'''But if we get data in another form too ???'''

person2="Arham-21"
p2= Person(person2.split("-")[0],person2.split("-")[1])   # We can do this, but we would have to do it every
print(p2.name)                                              # single time
print(p2.age)


# Although we can define a constructor like class method in the class to handle each format of data, so now:

person3="Arqam-231"
p3= Person.forstr(person3)
print(p3.name)
print(p3.age)

