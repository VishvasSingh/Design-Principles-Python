import asyncio

semaphore = asyncio.Semaphore(5)


async def func_1():
    a = list()
    await asyncio.sleep(2)
    b = a[0]


async def func_2():
    for _ in range(5):
        await asyncio.sleep(1)

    return "Hello, I had a nice sleep !!"


async def limited_tasks(n):
    async with semaphore:
        print(f'Task {n} started')
        await asyncio.sleep(1)
        print(f'Task {n} finished')


async def slow_task():
    await asyncio.sleep(5)
    return "Task Finished"


async def main():
    """
        1. If we use return_exceptions=True then the exception is stored in the assigned variable, instead of throwing
           error and stopping the execution
    """
    results = await asyncio.gather(func_1(), func_2(), return_exceptions=True)
    for task_no, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Exception occurred for task no -> {task_no}")

        else:
            print(f"Task result is -> {result}")

    tasks = [limited_tasks(i) for i in range(10)]
    await asyncio.gather(*tasks)

    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(result)

    except asyncio.TimeoutError:
        print("Task timed out")

if __name__ == '__main__':
    asyncio.run(main())
