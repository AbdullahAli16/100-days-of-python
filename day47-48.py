# Day: 47(Excercise 4 solution)

# Day: 48(Local and Global Variables)

var_1= 7          #Global variable

def func():
    var_1=2         #Local variable
    print(f"The local variable is: {var_1}")

func()
print(f"The global variable is: {var_1}")

#Local variables are destroyed once the function is executed, but global varibales don't

# You can access a global variable in a function by using the global keyword before the name of the variable
   # however, this is not a good practice and it's better to avoid it