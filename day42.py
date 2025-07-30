# Day 42 (Enumerate Function)

marks = [89,74,64,91,57]

for index, mark in enumerate(marks):
    print(f"On index {index} is {mark} marks.")    
    
#It returns a tuple but because we used 2 variables, the tuple is unpacked
# Example: 
for studentmark in enumerate(marks):
    print(studentmark)
    
# You can also specify the start index in enumerate function like: enumeratte(marks,start=1) (start is predefined)



# --------------x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x---------- (not related and is being used in day43.py)
