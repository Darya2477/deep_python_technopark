import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all_urls(urls, max_concurrent_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

async def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()
        urls = [url.rstrip('\n') for url in urls]
    max_concurrent_requests = 10 

    responses = await fetch_all_urls(urls, max_concurrent_requests)
    for response in responses:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())



