#Day 22(List)
rand_List=[3,6,9,"Ali",True,False]
print(rand_List[1:5:2])

lst2=[i+i for i in range(4)] #Any expression could be passed here
print(lst2)

lst2=[i+i for i in range(4) if (i%2==0) or (i%3==0)] #If else can also be applied here
print(lst2)

#Day 23(List Methods)
'''.append() == adds an elements in the list from end
    .sort() == sorts in ascending order
    .sort(reverse= True) == sorts in descending order
    .reverse() == reverses a list
    .index(a) == returns the index of first occurence of element 'a'
    .count(a) == returns the number of times element 'a' occured
    .copy() == makes a clone of that list (cuz if you use list1=list2 and then change list2, list1 changes too)
    .insert(1,a) == to insert an element 'a' at a specific index '1'
    .extend(a) == add the whole list 'a' at the end of an existing list
    '''