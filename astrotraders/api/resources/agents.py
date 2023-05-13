from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import AgentSchema


class AgentsResource(BaseResource):
    def info(self) -> AgentSchema:
        """
        Fetch your agent's details.
        """
        return self._client.request_to_model("GET", "/my/agent", AgentSchema)
