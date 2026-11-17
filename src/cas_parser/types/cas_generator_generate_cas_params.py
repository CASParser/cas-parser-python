# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CasGeneratorGenerateCasParams"]


class CasGeneratorGenerateCasParams(TypedDict, total=False):
    email: Required[str]
    """Email address to receive the CAS document"""

    from_date: Required[str]
    """Start date (YYYY-MM-DD)"""

    password: Required[str]
    """
    Password protecting the emailed PDF. Must satisfy the chosen authority's policy — `cams` requires 6-20 characters with at least two digits, so a PAN works.
    """

    to_date: Required[str]
    """End date (YYYY-MM-DD)"""

    cas_authority: Literal["kfintech", "cams"]
    """RTA that sends the mailback. Affects only the password policy, not the portfolio data returned."""

    pan_no: str
    """PAN number (optional)"""
