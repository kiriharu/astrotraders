from typing import Optional, cast, Any

from astrotraders.api.resources.base import BaseResource
from astrotraders.api.schemas import (
    PaginatedObject,
    ShipSchema,
    ShipType,
    PurchaseShipResult,
    ShipCargo,
    ShipNav,
    Produce,
    ShipRefineResult,
    ChartShipResult,
    Cooldown,
    CreateSurveyResult,
    ExtractResourcesResult,
    Survey,
    ShipJumpResult,
    ShipNavigateResult,
    ShipNavFlightMode,
    SellCargoResult,
    ScanSystemsResult,
    ScanWaypointsResult,
    ScanShipsResult,
    RefuelShipResult,
    PurchaseCargoResult,
    TradeSymbol,
)
from astrotraders.api.wrapper import HttpxClientWrapper


class CargoResource(BaseResource):
    def get(self, ship: str) -> ShipCargo:
        """
        Retrieve the cargo of your ship.
        """
        return self._client.request_to_model(
            "GET",
            f"/my/ships/{ship}/cargo",
            ShipCargo,
        )

    def jettison(self, ship: str, cargo: str, units: int) -> ShipCargo:
        """
        Jettison cargo from your ship's cargo hold.
        """
        result = cast(
            dict[str, Any],
            self._client.raw_request(
                "POST",
                f"/my/ships/{ship}/jettison",
                json={"symbol": cargo, "units": units},
            ),
        )
        return ShipCargo(**result["data"]["cargo"])

    def sell(self, ship: str, cargo: str, units: int) -> SellCargoResult:
        """
        Sell cargo.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/sell",
            SellCargoResult,
            json={"symbol": cargo, "units": units},
        )

    def purchase(self, ship: str, cargo: str, units: int) -> PurchaseCargoResult:
        """
        Purchase cargo.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/purchase",
            PurchaseCargoResult,
            json={"symbol": cargo, "units": units},
        )

    def transfer(
        self, from_ship: str, to_ship: str, cargo: TradeSymbol, units: int
    ) -> ShipCargo:
        """
        Transfer cargo between ships.
        """
        result = cast(
            dict[str, Any],
            self._client.raw_request(
                "POST",
                f"/my/ships/{from_ship}/transfer",
                json={"tradeSymbol": cargo, "units": units, "shipSymbol": to_ship},
            ),
        )
        return ShipCargo(**result["data"]["cargo"])


