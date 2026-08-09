# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboxConnectEmailParams"]


class InboxConnectEmailParams(TypedDict, total=False):
    redirect_uri: Required[str]
    """Your callback URL to receive the inbox_token (must be http or https)"""

    provider: Literal["gmail", "outlook", "zoho"]
    """Mail provider to connect. Defaults to `gmail`.

    - `gmail` - Google accounts: `@gmail.com` and Google Workspace domains.
    - `outlook` - personal Microsoft accounts: `@outlook.com`, `@hotmail.com`,
      `@live.com`, `@msn.com` and localised variants (`@hotmail.co.uk`, `@live.in`,
      `@hotmail.fr`). Any other address registered as a personal Microsoft account
      also works, including custom domains.
    - `zoho` - Zoho Mail accounts, including custom domains hosted on Zoho.

    Any unrecognised value is treated as `gmail`. The resolved provider is returned
    in the response.
    """

    state: str
    """State parameter for CSRF protection (returned in redirect)"""
