# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import access_token_create_params
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
from ..types.access_token_create_response import AccessTokenCreateResponse

__all__ = ["AccessTokenResource", "AsyncAccessTokenResource"]


class AccessTokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AccessTokenResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        expiry_minutes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """
        Generate a short-lived access token from your API key.

        **Use this endpoint from your backend** to create tokens that can be safely
        passed to frontend/SDK.

        Access tokens:

        - Are prefixed with `at_` for easy identification
        - Valid for up to 60 minutes
        - Can be used in place of API keys on all v4 endpoints
        - Cannot be used to generate other access tokens

        Args:
          expiry_minutes: Token validity in minutes (max 60)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/access-token",
            body=maybe_transform(
                {"expiry_minutes": expiry_minutes}, access_token_create_params.AccessTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AsyncAccessTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncAccessTokenResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        expiry_minutes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """
        Generate a short-lived access token from your API key.

        **Use this endpoint from your backend** to create tokens that can be safely
        passed to frontend/SDK.

        Access tokens:

        - Are prefixed with `at_` for easy identification
        - Valid for up to 60 minutes
        - Can be used in place of API keys on all v4 endpoints
        - Cannot be used to generate other access tokens

        Args:
          expiry_minutes: Token validity in minutes (max 60)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/access-token",
            body=await async_maybe_transform(
                {"expiry_minutes": expiry_minutes}, access_token_create_params.AccessTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_raw_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_raw_response_wrapper(
            access_token.create,
        )


class AccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_streamed_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_streamed_response_wrapper(
            access_token.create,
        )
