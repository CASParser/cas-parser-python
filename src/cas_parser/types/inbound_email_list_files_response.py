# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundEmailListFilesResponse", "File"]


class File(BaseModel):
    """
    A CAS file that has arrived at an inbound email address.
    Matches `EmailCASFile` plus a `received_at` timestamp used as a
    monotonic cursor for polling.
    """

    cas_type: Optional[Literal["cdsl", "nsdl", "cams", "kfintech"]] = None
    """Detected CAS provider based on sender email"""

    expires_in: Optional[int] = None
    """
    URL expiration time in seconds. Defaults vary by source:
    - Email Inbox Import (Gmail, Outlook, Zoho): 86400 (24h)
    - Inbound Email with `callback_url` set: 172800 (48h)
    - Inbound Email without `callback_url`: aligned with the session TTL (~30 min)
    """

    filename: Optional[str] = None
    """Standardized filename (provider_YYYYMMDD_uniqueid.pdf)"""

    message_date: Optional[date] = None
    """Date the email was received"""

    message_id: Optional[str] = None
    """Unique identifier for the email message (use for subsequent API calls)"""

    original_filename: Optional[str] = None
    """Original attachment filename from the email"""

    received_at: Optional[datetime] = None
    """
    ISO 8601 timestamp (microsecond precision) when the file was
    persisted. Use as the `since` cursor on subsequent polls.
    """

    sender_email: Optional[str] = None
    """Email address of the CAS authority (CDSL, NSDL, CAMS, or KFintech) who originally sent this statement"""

    size: Optional[int] = None
    """File size in bytes"""

    url: Optional[str] = None
    """Direct download URL (presigned, expires based on expires_in)"""


class InboundEmailListFilesResponse(BaseModel):
    count: Optional[int] = None

    cursor: Optional[datetime] = None
    """Pass as `since` on the next poll. `null` if no files and no prior cursor."""

    files: Optional[List[File]] = None
    """Files received (sorted oldest-first)"""

    status: Optional[str] = None
