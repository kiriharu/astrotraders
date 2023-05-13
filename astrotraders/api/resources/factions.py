from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import PaginatedObject, Faction


class FactionsResource(BaseResource):
    def list(self, limit: int = 20, page: int = 1) -> PaginatedObject[Faction]:
        """
        List all discovered factions in the game.
        """
        return self._client.request_to_paginated(
            "GET",
            "/factions",
            Faction,
            params={"limit": limit, "page": page},
        )

    def get(self, faction: str) -> Faction:
        """
        View the details of a faction.
        """
        return self._client.request_to_model("GET", f"/factions/{faction}", Faction)
