# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InboxCheckConnectionStatusResponse"]


class InboxCheckConnectionStatusResponse(BaseModel):
    connected: Optional[bool] = None
    """Whether the token is valid and usable"""

    email: Optional[str] = None
    """Email address of the connected account"""

    provider: Optional[str] = None

    status: Optional[str] = None
