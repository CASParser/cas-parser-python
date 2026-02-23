# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundEmailCreateParams"]


class InboundEmailCreateParams(TypedDict, total=False):
    callback_url: Required[str]
    """
    Webhook URL where we POST email notifications. Must be HTTPS in production (HTTP
    allowed for localhost during development).
    """

    alias: str
    """Optional custom email prefix for user-friendly addresses.

    - Must be 3-32 characters
    - Alphanumeric + hyphens only
    - Must start and end with letter/number
    - Example: `john-portfolio@import.casparser.in`
    - If omitted, generates random ID like `ie_abc123xyz@import.casparser.in`
    """

    allowed_sources: List[Literal["cdsl", "nsdl", "cams", "kfintech"]]
    """Filter emails by CAS provider. If omitted, accepts all providers.

    - `cdsl` → eCAS@cdslstatement.com
    - `nsdl` → NSDL-CAS@nsdl.co.in
    - `cams` → donotreply@camsonline.com
    - `kfintech` → samfS@kfintech.com
    """

    metadata: Dict[str, str]
    """
    Optional key-value pairs (max 10) to include in webhook payload. Useful for
    passing context like plan_type, campaign_id, etc.
    """

    reference: str
    """
    Your internal identifier (e.g., user_id, account_id). Returned in webhook
    payload for correlation.
    """
