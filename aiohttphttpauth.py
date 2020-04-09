import asyncio
import aiohttp

proxy = 'http://username:password@127.0.0.1:7890'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', proxy=proxy) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
