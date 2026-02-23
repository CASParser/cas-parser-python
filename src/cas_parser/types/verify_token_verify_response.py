# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VerifyTokenVerifyResponse"]


class VerifyTokenVerifyResponse(BaseModel):
    error: Optional[str] = None
    """Error message (only shown if invalid)"""

    masked_api_key: Optional[str] = None
    """Masked API key (only shown if valid)"""

    valid: Optional[bool] = None
    """Whether the token is valid"""
