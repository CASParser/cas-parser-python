# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import inbox_connect_email_params, inbox_list_cas_files_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.inbox_connect_email_response import InboxConnectEmailResponse
from ..types.inbox_list_cas_files_response import InboxListCasFilesResponse
from ..types.inbox_disconnect_email_response import InboxDisconnectEmailResponse
from ..types.inbox_check_connection_status_response import InboxCheckConnectionStatusResponse

__all__ = ["InboxResource", "AsyncInboxResource"]


class InboxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return InboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
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
        calls.

        Args:
          redirect_uri: Your callback URL to receive the inbox_token (must be http or https)

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


class AsyncInboxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
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
        calls.

        Args:
          redirect_uri: Your callback URL to receive the inbox_token (must be http or https)

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
