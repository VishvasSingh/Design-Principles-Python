import threading
import time


def cpu_bound_task():
    count = 0
    for i in range(10 ** 7):
        count += 1
    return count


def thread_task():
    result = cpu_bound_task()
    print(f"Task completed with count = {result}")


if __name__ == '__main__':
    start_time = time.time()

    # Creating 10 threads
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=thread_task)
        threads.append(thread)
        thread.start()

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()

    print(f"Multithreading duration: {time.time() - start_time:.2f} seconds")
