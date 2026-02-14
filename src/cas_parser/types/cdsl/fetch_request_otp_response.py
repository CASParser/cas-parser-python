# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FetchRequestOtpResponse"]


class FetchRequestOtpResponse(BaseModel):
    msg: Optional[str] = None

    session_id: Optional[str] = None
    """Session ID for verify step"""

    status: Optional[str] = None
