# Day: 97(Multi-threading)

''' Multi threading is basically a technique in programming that allows mutipple threads of execution
    to run concurrently within a single process. In python we can use the threading module to implement it '''

import threading, time
from concurrent.futures import ThreadPoolExecutor

# The Usual Way
def func_1(seconds):
    time.sleep(seconds)
    print(f"Function 1 is done executing after: {seconds} seconds")
    
def func_2(seconds):
    time.sleep(seconds)
    print(f"Function 2 is done executing after: {seconds} seconds")

def func_3(seconds):
    time.sleep(seconds)
    print(f"Function 3 is done executing after: {seconds} seconds")

print("The usual way: ")
func_1(4)
func_2(4)
func_3(4)

# Using Multi-threading
print("This is using threading: ")
# f1=threading.Thread(target=func_1, args=[4]).start()
# f2=threading.Thread(target=func_2, args=[4]).start()
# f3=threading.Thread(target=func_3, args=[4]).start()

# f1.join()
# f2.join()
# f3.join()

print("All function done using threading")

''' If you have content to execute after the threads you need to call start() and join() separately on the
    threads because when you call start on the direct expression of the threads it returns NONE so you would
    be calling the join method on NONE which wont return anything however in another case when you dont have
    anything to execute afterwards then we dont need join and we can call start in the expression itself.
    (daeman=True) means that the main program won't wait for the threads to execute and the program will
    finish early. (In the example provided above the three threads will never execute because the main 
    program will exit too early). The default value for threads are (daemon=False) '''
    
    
# You can also use a class ThreadPoolExecutor from the module concurrent.futures and it will start and join
#  on its own: 

with ThreadPoolExecutor() as executor:
    executor.submit(func_1,4)
    executor.submit(func_2,4)
    executor.submit(func_3,4)
    #.map() can be used to call a function on different values
    nums=[3,4,5]
    results=executor.map(func_1,nums)
    
    