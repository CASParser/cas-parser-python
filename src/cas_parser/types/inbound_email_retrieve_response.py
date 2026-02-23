# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundEmailRetrieveResponse"]


class InboundEmailRetrieveResponse(BaseModel):
    """An inbound email address for receiving forwarded CAS emails"""

    allowed_sources: Optional[List[Literal["cdsl", "nsdl", "cams", "kfintech"]]] = None
    """Accepted CAS providers (empty = all)"""

    callback_url: Optional[str] = None
    """Webhook URL for email notifications"""

    created_at: Optional[datetime] = None
    """When the mailbox was created"""

    email: Optional[str] = None
    """The inbound email address to forward CAS statements to"""

    inbound_email_id: Optional[str] = None
    """Unique inbound email identifier"""

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata"""

    reference: Optional[str] = None
    """Your internal reference identifier"""

    status: Optional[Literal["active", "paused"]] = None
    """Current mailbox status"""

    updated_at: Optional[datetime] = None
    """When the mailbox was last updated"""
