# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InboundEmailListParams"]


class InboundEmailListParams(TypedDict, total=False):
    limit: int
    """Maximum number of inbound emails to return"""

    offset: int
    """Pagination offset"""

    status: Literal["active", "paused", "all"]
    """Filter by status"""
