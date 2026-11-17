# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KycCheckPanStatusParams"]


class KycCheckPanStatusParams(TypedDict, total=False):
    pan_no: Required[str]
    """PAN number to look up (10 characters, uppercase)"""
