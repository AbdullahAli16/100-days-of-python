# Day: 81(Hybrid or Hierarchical Inheritance)

''' Hybrid Inheritance is the combination of multiple inheritance and single inheritance in OOP. In
    Hybrid Inheritance multiple inheritance is used to inherit the properties of multiple base classes
    into a single derived class and single inheritance is used to inherit the properties of that derived
    class into a sub-derived class. For example: '''

class Baseclass1:
    pass

class Baseclass2:
    pass

class Derivedclass(Baseclass1,Baseclass2):
    pass

class SubDerivedclass(Derivedclass):
    pass



''' Heirarchical Inheritance is the type of inheritance in OOP where mutliple subclasses inherit from a
    single base class'''

class Parentclass:
    pass

class Childclass1(Parentclass):
    pass

class Childclass2(Parentclass):
    pass