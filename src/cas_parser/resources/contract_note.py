# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import contract_note_parse_params
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
from ..types.contract_note_parse_response import ContractNoteParseResponse

__all__ = ["ContractNoteResource", "AsyncContractNoteResource"]


class ContractNoteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractNoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return ContractNoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractNoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
        """
        return ContractNoteResourceWithStreamingResponse(self)

    def parse(
        self,
        *,
        broker_type: Literal["zerodha", "groww", "upstox", "icici"] | Omit = omit,
        password: str | Omit = omit,
        pdf_file: str | Omit = omit,
        pdf_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractNoteParseResponse:
        """
        This endpoint parses Contract Note PDF files from various brokers including
        Zerodha, Groww, Upstox, ICICI Securities, and others.

        **What is a Contract Note?** A contract note is a legal document that provides
        details of all trades executed by an investor. It includes:

        - Trade details with timestamps, quantities, and prices
        - Brokerage and charges breakdown
        - Settlement information
        - Regulatory compliance details

        **Supported Brokers:**

        - Zerodha Broking Limited
        - Groww Invest Tech Private Limited
        - Upstox (RKSV Securities)
        - ICICI Securities Limited
        - Auto-detection for unknown brokers

        **Key Features:**

        - **Auto-detection**: Automatically identifies broker type from PDF content
        - **Comprehensive parsing**: Extracts equity transactions, derivatives
          transactions, detailed trades, and charges
        - **Flexible input**: Accepts both file upload and URL-based PDF input
        - **Password protection**: Supports password-protected PDFs

        The API returns structured data including contract note information, client
        details, transaction summaries, and detailed trade-by-trade breakdowns.

        Args:
          broker_type: Optional broker type override. If not provided, system will auto-detect.

          password: Password for the PDF file (usually PAN number for Zerodha)

          pdf_file: Base64 encoded contract note PDF file

          pdf_url: URL to the contract note PDF file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "broker_type": broker_type,
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
            "/v4/contract_note/parse",
            body=maybe_transform(body, contract_note_parse_params.ContractNoteParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractNoteParseResponse,
        )


class AsyncContractNoteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractNoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractNoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractNoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cas-parser-python#with_streaming_response
        """
        return AsyncContractNoteResourceWithStreamingResponse(self)

    async def parse(
        self,
        *,
        broker_type: Literal["zerodha", "groww", "upstox", "icici"] | Omit = omit,
        password: str | Omit = omit,
        pdf_file: str | Omit = omit,
        pdf_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractNoteParseResponse:
        """
        This endpoint parses Contract Note PDF files from various brokers including
        Zerodha, Groww, Upstox, ICICI Securities, and others.

        **What is a Contract Note?** A contract note is a legal document that provides
        details of all trades executed by an investor. It includes:

        - Trade details with timestamps, quantities, and prices
        - Brokerage and charges breakdown
        - Settlement information
        - Regulatory compliance details

        **Supported Brokers:**

        - Zerodha Broking Limited
        - Groww Invest Tech Private Limited
        - Upstox (RKSV Securities)
        - ICICI Securities Limited
        - Auto-detection for unknown brokers

        **Key Features:**

        - **Auto-detection**: Automatically identifies broker type from PDF content
        - **Comprehensive parsing**: Extracts equity transactions, derivatives
          transactions, detailed trades, and charges
        - **Flexible input**: Accepts both file upload and URL-based PDF input
        - **Password protection**: Supports password-protected PDFs

        The API returns structured data including contract note information, client
        details, transaction summaries, and detailed trade-by-trade breakdowns.

        Args:
          broker_type: Optional broker type override. If not provided, system will auto-detect.

          password: Password for the PDF file (usually PAN number for Zerodha)

          pdf_file: Base64 encoded contract note PDF file

          pdf_url: URL to the contract note PDF file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "broker_type": broker_type,
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
            "/v4/contract_note/parse",
            body=await async_maybe_transform(body, contract_note_parse_params.ContractNoteParseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractNoteParseResponse,
        )


class ContractNoteResourceWithRawResponse:
    def __init__(self, contract_note: ContractNoteResource) -> None:
        self._contract_note = contract_note

        self.parse = to_raw_response_wrapper(
            contract_note.parse,
        )


class AsyncContractNoteResourceWithRawResponse:
    def __init__(self, contract_note: AsyncContractNoteResource) -> None:
        self._contract_note = contract_note

        self.parse = async_to_raw_response_wrapper(
            contract_note.parse,
        )


class ContractNoteResourceWithStreamingResponse:
    def __init__(self, contract_note: ContractNoteResource) -> None:
        self._contract_note = contract_note

        self.parse = to_streamed_response_wrapper(
            contract_note.parse,
        )


class AsyncContractNoteResourceWithStreamingResponse:
    def __init__(self, contract_note: AsyncContractNoteResource) -> None:
        self._contract_note = contract_note

        self.parse = async_to_streamed_response_wrapper(
            contract_note.parse,
        )
