from typing import cast, Any

from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import ServerStatsResponse


class ServerResource(BaseResource):
    def stats(self) -> ServerStatsResponse:
        """
        Return server API stats and leaderboards
        """
        response = cast(dict[str, Any], self._client.raw_request("GET", "/"))
        return ServerStatsResponse(**response)
