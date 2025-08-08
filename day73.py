# Day: 73(Magic/Dunder Methods)

''' Magic/Dunder (short for double underscore) methods are hooks that let you customize how your objects
    behave with built in operations, instead of calling them manually like other methods, they are called
    automatically by python '''
class Employee:
    def __init__(self,name):        # Automatically runs when you create an object
        self.name=name
        print("This is __init__ running")
        
    def __str__(self):              # Runs when you call print on an object
        return(f"This is __str__ runnning")
        
    def __len__(self):              # Lets you use the built-in len on an object
        print (f"This is __len__ running:")
        return len(self.name)

    def __repr__(self):             # runs when you write 'object'(only in python shell/Jupyter notebook) or 
        return ("This is repr running") # 'repr(object)' (in a normal py script) great for debugging    
    
    def __call__(self):             # Lets you call an object like a function (called when you use paranthesis
        return ("This is __call__ runnning")  # after an object) like: object()


e1= Employee("hamza")       # __init__
print(e1)                   # __str__
print(len(e1))              # __len__
print(repr(e1))             # __repr__
print(e1())                 # __call__