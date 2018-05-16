#!/usr/bin/python3

import aiohttp

from typing import Dict

from . import defaults


async def get(
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
