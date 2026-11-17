# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["KycGetDigilockerResultParams"]


class KycGetDigilockerResultParams(TypedDict, total=False):
    fetch_documents: List[Literal["pan", "aadhaar", "driving_licence"]]
    """
    Documents to additionally fetch + parse from the locker.
    Default: [] (no document fetch, no fetch billing).
    """

    include_documents: bool
    """Include the issued-documents list."""
