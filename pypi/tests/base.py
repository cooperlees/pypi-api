#!/usr/bin/env python3

import asyncio
import datetime
import unittest

from .. import projects, journals


class TestJournals(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    # TODO: Mock aiohttp
    def test_latest(self) -> None:
        self.assertTrue(self.loop.run_until_complete(journals.latest()))

    def test_since(self) -> None:
        # one_hour_ago = datetime.now() - datetime.timedelta(hours=1)
        a_date = datetime.date(2017, 5, 15)
        js = self.loop.run_until_complete(journals.since(int(a_date.strftime("%s"))))
        self.assertTrue(len(js), 5000)


class TestProjects(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    # TODO: Mock aiohttp
    def test_get(self) -> None:
        pulp = self.loop.run_until_complete(projects.get("pulpcore"))
        self.assertTrue("3.0.0a1.dev0" in pulp["releases"])
        self.assertEqual(275959, pulp["last_serial"])

    def test_since(self) -> None:
        since_projects = self.loop.run_until_complete(projects.since(275959)),
        self.assertTrue(since_projects)
