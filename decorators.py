import asyncio
from enum import Enum


def logger(func):
    async def wrapper(*args, **kwargs):
        print("decorator called")
        result = await func(*args, **kwargs)
        print("function execution is complete")
        return result

    return wrapper


@logger
async def print_hello():
    await print_how()
    await print_are()
    print("you")


async def print_how():
    print('how')


async def print_are():
    print('are')


class Relationship(Enum):
    PARENT = 0
    CHILD = 1


if __name__ == '__main__':
    asyncio.run(print_hello())
