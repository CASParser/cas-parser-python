# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboundEmailListFilesParams"]


class InboundEmailListFilesParams(TypedDict, total=False):
    limit: int
    """Maximum files to return."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    ISO 8601 timestamp. Only files with `received_at` strictly greater
    than this value are returned. Use the `cursor` value from the
    previous response.
    """
