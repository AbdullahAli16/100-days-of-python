# Day 33(Dictionaries)

#Dictionary are collection of data items in key value pairs

info ={'name':"Abdullah", 'age':20, 'eligible':True    }
print(info['name']) #will generate an error if not found
print(info.get('name2'))   #will not generate an error and will display 'none' if not found
#.keys(), .values(), .items()

for key in info.keys(): # or for key value in info.items():
    print(f"The value correspodning to the key {key} is {info[key]}")
    
