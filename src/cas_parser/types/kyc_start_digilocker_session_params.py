# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["KycStartDigilockerSessionParams"]


class KycStartDigilockerSessionParams(TypedDict, total=False):
    consent: Required[bool]
    """
    Explicit end-user consent. Must be `true` to proceed
    (regulatory requirement under DPDP / RBI). Captured for audit.
    """

    consent_purpose: Required[str]
    """
    Specific purpose for which consent is taken (min 20 chars).
    Stored in the session and returned as a consent receipt.
    """

    redirect_url: Required[str]
    """Where to redirect the user after consent. Must be a valid http/https URL."""

    documents: List[Literal["aadhaar", "pan", "driving_licence", "email", "mobile"]]
    """Identities to verify and return in the response."""

    prefill_mobile: str
    """Pre-verified mobile to skip the signup OTP step (only applies with user_flow=signup)."""

    state: str
    """Opaque value echoed back to your redirect_url unchanged."""

    user_flow: Literal["signin", "signup"]
    """Use "signin" for users with an existing DigiLocker account, "signup" for account-on-the-fly."""
