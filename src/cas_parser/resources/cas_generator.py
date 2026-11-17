# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import cas_generator_generate_cas_params
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
from ..types.cas_generator_generate_cas_response import CasGeneratorGenerateCasResponse

__all__ = ["CasGeneratorResource", "AsyncCasGeneratorResource"]


class CasGeneratorResource(SyncAPIResource):
    """Endpoints for generating new CAS documents via email mailback (KFintech and CAMS)."""

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
        cas_authority: Literal["kfintech", "cams"] | Omit = omit,
        pan_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CasGeneratorGenerateCasResponse:
        """
        Generate a mutual fund CAS statement via email mailback. The CAS PDF will be sent to the investor's email.

        KFintech and CAMS have a mutual partnership for data sharing and consolidation,
        so this endpoint retrieves mutual fund data from **both RTAs**, covering all
        mutual funds in India.

        This is an async operation - the investor receives the CAS via email within a few minutes.

        By default, a **Detailed CAS** is generated, which includes the complete transaction history.
        The parsing layer supports all statement types (Detailed, Summary, etc.), but generation
        always requests the Detailed variant for maximum data coverage.

        `cas_authority` picks which RTA sends the email. The portfolio data is the same either
        way — only the PDF password policy differs. With `cams`, a PAN is a valid password.

        Args:
          cas_authority: RTA that sends the mailback. Affects only the password policy, not the portfolio data returned.

          email: Email address to receive the CAS document

          from_date: Start date (YYYY-MM-DD)

          pan_no: PAN number (optional)

          password: Password protecting the emailed PDF. Must satisfy the chosen authority's policy — `cams` requires 6-20 characters with at least two digits, so a PAN works.

          to_date: End date (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/generate",
            body=maybe_transform(
                {
                    "cas_authority": cas_authority,
                    "email": email,
                    "from_date": from_date,
                    "pan_no": pan_no,
                    "password": password,
                    "to_date": to_date,
                },
                cas_generator_generate_cas_params.CasGeneratorGenerateCasParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CasGeneratorGenerateCasResponse,
        )


class AsyncCasGeneratorResource(AsyncAPIResource):
    """Endpoints for generating new CAS documents via email mailback (KFintech and CAMS)."""

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
        cas_authority: Literal["kfintech", "cams"] | Omit = omit,
        pan_no: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CasGeneratorGenerateCasResponse:
        """
        Generate a mutual fund CAS statement via email mailback. The CAS PDF will be sent to the investor's email.

        KFintech and CAMS have a mutual partnership for data sharing and consolidation,
        so this endpoint retrieves mutual fund data from **both RTAs**, covering all
        mutual funds in India.

        This is an async operation - the investor receives the CAS via email within a few minutes.

        By default, a **Detailed CAS** is generated, which includes the complete transaction history.
        The parsing layer supports all statement types (Detailed, Summary, etc.), but generation
        always requests the Detailed variant for maximum data coverage.

        `cas_authority` picks which RTA sends the email. The portfolio data is the same either
        way — only the PDF password policy differs. With `cams`, a PAN is a valid password.

        Args:
          cas_authority: RTA that sends the mailback. Affects only the password policy, not the portfolio data returned.

          email: Email address to receive the CAS document

          from_date: Start date (YYYY-MM-DD)

          pan_no: PAN number (optional)

          password: Password protecting the emailed PDF. Must satisfy the chosen authority's policy — `cams` requires 6-20 characters with at least two digits, so a PAN works.

          to_date: End date (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/generate",
            body=await async_maybe_transform(
                {
                    "cas_authority": cas_authority,
                    "email": email,
                    "from_date": from_date,
                    "pan_no": pan_no,
                    "password": password,
                    "to_date": to_date,
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
