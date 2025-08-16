# Day: 98(Multi-Processing)

''' Multiprocessing is a Python module that provides a simple way to run processes in parallel. It allows
    you to take advantage of mutiple cores or processors  on your system and can significantly improve the
    performance of your code '''

import multiprocessing,requests

def downloadFile(url, name):
    print(f"Started downloading: file {name}")
    response= requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"Completed downloading: file {name}")


if __name__=="__main__":
    url="https://fastly.picsum.photos/id/3650/2000/3000.jpg?hmac=n_4DxqK0o938eabBZRnEywWtPwgF2MKoTfnRmJ7vlKQ"
    processes=[]

    for i in range(50):
        downloadFile(url,i)
        # Difference between them is stated below: 
        p= multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        processes.append(p)
            
    for p in processes:
        p.join()
    
    # You can also use the ProcessPoolExecutor() class of concurrent.futures module just like we used it in
    #  multithreading, the remaining methods like sumit and map work the same
    
''' 1. Sequential execution (function calls in a loop)
---------------------------------------
for i in range(50):
    downloadFile(url, i)
---------------------------------------

Python runs one function at a time.

File 0 finishes, then 1, then 2… exactly in order.

No overlap, no randomness.

---------------------------------------------------------------------
2. Multiprocessing execution
p = multiprocessing.Process(target=downloadFile, args=[url, i])
p.start()
---------------------------------------------------------------------

You are launching 50 independent processes.

Each process runs concurrently and competes for:

CPU scheduling (OS decides which process gets time first)

Network bandwidth (one download might be faster/slower depending on timing)

Disk write access (writing files may take longer for some processes).

So file 50 might start before file 2 finishes.

Completion order depends on system load, network speed, and OS scheduling → non-deterministic.

That is why you saw file 2 complete last instead of file 50. It doesnot mean file 2 started last — just that its download + write took longer compared to others.

SO,

Sequential = predictable, ordered, but slow.

Multiprocessing/Threading = faster (parallel), but completion order is unpredictable.

If you need to preserve order of results, you usually:

Collect them in a list/dictionary keyed by i, or

Use higher-level abstractions like ThreadPoolExecutor.map (which preserves input order). '''
