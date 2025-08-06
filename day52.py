<<<<<<< HEAD
# Day: 52(Lambda Functions)

def double(x):                      # Usual Function
    return x*2

double= lambda x: x*2               #Anonymous function performing the same operation
print(double(3))

# Lambda functions are a good approach when you have to define small function in your program

average= lambda x,y: (x+y)/2
print(average(8,2))


totalmarks= lambda x,y,z: (x+y+z)/3
print(totalmarks(20,30,40))

# It can include multiple lines but not a good approach

# The usual use of lamba function lies when you pass a function as an argument

def cube10(func, value):
    return(func(value)+10)

cube= lambda x: x*x*x

print(cube10(cube,2)) 

#or we can also do

print(cube10(lambda x:x*x*x,2))

=======
# Day: 52(Lambda Functions)

def double(x):                      # Usual Function
    return x*2

double= lambda x: x*2               #Anonymous function performing the same operation
print(double(3))

# Lambda functions are a good approach when you have to define small function in your program

average= lambda x,y: (x+y)/2
print(average(8,2))


totalmarks= lambda x,y,z: (x+y+z)/3
print(totalmarks(20,30,40))

# It can include multiple lines but not a good approach

# The usual use of lamba function lies when you pass a function as an argument

def cube10(func, value):
    return(func(value)+10)

cube= lambda x: x*x*x

print(cube10(cube,2)) 

#or we can also do

print(cube10(lambda x:x*x*x,2))

>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
 