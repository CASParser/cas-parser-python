# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationVerifyMfdResponse", "NegativeList"]


class NegativeList(BaseModel):
    """Details of the adverse-list hit, else null."""

    since: Optional[str] = None
    """Effective date as published by AMFI."""

    type: Optional[Literal["suspended", "terminated", "euin_terminated"]] = None


class VerificationVerifyMfdResponse(BaseModel):
    """
    Result of an AMFI mutual-fund distributor (ARN) verification. Every listed property is always present on a 200 response (null when not applicable); `verified` is the boolean gate to act on.
    """

    address: Optional[str] = None

    arn: str

    authority: Literal["AMFI"]

    category: Literal["mutual-fund-distributor"]

    category_label: Optional[str] = None

    euin: Optional[str] = None

    is_perpetual: Optional[bool] = None

    kyd_compliant: Optional[bool] = None

    name: Optional[str] = None

    negative_list: Optional[NegativeList] = None
    """Details of the adverse-list hit, else null."""

    negative_list_hit: bool
    """True when the ARN/EUIN appears on an AMFI adverse list."""

    pincode: Optional[str] = None

    registration_status: Literal["ACTIVE", "EXPIRED", "SUSPENDED", "TERMINATED", "NOT_FOUND"]
    """
    ACTIVE = on the active register; SUSPENDED / TERMINATED = on an AMFI adverse list (see `negative_list`); EXPIRED = ARN validity lapsed; NOT_FOUND = no active registration and not on an adverse list.
    """

    status: Literal["success"]

    valid_from: Optional[date] = None

    valid_till: Optional[date] = None

    verified: bool
    """True only when the ARN is on the active register and not on an adverse list."""
