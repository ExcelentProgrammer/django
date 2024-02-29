import asyncio
import time

import aiohttp


class Requests:
    count = 0


async def make_request(session, _):
    url = "https://omma.iprogrammer.uz/api/questions"  # API manzilini o'zgartiring

    for i in range(100):
        start_time = time.time()
        async with session.get(url) as response:
            try:
                res = await response.json()
            except Exception as e:
                print(e)
        Requests.count = Requests.count + 1
        print("{} {}".format(Requests.count, time.time() - start_time))


async def main():
    num_clients = 100
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, _) for _ in range(num_clients)]
        responses = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
