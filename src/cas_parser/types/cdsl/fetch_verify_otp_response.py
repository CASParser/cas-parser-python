# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FetchVerifyOtpResponse", "File"]


class File(BaseModel):
    filename: Optional[str] = None

    url: Optional[str] = None
    """Direct download URL (cloud storage)"""


class FetchVerifyOtpResponse(BaseModel):
    files: Optional[List[File]] = None

    msg: Optional[str] = None

    status: Optional[str] = None
