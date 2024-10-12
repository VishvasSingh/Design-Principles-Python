import asyncio
import time


async def print_numbers():
    for i in range(10):
        print(f"Number: {i}")
        await asyncio.sleep(1)  # Non-blocking sleep


async def print_letters():
    for letter in 'abcdefghij':
        print(f"Letter: {letter}")
        await asyncio.sleep(1)  # Non-blocking sleep


async def main():
    await asyncio.gather(print_numbers(), print_letters())  # Run both coroutines concurrently


# Run the main coroutine
# asyncio.run(main())

async def cpu_bound_task():
    count = 0
    for i in range(10 ** 7):
        count += 1
    return count


async def process_task():
    result = await cpu_bound_task()
    print(f"Task completed with count = {result}")


async def main_asyncio_test():
    start_time = time.time()
    coroutines = [process_task() for _ in range(10)]
    await asyncio.gather(*coroutines)
    print(f"Using asyncio gather duration is : {time.time() - start_time:.2f} seconds")

asyncio.run(main_asyncio_test())
