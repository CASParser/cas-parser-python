# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import cams_kfintech_parse_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.unified_response import UnifiedResponse

__all__ = ["CamsKfintechResource", "AsyncCamsKfintechResource"]


class CamsKfintechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CamsKfintechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return CamsKfintechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CamsKfintechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return CamsKfintechResourceWithStreamingResponse(self)

    def parse(
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
        This endpoint specifically parses CAMS/KFintech CAS (Consolidated Account
        Statement) PDF files and returns data in a unified format. Use this endpoint
        when you know the PDF is from CAMS or KFintech.

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
            "/v4/cams_kfintech/parse",
            body=maybe_transform(body, cams_kfintech_parse_params.CamsKfintechParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class AsyncCamsKfintechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCamsKfintechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCamsKfintechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCamsKfintechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncCamsKfintechResourceWithStreamingResponse(self)

    async def parse(
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
        This endpoint specifically parses CAMS/KFintech CAS (Consolidated Account
        Statement) PDF files and returns data in a unified format. Use this endpoint
        when you know the PDF is from CAMS or KFintech.

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
            "/v4/cams_kfintech/parse",
            body=await async_maybe_transform(body, cams_kfintech_parse_params.CamsKfintechParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class CamsKfintechResourceWithRawResponse:
    def __init__(self, cams_kfintech: CamsKfintechResource) -> None:
        self._cams_kfintech = cams_kfintech

        self.parse = to_raw_response_wrapper(
            cams_kfintech.parse,
        )


class AsyncCamsKfintechResourceWithRawResponse:
    def __init__(self, cams_kfintech: AsyncCamsKfintechResource) -> None:
        self._cams_kfintech = cams_kfintech

        self.parse = async_to_raw_response_wrapper(
            cams_kfintech.parse,
        )


class CamsKfintechResourceWithStreamingResponse:
    def __init__(self, cams_kfintech: CamsKfintechResource) -> None:
        self._cams_kfintech = cams_kfintech

        self.parse = to_streamed_response_wrapper(
            cams_kfintech.parse,
        )


class AsyncCamsKfintechResourceWithStreamingResponse:
    def __init__(self, cams_kfintech: AsyncCamsKfintechResource) -> None:
        self._cams_kfintech = cams_kfintech

        self.parse = async_to_streamed_response_wrapper(
            cams_kfintech.parse,
        )
