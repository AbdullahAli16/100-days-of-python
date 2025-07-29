#Day 20(Functions)
def calculateGmean(a,b):
    print((a*b)/(a+b))
    if a>b:
        print("A is greater")
    else:
        print("B is greater or equal")

def emptyFunction ():
    pass #Doesnt generate an error

calculateGmean(1,4)

#Day 21(Function arguments)
def average(*numbers): #Arguments weill be taken in the form of a tuple
    sum=0
    for n in numbers:
        sum += n
    print("Average is:",sum/len(numbers))
        
average(2,2,2)

def name(**name): #Arguments will be taken in the form of a dictionay
    print("Hello,", name["fname"] ,name["mname"], name["lname"])
    
name(mname="Muhammad", lname="Ali", fname="Abdullah")

'''return statement is used insted of print, if the result is to be stored in a variable and would be used further
    if there are multiple return statements only the first one will be executed'''