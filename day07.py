<<<<<<< HEAD
#Day 7 (Calculator Exercise)
cond=True
while cond==True:
    print("Welcome to My Calculator Program")
    num1= float (input("Enter First Number: "))
    num2= float(input("Enter Second Number: "))
    op= input("Enter Operator(+,-,*,/): ")
    
    #Expressions
    if(op=="+"):
     print(num1+num2)
    elif(op=="-"):
     print(num1-num2)
    elif(op=="*"):
     print(num1*num2)
    elif(op=="/"):
     print(num1/num2)
    else:
     print("Invalid Operation try again")
     break
 
     #checking if user wants to go again
    cond=input("Do you want to perform another calculation (y/n): ")
    if(cond=="y"):
     cond=True
    elif(cond=="n"):
     cond=False
    else:
        print("Invalid character pressed, so exiting anyways")  
=======
#Day 7 (Calculator Exercise)
cond=True
while cond==True:
    print("Welcome to My Calculator Program")
    num1= float (input("Enter First Number: "))
    num2= float(input("Enter Second Number: "))
    op= input("Enter Operator(+,-,*,/): ")
    
    #Expressions
    if(op=="+"):
     print(num1+num2)
    elif(op=="-"):
     print(num1-num2)
    elif(op=="*"):
     print(num1*num2)
    elif(op=="/"):
     print(num1/num2)
    else:
     print("Invalid Operation try again")
     break
 
     #checking if user wants to go again
    cond=input("Do you want to perform another calculation (y/n): ")
    if(cond=="y"):
     cond=True
    elif(cond=="n"):
     cond=False
    else:
        print("Invalid character pressed, so exiting anyways")  
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
    