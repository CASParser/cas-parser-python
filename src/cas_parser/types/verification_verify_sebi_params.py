# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VerificationVerifySebiParams"]


class VerificationVerifySebiParams(TypedDict, total=False):
    name: str
    """Entity/trade name to search by. Used only when `registration_number` is absent, and then `type` is required."""

    registration_number: str
    """
    SEBI registration number. When provided, the category is auto-detected from its sequence (INA…→investment-adviser, INH…→research-analyst, INP…→portfolio-manager, INM…→merchant-banker, INR…→registrar-transfer-agent, INZ…→stock-broker). This is the authoritative input — any `name` sent alongside it is ignored.
    """

    type: Literal[
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
    """
    Category slug. Overrides auto-detection; required for a name search and for fund/FPI registration numbers that don't encode a category. Short aliases are also accepted (ria, ra, pms, broker, rta, mf, aif, cra, vcf, fvci, fpi, kra, invit, reit).
    """
