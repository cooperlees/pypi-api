#!/usr/bin/env python3

from setuptools import setup
from sys import version_info

from pypi import __version__


assert version_info >= (3, 6, 0), "pypi-api requires >= Python 3.6"


setup(
    name="pypi",
    version=__version__,
    description=("RESTful JSON API client for PyPI Warehouse"),
    #    long_description='\n\n'.join(
    #        [open('README.md').read(), open('CHANGES.md').read()]
    #    ),
    #    long_description_content_type="text/markdown",
    packages=["pypi"],
    url="http://github.com/cooperlees/pypi-api",
    license="Apache",
    author="Cooper Lees",
    author_email="me@cooperlees.com",
    classifiers=(
        "License :: OSI Approved :: Apache Software License"
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Development Status :: 3 - Alpha",
    ),
    python_requires=">=3.6",
    install_requires=["aiohttp", "aiodns", "cchardet"],
    test_suite="pypi.tests.base",
)
