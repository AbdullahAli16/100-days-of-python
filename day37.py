#Day 37 (Finally keyword)
# The content after the finally keyword is always executed
def func():
    try:
        list=[1,5,9]
        n=int(input("Enter a number: "))
        print(list[n])
        return ("This is one",1)
    except:
        print("An error occured")
        return ("This is zero",0)
    finally:
        print("It is always executed") 

print(func())
    
# but the most common question about it is that even if we don't use the finally keyword the content will execute
# regardless and they are right, but if we wrap it all into a function and then try it, only the content is 
# written after the finally keyword, will end up getting executed
# You can test it by wrapping this all into a function and then running the program again