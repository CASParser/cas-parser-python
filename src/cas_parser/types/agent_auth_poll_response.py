# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AgentAuthPollResponse", "AgentAuthPollResponsePending", "AgentAuthPollResponseApproved"]


class AgentAuthPollResponsePending(BaseModel):
    status: Optional[Literal["pending"]] = None


class AgentAuthPollResponseApproved(BaseModel):
    api_key: Optional[str] = None
    """The issued API key (sk_ prefix)"""

    email: Optional[str] = None
    """Email of the user who approved"""

    status: Optional[Literal["approved"]] = None


AgentAuthPollResponse: TypeAlias = Union[AgentAuthPollResponsePending, AgentAuthPollResponseApproved]
