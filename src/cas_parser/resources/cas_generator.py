# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import cas_generator_generate_cas_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.cas_generator_generate_cas_response import CasGeneratorGenerateCasResponse

__all__ = ["CasGeneratorResource", "AsyncCasGeneratorResource"]


class CasGeneratorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CasGeneratorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return CasGeneratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasGeneratorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return CasGeneratorResourceWithStreamingResponse(self)

    def generate_cas(
        self,
        *,
        email: str,
        from_date: str,
        password: str,
        to_date: str,
        cas_authority: Literal["kfintech", "cams", "cdsl", "nsdl"] | NotGiven = NOT_GIVEN,
        pan_no: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CasGeneratorGenerateCasResponse:
        """
        This endpoint generates CAS (Consolidated Account Statement) documents by
        submitting a mailback request to the specified CAS authority. Currently only
        supports KFintech, with plans to support CAMS, CDSL, and NSDL in the future.

        Args:
          email: Email address to receive the CAS document

          from_date: Start date for the CAS period (format YYYY-MM-DD)

          password: Password to protect the generated CAS PDF

          to_date: End date for the CAS period (format YYYY-MM-DD)

          cas_authority: CAS authority to generate the document from (currently only kfintech is
              supported)

          pan_no: PAN number (optional for some CAS authorities)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/generate",
            body=maybe_transform(
                {
                    "email": email,
                    "from_date": from_date,
                    "password": password,
                    "to_date": to_date,
                    "cas_authority": cas_authority,
                    "pan_no": pan_no,
                },
                cas_generator_generate_cas_params.CasGeneratorGenerateCasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CasGeneratorGenerateCasResponse,
        )


class AsyncCasGeneratorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCasGeneratorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCasGeneratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasGeneratorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncCasGeneratorResourceWithStreamingResponse(self)

    async def generate_cas(
        self,
        *,
        email: str,
        from_date: str,
        password: str,
        to_date: str,
        cas_authority: Literal["kfintech", "cams", "cdsl", "nsdl"] | NotGiven = NOT_GIVEN,
        pan_no: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CasGeneratorGenerateCasResponse:
        """
        This endpoint generates CAS (Consolidated Account Statement) documents by
        submitting a mailback request to the specified CAS authority. Currently only
        supports KFintech, with plans to support CAMS, CDSL, and NSDL in the future.

        Args:
          email: Email address to receive the CAS document

          from_date: Start date for the CAS period (format YYYY-MM-DD)

          password: Password to protect the generated CAS PDF

          to_date: End date for the CAS period (format YYYY-MM-DD)

          cas_authority: CAS authority to generate the document from (currently only kfintech is
              supported)

          pan_no: PAN number (optional for some CAS authorities)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/generate",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "from_date": from_date,
                    "password": password,
                    "to_date": to_date,
                    "cas_authority": cas_authority,
                    "pan_no": pan_no,
                },
                cas_generator_generate_cas_params.CasGeneratorGenerateCasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CasGeneratorGenerateCasResponse,
        )


class CasGeneratorResourceWithRawResponse:
    def __init__(self, cas_generator: CasGeneratorResource) -> None:
        self._cas_generator = cas_generator

        self.generate_cas = to_raw_response_wrapper(
            cas_generator.generate_cas,
        )


class AsyncCasGeneratorResourceWithRawResponse:
    def __init__(self, cas_generator: AsyncCasGeneratorResource) -> None:
        self._cas_generator = cas_generator

        self.generate_cas = async_to_raw_response_wrapper(
            cas_generator.generate_cas,
        )


class CasGeneratorResourceWithStreamingResponse:
    def __init__(self, cas_generator: CasGeneratorResource) -> None:
        self._cas_generator = cas_generator

        self.generate_cas = to_streamed_response_wrapper(
            cas_generator.generate_cas,
        )


class AsyncCasGeneratorResourceWithStreamingResponse:
    def __init__(self, cas_generator: AsyncCasGeneratorResource) -> None:
        self._cas_generator = cas_generator

        self.generate_cas = async_to_streamed_response_wrapper(
            cas_generator.generate_cas,
        )
