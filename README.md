# astrotraders

A typed, handwrited and powerful library for spacetraders.io game.

SpaceTraders is an API-based game where you acquire and manage a fleet of ships to explore, trade, and fight your way across the galaxy.

This client based on [HTTPX](https://www.python-httpx.org/) and [Pydantic](https://docs.pydantic.dev/latest/).

## Install
```
pip install astrotraders
```

## Usage

Currently, you can use API wrapper which  represented by `AstroTradersClient` class:

```python
from astrotraders import AstroTradersClient
client = AstroTradersClient.set_up(
    "token_here",
)
```

After initializing client you can use API resources, for example:

```python
agent = client.agents.info()
systems = client.systems.list()
contracts = client.contracts.list()
factions = client.factions.list()
```

## TODO
1. "Game objects" with data caching and more pythonic usage
2. CLI tool for manage fleet (and as example)
