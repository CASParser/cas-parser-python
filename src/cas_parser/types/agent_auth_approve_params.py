# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentAuthApproveParams"]


class AgentAuthApproveParams(TypedDict, total=False):
    id_token: Required[str]
    """Identity token obtained after the user signs in on the approval page"""

    client_name: str
    """Name of the agent/application (stored in customer metadata for audit)"""
