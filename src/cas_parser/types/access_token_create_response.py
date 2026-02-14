# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccessTokenCreateResponse"]


class AccessTokenCreateResponse(BaseModel):
    access_token: Optional[str] = None
    """The at\\__ prefixed access token"""

    expires_in: Optional[int] = None
    """Token validity in seconds"""

    token_type: Optional[str] = None
    """Always "api_key" - token is a drop-in replacement for x-api-key header"""
