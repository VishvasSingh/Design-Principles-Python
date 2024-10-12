from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def cpu_bound_task():
    count = 0
    for i in range(10 ** 7):
        count += 1
    return count


def process_task():
    cpu_bound_task()

# Using ThreadPoolExecutor


# with ThreadPoolExecutor() as executor:
#     start_time = time.time()
#     futures = [executor.submit(process_task) for _ in range(10)]
#     for future in futures:
#         future.result()
#         print(f"task completed in {time.time() - start_time:.2f}")
#
#     print(f"Total task completion time with multithreading is -> {time.time() - start_time:.2f}")
#
#
# print("All tasks completed with ThreadPoolExecutor")

# Using ProcessPoolExecutor

if __name__ == "__main__":
    """
        if __name__ == '__main__': This ensures that the multiprocessing logic is executed only when running
        the script directly, not when it is imported or when subprocesses are spawned.

        Why this error occurs: When using spawn() (as on Windows and macOS), the entire module is re-executed when
        creating new processes. Without this guard, the new processes would also try to create even more processes,
        leading to an infinite loop of process creation. The guard ensures that only the parent process creates the
        pool of subprocesses.
    """

    with ProcessPoolExecutor() as executor:
        start_time = time.time()
        futures = [executor.submit(process_task) for _ in range(10)]
        for future in futures:
            future.result()
            print(f"task completed in {time.time() - start_time:.2f}")

        print(f"Total task completion time with multi processing is -> {time.time() - start_time:.2f}")

    print("All tasks completed with ProcessPoolExecutor")
