# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["KycCheckPanStatusResponse", "KrasCams", "KrasCvl", "KrasKarvy", "KrasKfin", "KrasNdml", "Kras"]


class KrasCams(BaseModel):
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """KYC completion mode at this KRA"""

    last_updated_on: Optional[date] = None
    """Date KYC was last updated at this KRA"""

    raw_status: Optional[str] = None
    """
    The original status string from the CVL portal. `null` for exact-matched
    statuses. Non-null when a fuzzy match or unknown string was encountered —
    preserve this for debugging and to help us expand coverage.
    """

    registered_on: Optional[date] = None
    """Date KYC was first registered at this KRA"""

    remarks: Optional[str] = None
    """
    Remarks from the KRA. Only actionable when `status` is `on_hold`
    (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
    remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.
    Multiple remarks are comma-separated.
    """

    status: Literal[
        "validated",
        "registered",
        "under_process",
        "on_hold",
        "rejected",
        "legacy",
        "not_available",
        "not_checked",
        "unknown",
    ]
    """Normalized status for this KRA"""


class KrasCvl(BaseModel):
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """KYC completion mode at this KRA"""

    last_updated_on: Optional[date] = None
    """Date KYC was last updated at this KRA"""

    raw_status: Optional[str] = None
    """
    The original status string from the CVL portal. `null` for exact-matched
    statuses. Non-null when a fuzzy match or unknown string was encountered —
    preserve this for debugging and to help us expand coverage.
    """

    registered_on: Optional[date] = None
    """Date KYC was first registered at this KRA"""

    remarks: Optional[str] = None
    """
    Remarks from the KRA. Only actionable when `status` is `on_hold`
    (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
    remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.
    Multiple remarks are comma-separated.
    """

    status: Literal[
        "validated",
        "registered",
        "under_process",
        "on_hold",
        "rejected",
        "legacy",
        "not_available",
        "not_checked",
        "unknown",
    ]
    """Normalized status for this KRA"""


class KrasKarvy(BaseModel):
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """KYC completion mode at this KRA"""

    last_updated_on: Optional[date] = None
    """Date KYC was last updated at this KRA"""

    raw_status: Optional[str] = None
    """
    The original status string from the CVL portal. `null` for exact-matched
    statuses. Non-null when a fuzzy match or unknown string was encountered —
    preserve this for debugging and to help us expand coverage.
    """

    registered_on: Optional[date] = None
    """Date KYC was first registered at this KRA"""

    remarks: Optional[str] = None
    """
    Remarks from the KRA. Only actionable when `status` is `on_hold`
    (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
    remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.
    Multiple remarks are comma-separated.
    """

    status: Literal[
        "validated",
        "registered",
        "under_process",
        "on_hold",
        "rejected",
        "legacy",
        "not_available",
        "not_checked",
        "unknown",
    ]
    """Normalized status for this KRA"""


class KrasKfin(BaseModel):
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """KYC completion mode at this KRA"""

    last_updated_on: Optional[date] = None
    """Date KYC was last updated at this KRA"""

    raw_status: Optional[str] = None
    """
    The original status string from the CVL portal. `null` for exact-matched
    statuses. Non-null when a fuzzy match or unknown string was encountered —
    preserve this for debugging and to help us expand coverage.
    """

    registered_on: Optional[date] = None
    """Date KYC was first registered at this KRA"""

    remarks: Optional[str] = None
    """
    Remarks from the KRA. Only actionable when `status` is `on_hold`
    (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
    remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.
    Multiple remarks are comma-separated.
    """

    status: Literal[
        "validated",
        "registered",
        "under_process",
        "on_hold",
        "rejected",
        "legacy",
        "not_available",
        "not_checked",
        "unknown",
    ]
    """Normalized status for this KRA"""


class KrasNdml(BaseModel):
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """KYC completion mode at this KRA"""

    last_updated_on: Optional[date] = None
    """Date KYC was last updated at this KRA"""

    raw_status: Optional[str] = None
    """
    The original status string from the CVL portal. `null` for exact-matched
    statuses. Non-null when a fuzzy match or unknown string was encountered —
    preserve this for debugging and to help us expand coverage.
    """

    registered_on: Optional[date] = None
    """Date KYC was first registered at this KRA"""

    remarks: Optional[str] = None
    """
    Remarks from the KRA. Only actionable when `status` is `on_hold`
    (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
    remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.
    Multiple remarks are comma-separated.
    """

    status: Literal[
        "validated",
        "registered",
        "under_process",
        "on_hold",
        "rejected",
        "legacy",
        "not_available",
        "not_checked",
        "unknown",
    ]
    """Normalized status for this KRA"""


class Kras(BaseModel):
    """Per-KRA status breakdown. All five KRA keys are always present."""

    cams: KrasCams
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    cvl: KrasCvl
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    karvy: KrasKarvy
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    kfin: KrasKfin
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """

    ndml: KrasNdml
    """
    KYC status at a single KRA. All six keys are always present (never omitted).
    For `not_checked` and `not_available` KRAs, date/mode/remarks fields are `null`.
    """


class KycCheckPanStatusResponse(BaseModel):
    """Normalized KYC status response for a PAN number"""

    active_kra: Optional[Literal["cvl", "ndml", "cams", "karvy", "kfin"]] = None
    """Short key of the KRA where the active KYC record was found"""

    kras: Optional[Kras] = None
    """Per-KRA status breakdown. All five KRA keys are always present."""

    kyc_compliant: Optional[bool] = None
    """
    `true` if the investor has a `validated` or `registered` KYC record.
    Use this as the primary onboarding gate signal.
    """

    kyc_mode: Optional[Literal["normal", "digilocker", "ekyc", "paper", "unknown"]] = None
    """
    How the KYC was completed. Possible values:
    - `normal` — Physical/paper KYC
    - `digilocker` — DigiLocker-backed digital KYC
    - `ekyc` — Aadhaar eKYC (OTP-based)
    - `paper` — Offline paper submission
    - `unknown` — Mode string not recognized
    """

    kyc_status: Optional[
        Literal["validated", "registered", "under_process", "on_hold", "rejected", "legacy", "not_available", "unknown"]
    ] = None
    """
    Normalized KYC status from the active KRA. Possible values:
    - `validated` — KYC complete, investor can onboard and transact freely
    - `registered` — KYC registered; some restrictions may apply depending on your platform's onboarding policy
    - `under_process` — Recently submitted KYC, still being processed by KRA
    - `on_hold` — KYC on hold due to discrepancy; check `remarks` on the KRA object
    - `rejected` — KYC rejected; investor must submit fresh KYC
    - `legacy` — Old/incomplete record; re-KYC recommended
    - `not_available` — No KYC record found at any KRA
    - `unknown` — Portal returned an unrecognized string; `raw_status` preserved
    """

    last_updated_on: Optional[date] = None
    """Date the KYC record was last updated at the active KRA (ISO 8601)"""

    pan: Optional[str] = None
    """The PAN number that was queried (uppercase)"""

    registered_on: Optional[date] = None
    """Date the KYC was first registered at the active KRA (ISO 8601)"""

    status: Optional[Literal["success"]] = None
