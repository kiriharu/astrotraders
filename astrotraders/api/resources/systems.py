from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import (
    PaginatedObject,
    System,
    Waypoint,
    Market,
    Shipyard,
    JumpGate,
)
from astrotraders.api.wrapper import HttpxClientWrapper


class SystemsResource(BaseResource):
    def __init__(self, client: HttpxClientWrapper):
        super().__init__(client)
        self.waypoints = WaypointsResource(client)

    def list(self, limit: int = 20, page: int = 1) -> PaginatedObject[System]:
        """
        Return a list of all systems.
        """
        return self._client.request_to_paginated(
            "GET",
            "/systems",
            System,
            params={"limit": limit, "page": page},
        )

    def get(self, name: str) -> System:
        """
        Get the details of a system.
        """
        return self._client.request_to_model("GET", f"/systems/{name}", System)


class WaypointsResource(BaseResource):
    def list(
        self, system: str, limit: int = 20, page: int = 1
    ) -> PaginatedObject[Waypoint]:
        """
        Fetch all waypoints for a given system.
        System must be charted or a ship must be present to return waypoint details.
        """
        return self._client.request_to_paginated(
            "GET",
            f"/systems/{system}/waypoints",
            Waypoint,
            params={"limit": limit, "page": page, "systemSymbol": system},
        )

    def get(self, system: str, waypoint: str) -> Waypoint:
        """
        View the details of a waypoint.
        """
        return self._client.request_to_model(
            "GET",
            f"/systems/{system}/waypoints/{waypoint}",
            Waypoint,
            params={"waypointSymbol": waypoint, "systemSymbol": system},
        )

    def market(self, system: str, waypoint: str) -> Market:
        """
        Retrieve imports, exports and exchange data from a marketplace.
        Imports can be sold, exports can be purchased,
        and exchange goods can be purchased or sold.
        Send a ship to the waypoint to access trade good prices and recent transactions.
        """
        return self._client.request_to_model(
            "GET",
            f"/systems/{system}/waypoints/{waypoint}/market",
            Market,
            params={"waypointSymbol": waypoint, "systemSymbol": system},
        )

    def shipyard(self, system: str, waypoint: str) -> Shipyard:
        """
        Get the shipyard for a waypoint.
        Send a ship to the waypoint to access ships that are currently available for purchase and recent transactions.
        """
        return self._client.request_to_model(
            "GET",
            f"/systems/{system}/waypoints/{waypoint}/shipyard",
            Shipyard,
            params={"waypointSymbol": waypoint, "systemSymbol": system},
        )

    def jump_gate(self, system: str, waypoint: str) -> JumpGate:
        """
        Get jump gate details for a waypoint.
        """
        return self._client.request_to_model(
            "GET",
            f"/systems/{system}/waypoints/{waypoint}/jump-gate",
            JumpGate,
            params={"waypointSymbol": waypoint, "systemSymbol": system},
        )
