from typing import TypeVar, Optional, Union, TYPE_CHECKING, Type, Any, Mapping, cast

from pydantic import BaseModel
from typing_extensions import Unpack

import orjson

from astrotraders.api.schemas import PaginatedObject
from astrotraders.api.utils import ORJSONDecoder

if TYPE_CHECKING:
    from typing import TypedDict
    from httpx import Client
    from httpx._client import UseClientDefault
    from httpx._types import (
        RequestContent,
        RequestData,
        RequestFiles,
        QueryParamTypes,
        HeaderTypes,
        CookieTypes,
        AuthTypes,
        TimeoutTypes,
        RequestExtensions,
    )

    class HttpxRequestParams(TypedDict, total=False):
        content: Optional[RequestContent]
        data: Optional[RequestData]
        files: Optional[RequestFiles]
        json: Optional[Any]
        params: Optional[QueryParamTypes]
        headers: Optional[HeaderTypes]
        cookies: Optional[CookieTypes]
        auth: Union[AuthTypes, UseClientDefault, None]
        follow_redirects: Union[bool, UseClientDefault]
        timeout: Union[TimeoutTypes, UseClientDefault]
        extensions: Optional[RequestExtensions]


T = TypeVar("T", bound=BaseModel)


class HttpxClientWrapper:
    def __init__(self, client: "Client"):
        self._client = client

    def raw_request(
        self, method: str, uri: str, **params: Unpack["HttpxRequestParams"]
    ) -> Optional[Union[dict[Any, Any], list[dict]]]:
        # because httpx doesn't have default way to change json encoder
        if json_obj := params.get("json"):
            # it works as well with bytes
            params["data"] = orjson.dumps(json_obj)  # type: ignore[typeddict-item]
            params["headers"] = {"Content-Type": "application/json"}
            del params["json"]
        result = self._client.request(method, uri, **params)
        # in a few requests we get 204, so we should handle this
        if result.status_code == 204:
            return None
        return result.json(cls=ORJSONDecoder)

    def request_to_model(
        self,
        method: str,
        uri: str,
        to_type: Type[T],
        **params: Unpack["HttpxRequestParams"],
    ) -> T:
        data = cast(Mapping[str, Any], self.raw_request(method, uri, **params))
        return to_type(**data["data"])

    def request_to_model_optioned(
        self,
        method: str,
        uri: str,
        to_type: Type[T],
        **params: Unpack["HttpxRequestParams"],
    ) -> Optional[T]:
        data = cast(Mapping[str, Any], self.raw_request(method, uri, **params))
        if data:
            return to_type(**data["data"])
        return None

    def request_to_paginated(
        self,
        method: str,
        uri: str,
        to_type: Type[T],
        **params: Unpack["HttpxRequestParams"],
    ) -> PaginatedObject[T]:
        data = cast(Mapping[str, Any], self.raw_request(method, uri, **params))
        # TODO: fix mypy error
        return PaginatedObject[to_type](**data)  # type: ignore[valid-type]
