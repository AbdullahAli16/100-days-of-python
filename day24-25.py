#Day 24(Tuples)
tup =(1,3) # If you want to declare a tuple consisiting of just a single element then you have to pass coma after the first element
tup1=(1) #type of tup1 is integer
tup2=(1,) #type of tup2 in tuple
print(type(tup),tup)

#Day 25(Tuples Methods)
'''.count(a)== tells the number of times a occured in a tuple
    .index(a)== returns the first index number on which a element is found 
    can also be used to slice a particular range of indexes ex .index(a,startindex,endindex-1)
    (will raise a value error if elementis not present in tuple)
    .length(a)== tells the length of the tuple'''