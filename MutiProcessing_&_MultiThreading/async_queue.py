import asyncio


async def producer(queue):
    """
        This function fetches some data and pushes it to queue, which will be picked up by consumer and processed,
        instead of waiting for all the producers to finish and then processing them, we are sending the data to be
        processed as soon as it is available and producer can keep producing events for other use cases.
    :param queue: Asyncio Queue
    :return: None
    """
    for i in range(3):
        print(f"Producing {i}")
        await queue.put(i)
        await asyncio.sleep(2)


async def consume(queue):
    """
        Consumer takes events from the queue and processes them, as soon as a producer pushes some event, it will
        pick up that event and process it, production of multiple events and their consumption is happening concurrently
        using this pattern.
    :param queue: Asyncio queue
    :return: None
    """
    while True:
        item = await queue.get()  # this gets the available item in queue, if nothing is available then it waits
        print(f"Consuming item -> {item}")
        queue.task_done()  # this will signal that the event that was picked up has been processed and queue.join()
        # relies on this


async def main():
    queue = asyncio.Queue()  # initializing the asyncio queue
    prod = asyncio.create_task(producer(queue))  # creating task for producer, it will start running after this
    cons = asyncio.create_task(consume(queue))  # creating task for consumer, consumer will start after this

    await asyncio.gather(prod)  # this is to ensure that main program waits for producer to finish producing all events
    await queue.join()  # this will block the main thread until all the tasks in queue have been picked up by consumer
    cons.cancel()  # terminating the consumer after all events have been processed, since it is running in while loop


if __name__ == '__main__':
    asyncio.run(main())
