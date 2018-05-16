# pypi-api

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

API for the new PyPI RESTful JSON API

## Usage

```
import asyncio
import pypi

loop = asyncio.get_event_loop()
try:
    print(loop.run_until_complete(pypi.projects.get("pip"))
finally:
    loop.close()
```

## Quotes

Jason Fried (RPC Thrift Guy): "This is the glorious future!"

Łukasz Langa (Linter Expert): "Why isn't it blacker?"
