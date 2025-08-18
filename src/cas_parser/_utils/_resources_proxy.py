from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `cas_parser.resources` module.

    This is used so that we can lazily import `cas_parser.resources` only when
    needed *and* so that users can just import `cas_parser` and reference `cas_parser.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("cas_parser.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
