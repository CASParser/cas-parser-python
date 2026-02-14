# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from .fetch import (
    FetchResource,
    AsyncFetchResource,
    FetchResourceWithRawResponse,
    AsyncFetchResourceWithRawResponse,
    FetchResourceWithStreamingResponse,
    AsyncFetchResourceWithStreamingResponse,
)
from ...types import cdsl_parse_pdf_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.unified_response import UnifiedResponse

__all__ = ["CdslResource", "AsyncCdslResource"]


class CdslResource(SyncAPIResource):
    @cached_property
    def fetch(self) -> FetchResource:
        return FetchResource(self._client)

    @cached_property
    def with_raw_response(self) -> CdslResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return CdslResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CdslResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
        """
        return CdslResourceWithStreamingResponse(self)

    def parse_pdf(
        self,
        *,
        password: str | Omit = omit,
        pdf_file: str | Omit = omit,
        pdf_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CDSL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from CDSL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file (required if pdf_url not provided)

          pdf_url: URL to the CAS PDF file (required if pdf_file not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "password": password,
                "pdf_file": pdf_file,
                "pdf_url": pdf_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["pdf_file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v4/cdsl/parse",
            body=maybe_transform(body, cdsl_parse_pdf_params.CdslParsePdfParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class AsyncCdslResource(AsyncAPIResource):
    @cached_property
    def fetch(self) -> AsyncFetchResource:
        return AsyncFetchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCdslResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCdslResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCdslResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
        """
        return AsyncCdslResourceWithStreamingResponse(self)

    async def parse_pdf(
        self,
        *,
        password: str | Omit = omit,
        pdf_file: str | Omit = omit,
        pdf_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CDSL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from CDSL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file (required if pdf_url not provided)

          pdf_url: URL to the CAS PDF file (required if pdf_file not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "password": password,
                "pdf_file": pdf_file,
                "pdf_url": pdf_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["pdf_file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v4/cdsl/parse",
            body=await async_maybe_transform(body, cdsl_parse_pdf_params.CdslParsePdfParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class CdslResourceWithRawResponse:
    def __init__(self, cdsl: CdslResource) -> None:
        self._cdsl = cdsl

        self.parse_pdf = to_raw_response_wrapper(
            cdsl.parse_pdf,
        )

    @cached_property
    def fetch(self) -> FetchResourceWithRawResponse:
        return FetchResourceWithRawResponse(self._cdsl.fetch)


class AsyncCdslResourceWithRawResponse:
    def __init__(self, cdsl: AsyncCdslResource) -> None:
        self._cdsl = cdsl

        self.parse_pdf = async_to_raw_response_wrapper(
            cdsl.parse_pdf,
        )

    @cached_property
    def fetch(self) -> AsyncFetchResourceWithRawResponse:
        return AsyncFetchResourceWithRawResponse(self._cdsl.fetch)


class CdslResourceWithStreamingResponse:
    def __init__(self, cdsl: CdslResource) -> None:
        self._cdsl = cdsl

        self.parse_pdf = to_streamed_response_wrapper(
            cdsl.parse_pdf,
        )

    @cached_property
    def fetch(self) -> FetchResourceWithStreamingResponse:
        return FetchResourceWithStreamingResponse(self._cdsl.fetch)


class AsyncCdslResourceWithStreamingResponse:
    def __init__(self, cdsl: AsyncCdslResource) -> None:
        self._cdsl = cdsl

        self.parse_pdf = async_to_streamed_response_wrapper(
            cdsl.parse_pdf,
        )

    @cached_property
    def fetch(self) -> AsyncFetchResourceWithStreamingResponse:
        return AsyncFetchResourceWithStreamingResponse(self._cdsl.fetch)
