import asyncio


async def func_1():
    while True:
        print("Long running task, sleeping again")
        await asyncio.sleep(2)


async def func_2():
    for _ in range(5):
        await asyncio.sleep(1)
        print("Processing some data")

    return "Task completed successfully"


def callback_func2(future):
    print("Task 2 has finished, executing it's callback")
    result = future.result()
    print(f"Result of the task -> {result}")


async def main():
    """
        Example 1
        If we use the below code then the task 1 and task 2 will keep running in background and our main thread won't
        be affected.
    """
    # task_1, task2 = asyncio.create_task(func_1()), asyncio.create_task(func_2())
    #
    # for i in range(10):
    #     print(f"Printing numbers after interval of 3 seconds -> {i}")
    #     await asyncio.sleep(3)

    """
        Example 2

        If we use the below code then task 1 will keep executing in background, but before starting the for loop, our
        main thread will wait for task2 to finish first
    """
    # task_1, task2 = asyncio.create_task(func_1()), asyncio.create_task(func_2())
    #
    # await task2
    #
    # for i in range(10):
    #     print(f"Printing numbers after interval of 3 seconds -> {i}")
    #     await asyncio.sleep(3)

    """
        Example 3

        If we use the below code then task 1 will keep executing in background, until it is cancelled and since there
        is a callback added to task2, the callback will execute once the execution of task 2 is complete. 
    """
    task_1, task2 = asyncio.create_task(func_1()), asyncio.create_task(func_2())

    task_1.cancel()
    task2.add_done_callback(callback_func2)

    for i in range(10):
        print(f"Printing numbers after interval of 3 seconds -> {i}")
        await asyncio.sleep(3)


if __name__ == '__main__':
    asyncio.run(main())
