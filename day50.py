# Day: 50(File Handling continued: read(),readlines() and other methods)

line= open("myfile.txt",'r')
i=0
while True:
    i+=1
    marks= line.readline()           # used to read a single line
    if not marks:
        break   
    s1= int(marks.split(",")[0])
    s2= int(marks.split(",")[1])
    s3= int(marks.split(",")[2])
    
    print(f"The marks of student {i} in Science is: {s1}")
    print(f"The marks of student {i} in English is: {s2}")
    print(f"The marks of student {i} in Sindhi is: {s3}")
    
    print(f"\nThis is the list of all the marks of student {i}: {marks}")


file= open("myfile.txt","a")
lines=["Hello pehli baar\n","Hello doosri baar\n","Hello teesri baar\n"]
text=file.writelines(lines)
print(text)            # This will print none