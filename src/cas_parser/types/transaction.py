# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Transaction", "AdditionalInfo"]


class AdditionalInfo(BaseModel):
    """Additional transaction-specific fields that vary by source"""

    capital_withdrawal: Optional[float] = None
    """Capital withdrawal amount (CDSL MF transactions)"""

    credit: Optional[float] = None
    """Units credited (demat transactions)"""

    debit: Optional[float] = None
    """Units debited (demat transactions)"""

    income_distribution: Optional[float] = None
    """Income distribution amount (CDSL MF transactions)"""

    order_no: Optional[str] = None
    """Order/transaction reference number (demat transactions)"""

    price: Optional[float] = None
    """Price per unit (NSDL/CDSL MF transactions)"""

    stamp_duty: Optional[float] = None
    """Stamp duty charged"""


class Transaction(BaseModel):
    """
    Unified transaction schema for all holding types (MF folios, equities, bonds, etc.)
    """

    additional_info: Optional[AdditionalInfo] = None
    """Additional transaction-specific fields that vary by source"""

    amount: Optional[float] = None
    """Transaction amount in currency (computed from units × price/NAV)"""

    balance: Optional[float] = None
    """Balance units after transaction"""

    date: Optional[datetime.date] = None
    """Transaction date (YYYY-MM-DD)"""

    description: Optional[str] = None
    """Transaction description/particulars"""

    dividend_rate: Optional[float] = None
    """Dividend rate (for DIVIDEND_PAYOUT transactions)"""

    nav: Optional[float] = None
    """NAV/price per unit on transaction date"""

    type: Optional[
        Literal[
            "PURCHASE",
            "PURCHASE_SIP",
            "REDEMPTION",
            "SWITCH_IN",
            "SWITCH_IN_MERGER",
            "SWITCH_OUT",
            "SWITCH_OUT_MERGER",
            "DIVIDEND_PAYOUT",
            "DIVIDEND_REINVEST",
            "SEGREGATION",
            "STAMP_DUTY_TAX",
            "TDS_TAX",
            "STT_TAX",
            "MISC",
            "REVERSAL",
            "UNKNOWN",
        ]
    ] = None
    """Transaction type.

    Possible values are PURCHASE, PURCHASE_SIP, REDEMPTION, SWITCH_IN,
    SWITCH_IN_MERGER, SWITCH_OUT, SWITCH_OUT_MERGER, DIVIDEND_PAYOUT,
    DIVIDEND_REINVEST, SEGREGATION, STAMP_DUTY_TAX, TDS_TAX, STT_TAX, MISC,
    REVERSAL, UNKNOWN.
    """

    units: Optional[float] = None
    """Number of units involved in transaction"""
