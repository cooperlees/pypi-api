#!/usr/bin/env python3

import asyncio
import unittest

from .. import projects, journals
from typing import Awaitable, List


class TestJournals(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    # TODO: Mock aiohttp
    def test_latest(self) -> None:
        latest = self.loop.run_until_complete(journals.latest())
        self.assertTrue(latest)

    def test_since(self) -> None:
        latest = self.loop.run_until_complete(journals.latest())
        js = self.loop.run_until_complete(journals.since(latest["last_serial"]))
        self.assertTrue(len(js), 5000)


class TestProjects(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()
        self.queue = asyncio.Queue(loop=self.loop, maxsize=10)

    # TODO: Mock aiohttp
    def test_get_detail(self) -> None:
        pulp = self.loop.run_until_complete(projects.get_detail("pulpcore"))
        self.assertTrue("3.0.0a1.dev0" in pulp["releases"])
        self.assertEqual(275959, pulp["last_serial"])

    def test_since(self) -> None:
        since_projects = self.loop.run_until_complete(projects.since(275959)),
        self.assertTrue(since_projects)

    def test_paginate(self) -> None:
        last_page = self.loop.run_until_complete(projects.get_last_page())
        pages = self.loop.run_until_complete(projects.get_pages(last_page, self.queue))
        self.assertTrue(len(pages) > 200)
