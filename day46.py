# Day: 46(OS module) (Don't run multiple outputs alert)

import os

os.mkdir("new") #Makes a new directory

# Creates multiple folders in an instant

if (not os.path.exists("data")):
    for i in range(1,101):
        os.mkdir(f"new/Day{i}")
    
    
# # To rename muliple files

for i in range(1,101):
    os.rename(f"new/Day{i}",f"new/Tutorial{i}")



folders= os.listdir("new")
print(folders)              #Returns a list of all the folders in a directory

for folder in folders:
    print(folder)
    print(os.listdir(f"new/{folder}"))     #List of Files in each folder
    
address= os.getcwd()
print(address)    #Tells the path of the directory you are presesnt in

os.chdir()     #Can be used to change directory(enter path in paranthesis)

for o in (1,101):
    os.remove(f"new/Tutorial{o}")   #You can only delete file using the os module and also empty directories
                                        # by using os.rmdir() and for deleting non-empty directories
                                            # use 'rmtree' function of 'shutill' module (explore it)