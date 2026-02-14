# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LogCreateResponse", "Log"]


class Log(BaseModel):
    credits: Optional[float] = None
    """Credits consumed for this request"""

    feature: Optional[str] = None
    """API feature used"""

    path: Optional[str] = None
    """API endpoint path"""

    request_id: Optional[str] = None
    """Unique request identifier"""

    status_code: Optional[int] = None
    """HTTP response status code"""

    timestamp: Optional[datetime] = None
    """When the request was made"""


class LogCreateResponse(BaseModel):
    count: Optional[int] = None
    """Number of logs returned"""

    logs: Optional[List[Log]] = None

    status: Optional[str] = None
