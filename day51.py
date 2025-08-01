# Day: 51(File handling Continued: seek(), tell() and other functions)

with open('myfile.txt','r') as file:

    file.seek(5)         #Moves to the 5th bite in the file
    print(file.tell())             #It is a function which tells at which byte we are present right now in the file 
    print(file.read(2))    #Reads the next 2 bytes  

with open('myfile.txt','w') as writing:
    writing.write("Hello, brother")
    print(writing.truncate(5))   #Only keeps the bytes that are specified as parameters and deletes the rest

with open('myfile.txt','r') as writing:
    print(writing.read())
    #The out put here of truncate will be: 'Hello'