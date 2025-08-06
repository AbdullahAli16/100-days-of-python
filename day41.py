<<<<<<< HEAD
# Day 41: (Short hand if-else statements)

num1= 300
num2= 3300

print("No 1 is greater than no 2") if num1>num2 else print("Equals") if num1==num2 else print ("No 2 is greater")

num3= 200 if num1<num2 else 1
print(num3)

# Demonstration using a side by side comparison

condition= True
valuetrue= True
valuefalse= False

# Method 1(More convenient and professional)
result = valuetrue if condition else valuefalse

#Method 2(Simple but unnecessary and not suitable for short approaches)
if condition:
    result= valuetrue
else:
=======
# Day 41: (Short hand if-else statements)

num1= 300
num2= 3300

print("No 1 is greater than no 2") if num1>num2 else print("Equals") if num1==num2 else print ("No 2 is greater")

num3= 200 if num1<num2 else 1
print(num3)

# Demonstration using a side by side comparison

condition= True
valuetrue= True
valuefalse= False

# Method 1(More convenient and professional)
result = valuetrue if condition else valuefalse

#Method 2(Simple but unnecessary and not suitable for short approaches)
if condition:
    result= valuetrue
else:
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
    result= valuefalse