# Day: 96(AsyncIO)

''' Asynchronous I/O or async for short is a programming pattern that allows for higher I/O operations in a
    concurrent and non blocking manner '''

import asyncio,time

async def func1():
    await asyncio.sleep(1)
    print("Function 1")

async def func2():
    await asyncio.sleep(2)
    print("Function 2")

async def func3():
    await asyncio.sleep(3)
    print("Function 3")
    
async def main():
   await asyncio.gather(func1(),func2(),func3())

asyncio.run(main())

''' Quick Rule of Thumb

Use Multithreading → when you have a moderate number of I/O tasks (like downloading 10–100 files).

Use Multiprocessing → when you need to speed up CPU-heavy work (like image resizing, video encoding).

Use AsyncIO → when you need to handle huge numbers of I/O tasks (like 10,000+ API calls).'''