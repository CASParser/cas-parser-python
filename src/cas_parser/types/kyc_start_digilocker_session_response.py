# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["KycStartDigilockerSessionResponse"]


class KycStartDigilockerSessionResponse(BaseModel):
    authorization_url: Optional[str] = None
    """DigiLocker consent URL to redirect the investor to."""

    expires_in: Optional[int] = None
    """Seconds the authorization_url is valid for."""

    session_id: Optional[str] = None
    """
    The single identifier for this verification. Use it as the
    path parameter in `POST /v1/kyc/digilocker/result/{session_id}`
    to retrieve identity + documents.
    """

    status: Optional[str] = None
