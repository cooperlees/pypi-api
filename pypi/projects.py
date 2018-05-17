#!/usr/bin/python3

import aiohttp, asyncio

from typing import Dict, List
from urllib.parse import urlparse, parse_qs

from . import defaults


async def get_detail(
    name: str, url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> Dict:
    url = f"{url}api/projects/{name}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as resp:
            return await resp.json()


async def since(
    serial: int, url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> Dict:
    url = f"{url}api/projects/?serial_since={serial}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as resp:
            return await resp.json()


async def get_page(
    page: int, url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> List:
    url = f"{url}api/projects/?page={page}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as resp:
            print("Checking Page %d " % page)
            return await resp.json()


async def get_pages(
    num_pages: int, queue, url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> List:
    queue = asyncio.Queue()

    result_pages = []

    # Create X Consumers
    consumers = [
        asyncio.ensure_future(_consume_page(queue, result_pages))
        for i in range(defaults.CONSUMERS)
    ]

    await _produce_pages(queue, num_pages)

    # wait until the consumer has processed all items
    await queue.join()

    # cancel all consumers after queue.join() is complete
    for consumer in consumers:
        consumer.cancel()
    return result_pages


async def get_last_page(
    url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> int:

    # Getting the resulting previous_page of a large pagination number
    # to figure out how many total pages of data there are
    i: int = 9999
    page = await get_page(i)
    last_page = parse_qs(urlparse(page["links"]["previous_page"]).query)["page"][0]
    return int(last_page)


async def _consume_page(queue, result_pages):
    while True:
        item = await queue.get()
        result_pages.append(await item)
        queue.task_done()


async def _produce_pages(queue, n):
    for i in range(1, n):
        project = get_page(i)
        await queue.put(project)
