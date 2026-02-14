# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import kfintech_generate_cas_params
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
from ..types.kfintech_generate_cas_response import KfintechGenerateCasResponse

__all__ = ["KfintechResource", "AsyncKfintechResource"]


class KfintechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KfintechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return KfintechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KfintechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return KfintechResourceWithStreamingResponse(self)

    def generate_cas(
        self,
        *,
        email: str,
        from_date: str,
        password: str,
        to_date: str,
        pan_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KfintechGenerateCasResponse:
        """Generate CAS via KFintech mailback.

        The CAS PDF will be sent to the investor's
        email.

        This is an async operation - the investor receives the CAS via email within a
        few minutes. For instant CAS retrieval, use CDSL Fetch (`/v4/cdsl/fetch`).

        Args:
          email: Email address to receive the CAS document

          from_date: Start date (YYYY-MM-DD)

          password: Password for the PDF

          to_date: End date (YYYY-MM-DD)

          pan_no: PAN number (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/kfintech/generate",
            body=maybe_transform(
                {
                    "email": email,
                    "from_date": from_date,
                    "password": password,
                    "to_date": to_date,
                    "pan_no": pan_no,
                },
                kfintech_generate_cas_params.KfintechGenerateCasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KfintechGenerateCasResponse,
        )


class AsyncKfintechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKfintechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKfintechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKfintechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncKfintechResourceWithStreamingResponse(self)

    async def generate_cas(
        self,
        *,
        email: str,
        from_date: str,
        password: str,
        to_date: str,
        pan_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KfintechGenerateCasResponse:
        """Generate CAS via KFintech mailback.

        The CAS PDF will be sent to the investor's
        email.

        This is an async operation - the investor receives the CAS via email within a
        few minutes. For instant CAS retrieval, use CDSL Fetch (`/v4/cdsl/fetch`).

        Args:
          email: Email address to receive the CAS document

          from_date: Start date (YYYY-MM-DD)

          password: Password for the PDF

          to_date: End date (YYYY-MM-DD)

          pan_no: PAN number (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/kfintech/generate",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "from_date": from_date,
                    "password": password,
                    "to_date": to_date,
                    "pan_no": pan_no,
                },
                kfintech_generate_cas_params.KfintechGenerateCasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KfintechGenerateCasResponse,
        )


class KfintechResourceWithRawResponse:
    def __init__(self, kfintech: KfintechResource) -> None:
        self._kfintech = kfintech

        self.generate_cas = to_raw_response_wrapper(
            kfintech.generate_cas,
        )


class AsyncKfintechResourceWithRawResponse:
    def __init__(self, kfintech: AsyncKfintechResource) -> None:
        self._kfintech = kfintech

        self.generate_cas = async_to_raw_response_wrapper(
            kfintech.generate_cas,
        )


class KfintechResourceWithStreamingResponse:
    def __init__(self, kfintech: KfintechResource) -> None:
        self._kfintech = kfintech

        self.generate_cas = to_streamed_response_wrapper(
            kfintech.generate_cas,
        )


class AsyncKfintechResourceWithStreamingResponse:
    def __init__(self, kfintech: AsyncKfintechResource) -> None:
        self._kfintech = kfintech

        self.generate_cas = async_to_streamed_response_wrapper(
            kfintech.generate_cas,
        )
