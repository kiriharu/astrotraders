import pytest

from astrotraders import AstroTradersClient


@pytest.fixture(scope="function")
def api_client() -> AstroTradersClient:
    client = AstroTradersClient.set_up(
        "test",
        # test stoplight mock server for integration tests
        "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"
    )
    return client
