from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import (
    PaginatedObject,
    ContractSchema,
    AcceptContractResult,
    DeliverContractResult,
    FullfillContractResult,
)


class ContractsResource(BaseResource):
    def list(self, limit: int = 20, page: int = 1) -> PaginatedObject[ContractSchema]:
        """
        List all of your contracts.
        """
        return self._client.request_to_paginated(
            "GET",
            "/my/contracts",
            ContractSchema,
            params={"limit": limit, "page": page},
        )

    def get(self, contract_id: str) -> ContractSchema:
        """
        Get the details of a contract by ID.
        """
        return self._client.request_to_model(
            "GET", f"/my/contracts/{contract_id}", ContractSchema
        )

    def accept(self, contract_id: str) -> AcceptContractResult:
        """
        Accept a contract.
        """
        return self._client.request_to_model(
            "POST", f"/my/contracts/{contract_id}/accept", AcceptContractResult
        )

    def deliver(
        self, contract_id: str, ship: str, trade: str, units: int
    ) -> DeliverContractResult:
        """
        Deliver cargo on a given contract.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/contracts/{contract_id}/deliver",
            DeliverContractResult,
            json={"shipSymbol": ship, "tradeSymbol": trade, "units": units},
        )

    def fulfill(self, contract_id: str) -> FullfillContractResult:
        """
        Fulfill a contract.
        """
        return self._client.request_to_model(
            "POST", f"/my/contracts/{contract_id}/fulfill", FullfillContractResult
        )
