# Day: 86(Walrus Operator)

''' The walrus operator is a new addition in python 3.8 and allows you to sign a value to a variable within
    an expression . It assigns values to a variable as part of a larger expression '''

# Example 1:

condition= True
print(condition:=False)

# Example: 2

numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())
    print(f"Remaining numbers are: {numbers}")

# Example: 3

fruits=[]                                       # The usual way
while True:
    fruit=input("Which food do you like ? ")            
    if fruit=="quit":
        break
    fruits.append(fruit)
    
vegetables=[]                                      # The walrus operator way
while (vegetable:=input("Which vegetable you like ? ")) != "quit": 
    vegetables.append(vegetable)