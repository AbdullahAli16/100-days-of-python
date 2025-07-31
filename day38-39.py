#Day 38 (Raising custom errors)

num= int(input("Enter a number (between 7 and 15): "))
if num<7 or num>15:
    raise ValueError("Value should be between 7 and 16")

# ValueError, IndexError etc are built in errors in python which we can use but we can also define our own errors
# custom errors to be exact by defining a class of that custom error

#Quick quiz:

num= input("Enter a number (between 7 and 15): ")
if num=="yes":
   print("no error")
elif int(num)<7 or int(num)>15:
    raise ValueError("Value should be between 7 and 16")

#Day 39 (Ex 3: Kaun Banega crorepati solution)
