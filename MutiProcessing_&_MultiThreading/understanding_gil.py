import threading
import time

"""
    Even after using multithreading the time almost remains the same, that is because of the Global Interpreter lock
    to ensure that the code is safe from race conditions.
"""

def cpu_bound_task():
    count = 0
    for i in range(10 ** 7):
        count += 1

    print(f" Task completed with count = {count}")


start_time = time.time()
cpu_bound_task()
cpu_bound_task()
print(f"Single execution duration (after running twice): {time.time()-start_time:.2f} seconds")

# Measuring time for two threads running the task concurrently

"""
    Multithreading involves running multiple threads within a single process. Each thread runs independently 
    but shares the same memory space, making it useful for tasks that involve a lot of waiting, 
    such as I/O operations (reading and writing files, and handling network requests). 
"""

thread1 = threading.Thread(target=cpu_bound_task)
thread2 = threading.Thread(target=cpu_bound_task)

start_time = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Two threads duration: {time.time() - start_time:.2f} seconds")
