import asyncio


async def func_1():
    a = list()
    await asyncio.sleep(2)
    b = a[0]


async def func_2():
    for _ in range(5):
        await asyncio.sleep(1)

    return "Hello, I had a nice sleep !!"


async def main():
    """
        1. If we use return_exceptions=True then the exception is stored in the assigned variable, instead of throwing
           error and stopping the execution
        2.
    """
    results = await asyncio.gather(func_1(), func_2(), return_exceptions=True)
    for task_no, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Exception occurred for task no -> {task_no}")

        else:
            print(f"Task result is -> {result}")


if __name__ == '__main__':
    asyncio.run(main())
