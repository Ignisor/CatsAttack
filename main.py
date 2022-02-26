import asyncio
import time

import aiohttp

TARGET = 'http://vsrf.ru'
DELAY = 1
CONCURRENCY = 20

async def call():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(TARGET) as resp:
                    print(time.time(), resp.status)
    
                await asyncio.sleep(DELAY)
            except Exception:
                pass

async def launch():
    await asyncio.gather(*(call() for _ in range(CONCURRENCY)))

asyncio.run(launch())
