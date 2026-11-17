# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["InboxReadParams"]


class InboxReadParams(TypedDict, total=False):
    x_inbox_token: Required[Annotated[str, PropertyInfo(alias="x-inbox-token")]]
    """The encrypted inbox token"""

    categories: List[Literal["investments", "credit", "banking", "insurance", "tax"]]
    """Read every source in these categories."""

    document_types: List[
        Literal[
            "consolidated_statement",
            "contract_note",
            "broker_statement",
            "nps_statement",
            "card_statement",
            "account_statement",
            "insurance_document",
            "tax_notice",
            "tds_certificate",
        ]
    ]
    """Read every source of these document types."""

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Last day to search (YYYY-MM-DD, inclusive, IST). Defaults to today in IST."""

    include_body: bool
    """Return each message's body as well."""

    senders: SequenceNotStr[str]
    """
    Exact sender addresses to read, for institutions not in the table above. Domains and wildcards aren't accepted.
    """

    sources: List[
        Literal[
            "cams",
            "kfintech",
            "cdsl",
            "nsdl",
            "zerodha_contract_note",
            "zerodha_statement",
            "kfintech_nps",
            "protean_nps",
            "hdfc_credit_card",
            "sbi_card",
            "icici_credit_card",
            "axis_credit_card",
            "idfc_first_credit_card",
            "kotak_credit_card",
            "rbl_credit_card",
            "bobcard",
            "yes_credit_card",
            "indusind_credit_card",
            "scapia_credit_card",
            "au_credit_card",
            "niyo_global_credit_card",
            "hdfc_bank_account",
            "sbi_bank_account",
            "icici_bank_account",
            "axis_bank_account",
            "kotak_bank_account",
            "idfc_first_bank_account",
            "yes_bank_account",
            "au_bank_account",
            "sbm_bank_account",
            "federal_bank_account",
            "policybazaar",
            "icici_lombard",
            "hdfc_life",
            "income_tax",
            "dividend_tds",
        ]
    ]
    """Read these sources."""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """First day to search (YYYY-MM-DD, inclusive, IST). Defaults to 30 days before `end_date`."""
