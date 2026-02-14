# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FetchRequestOtpParams"]


class FetchRequestOtpParams(TypedDict, total=False):
    bo_id: Required[str]
    """CDSL BO ID (16 digits)"""

    dob: Required[str]
    """Date of birth (YYYY-MM-DD)"""

    pan: Required[str]
    """PAN number"""
