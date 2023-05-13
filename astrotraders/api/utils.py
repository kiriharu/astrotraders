from json import JSONDecoder
from typing import TypeVar, Any, Type, Union, Callable, Optional

import orjson

from astrotraders.api.schemas import PaginatedObject

T = TypeVar("T")


def to_schema(obj: dict, schema: Type[T]) -> Union[T, PaginatedObject[T]]:
    if issubclass(schema, PaginatedObject):
        return schema(**obj)
    return schema(**obj["data"])


class ORJSONDecoder(JSONDecoder):
    def decode(self, s: str, _w: Optional[Callable[..., Any]] = None) -> Any:
        return orjson.loads(s)
