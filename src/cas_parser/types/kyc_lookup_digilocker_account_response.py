# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["KycLookupDigilockerAccountResponse", "NextStep"]


class NextStep(BaseModel):
    action: Optional[str] = None

    endpoint: Optional[str] = None

    message: Optional[str] = None


class KycLookupDigilockerAccountResponse(BaseModel):
    digilocker_id: Optional[str] = None
    """DigiLocker username if registered, null otherwise."""

    next_step: Optional[NextStep] = None

    reference_id: Optional[str] = None

    registered: Optional[bool] = None
    """Whether the identifier has a DigiLocker account."""

    status: Optional[str] = None

    suggested_user_flow: Optional[Literal["signin", "signup"]] = None
