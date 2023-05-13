from typing import Optional, Any

from httpx import Response

from astrotraders.api.utils import ORJSONDecoder


def exception_hook(response: Response) -> None:
    response.read()
    if response.content:
        data: Any = response.json(cls=ORJSONDecoder)
        if isinstance(response, dict) and data.get("error"):
            raise APIException(data.get("error"))


class APIException(Exception):
    def __init__(self, response: dict):
        self.message: str = response["message"]
        self.code: int = response["code"]
        self.data: Optional[str] = None
        if "data" in response:
            self.data = response["data"]
        super(APIException, self).__init__(response)
