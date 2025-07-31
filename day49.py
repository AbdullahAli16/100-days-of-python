# Day: 49(File Handling)

new_file=open('myfile.txt','r')   #Method to open a file 

#  r means read
#  w means write (existing content will be removed)
#  a means append (it will appear after the existing content)
#  x means create (if file already exists it will throw an error)
#  in case of no parameter it will be considered r by default

# apart from these 4 there is t and b, they are used to specify the format in which the file is to be handled
    # for example: 'rt' "means read a text file" and 'b' is used to read files like images, pdfs etc

#   If you tried to open a file in write mode and it doesnt exist, it will be created

print(new_file) # Returns an object

text=new_file.read()
print(text)

new_file.close()             # Closes the opened file(must)

with open("myfile.txt","a") as new_file:
    new_file.write("No need to close now")        # You don't need to run the close method when you use 
                                                    # with keyword because it closes automatically