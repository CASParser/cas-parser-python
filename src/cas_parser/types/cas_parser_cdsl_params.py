# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CasParserCdslParams"]


class CasParserCdslParams(TypedDict, total=False):
    password: str
    """Password for the PDF file (if required)"""

    pdf_file: str
    """Base64 encoded CAS PDF file"""

    pdf_url: str
    """URL to the CAS PDF file"""
