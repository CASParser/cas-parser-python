# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentAuthApproveResponse"]


class AgentAuthApproveResponse(BaseModel):
    email: Optional[str] = None

    status: Optional[str] = None
