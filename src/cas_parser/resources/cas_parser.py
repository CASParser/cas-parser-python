# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import (
    cas_parser_cdsl_params,
    cas_parser_nsdl_params,
    cas_parser_smart_parse_params,
    cas_parser_cams_kfintech_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["CasParserResource", "AsyncCasParserResource"]


class CasParserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CasParserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return CasParserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasParserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return CasParserResourceWithStreamingResponse(self)

    def cams_kfintech(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CAMS/KFintech CAS (Consolidated Account
        Statement) PDF files and returns data in a unified format. Use this endpoint
        when you know the PDF is from CAMS or KFintech.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            body=maybe_transform(body, cas_parser_cams_kfintech_params.CasParserCamsKfintechParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    def cdsl(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CDSL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from CDSL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            body=maybe_transform(body, cas_parser_cdsl_params.CasParserCdslParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    def nsdl(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses NSDL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from NSDL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            "/v4/nsdl/parse",
            body=maybe_transform(body, cas_parser_nsdl_params.CasParserNsdlParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    def smart_parse(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint parses CAS (Consolidated Account Statement) PDF files from NSDL,
        CDSL, or CAMS/KFintech and returns data in a unified format. It auto-detects the
        CAS type and transforms the data into a consistent structure regardless of the
        source.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            "/v4/smart/parse",
            body=maybe_transform(body, cas_parser_smart_parse_params.CasParserSmartParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class AsyncCasParserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCasParserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCasParserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasParserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncCasParserResourceWithStreamingResponse(self)

    async def cams_kfintech(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CAMS/KFintech CAS (Consolidated Account
        Statement) PDF files and returns data in a unified format. Use this endpoint
        when you know the PDF is from CAMS or KFintech.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            body=await async_maybe_transform(body, cas_parser_cams_kfintech_params.CasParserCamsKfintechParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    async def cdsl(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses CDSL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from CDSL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            body=await async_maybe_transform(body, cas_parser_cdsl_params.CasParserCdslParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    async def nsdl(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint specifically parses NSDL CAS (Consolidated Account Statement) PDF
        files and returns data in a unified format. Use this endpoint when you know the
        PDF is from NSDL.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            "/v4/nsdl/parse",
            body=await async_maybe_transform(body, cas_parser_nsdl_params.CasParserNsdlParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )

    async def smart_parse(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        pdf_file: str | NotGiven = NOT_GIVEN,
        pdf_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnifiedResponse:
        """
        This endpoint parses CAS (Consolidated Account Statement) PDF files from NSDL,
        CDSL, or CAMS/KFintech and returns data in a unified format. It auto-detects the
        CAS type and transforms the data into a consistent structure regardless of the
        source.

        Args:
          password: Password for the PDF file (if required)

          pdf_file: Base64 encoded CAS PDF file

          pdf_url: URL to the CAS PDF file

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
            "/v4/smart/parse",
            body=await async_maybe_transform(body, cas_parser_smart_parse_params.CasParserSmartParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnifiedResponse,
        )


class CasParserResourceWithRawResponse:
    def __init__(self, cas_parser: CasParserResource) -> None:
        self._cas_parser = cas_parser

        self.cams_kfintech = to_raw_response_wrapper(
            cas_parser.cams_kfintech,
        )
        self.cdsl = to_raw_response_wrapper(
            cas_parser.cdsl,
        )
        self.nsdl = to_raw_response_wrapper(
            cas_parser.nsdl,
        )
        self.smart_parse = to_raw_response_wrapper(
            cas_parser.smart_parse,
        )


class AsyncCasParserResourceWithRawResponse:
    def __init__(self, cas_parser: AsyncCasParserResource) -> None:
        self._cas_parser = cas_parser

        self.cams_kfintech = async_to_raw_response_wrapper(
            cas_parser.cams_kfintech,
        )
        self.cdsl = async_to_raw_response_wrapper(
            cas_parser.cdsl,
        )
        self.nsdl = async_to_raw_response_wrapper(
            cas_parser.nsdl,
        )
        self.smart_parse = async_to_raw_response_wrapper(
            cas_parser.smart_parse,
        )


class CasParserResourceWithStreamingResponse:
    def __init__(self, cas_parser: CasParserResource) -> None:
        self._cas_parser = cas_parser

        self.cams_kfintech = to_streamed_response_wrapper(
            cas_parser.cams_kfintech,
        )
        self.cdsl = to_streamed_response_wrapper(
            cas_parser.cdsl,
        )
        self.nsdl = to_streamed_response_wrapper(
            cas_parser.nsdl,
        )
        self.smart_parse = to_streamed_response_wrapper(
            cas_parser.smart_parse,
        )


class AsyncCasParserResourceWithStreamingResponse:
    def __init__(self, cas_parser: AsyncCasParserResource) -> None:
        self._cas_parser = cas_parser

        self.cams_kfintech = async_to_streamed_response_wrapper(
            cas_parser.cams_kfintech,
        )
        self.cdsl = async_to_streamed_response_wrapper(
            cas_parser.cdsl,
        )
        self.nsdl = async_to_streamed_response_wrapper(
            cas_parser.nsdl,
        )
        self.smart_parse = async_to_streamed_response_wrapper(
            cas_parser.smart_parse,
        )
