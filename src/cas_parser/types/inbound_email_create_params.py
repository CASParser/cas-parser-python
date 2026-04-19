# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["InboundEmailCreateParams"]


class InboundEmailCreateParams(TypedDict, total=False):
    alias: str
    """Optional custom email prefix (e.g. `john-portfolio@import.casparser.in`).

    3-32 chars, alphanumeric + hyphens, must start/end with a letter or number. If
    omitted, a random ID is generated.
    """

    allowed_sources: List[Literal["cdsl", "nsdl", "cams", "kfintech"]]
    """Filter emails by CAS provider. If omitted, accepts all providers.

    - `cdsl` → eCAS@cdslstatement.com
    - `nsdl` → NSDL-CAS@nsdl.co.in
    - `cams` → donotreply@camsonline.com
    - `kfintech` → samfS@kfintech.com
    """

    callback_url: Optional[str]
    """Optional webhook URL where we POST parsed emails.

    Must be HTTPS in production (HTTP allowed for localhost). If omitted, retrieve
    files via `GET /v4/inbound-email/{id}/files`.
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
