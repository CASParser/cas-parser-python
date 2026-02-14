# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FetchVerifyOtpParams"]


class FetchVerifyOtpParams(TypedDict, total=False):
    otp: Required[str]
    """OTP received on mobile"""

    num_periods: int
    """Number of monthly statements to fetch (default 6)"""
