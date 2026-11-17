# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import inbox_read_params, inbox_connect_email_params, inbox_list_cas_files_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.inbox_read_response import InboxReadResponse
from ..types.inbox_connect_email_response import InboxConnectEmailResponse
from ..types.inbox_list_cas_files_response import InboxListCasFilesResponse
from ..types.inbox_disconnect_email_response import InboxDisconnectEmailResponse
from ..types.inbox_check_connection_status_response import InboxCheckConnectionStatusResponse

__all__ = ["InboxResource", "AsyncInboxResource"]


class InboxResource(SyncAPIResource):
    """Endpoints for importing CAS files directly from user email inboxes.

    **Supported Providers:**

    - **Gmail** (`gmail`, default) — `@gmail.com` and Google Workspace domains
    - **Microsoft** (`outlook`) — personal Microsoft accounts: `@outlook.com`,
      `@hotmail.com`, `@live.com`, `@msn.com`, and localised variants such as
      `@hotmail.co.uk`, `@live.in`, `@hotmail.fr`. Any other address registered
      as a personal Microsoft account also works, including custom domains.
    - **Zoho Mail** (`zoho`) — Zoho-hosted mailboxes, including custom domains

    **How it works:**
    1. Call `POST /v4/inbox/connect` to get an OAuth URL
    2. Redirect user to the OAuth URL for consent
    3. User is redirected back to your `redirect_uri` with an encrypted `inbox_token`
    4. Use the token to list/fetch CAS files from their inbox (`/v4/inbox/cas`)
    5. Files are uploaded to temporary cloud storage (URLs expire in 24 hours)

    **Security:**
    - Read-only access (we cannot send emails)
    - Tokens are encrypted with server-side secret
    - User can revoke access anytime via `/v4/inbox/disconnect`
    """

    @cached_property
    def with_raw_response(self) -> InboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return InboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return InboxResourceWithStreamingResponse(self)

    def check_connection_status(
        self,
        *,
        x_inbox_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxCheckConnectionStatusResponse:
        """
        Verify if an `inbox_token` is still valid and check connection status.

        Use this to check if the user needs to re-authenticate (e.g., if they revoked
        access in their email provider settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return self._post(
            "/v4/inbox/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxCheckConnectionStatusResponse,
        )

    def connect_email(
        self,
        *,
        redirect_uri: str,
        provider: Literal["gmail", "outlook", "zoho"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxConnectEmailResponse:
        """
        Initiate OAuth flow to connect user's email inbox.

        Returns an `oauth_url` that you should redirect the user to. After
        authorization, they are redirected back to your `redirect_uri` with the
        following query parameters:

        **On success:**

        - `inbox_token` - Encrypted token to store client-side
        - `email` - Email address of the connected account
        - `state` - Your original state parameter (for CSRF verification)

        **On error:**

        - `error` - Error code (e.g., `access_denied`, `token_exchange_failed`)
        - `state` - Your original state parameter

        **Store the `inbox_token` client-side** and use it for all subsequent inbox API
        calls. The token is long-lived (it stores an encrypted refresh token), so a
        single OAuth connect gives ongoing access to both historical and future CAS
        statements in the user's inbox. Reuse the same token until the user revokes
        access via `/v4/inbox/disconnect` or their provider's account settings.

        Args:
          redirect_uri: Your callback URL to receive the inbox_token (must be http or https)

          provider: Mail provider to connect. Defaults to `gmail`.

              - `gmail` - Google accounts: `@gmail.com` and Google Workspace domains.
              - `outlook` - personal Microsoft accounts: `@outlook.com`, `@hotmail.com`,
                `@live.com`, `@msn.com` and localised variants (`@hotmail.co.uk`, `@live.in`,
                `@hotmail.fr`). Any other address registered as a personal Microsoft account
                also works, including custom domains.
              - `zoho` - Zoho Mail accounts, including custom domains hosted on Zoho.

              Any unrecognised value is treated as `gmail`. The resolved provider is returned
              in the response.

          state: State parameter for CSRF protection (returned in redirect)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/inbox/connect",
            body=maybe_transform(
                {
                    "redirect_uri": redirect_uri,
                    "provider": provider,
                    "state": state,
                },
                inbox_connect_email_params.InboxConnectEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxConnectEmailResponse,
        )

    def disconnect_email(
        self,
        *,
        x_inbox_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxDisconnectEmailResponse:
        """
        Revoke email access and invalidate the token.

        This calls the provider's token revocation API (e.g., Google's revoke endpoint)
        to ensure the user's consent is properly removed.

        After calling this, the `inbox_token` becomes unusable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return self._post(
            "/v4/inbox/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxDisconnectEmailResponse,
        )

    def list_cas_files(
        self,
        *,
        x_inbox_token: str,
        cas_types: List[Literal["cdsl", "nsdl", "cams", "kfintech"]] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxListCasFilesResponse:
        """
        Search the user's email inbox for CAS files from known senders (CAMS, KFintech,
        CDSL, NSDL).

        Files are uploaded to temporary cloud storage. **URLs expire in 24 hours.**

        Optionally filter by CAS provider and date range.

        **Billing:** 0.2 credits per request (charged regardless of success or number of
        files found).

        Args:
          cas_types:
              Filter by CAS provider(s):

              - `cdsl` → eCAS@cdslstatement.com
              - `nsdl` → NSDL-CAS@nsdl.co.in
              - `cams` → donotreply@camsonline.com
              - `kfintech` → samfS@kfintech.com

          end_date: End date in ISO format (YYYY-MM-DD). Defaults to today.

          start_date: Start date in ISO format (YYYY-MM-DD). Defaults to 30 days ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return self._post(
            "/v4/inbox/cas",
            body=maybe_transform(
                {
                    "cas_types": cas_types,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                inbox_list_cas_files_params.InboxListCasFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxListCasFilesResponse,
        )

    def read(
        self,
        *,
        x_inbox_token: str,
        categories: List[Literal["investments", "credit", "banking", "insurance", "tax"]] | Omit = omit,
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
        | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        include_body: bool | Omit = omit,
        senders: SequenceNotStr[str] | Omit = omit,
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
        | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxReadResponse:
        """
        List statement emails and their attachment details in a connected mailbox.

        Download files directly from their `attachment_url`. No additional
        headers are needed. URLs expire 30 minutes after this read.
        Anyone with a URL can download that file until it expires, so keep
        these URLs private.

        A source is one institution sending one kind of document. Each has a
        category and a document type, listed below. Choose what to read with any
        mix of `categories`, `document_types`, `sources` and `senders` (at least
        one); you get everything that matches any of them. For example,
        `document_types: ["card_statement"]` reads every card issuer, and
        `document_types: ["consolidated_statement"]` reads CAS only.

        | Category | Document type | Sources |
        |---|---|---|
        | `investments` | `consolidated_statement` | `cams`, `kfintech`, `cdsl`, `nsdl` |
        | `investments` | `contract_note` | `zerodha_contract_note` |
        | `investments` | `broker_statement` | `zerodha_statement` |
        | `investments` | `nps_statement` | `kfintech_nps`, `protean_nps` |
        | `credit` | `card_statement` | `hdfc_credit_card`, `sbi_card`, `icici_credit_card`, `axis_credit_card`, `idfc_first_credit_card`, `kotak_credit_card`, `rbl_credit_card`, `bobcard`, `yes_credit_card`, `indusind_credit_card`, `scapia_credit_card`, `au_credit_card`, `niyo_global_credit_card` |
        | `banking` | `account_statement` | `hdfc_bank_account`, `sbi_bank_account`, `icici_bank_account`, `axis_bank_account`, `kotak_bank_account`, `idfc_first_bank_account`, `yes_bank_account`, `au_bank_account`, `sbm_bank_account`, `federal_bank_account` |
        | `insurance` | `insurance_document` | `policybazaar`, `icici_lombard`, `hdfc_life` |
        | `tax` | `tax_notice` | `income_tax` |
        | `tax` | `tds_certificate` | `dividend_tds` |

        To read from an institution that isn't listed, pass its exact addresses
        in `senders` (up to 20 per request). A message from one of them is
        labelled with the known source it matches, if any; otherwise `source`,
        `category`, `document_type` and `institution` are `null`.

        **Sender verification:** `sender_verified` is the email provider's DMARC
        check of the sender's domain: `true` means it passed, `false` means it
        failed, and `null` means no result was available.

        **Paging:** at most 50 messages per call, newest first. When `truncated`
        is true, call again with `end_date` set to the oldest `message_date` you
        received, and skip `message_id`s you already have.

        `start_date` and `end_date` are inclusive calendar dates in IST
        (UTC+05:30). `message_date` is the date the email was received, also in IST.

        **Billing:** 0.2 credits per request (charged regardless of success or number of messages found). Attachment downloads are free.

        Args:
          categories: Read every source in these categories.

          document_types: Read every source of these document types.

          end_date: Last day to search (YYYY-MM-DD, inclusive, IST). Defaults to today in IST.

          include_body: Return each message's body as well.

          senders: Exact sender addresses to read, for institutions not in the table above. Domains and wildcards aren't accepted.

          sources: Read these sources.

          start_date: First day to search (YYYY-MM-DD, inclusive, IST). Defaults to 30 days before `end_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return self._post(
            "/v4/inbox/read",
            body=maybe_transform(
                {
                    "categories": categories,
                    "document_types": document_types,
                    "end_date": end_date,
                    "include_body": include_body,
                    "senders": senders,
                    "sources": sources,
                    "start_date": start_date,
                },
                inbox_read_params.InboxReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxReadResponse,
        )


class AsyncInboxResource(AsyncAPIResource):
    """Endpoints for importing CAS files directly from user email inboxes.

    **Supported Providers:**

    - **Gmail** (`gmail`, default) — `@gmail.com` and Google Workspace domains
    - **Microsoft** (`outlook`) — personal Microsoft accounts: `@outlook.com`,
      `@hotmail.com`, `@live.com`, `@msn.com`, and localised variants such as
      `@hotmail.co.uk`, `@live.in`, `@hotmail.fr`. Any other address registered
      as a personal Microsoft account also works, including custom domains.
    - **Zoho Mail** (`zoho`) — Zoho-hosted mailboxes, including custom domains

    **How it works:**
    1. Call `POST /v4/inbox/connect` to get an OAuth URL
    2. Redirect user to the OAuth URL for consent
    3. User is redirected back to your `redirect_uri` with an encrypted `inbox_token`
    4. Use the token to list/fetch CAS files from their inbox (`/v4/inbox/cas`)
    5. Files are uploaded to temporary cloud storage (URLs expire in 24 hours)

    **Security:**
    - Read-only access (we cannot send emails)
    - Tokens are encrypted with server-side secret
    - User can revoke access anytime via `/v4/inbox/disconnect`
    """

    @cached_property
    def with_raw_response(self) -> AsyncInboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncInboxResourceWithStreamingResponse(self)

    async def check_connection_status(
        self,
        *,
        x_inbox_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxCheckConnectionStatusResponse:
        """
        Verify if an `inbox_token` is still valid and check connection status.

        Use this to check if the user needs to re-authenticate (e.g., if they revoked
        access in their email provider settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return await self._post(
            "/v4/inbox/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxCheckConnectionStatusResponse,
        )

    async def connect_email(
        self,
        *,
        redirect_uri: str,
        provider: Literal["gmail", "outlook", "zoho"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxConnectEmailResponse:
        """
        Initiate OAuth flow to connect user's email inbox.

        Returns an `oauth_url` that you should redirect the user to. After
        authorization, they are redirected back to your `redirect_uri` with the
        following query parameters:

        **On success:**

        - `inbox_token` - Encrypted token to store client-side
        - `email` - Email address of the connected account
        - `state` - Your original state parameter (for CSRF verification)

        **On error:**

        - `error` - Error code (e.g., `access_denied`, `token_exchange_failed`)
        - `state` - Your original state parameter

        **Store the `inbox_token` client-side** and use it for all subsequent inbox API
        calls. The token is long-lived (it stores an encrypted refresh token), so a
        single OAuth connect gives ongoing access to both historical and future CAS
        statements in the user's inbox. Reuse the same token until the user revokes
        access via `/v4/inbox/disconnect` or their provider's account settings.

        Args:
          redirect_uri: Your callback URL to receive the inbox_token (must be http or https)

          provider: Mail provider to connect. Defaults to `gmail`.

              - `gmail` - Google accounts: `@gmail.com` and Google Workspace domains.
              - `outlook` - personal Microsoft accounts: `@outlook.com`, `@hotmail.com`,
                `@live.com`, `@msn.com` and localised variants (`@hotmail.co.uk`, `@live.in`,
                `@hotmail.fr`). Any other address registered as a personal Microsoft account
                also works, including custom domains.
              - `zoho` - Zoho Mail accounts, including custom domains hosted on Zoho.

              Any unrecognised value is treated as `gmail`. The resolved provider is returned
              in the response.

          state: State parameter for CSRF protection (returned in redirect)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/inbox/connect",
            body=await async_maybe_transform(
                {
                    "redirect_uri": redirect_uri,
                    "provider": provider,
                    "state": state,
                },
                inbox_connect_email_params.InboxConnectEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxConnectEmailResponse,
        )

    async def disconnect_email(
        self,
        *,
        x_inbox_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxDisconnectEmailResponse:
        """
        Revoke email access and invalidate the token.

        This calls the provider's token revocation API (e.g., Google's revoke endpoint)
        to ensure the user's consent is properly removed.

        After calling this, the `inbox_token` becomes unusable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return await self._post(
            "/v4/inbox/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxDisconnectEmailResponse,
        )

    async def list_cas_files(
        self,
        *,
        x_inbox_token: str,
        cas_types: List[Literal["cdsl", "nsdl", "cams", "kfintech"]] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxListCasFilesResponse:
        """
        Search the user's email inbox for CAS files from known senders (CAMS, KFintech,
        CDSL, NSDL).

        Files are uploaded to temporary cloud storage. **URLs expire in 24 hours.**

        Optionally filter by CAS provider and date range.

        **Billing:** 0.2 credits per request (charged regardless of success or number of
        files found).

        Args:
          cas_types:
              Filter by CAS provider(s):

              - `cdsl` → eCAS@cdslstatement.com
              - `nsdl` → NSDL-CAS@nsdl.co.in
              - `cams` → donotreply@camsonline.com
              - `kfintech` → samfS@kfintech.com

          end_date: End date in ISO format (YYYY-MM-DD). Defaults to today.

          start_date: Start date in ISO format (YYYY-MM-DD). Defaults to 30 days ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return await self._post(
            "/v4/inbox/cas",
            body=await async_maybe_transform(
                {
                    "cas_types": cas_types,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                inbox_list_cas_files_params.InboxListCasFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxListCasFilesResponse,
        )

    async def read(
        self,
        *,
        x_inbox_token: str,
        categories: List[Literal["investments", "credit", "banking", "insurance", "tax"]] | Omit = omit,
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
        | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        include_body: bool | Omit = omit,
        senders: SequenceNotStr[str] | Omit = omit,
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
        | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboxReadResponse:
        """
        List statement emails and their attachment details in a connected mailbox.

        Download files directly from their `attachment_url`. No additional
        headers are needed. URLs expire 30 minutes after this read.
        Anyone with a URL can download that file until it expires, so keep
        these URLs private.

        A source is one institution sending one kind of document. Each has a
        category and a document type, listed below. Choose what to read with any
        mix of `categories`, `document_types`, `sources` and `senders` (at least
        one); you get everything that matches any of them. For example,
        `document_types: ["card_statement"]` reads every card issuer, and
        `document_types: ["consolidated_statement"]` reads CAS only.

        | Category | Document type | Sources |
        |---|---|---|
        | `investments` | `consolidated_statement` | `cams`, `kfintech`, `cdsl`, `nsdl` |
        | `investments` | `contract_note` | `zerodha_contract_note` |
        | `investments` | `broker_statement` | `zerodha_statement` |
        | `investments` | `nps_statement` | `kfintech_nps`, `protean_nps` |
        | `credit` | `card_statement` | `hdfc_credit_card`, `sbi_card`, `icici_credit_card`, `axis_credit_card`, `idfc_first_credit_card`, `kotak_credit_card`, `rbl_credit_card`, `bobcard`, `yes_credit_card`, `indusind_credit_card`, `scapia_credit_card`, `au_credit_card`, `niyo_global_credit_card` |
        | `banking` | `account_statement` | `hdfc_bank_account`, `sbi_bank_account`, `icici_bank_account`, `axis_bank_account`, `kotak_bank_account`, `idfc_first_bank_account`, `yes_bank_account`, `au_bank_account`, `sbm_bank_account`, `federal_bank_account` |
        | `insurance` | `insurance_document` | `policybazaar`, `icici_lombard`, `hdfc_life` |
        | `tax` | `tax_notice` | `income_tax` |
        | `tax` | `tds_certificate` | `dividend_tds` |

        To read from an institution that isn't listed, pass its exact addresses
        in `senders` (up to 20 per request). A message from one of them is
        labelled with the known source it matches, if any; otherwise `source`,
        `category`, `document_type` and `institution` are `null`.

        **Sender verification:** `sender_verified` is the email provider's DMARC
        check of the sender's domain: `true` means it passed, `false` means it
        failed, and `null` means no result was available.

        **Paging:** at most 50 messages per call, newest first. When `truncated`
        is true, call again with `end_date` set to the oldest `message_date` you
        received, and skip `message_id`s you already have.

        `start_date` and `end_date` are inclusive calendar dates in IST
        (UTC+05:30). `message_date` is the date the email was received, also in IST.

        **Billing:** 0.2 credits per request (charged regardless of success or number of messages found). Attachment downloads are free.

        Args:
          categories: Read every source in these categories.

          document_types: Read every source of these document types.

          end_date: Last day to search (YYYY-MM-DD, inclusive, IST). Defaults to today in IST.

          include_body: Return each message's body as well.

          senders: Exact sender addresses to read, for institutions not in the table above. Domains and wildcards aren't accepted.

          sources: Read these sources.

          start_date: First day to search (YYYY-MM-DD, inclusive, IST). Defaults to 30 days before `end_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-inbox-token": x_inbox_token, **(extra_headers or {})}
        return await self._post(
            "/v4/inbox/read",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "document_types": document_types,
                    "end_date": end_date,
                    "include_body": include_body,
                    "senders": senders,
                    "sources": sources,
                    "start_date": start_date,
                },
                inbox_read_params.InboxReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboxReadResponse,
        )


class InboxResourceWithRawResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.check_connection_status = to_raw_response_wrapper(
            inbox.check_connection_status,
        )
        self.connect_email = to_raw_response_wrapper(
            inbox.connect_email,
        )
        self.disconnect_email = to_raw_response_wrapper(
            inbox.disconnect_email,
        )
        self.list_cas_files = to_raw_response_wrapper(
            inbox.list_cas_files,
        )
        self.read = to_raw_response_wrapper(
            inbox.read,
        )


class AsyncInboxResourceWithRawResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.check_connection_status = async_to_raw_response_wrapper(
            inbox.check_connection_status,
        )
        self.connect_email = async_to_raw_response_wrapper(
            inbox.connect_email,
        )
        self.disconnect_email = async_to_raw_response_wrapper(
            inbox.disconnect_email,
        )
        self.list_cas_files = async_to_raw_response_wrapper(
            inbox.list_cas_files,
        )
        self.read = async_to_raw_response_wrapper(
            inbox.read,
        )


class InboxResourceWithStreamingResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.check_connection_status = to_streamed_response_wrapper(
            inbox.check_connection_status,
        )
        self.connect_email = to_streamed_response_wrapper(
            inbox.connect_email,
        )
        self.disconnect_email = to_streamed_response_wrapper(
            inbox.disconnect_email,
        )
        self.list_cas_files = to_streamed_response_wrapper(
            inbox.list_cas_files,
        )
        self.read = to_streamed_response_wrapper(
            inbox.read,
        )


class AsyncInboxResourceWithStreamingResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.check_connection_status = async_to_streamed_response_wrapper(
            inbox.check_connection_status,
        )
        self.connect_email = async_to_streamed_response_wrapper(
            inbox.connect_email,
        )
        self.disconnect_email = async_to_streamed_response_wrapper(
            inbox.disconnect_email,
        )
        self.list_cas_files = async_to_streamed_response_wrapper(
            inbox.list_cas_files,
        )
        self.read = async_to_streamed_response_wrapper(
            inbox.read,
        )
