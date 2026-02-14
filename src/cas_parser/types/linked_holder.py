# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LinkedHolder"]


class LinkedHolder(BaseModel):
    name: Optional[str] = None
    """Name of the account holder"""

    pan: Optional[str] = None
    """PAN of the account holder"""
