<<<<<<< HEAD
#Day 16(Switch case (Match))

x= int(input("Enter value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if (x!=40):
        print("x is not 40")
    case _ if (x!=50):
        print("x is not 50")
    case _:                            #Default case of Match in python
        print("No case satisfied. So default case running")
=======
#Day 16(Switch case (Match))

x= int(input("Enter value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if (x!=40):
        print("x is not 40")
    case _ if (x!=50):
        print("x is not 50")
    case _:                            #Default case of Match in python
        print("No case satisfied. So default case running")
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
    