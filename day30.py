# Day 30(Recursion)

#Defining something in terms of itself is called recursion

#Example:
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))

#It will work like: 
# 5* factorial(4)
# 5* 4 factorial(3)
# 5* 4 * 3 factorial(2)
# 5* 4 * 3 *2 factorial(1)

#Quick quiz: Make a fibonacchi sequence program

def fib_series(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    elif (n<0):
        print("Sorry, fibonacchi series include only positive numbers")
    else:
        return(fib_series(n-1)+fib_series(n-2))
    
n= int(input("Enter the number for the fibonacchi series: "))
result= fib_series(n)
print(result)
