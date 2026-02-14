# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ContractNoteParseParams"]


class ContractNoteParseParams(TypedDict, total=False):
    broker_type: Literal["zerodha", "groww", "upstox", "icici"]
    """Optional broker type override. If not provided, system will auto-detect."""

    password: str
    """Password for the PDF file (usually PAN number for Zerodha)"""

    pdf_file: str
    """Base64 encoded contract note PDF file"""

    pdf_url: str
    """URL to the contract note PDF file"""
