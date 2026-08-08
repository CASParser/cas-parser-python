# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboxConnectEmailResponse"]


class InboxConnectEmailResponse(BaseModel):
    expires_in: Optional[int] = None
    """Seconds until the OAuth URL expires (typically 10 minutes)"""

    oauth_url: Optional[str] = None
    """Redirect user to this URL to start OAuth flow"""

    provider: Optional[Literal["gmail", "outlook"]] = None
    """The provider this OAuth URL was generated for"""

    status: Optional[str] = None
