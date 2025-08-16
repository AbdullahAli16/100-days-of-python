# Day: 92(Function Caching)

''' Function caching is a technique for improving the performance of a program by storing the results
    of a function call so that you can reuse the results instead of recomputing them everytime the
    function is called '''

import functools
import time

@functools.lru_cache(maxsize=None)
def printer(n):
    time.sleep(5)
    return n*5
    
print(printer(20))
print("Printed 20\n")

print(printer(6))
print("Printed 6\n")

''' time.sleep wont affect these last 2 because earlier we calculated the same expression, so instead of
    recalculating, it just fetches both of them from cache memory '''

print(printer(20))    
print("Printed 20")

print(printer(6))
print("Printed 6")

# It will stop here again, because this is a new calculation

print(printer(7))
print("Printed 7")
