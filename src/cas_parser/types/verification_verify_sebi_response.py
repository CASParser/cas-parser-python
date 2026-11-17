# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationVerifySebiResponse"]


class VerificationVerifySebiResponse(BaseModel):
    """
    Result of a SEBI intermediary verification. Every listed property is always present on a 200 response (fields are null when not applicable); `verified` is the boolean gate to act on.
    """

    address: Optional[str] = None

    authority: Literal["SEBI"]

    category: Literal[
        "investment-adviser",
        "research-analyst",
        "portfolio-manager",
        "stock-broker",
        "merchant-banker",
        "registrar-transfer-agent",
        "mutual-fund",
        "alternative-investment-fund",
        "credit-rating-agency",
        "custodian",
        "debenture-trustee",
        "venture-capital-fund",
        "foreign-venture-capital-investor",
        "foreign-portfolio-investor",
        "kyc-registration-agency",
        "infrastructure-investment-trust",
        "real-estate-investment-trust",
        "esg-rating-provider",
        "vault-manager",
    ]
    """Detected/selected category slug."""

    category_label: Optional[str] = None

    contact_person: Optional[str] = None

    detected_by: Literal["registration_number", "type"]
    """How the category was resolved."""

    email: Optional[str] = None

    is_perpetual: Optional[bool] = None

    name: Optional[str] = None

    registration_number: Optional[str] = None

    registration_status: Literal["ACTIVE", "EXPIRED", "NOT_FOUND"]
    """
    ACTIVE = currently registered; EXPIRED = validity end date passed; NOT_FOUND = no current registration in this category.
    """

    status: Literal["success"]

    telephone: Optional[str] = None

    valid_from: Optional[date] = None

    valid_till: Optional[date] = None
    """Null when the registration is perpetual."""

    verified: bool
    """True only when a current registration is found and ACTIVE."""
