# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import inbound_email_list_params, inbound_email_create_params
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
from ..types.inbound_email_list_response import InboundEmailListResponse
from ..types.inbound_email_create_response import InboundEmailCreateResponse
from ..types.inbound_email_delete_response import InboundEmailDeleteResponse
from ..types.inbound_email_retrieve_response import InboundEmailRetrieveResponse

__all__ = ["InboundEmailResource", "AsyncInboundEmailResource"]


class InboundEmailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return InboundEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return InboundEmailResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        callback_url: str,
        alias: str | Omit = omit,
        allowed_sources: List[Literal["cdsl", "nsdl", "cams", "kfintech"]] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reference: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailCreateResponse:
        """
        Create a dedicated inbound email address for collecting CAS statements via email
        forwarding.

        **How it works:**

        1. Create an inbound email with your webhook URL
        2. Display the email address to your user (e.g., "Forward your CAS to
           ie_xxx@import.casparser.in")
        3. When an investor forwards a CAS email, we verify the sender and deliver to
           your webhook

        **Webhook Delivery:**

        - We POST to your `callback_url` with JSON body containing files (matching
          EmailCASFile schema)
        - Failed deliveries are retried automatically with exponential backoff

        **Inactivity:**

        - Inbound emails with no activity in 30 days are marked inactive
        - Active inbound emails remain operational indefinitely

        Args:
          callback_url: Webhook URL where we POST email notifications. Must be HTTPS in production (HTTP
              allowed for localhost during development).

          alias: Optional custom email prefix for user-friendly addresses.

              - Must be 3-32 characters
              - Alphanumeric + hyphens only
              - Must start and end with letter/number
              - Example: `john-portfolio@import.casparser.in`
              - If omitted, generates random ID like `ie_abc123xyz@import.casparser.in`

          allowed_sources: Filter emails by CAS provider. If omitted, accepts all providers.

              - `cdsl` → eCAS@cdslstatement.com
              - `nsdl` → NSDL-CAS@nsdl.co.in
              - `cams` → donotreply@camsonline.com
              - `kfintech` → samfS@kfintech.com

          metadata: Optional key-value pairs (max 10) to include in webhook payload. Useful for
              passing context like plan_type, campaign_id, etc.

          reference: Your internal identifier (e.g., user_id, account_id). Returned in webhook
              payload for correlation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/inbound-email",
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "alias": alias,
                    "allowed_sources": allowed_sources,
                    "metadata": metadata,
                    "reference": reference,
                },
                inbound_email_create_params.InboundEmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailCreateResponse,
        )

    def retrieve(
        self,
        inbound_email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailRetrieveResponse:
        """
        Retrieve details of a specific mailbox including statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_email_id:
            raise ValueError(f"Expected a non-empty value for `inbound_email_id` but received {inbound_email_id!r}")
        return self._get(
            f"/v4/inbound-email/{inbound_email_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "paused", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailListResponse:
        """List all mailboxes associated with your API key.

        Returns active and inactive
        mailboxes (deleted mailboxes are excluded).

        Args:
          limit: Maximum number of inbound emails to return

          offset: Pagination offset

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v4/inbound-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    inbound_email_list_params.InboundEmailListParams,
                ),
            ),
            cast_to=InboundEmailListResponse,
        )

    def delete(
        self,
        inbound_email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailDeleteResponse:
        """Permanently delete an inbound email address.

        It will stop accepting emails.

        **Note:** Deletion is immediate and cannot be undone. Any emails received after
        deletion will be rejected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_email_id:
            raise ValueError(f"Expected a non-empty value for `inbound_email_id` but received {inbound_email_id!r}")
        return self._delete(
            f"/v4/inbound-email/{inbound_email_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailDeleteResponse,
        )


class AsyncInboundEmailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncInboundEmailResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        callback_url: str,
        alias: str | Omit = omit,
        allowed_sources: List[Literal["cdsl", "nsdl", "cams", "kfintech"]] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        reference: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailCreateResponse:
        """
        Create a dedicated inbound email address for collecting CAS statements via email
        forwarding.

        **How it works:**

        1. Create an inbound email with your webhook URL
        2. Display the email address to your user (e.g., "Forward your CAS to
           ie_xxx@import.casparser.in")
        3. When an investor forwards a CAS email, we verify the sender and deliver to
           your webhook

        **Webhook Delivery:**

        - We POST to your `callback_url` with JSON body containing files (matching
          EmailCASFile schema)
        - Failed deliveries are retried automatically with exponential backoff

        **Inactivity:**

        - Inbound emails with no activity in 30 days are marked inactive
        - Active inbound emails remain operational indefinitely

        Args:
          callback_url: Webhook URL where we POST email notifications. Must be HTTPS in production (HTTP
              allowed for localhost during development).

          alias: Optional custom email prefix for user-friendly addresses.

              - Must be 3-32 characters
              - Alphanumeric + hyphens only
              - Must start and end with letter/number
              - Example: `john-portfolio@import.casparser.in`
              - If omitted, generates random ID like `ie_abc123xyz@import.casparser.in`

          allowed_sources: Filter emails by CAS provider. If omitted, accepts all providers.

              - `cdsl` → eCAS@cdslstatement.com
              - `nsdl` → NSDL-CAS@nsdl.co.in
              - `cams` → donotreply@camsonline.com
              - `kfintech` → samfS@kfintech.com

          metadata: Optional key-value pairs (max 10) to include in webhook payload. Useful for
              passing context like plan_type, campaign_id, etc.

          reference: Your internal identifier (e.g., user_id, account_id). Returned in webhook
              payload for correlation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/inbound-email",
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "alias": alias,
                    "allowed_sources": allowed_sources,
                    "metadata": metadata,
                    "reference": reference,
                },
                inbound_email_create_params.InboundEmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailCreateResponse,
        )

    async def retrieve(
        self,
        inbound_email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailRetrieveResponse:
        """
        Retrieve details of a specific mailbox including statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_email_id:
            raise ValueError(f"Expected a non-empty value for `inbound_email_id` but received {inbound_email_id!r}")
        return await self._get(
            f"/v4/inbound-email/{inbound_email_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "paused", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailListResponse:
        """List all mailboxes associated with your API key.

        Returns active and inactive
        mailboxes (deleted mailboxes are excluded).

        Args:
          limit: Maximum number of inbound emails to return

          offset: Pagination offset

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v4/inbound-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    inbound_email_list_params.InboundEmailListParams,
                ),
            ),
            cast_to=InboundEmailListResponse,
        )

    async def delete(
        self,
        inbound_email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundEmailDeleteResponse:
        """Permanently delete an inbound email address.

        It will stop accepting emails.

        **Note:** Deletion is immediate and cannot be undone. Any emails received after
        deletion will be rejected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_email_id:
            raise ValueError(f"Expected a non-empty value for `inbound_email_id` but received {inbound_email_id!r}")
        return await self._delete(
            f"/v4/inbound-email/{inbound_email_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundEmailDeleteResponse,
        )


class InboundEmailResourceWithRawResponse:
    def __init__(self, inbound_email: InboundEmailResource) -> None:
        self._inbound_email = inbound_email

        self.create = to_raw_response_wrapper(
            inbound_email.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inbound_email.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_email.list,
        )
        self.delete = to_raw_response_wrapper(
            inbound_email.delete,
        )


class AsyncInboundEmailResourceWithRawResponse:
    def __init__(self, inbound_email: AsyncInboundEmailResource) -> None:
        self._inbound_email = inbound_email

        self.create = async_to_raw_response_wrapper(
            inbound_email.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inbound_email.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_email.list,
        )
        self.delete = async_to_raw_response_wrapper(
            inbound_email.delete,
        )


class InboundEmailResourceWithStreamingResponse:
    def __init__(self, inbound_email: InboundEmailResource) -> None:
        self._inbound_email = inbound_email

        self.create = to_streamed_response_wrapper(
            inbound_email.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inbound_email.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_email.list,
        )
        self.delete = to_streamed_response_wrapper(
            inbound_email.delete,
        )


class AsyncInboundEmailResourceWithStreamingResponse:
    def __init__(self, inbound_email: AsyncInboundEmailResource) -> None:
        self._inbound_email = inbound_email

        self.create = async_to_streamed_response_wrapper(
            inbound_email.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inbound_email.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_email.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            inbound_email.delete,
        )
