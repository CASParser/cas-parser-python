# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KfintechGenerateCasParams"]


class KfintechGenerateCasParams(TypedDict, total=False):
    email: Required[str]
    """Email address to receive the CAS document"""

    from_date: Required[str]
    """Start date (YYYY-MM-DD)"""

    password: Required[str]
    """Password for the PDF"""

    to_date: Required[str]
    """End date (YYYY-MM-DD)"""

    pan_no: str
    """PAN number (optional)"""
