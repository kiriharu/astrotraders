from typing import TYPE_CHECKING, cast

from httpx import Client

from astrotraders.api.resources import (
    AgentsResource,
    SystemsResource,
    ContractsResource,
    FactionsResource,
    FleetResource,
)
from astrotraders.api.exceptions import exception_hook
from astrotraders.api.wrapper import HttpxClientWrapper


class AstroTradersClient:
    def __init__(self, httpx_instance: Client):
        self._httpx_instance = httpx_instance
        self._client = HttpxClientWrapper(self._httpx_instance)
        self.agents = AgentsResource(self._client)
        self.systems = SystemsResource(self._client)
        self.contracts = ContractsResource(self._client)
        self.factions = FactionsResource(self._client)
        self.fleet = FleetResource(self._client)

    @classmethod
    def set_up(
        cls, token: str, url: str = "https://api.spacetraders.io/v2"
    ) -> "AstroTradersClient":
        client = Client(
            base_url=url,
            event_hooks={"response": [exception_hook]},
            headers={"Authorization": f"Bearer {token}"},
        )
        return cls(client)

    def close(self) -> "None":
        self._httpx_instance.close()
