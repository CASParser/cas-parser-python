# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import verification_verify_mfd_params, verification_verify_sebi_params
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
from ..types.verification_verify_mfd_response import VerificationVerifyMfdResponse
from ..types.verification_verify_sebi_response import VerificationVerifySebiResponse

__all__ = ["VerificationResource", "AsyncVerificationResource"]


class VerificationResource(SyncAPIResource):
    """
    Verify the regulatory registration of a financial intermediary — a yes/no
    check rather than a directory search.

    - **`/v1/verify/sebi`** — any SEBI-registered intermediary (Investment
      Adviser, Research Analyst, Portfolio Manager, Stock Broker, Mutual Fund,
      AIF, and more). Send a `registration_number` and the category is
      auto-detected from its sequence; or send a `name` with an explicit `type`.
    - **`/v1/verify/mfd`** — AMFI mutual-fund distributors by ARN, including a
      screen against AMFI's suspended / terminated / terminated-EUIN lists.

    A "not found" result is a successful verification (HTTP 200,
    `verified: false`) and is billed. Upstream failures surface as 5xx and are
    not billed.

    **Credits:** 0.25 per successful verification.
    """

    @cached_property
    def with_raw_response(self) -> VerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return VerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return VerificationResourceWithStreamingResponse(self)

    def verify_mfd(
        self,
        *,
        arn: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationVerifyMfdResponse:
        """
        Verify a mutual-fund distributor by ARN. The ARN (and its EUIN) is
        screened against AMFI's suspended, terminated, and terminated-EUIN
        lists; a hit sets `registration_status` to `SUSPENDED`/`TERMINATED`,
        `negative_list_hit` to `true`, and `verified` to `false`.

        **Credits:** 0.25 per successful verification.

        Args:
          arn: AMFI Registration Number. Digits only; an `ARN-` prefix is tolerated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/verify/mfd",
            body=maybe_transform(
                {
                    "arn": arn,
                },
                verification_verify_mfd_params.VerificationVerifyMfdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationVerifyMfdResponse,
        )

    def verify_sebi(
        self,
        *,
        name: str | Omit = omit,
        registration_number: str | Omit = omit,
        type: Literal[
            "investment-adviser",
            "research-analyst",
            "portfolio-manager",
            "stock-broker",
            "merchant-banker",
            "registrar-transfer-agent",
            "mutual-fund",
            "alternative-investment-fund",
            "credit-rating-agency",
            "custodian",
            "debenture-trustee",
            "venture-capital-fund",
            "foreign-venture-capital-investor",
            "foreign-portfolio-investor",
            "kyc-registration-agency",
            "infrastructure-investment-trust",
            "real-estate-investment-trust",
            "esg-rating-provider",
            "vault-manager",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationVerifySebiResponse:
        """
        Verify any SEBI-registered intermediary. Provide a `registration_number`
        and the category is auto-detected from its sequence (e.g. `INA…` →
        Investment Adviser, `INP…` → Portfolio Manager, `INZ…` → Stock Broker).
        Alternatively, provide a `name` together with a `type` slug. `type` can
        also override detection, and is required for fund/FPI registration
        numbers that do not encode a category.

        `verified` is `true` only when a current registration is found and its
        status is `ACTIVE`. A missing registration returns HTTP 200 with
        `verified: false` and `registration_status: NOT_FOUND`.

        **Credits:** 0.25 per successful verification.

        Args:
          name: Entity/trade name to search by. Used only when `registration_number` is absent, and then `type` is required.

          registration_number: SEBI registration number. When provided, the category is auto-detected from its sequence (INA…→investment-adviser, INH…→research-analyst, INP…→portfolio-manager, INM…→merchant-banker, INR…→registrar-transfer-agent, INZ…→stock-broker). This is the authoritative input — any `name` sent alongside it is ignored.

          type: Category slug. Overrides auto-detection; required for a name search and for fund/FPI registration numbers that don't encode a category. Short aliases are also accepted (ria, ra, pms, broker, rta, mf, aif, cra, vcf, fvci, fpi, kra, invit, reit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/verify/sebi",
            body=maybe_transform(
                {
                    "name": name,
                    "registration_number": registration_number,
                    "type": type,
                },
                verification_verify_sebi_params.VerificationVerifySebiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationVerifySebiResponse,
        )


class AsyncVerificationResource(AsyncAPIResource):
    """
    Verify the regulatory registration of a financial intermediary — a yes/no
    check rather than a directory search.

    - **`/v1/verify/sebi`** — any SEBI-registered intermediary (Investment
      Adviser, Research Analyst, Portfolio Manager, Stock Broker, Mutual Fund,
      AIF, and more). Send a `registration_number` and the category is
      auto-detected from its sequence; or send a `name` with an explicit `type`.
    - **`/v1/verify/mfd`** — AMFI mutual-fund distributors by ARN, including a
      screen against AMFI's suspended / terminated / terminated-EUIN lists.

    A "not found" result is a successful verification (HTTP 200,
    `verified: false`) and is billed. Upstream failures surface as 5xx and are
    not billed.

    **Credits:** 0.25 per successful verification.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncVerificationResourceWithStreamingResponse(self)

    async def verify_mfd(
        self,
        *,
        arn: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationVerifyMfdResponse:
        """
        Verify a mutual-fund distributor by ARN. The ARN (and its EUIN) is
        screened against AMFI's suspended, terminated, and terminated-EUIN
        lists; a hit sets `registration_status` to `SUSPENDED`/`TERMINATED`,
        `negative_list_hit` to `true`, and `verified` to `false`.

        **Credits:** 0.25 per successful verification.

        Args:
          arn: AMFI Registration Number. Digits only; an `ARN-` prefix is tolerated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/verify/mfd",
            body=await async_maybe_transform(
                {
                    "arn": arn,
                },
                verification_verify_mfd_params.VerificationVerifyMfdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationVerifyMfdResponse,
        )

    async def verify_sebi(
        self,
        *,
        name: str | Omit = omit,
        registration_number: str | Omit = omit,
        type: Literal[
            "investment-adviser",
            "research-analyst",
            "portfolio-manager",
            "stock-broker",
            "merchant-banker",
            "registrar-transfer-agent",
            "mutual-fund",
            "alternative-investment-fund",
            "credit-rating-agency",
            "custodian",
            "debenture-trustee",
            "venture-capital-fund",
            "foreign-venture-capital-investor",
            "foreign-portfolio-investor",
            "kyc-registration-agency",
            "infrastructure-investment-trust",
            "real-estate-investment-trust",
            "esg-rating-provider",
            "vault-manager",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationVerifySebiResponse:
        """
        Verify any SEBI-registered intermediary. Provide a `registration_number`
        and the category is auto-detected from its sequence (e.g. `INA…` →
        Investment Adviser, `INP…` → Portfolio Manager, `INZ…` → Stock Broker).
        Alternatively, provide a `name` together with a `type` slug. `type` can
        also override detection, and is required for fund/FPI registration
        numbers that do not encode a category.

        `verified` is `true` only when a current registration is found and its
        status is `ACTIVE`. A missing registration returns HTTP 200 with
        `verified: false` and `registration_status: NOT_FOUND`.

        **Credits:** 0.25 per successful verification.

        Args:
          name: Entity/trade name to search by. Used only when `registration_number` is absent, and then `type` is required.

          registration_number: SEBI registration number. When provided, the category is auto-detected from its sequence (INA…→investment-adviser, INH…→research-analyst, INP…→portfolio-manager, INM…→merchant-banker, INR…→registrar-transfer-agent, INZ…→stock-broker). This is the authoritative input — any `name` sent alongside it is ignored.

          type: Category slug. Overrides auto-detection; required for a name search and for fund/FPI registration numbers that don't encode a category. Short aliases are also accepted (ria, ra, pms, broker, rta, mf, aif, cra, vcf, fvci, fpi, kra, invit, reit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/verify/sebi",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "registration_number": registration_number,
                    "type": type,
                },
                verification_verify_sebi_params.VerificationVerifySebiParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationVerifySebiResponse,
        )


class VerificationResourceWithRawResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.verify_mfd = to_raw_response_wrapper(
            verification.verify_mfd,
        )
        self.verify_sebi = to_raw_response_wrapper(
            verification.verify_sebi,
        )


class AsyncVerificationResourceWithRawResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.verify_mfd = async_to_raw_response_wrapper(
            verification.verify_mfd,
        )
        self.verify_sebi = async_to_raw_response_wrapper(
            verification.verify_sebi,
        )


class VerificationResourceWithStreamingResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.verify_mfd = to_streamed_response_wrapper(
            verification.verify_mfd,
        )
        self.verify_sebi = to_streamed_response_wrapper(
            verification.verify_sebi,
        )


class AsyncVerificationResourceWithStreamingResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.verify_mfd = async_to_streamed_response_wrapper(
            verification.verify_mfd,
        )
        self.verify_sebi = async_to_streamed_response_wrapper(
            verification.verify_sebi,
        )
