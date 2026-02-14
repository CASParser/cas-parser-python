# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LogGetSummaryResponse", "Summary", "SummaryByFeature"]


class SummaryByFeature(BaseModel):
    credits: Optional[float] = None
    """Credits consumed by this feature"""

    feature: Optional[str] = None
    """API feature name"""

    requests: Optional[int] = None
    """Number of requests for this feature"""


class Summary(BaseModel):
    by_feature: Optional[List[SummaryByFeature]] = None
    """Usage breakdown by feature"""

    total_credits: Optional[float] = None
    """Total credits consumed in the period"""

    total_requests: Optional[int] = None
    """Total API requests made in the period"""


class LogGetSummaryResponse(BaseModel):
    status: Optional[str] = None

    summary: Optional[Summary] = None
