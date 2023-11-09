import unittest
from unittest.mock import MagicMock
import asyncio
import aiohttp
from fetcher import fetch_url, fetch_all_urls, main

class TestAsyncWebCrawler(unittest.TestCase):
    async def test_fetch_url_success(self):
        session = MagicMock()
        session.get.return_value.__aenter__.return_value.text.return_value = "Test response"
        response = await fetch_url(session, "http://test.com")
        self.assertEqual(response, "Test response")

    async def test_fetch_all_urls_success(self):
        urls = ["http://test1.com", "http://test2.com"]
        max_concurrent_requests = 5
        result = await fetch_all_urls(urls, max_concurrent_requests)
        self.assertTrue(all(isinstance(res, str) for res in result))

    async def test_main_success(self):
        with open("test_urls.txt", "w") as file:
            file.write("http://test1.com\nhttp://test2.com")
        result = await main()
        self.assertIsNone(result)

    def test_urls_file_format(self):
        with open("urls.txt", "r") as file:
            urls = file.readlines()
            self.assertTrue(all(url.strip() for url in urls))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
