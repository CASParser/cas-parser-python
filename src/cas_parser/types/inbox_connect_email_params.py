# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboxConnectEmailParams"]


class InboxConnectEmailParams(TypedDict, total=False):
    redirect_uri: Required[str]
    """Your callback URL to receive the inbox_token (must be http or https)"""

    provider: Literal["gmail", "outlook"]
    """Mail provider to connect. Defaults to `gmail`.

    - `gmail` - Google accounts
    - `outlook` - Microsoft accounts

    Any value other than `outlook` is treated as `gmail`. The resolved provider is
    returned in the response.
    """

    state: str
    """State parameter for CSRF protection (returned in redirect)"""
