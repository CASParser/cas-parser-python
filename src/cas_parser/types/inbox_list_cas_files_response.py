# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboxListCasFilesResponse", "File"]


class File(BaseModel):
    """A CAS file found in the user's email inbox"""

    cas_type: Optional[Literal["cdsl", "nsdl", "cams", "kfintech"]] = None
    """Detected CAS provider based on sender email"""

    expires_in: Optional[int] = None
    """URL expiration time in seconds (default 86400 = 24 hours)"""

    filename: Optional[str] = None
    """Standardized filename (provider_YYYYMMDD_uniqueid.pdf)"""

    message_date: Optional[date] = None
    """Date the email was received"""

    message_id: Optional[str] = None
    """Unique identifier for the email message (use for subsequent API calls)"""

    original_filename: Optional[str] = None
    """Original attachment filename from the email"""

    sender_email: Optional[str] = None
    """
    Email address of the CAS authority (CDSL, NSDL, CAMS, or KFintech) who
    originally sent this statement
    """

    size: Optional[int] = None
    """File size in bytes"""

    url: Optional[str] = None
    """Direct download URL (presigned, expires based on expires_in)"""


class InboxListCasFilesResponse(BaseModel):
    count: Optional[int] = None
    """Number of CAS files found"""

    files: Optional[List[File]] = None

    status: Optional[str] = None
