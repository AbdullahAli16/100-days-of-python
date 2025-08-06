<<<<<<< HEAD
# Day: 59(Decorators)

# Decorators are a tool way to extend the functionality of a function or method without modifying its
#  source code

# *args and **kwargs:

# *args: Non-keyword variable arguments
# *args allows a function to accept any number of positional arguments (like a tuple).

# **kwargs: Keyword variable arguments
# **kwargs allows a function to accept any number of keyword arguments (like a dictionary)
#   (NOT REALLY NEEDED RIGHT NOW but imagine if we add a 'showstatus=True' like boolean argument in our add
#     function)

# A decorator is basically a function that takes another function as an argument and returns a new
#  function that modifies the behaviour of the original function. The new wfunction is often to as a 
#   decorated function.
#    For Example:

def greetings(func):
    def modify(*args,**kwargs):
        print("Hello, Good morning dear")
        func(*args,**kwargs)
        print("Thanks for using this function dear")
    return modify
    
@greetings                                  # Method: 1
def add(a,b):                  
    print (a+b)

add(1,2)

greetings(add)(4,6)                             # Method: 2




=======
# Day: 59(Decorators)

# Decorators are a tool way to extend the functionality of a function or method without modifying its
#  source code

# *args and **kwargs:

# *args: Non-keyword variable arguments
# *args allows a function to accept any number of positional arguments (like a tuple).

# **kwargs: Keyword variable arguments
# **kwargs allows a function to accept any number of keyword arguments (like a dictionary)
#   (NOT REALLY NEEDED RIGHT NOW but imagine if we add a 'showstatus=True' like boolean argument in our add
#     function)

# A decorator is basically a function that takes another function as an argument and returns a new
#  function that modifies the behaviour of the original function. The new wfunction is often to as a 
#   decorated function.
#    For Example:

def greetings(func):
    def modify(*args,**kwargs):
        print("Hello, Good morning dear")
        func(*args,**kwargs)
        print("Thanks for using this function dear")
    return modify
    
@greetings                                  # Method: 1
def add(a,b):                  
    print (a+b)

add(1,2)

greetings(add)(4,6)                             # Method: 2




>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
