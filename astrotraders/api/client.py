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
        self._agents = AgentsResource(self._client)
        self._systems = SystemsResource(self._client)
        self._contracts = ContractsResource(self._client)
        self._factions = FactionsResource(self._client)
        self._fleet = FleetResource(self._client)

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

    @property
    def agents(self) -> AgentsResource:
        """
        Agents are the primary entity in SpaceTraders.
        Player controls a single agent which can be used to manage a fleet of ships and conduct trade with factions
        """
        return self._agents

    @property
    def systems(self) -> SystemsResource:
        """
        Systems are the primary locations in the SpaceTraders universe.
        Every system has a type, which is typically a type of star, and a set of x, y coordinates.
        """
        return self._systems

    @property
    def contracts(self) -> ContractsResource:
        """
        Faction contracts are a good way to earn credits and faction reputation.
        Your contract will have a set of terms, which describe the requirements for completing the contract.
        """
        return self._contracts

    @property
    def factions(self) -> FactionsResource:
        """
        Factions are the primary NPC organizations in SpaceTraders.
        Each faction will have a unique set of ships, contracts, and trade routes for you to explore.
        """
        return self._factions

    @property
    def fleet(self) -> FleetResource:
        """
        Fleet is the collection of your ships.
        """
        return self._fleet

    def close(self) -> "None":
        self._httpx_instance.close()
