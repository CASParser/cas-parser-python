# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CreditCheckResponse"]


class CreditCheckResponse(BaseModel):
    enabled_features: Optional[List[str]] = None
    """List of API features enabled for your plan"""

    is_unlimited: Optional[bool] = None
    """Whether the account has unlimited credits"""

    limit: Optional[int] = None
    """Total credit limit for billing period"""

    remaining: Optional[float] = None
    """Remaining credits (null if unlimited)"""

    resets_at: Optional[datetime] = None
    """When credits reset (ISO 8601)"""

    used: Optional[float] = None
    """Number of credits used this billing period"""
