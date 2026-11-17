# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KycLookupDigilockerAccountParams"]


class KycLookupDigilockerAccountParams(TypedDict, total=False):
    aadhaar_number: str
    """12-digit Aadhaar number."""

    mobile: str
    """10-digit Indian mobile number."""

    reference_id: str
    """Optional caller-side request identifier."""
