# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationVerifyMfdParams"]


class VerificationVerifyMfdParams(TypedDict, total=False):
    arn: Required[str]
    """AMFI Registration Number. Digits only; an `ARN-` prefix is tolerated."""
