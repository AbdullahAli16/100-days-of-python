<<<<<<< HEAD
# Day: 54( The different between 'is' and '==' operator )

# Both 'is' and '== ' are comparison operators

# 'is' operator checks the memory address and '==' checks the value

list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)         #Output: False
print(list1 == list2)           #Output: True


a = True                           # Variable 'a' and 'b' have the same memory address
b = True
print(a is b)               #Output: True
print(a == b)                #Output: True


''' Explanation: Both are true in the second expression because when we declare a constant variable in
python, and when refer to the same value again, python create a new memory address for it and just assigns
the same memory address to as many constants as we declare(same goes for tuples, boolean values and None),
=======
# Day: 54( The different between 'is' and '==' operator )

# Both 'is' and '== ' are comparison operators

# 'is' operator checks the memory address and '==' checks the value

list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)         #Output: False
print(list1 == list2)           #Output: True


a = True                           # Variable 'a' and 'b' have the same memory address
b = True
print(a is b)               #Output: True
print(a == b)                #Output: True


''' Explanation: Both are true in the second expression because when we declare a constant variable in
python, and when refer to the same value again, python create a new memory address for it and just assigns
the same memory address to as many constants as we declare(same goes for tuples, boolean values and None),
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
but this isnt the case for list and they can change over time as we perform operations on them'''