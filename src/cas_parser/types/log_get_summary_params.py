# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LogGetSummaryParams"]


class LogGetSummaryParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End time filter (ISO 8601). Defaults to now."""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time filter (ISO 8601). Defaults to start of current month."""
