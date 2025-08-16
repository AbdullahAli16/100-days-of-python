# Day: 84(Time Module)

import time

''' Time module is used for calculating time, it has methods for minutes seconds and hours etc, but you can
    also use the time function to get amount of time your code took to get executed. For example: '''

current_time =time.time()

# time.time() returns the total no: of seconds from 01 january 1970 to until now:
def forloop():
    for i in range(1,10000):
        print(i)
    print(f"The time for loop took in executing is: {time.time()-current_time}")
    
forloop()

# time.sleep() takes the no of seconds as an argument and then executes the content placed after it.

time.sleep(3)
print("It executed after 3 seconds")

# time.localtime() tells the time according to the device you are currently running
# time.strftime() formats the time value as a string based on a specified format

local_time=time.localtime()

formatted_time=time.strftime("%Y-%m-%d-%H:%M:%S",local_time)

print (formatted_time)