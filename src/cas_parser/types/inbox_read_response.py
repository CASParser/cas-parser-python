# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["InboxReadResponse", "MessageAttachment", "MessageBody", "Message"]


class MessageAttachment(BaseModel):
    """An attachment listed by `/v4/inbox/read`, with a direct download URL"""

    attachment_url: Optional[str] = None
    """Direct download URL. No headers required. Valid for 30 minutes after the read."""

    content_type: Optional[str] = None

    filename: Optional[str] = None
    """
    Standardized filename, `{source}_{YYYYMMDD}_{id}.{ext}`, with `custom` in place of the source when there's no known source. The same attachment always gets the same name.
    """

    original_filename: Optional[str] = None
    """Filename as sent"""

    size: Optional[int] = None
    """File size in bytes"""


class MessageBody(BaseModel):
    """
    Present when `include_body` is true. Gmail can return both `html` and `text`, Outlook one of them, Zoho `html` only.
    """

    html: Optional[str] = None

    text: Optional[str] = None


class Message(BaseModel):
    """A message returned by `/v4/inbox/read`"""

    attachments: Optional[List[MessageAttachment]] = None
    """PDF, CSV, XLS and XLSX attachments. Other files, such as images, are left out."""

    body: Optional[MessageBody] = None
    """
    Present when `include_body` is true. Gmail can return both `html` and `text`, Outlook one of them, Zoho `html` only.
    """

    category: Optional[str] = None
    """The source's category. `null` when `source` is."""

    document_type: Optional[str] = None
    """The kind of document the source sends. `null` when `source` is."""

    institution: Optional[str] = None
    """The institution's name. `null` when `source` is."""

    message_date: Optional[date] = None
    """Date the email was received, in IST (UTC+05:30)"""

    message_id: Optional[str] = None
    """The email provider's message ID. It stays the same across reads, so you can skip messages you already have."""

    sender_email: Optional[str] = None
    """Sender address, lowercased"""

    sender_verified: Optional[bool] = None
    """
    The email provider's DMARC check of the sender's domain.
    `true`: passed. `false`: failed. `null`: no result available.
    """

    source: Optional[str] = None
    """The source the message matched. `null` for a message from `senders` that matches no known source."""

    subject: Optional[str] = None


class InboxReadResponse(BaseModel):
    count: Optional[int] = None

    failures: Optional[int] = None
    """Messages that could not be read. The rest are still returned."""

    messages: Optional[List[Message]] = None
    """Newest first"""

    status: Optional[str] = None

    truncated: Optional[bool] = None
    """
    True when more messages may match than were returned. Page back with
    `end_date` as described above, or narrow the range if no messages came back.
    """
