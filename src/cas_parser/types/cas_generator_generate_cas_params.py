# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CasGeneratorGenerateCasParams"]


class CasGeneratorGenerateCasParams(TypedDict, total=False):
    email: Required[str]
    """Email address to receive the CAS document"""

    from_date: Required[str]
    """Start date for the CAS period (format YYYY-MM-DD)"""

    password: Required[str]
    """Password to protect the generated CAS PDF"""

    to_date: Required[str]
    """End date for the CAS period (format YYYY-MM-DD)"""

    cas_authority: Literal["kfintech", "cams", "cdsl", "nsdl"]
    """
    CAS authority to generate the document from (currently only kfintech is
    supported)
    """

    pan_no: str
    """PAN number (optional for some CAS authorities)"""