class ScanResource(BaseResource):
    def systems(self, ship: str) -> ScanSystemsResult:
        """
        Activate your ship's sensor arrays to scan for system information.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/scan/systems",
            ScanSystemsResult,
        )

    def waypoints(self, ship: str) -> ScanWaypointsResult:
        """
        Activate your ship's sensor arrays to scan for waypoint information.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/scan/waypoints",
            ScanWaypointsResult,
        )

    def ships(self, ship: str) -> ScanShipsResult:
        """
        Activate your ship's sensor arrays to scan for ship information.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/scan/ships",
            ScanShipsResult,
        )


class FleetResource(BaseResource):
    def __init__(self, client: HttpxClientWrapper):
        super().__init__(client)
        self.scan = ScanResource(client)
        self.cargo = CargoResource(client)

    def list(self, limit: int = 20, page: int = 1) -> PaginatedObject[ShipSchema]:
        """
        Retrieve all of your ships.
        """
        return self._client.request_to_paginated(
            "GET",
            "/my/ships",
            ShipSchema,
            params={"limit": limit, "page": page},
        )

    def get(self, name: str) -> ShipSchema:
        """
        Retrieve the details of your ship.
        """
        return self._client.request_to_model("GET", f"/my/ships/{name}", ShipSchema)

    def purchase(self, ship_type: ShipType, waypoint: str) -> PurchaseShipResult:
        """
        Purchase a ship
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships",
            PurchaseShipResult,
            json={"shipType": ship_type, "waypointSymbol": waypoint},
        )

    def orbit(self, ship: str) -> ShipNav:
        """
        Attempt to move your ship into orbit at it's current location.

        The request will only succeed if your ship is capable of moving into orbit at the time of the request.
        The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.
        """
        result = cast(
            dict[str, Any],
            self._client.raw_request(
                "POST",
                f"/my/ships/{ship}/orbit",
            ),
        )
        return ShipNav(**result["data"]["nav"])

    def refine(self, ship: str, produce: Produce) -> ShipRefineResult:
        """
        Attempt to refine the raw materials on your ship.

        The request will only succeed if your ship is capable of refining at the time of the request.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/refine",
            ShipRefineResult,
            json={"produce": produce},
        )

    def chart(self, ship: str) -> ChartShipResult:
        """
        Command a ship to chart the current waypoint.

        Waypoints in the universe are uncharted by default.
        These locations will not show up in the API until they have been charted by a ship.
        Charting a location will record your agent as the one who created the chart.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/chart",
            ChartShipResult,
        )

    def cooldown(self, ship: str) -> Optional[Cooldown]:
        """
        Retrieve the details of your ship's reactor cooldown.
        Some actions such as activating your jump drive, scanning,
        or extracting resources taxes your reactor and results in a cooldown.

        Your ship cannot perform additional actions until your cooldown has expired.
        The duration of your cooldown is relative to the power consumption
        of the related modules or mounts for the action taken.
        None returns when the ship has no cooldown.
        """
        return self._client.request_to_model_optioned(
            "GET",
            f"/my/ships/{ship}/cooldown",
            Cooldown,
        )

    def dock(self, ship: str) -> ShipNav:
        """
        Attempt to dock your ship at it's current location.

        Docking will only succeed if the waypoint is a dockable location,
        and your ship is capable of docking at the time of the request.
        The endpoint is idempotent - successive calls will succeed even if the ship is already docked.
        """
        result = cast(
            dict[str, Any],
            self._client.raw_request(
                "POST",
                f"/my/ships/{ship}/dock",
            ),
        )
        return ShipNav(**result["data"]["nav"])

    def survey(self, ship: str) -> CreateSurveyResult:
        """
        If you want to target specific yields for an extraction,
        you can survey a waypoint, such as an asteroid field,
        and send the survey in the body of the extract request.
        Each survey may have multiple deposits, and if a symbol
        shows up more than once, that indicates a higher chance of extracting that resource.

        Your ship will enter a cooldown between consecutive survey requests.
        Surveys will eventually expire after a period of time.
        Multiple ships can use the same survey for extraction.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/survey",
            CreateSurveyResult,
        )

    def extract(
        self, ship: str, survey: Optional[Survey] = None
    ) -> ExtractResourcesResult:
        """
        Extract resources from the waypoint into your ship.
        Send an optional survey as the payload to target specific yields.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/extract",
            ExtractResourcesResult,
            json={"survey": survey.dict()} if survey else {},
        )

    def jump(self, ship: str, system: str) -> ShipJumpResult:
        """
        Jump your ship instantly to a target system.
        Unlike other forms of navigation, jumping requires a unit of antimatter.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/jump",
            ShipJumpResult,
            json={"systemSymbol": system},
        )

    def navigate(self, ship: str, waypoint: str) -> ShipNavigateResult:
        """
        Navigate to a target destination.

        The destination must be located within the same system as the ship.
        Navigating will consume the necessary fuel and supplies from the ship's manifest,
        and will pay out crew wages from the agent's account.
        The returned response will detail the route information including the expected time of arrival.
        Most ship actions are unavailable until the ship has arrived at it's destination.
        To travel between systems, see the ship's warp or jump actions.
        """

        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/navigate",
            ShipNavigateResult,
            json={"waypointSymbol": waypoint},
        )

    def flight_mode(self, ship: str, mode: ShipNavFlightMode) -> ShipNav:
        """
        Update the nav data of a ship, such as the flight mode.
        """
        return self._client.request_to_model(
            "PATCH", f"/my/ships/{ship}/nav", ShipNav, json={"flightMode": mode}
        )

    def nav(self, ship: str) -> ShipNav:
        """
        Get the current nav status of a ship.
        """
        return self._client.request_to_model(
            "GET",
            f"/my/ships/{ship}/nav",
            ShipNav,
        )

    def warp(self, ship: str, waypoint: str) -> ShipNavigateResult:
        """
        Warp your ship to a target destination in another system.
        Warping will consume the necessary fuel and supplies
        from the ship's manifest, and will pay out crew wages from the agent's account.

        The returned response will detail the route information including the expected time of arrival.
        Most ship actions are unavailable until the ship has arrived at it's destination.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/warp",
            ShipNavigateResult,
            json={"waypointSymbol": waypoint},
        )

    def refuel(self, ship: str) -> RefuelShipResult:
        """
        Refuel your ship from the local market.
        """
        return self._client.request_to_model(
            "POST",
            f"/my/ships/{ship}/refuel",
            RefuelShipResult,
        )
