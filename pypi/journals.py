#!/usr/bin/python3

import aiohttp

from typing import Dict

from . import defaults


async def latest(url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT) -> Dict:
    url = f"{url}api/journals/latest/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as resp:
            return await resp.json()


async def since(
    timestamp: int, url: str = defaults.API_URL, timeout: int = defaults.TIMEOUT
) -> Dict:
    url = f"{url}api/journals/?since={timestamp}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as resp:
            return await resp.json()
