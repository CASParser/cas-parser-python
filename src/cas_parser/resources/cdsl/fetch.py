# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdsl import fetch_verify_otp_params, fetch_request_otp_params
from ..._base_client import make_request_options
from ...types.cdsl.fetch_verify_otp_response import FetchVerifyOtpResponse
from ...types.cdsl.fetch_request_otp_response import FetchRequestOtpResponse

__all__ = ["FetchResource", "AsyncFetchResource"]


class FetchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FetchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return FetchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FetchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return FetchResourceWithStreamingResponse(self)

    def request_otp(
        self,
        *,
        bo_id: str,
        dob: str,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchRequestOtpResponse:
        """**Step 1 of 2**: Request OTP for CDSL CAS fetch.

        This endpoint:

        1.

        Solves reCAPTCHA automatically (~15-20 seconds)
        2. Submits login credentials to CDSL portal
        3. Triggers OTP to user's registered mobile number

        After user receives OTP, call `/v4/cdsl/fetch/{session_id}/verify` to complete.

        Args:
          bo_id: CDSL BO ID (16 digits)

          dob: Date of birth (YYYY-MM-DD)

          pan: PAN number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/cdsl/fetch",
            body=maybe_transform(
                {
                    "bo_id": bo_id,
                    "dob": dob,
                    "pan": pan,
                },
                fetch_request_otp_params.FetchRequestOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchRequestOtpResponse,
        )

    def verify_otp(
        self,
        session_id: str,
        *,
        otp: str,
        num_periods: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchVerifyOtpResponse:
        """
        **Step 2 of 2**: Verify OTP and retrieve CDSL CAS files.

        After successful verification, CAS PDFs are fetched from CDSL portal, uploaded
        to cloud storage, and returned as direct download URLs.

        Args:
          otp: OTP received on mobile

          num_periods: Number of monthly statements to fetch (default 6)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v4/cdsl/fetch/{session_id}/verify",
            body=maybe_transform(
                {
                    "otp": otp,
                    "num_periods": num_periods,
                },
                fetch_verify_otp_params.FetchVerifyOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchVerifyOtpResponse,
        )


class AsyncFetchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFetchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFetchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFetchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncFetchResourceWithStreamingResponse(self)

    async def request_otp(
        self,
        *,
        bo_id: str,
        dob: str,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchRequestOtpResponse:
        """**Step 1 of 2**: Request OTP for CDSL CAS fetch.

        This endpoint:

        1.

        Solves reCAPTCHA automatically (~15-20 seconds)
        2. Submits login credentials to CDSL portal
        3. Triggers OTP to user's registered mobile number

        After user receives OTP, call `/v4/cdsl/fetch/{session_id}/verify` to complete.

        Args:
          bo_id: CDSL BO ID (16 digits)

          dob: Date of birth (YYYY-MM-DD)

          pan: PAN number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/cdsl/fetch",
            body=await async_maybe_transform(
                {
                    "bo_id": bo_id,
                    "dob": dob,
                    "pan": pan,
                },
                fetch_request_otp_params.FetchRequestOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchRequestOtpResponse,
        )

    async def verify_otp(
        self,
        session_id: str,
        *,
        otp: str,
        num_periods: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchVerifyOtpResponse:
        """
        **Step 2 of 2**: Verify OTP and retrieve CDSL CAS files.

        After successful verification, CAS PDFs are fetched from CDSL portal, uploaded
        to cloud storage, and returned as direct download URLs.

        Args:
          otp: OTP received on mobile

          num_periods: Number of monthly statements to fetch (default 6)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v4/cdsl/fetch/{session_id}/verify",
            body=await async_maybe_transform(
                {
                    "otp": otp,
                    "num_periods": num_periods,
                },
                fetch_verify_otp_params.FetchVerifyOtpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchVerifyOtpResponse,
        )


class FetchResourceWithRawResponse:
    def __init__(self, fetch: FetchResource) -> None:
        self._fetch = fetch

        self.request_otp = to_raw_response_wrapper(
            fetch.request_otp,
        )
        self.verify_otp = to_raw_response_wrapper(
            fetch.verify_otp,
        )


class AsyncFetchResourceWithRawResponse:
    def __init__(self, fetch: AsyncFetchResource) -> None:
        self._fetch = fetch

        self.request_otp = async_to_raw_response_wrapper(
            fetch.request_otp,
        )
        self.verify_otp = async_to_raw_response_wrapper(
            fetch.verify_otp,
        )


class FetchResourceWithStreamingResponse:
    def __init__(self, fetch: FetchResource) -> None:
        self._fetch = fetch

        self.request_otp = to_streamed_response_wrapper(
            fetch.request_otp,
        )
        self.verify_otp = to_streamed_response_wrapper(
            fetch.verify_otp,
        )


class AsyncFetchResourceWithStreamingResponse:
    def __init__(self, fetch: AsyncFetchResource) -> None:
        self._fetch = fetch

        self.request_otp = async_to_streamed_response_wrapper(
            fetch.request_otp,
        )
        self.verify_otp = async_to_streamed_response_wrapper(
            fetch.verify_otp,
        )
