# Day: 53(Map,Filter and Reduce)

def cube(x):
    return x*x*x

my_list=[2,6,3,9,7]

result_list=[]

for index,listitem in enumerate(my_list):
   result_list.append(cube(listitem)) 
   print(f"This is the {index+1} insertion, now the new list is: {result_list}")    #The usual way


# now let's use map:

mapped_list= map(cube,my_list)
print(mapped_list)        #returns a map object but you can covert it easily into a list by typecasting
print(list(mapped_list))      #Provides the same output as above but more simple and easy to understand

# You didn't even had to define a function, you can just a lambda function
mapped_list_using_lambda= map(lambda x: x*x*x,my_list)
print((f"Using lambda in map function: {list(mapped_list_using_lambda)}"))      #Same output


# Filter function:
def even(x):
    if x%2==0:
        return x
filtered_list= filter(even,my_list)
print(filtered_list)         #returns a filter object same as map
print((f"The list of the elements that are are even in my_list is: {list(filtered_list)}"))

#By using lambda function:

filtered_list_using_lambda=filter(lambda x: x%2==0,my_list)
print(f"Using lambda in filter function: {list(filtered_list_using_lambda)}")

# Reduce function:
from functools import reduce

sum= reduce(lambda x,y: x+y,my_list)                  # Returns a single value
print(sum)