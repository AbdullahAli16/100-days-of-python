# Day: 91(Generators)

''' Generators in python are special type of functions that allow you to create an iterable
    sequence of values. They are a powerful tool for working with large and complex datasets
    because, they allow you to generate values on-the-fly, rather than creating and storing
    the entire sequence in memory '''

def mera_generator():
    for i in range (500000000000):
        yield i

g1=mera_generator()

print(next(g1)) # 0
print(next(g1)) # 1
print(next(g1)) # 2
print(next(g1)) # 3
print(next(g1)) # 4
print(next(g1)) # 5

# It only increments when you call the next method on the object
