import asyncio

async def hello_after_delay(delay):
    await asyncio.sleep(delay)
    print("Hello")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_after_delay(5))
loop.close()
