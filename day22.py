# Day: 22(Lists)

rand_List=[3,6,9,"Ali",True,False]
print(rand_List[1:5:2])

lst2=[i+i for i in range(4)] #Any expression could be passed here
print(lst2)

lst2=[i+i for i in range(4) if (i%2==0) or (i%3==0)] #If else can also be applied here
print(lst2)