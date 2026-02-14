# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboxListCasFilesParams"]


class InboxListCasFilesParams(TypedDict, total=False):
    x_inbox_token: Required[Annotated[str, PropertyInfo(alias="x-inbox-token")]]

    cas_types: List[Literal["cdsl", "nsdl", "cams", "kfintech"]]
    """Filter by CAS provider(s):

    - `cdsl` → eCAS@cdslstatement.com
    - `nsdl` → NSDL-CAS@nsdl.co.in
    - `cams` → donotreply@camsonline.com
    - `kfintech` → samfS@kfintech.com
    """

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """End date in ISO format (YYYY-MM-DD). Defaults to today."""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Start date in ISO format (YYYY-MM-DD). Defaults to 30 days ago."""
