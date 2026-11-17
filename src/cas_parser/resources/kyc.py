# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    kyc_check_pan_status_params,
    kyc_get_digilocker_result_params,
    kyc_start_digilocker_session_params,
    kyc_lookup_digilocker_account_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.kyc_check_pan_status_response import KycCheckPanStatusResponse
from ..types.kyc_get_digilocker_result_response import KycGetDigilockerResultResponse
from ..types.kyc_start_digilocker_session_response import KycStartDigilockerSessionResponse
from ..types.kyc_lookup_digilocker_account_response import KycLookupDigilockerAccountResponse

__all__ = ["KycResource", "AsyncKycResource"]


class KycResource(SyncAPIResource):
    """
    Endpoints for verifying KYC (Know Your Customer) status of Indian investors.

    **Data source:** CVL KRA public inquiry portal (cvlkra.com), which aggregates
    records from all five SEBI-registered KRAs: CVL, NDML, CAMS, Karvy, and KFin.

    **Status normalization:** Raw CVL portal strings are normalized into clean enums.
    See the `kyc_status` property on `KycPanStatusResponse` for the full list.

    **Credits:** 0.25 per successful lookup. Failed lookups are not billed.
    """

    @cached_property
    def with_raw_response(self) -> KycResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return KycResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KycResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return KycResourceWithStreamingResponse(self)

    def lookup_digilocker_account(
        self,
        *,
        aadhaar_number: str | Omit = omit,
        mobile: str | Omit = omit,
        reference_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycLookupDigilockerAccountResponse:
        """
        Check whether a mobile number or Aadhaar number is already registered
        with DigiLocker. This is a pre-consent lookup: it helps you decide
        whether to start the user in `signin` or `signup` flow.

        Provide exactly one of `aadhaar_number` or `mobile`.

        **Credits:** Free.

        Args:
          aadhaar_number: 12-digit Aadhaar number.

          mobile: 10-digit Indian mobile number.

          reference_id: Optional caller-side request identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/kyc/digilocker/account-lookup",
            body=maybe_transform(
                {
                    "aadhaar_number": aadhaar_number,
                    "mobile": mobile,
                    "reference_id": reference_id,
                },
                kyc_lookup_digilocker_account_params.KycLookupDigilockerAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycLookupDigilockerAccountResponse,
        )

    def start_digilocker_session(
        self,
        *,
        consent: bool,
        consent_purpose: str,
        redirect_url: str,
        documents: List[Literal["aadhaar", "pan", "driving_licence", "email", "mobile"]] | Omit = omit,
        prefill_mobile: str | Omit = omit,
        state: str | Omit = omit,
        user_flow: Literal["signin", "signup"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycStartDigilockerSessionResponse:
        """
        Start a DigiLocker session to fetch the investor's government-issued
        documents (Aadhaar, PAN, etc.) with their consent.

        **How it works:**
        1. Call this endpoint — you get back an `authorization_url` and a
           `session_id`. The `session_id` is the single identifier you use
           for everything else.
        2. Redirect the investor to `authorization_url` to log in to DigiLocker
           and grant consent.
        3. After consent, the investor is redirected back to your `redirect_url`
           with query parameters appended (see the table below).
        4. Use the `session_id` (path parameter) on the
           `POST /v1/kyc/digilocker/result/{session_id}` endpoint to read the
           consented data — identity, documents, and parsed document content.

        **Redirect parameters appended to your `redirect_url`:**

        | Outcome | Appended query parameters |
        | --- | --- |
        | Consent granted | `?success=true&id={session_id}&state={state}&documents=pan+driving_licence&has_verified_data=1` |
        | Partial consent (e.g. PAN only) | `?success=true&id={session_id}&state={state}&documents=pan` |
        | Consent denied / failed | `?success=false&id={session_id}&state={state}&error={error}` |

        `documents` lists the documents the investor agreed to share;
        `has_verified_data=1` appears only when verified identity is available.

        **Credits:** Free. Billing happens when documents/identity are returned.

        Args:
          consent: Explicit end-user consent. Must be `true` to proceed
              (regulatory requirement under DPDP / RBI). Captured for audit.

          consent_purpose: Specific purpose for which consent is taken (min 20 chars).
              Stored in the session and returned as a consent receipt.

          documents: Identities to verify and return in the response.

          prefill_mobile: Pre-verified mobile to skip the signup OTP step (only applies with user_flow=signup).

          redirect_url: Where to redirect the user after consent. Must be a valid http/https URL.

          state: Opaque value echoed back to your redirect_url unchanged.

          user_flow: Use "signin" for users with an existing DigiLocker account, "signup" for account-on-the-fly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/kyc/digilocker/session",
            body=maybe_transform(
                {
                    "consent": consent,
                    "consent_purpose": consent_purpose,
                    "documents": documents,
                    "prefill_mobile": prefill_mobile,
                    "redirect_url": redirect_url,
                    "state": state,
                    "user_flow": user_flow,
                },
                kyc_start_digilocker_session_params.KycStartDigilockerSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycStartDigilockerSessionResponse,
        )

    def get_digilocker_result(
        self,
        session_id: str,
        *,
        fetch_documents: List[Literal["pan", "aadhaar", "driving_licence"]] | Omit = omit,
        include_documents: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycGetDigilockerResultResponse:
        """
        Return everything available for a DigiLocker session in a single call.
        Each section is independent: if one is unavailable (e.g. the investor
        didn't consent to it), it's reported under `errors` and the rest of the
        response still succeeds.

        - `identity` — verified identity, when requested via `documents` (free).
        - `documents` — list of the investor's documents (free). Set
          `include_documents: false` to skip.
        - `fetched` — for each document in `fetch_documents`, the parsed document data.

        **Credits:** 0.25 per call, regardless of how many documents are
        fetched or whether identity is returned.

        Args:
          fetch_documents: Documents to additionally fetch + parse from the locker.
              Default: [] (no document fetch, no fetch billing).

          include_documents: Include the issued-documents list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/v1/kyc/digilocker/result/{session_id}", session_id=session_id),
            body=maybe_transform(
                {
                    "fetch_documents": fetch_documents,
                    "include_documents": include_documents,
                },
                kyc_get_digilocker_result_params.KycGetDigilockerResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycGetDigilockerResultResponse,
        )

    def check_pan_status(
        self,
        *,
        pan_no: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycCheckPanStatusResponse:
        """
        Query KYC registration status for a PAN number across all five SEBI-registered KRAs
        (CVL, NDML, CAMS, Karvy, KFin) via the CVL KRA portal.

        Raw portal status strings are normalized into clean enums (see `kyc_status`).

        **`kyc_compliant`** is `true` only when `kyc_status` is `validated` or `registered`.
        Use this for quick onboarding gate decisions.

        **`remarks`** on a KRA object is only actionable when `status` is `on_hold` —
        it contains the reason (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
        remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.

        **Note:** This endpoint may take up to 60 seconds. Set your client timeout accordingly.

        **Credits:** 0.25 per successful lookup. Failed lookups are not billed.

        Args:
          pan_no: PAN number to look up (10 characters, uppercase)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/kyc/pan/status",
            body=maybe_transform(
                {
                    "pan_no": pan_no,
                },
                kyc_check_pan_status_params.KycCheckPanStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycCheckPanStatusResponse,
        )


class AsyncKycResource(AsyncAPIResource):
    """
    Endpoints for verifying KYC (Know Your Customer) status of Indian investors.

    **Data source:** CVL KRA public inquiry portal (cvlkra.com), which aggregates
    records from all five SEBI-registered KRAs: CVL, NDML, CAMS, Karvy, and KFin.

    **Status normalization:** Raw CVL portal strings are normalized into clean enums.
    See the `kyc_status` property on `KycPanStatusResponse` for the full list.

    **Credits:** 0.25 per successful lookup. Failed lookups are not billed.
    """

    @cached_property
    def with_raw_response(self) -> AsyncKycResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKycResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKycResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncKycResourceWithStreamingResponse(self)

    async def lookup_digilocker_account(
        self,
        *,
        aadhaar_number: str | Omit = omit,
        mobile: str | Omit = omit,
        reference_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycLookupDigilockerAccountResponse:
        """
        Check whether a mobile number or Aadhaar number is already registered
        with DigiLocker. This is a pre-consent lookup: it helps you decide
        whether to start the user in `signin` or `signup` flow.

        Provide exactly one of `aadhaar_number` or `mobile`.

        **Credits:** Free.

        Args:
          aadhaar_number: 12-digit Aadhaar number.

          mobile: 10-digit Indian mobile number.

          reference_id: Optional caller-side request identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/kyc/digilocker/account-lookup",
            body=await async_maybe_transform(
                {
                    "aadhaar_number": aadhaar_number,
                    "mobile": mobile,
                    "reference_id": reference_id,
                },
                kyc_lookup_digilocker_account_params.KycLookupDigilockerAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycLookupDigilockerAccountResponse,
        )

    async def start_digilocker_session(
        self,
        *,
        consent: bool,
        consent_purpose: str,
        redirect_url: str,
        documents: List[Literal["aadhaar", "pan", "driving_licence", "email", "mobile"]] | Omit = omit,
        prefill_mobile: str | Omit = omit,
        state: str | Omit = omit,
        user_flow: Literal["signin", "signup"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycStartDigilockerSessionResponse:
        """
        Start a DigiLocker session to fetch the investor's government-issued
        documents (Aadhaar, PAN, etc.) with their consent.

        **How it works:**
        1. Call this endpoint — you get back an `authorization_url` and a
           `session_id`. The `session_id` is the single identifier you use
           for everything else.
        2. Redirect the investor to `authorization_url` to log in to DigiLocker
           and grant consent.
        3. After consent, the investor is redirected back to your `redirect_url`
           with query parameters appended (see the table below).
        4. Use the `session_id` (path parameter) on the
           `POST /v1/kyc/digilocker/result/{session_id}` endpoint to read the
           consented data — identity, documents, and parsed document content.

        **Redirect parameters appended to your `redirect_url`:**

        | Outcome | Appended query parameters |
        | --- | --- |
        | Consent granted | `?success=true&id={session_id}&state={state}&documents=pan+driving_licence&has_verified_data=1` |
        | Partial consent (e.g. PAN only) | `?success=true&id={session_id}&state={state}&documents=pan` |
        | Consent denied / failed | `?success=false&id={session_id}&state={state}&error={error}` |

        `documents` lists the documents the investor agreed to share;
        `has_verified_data=1` appears only when verified identity is available.

        **Credits:** Free. Billing happens when documents/identity are returned.

        Args:
          consent: Explicit end-user consent. Must be `true` to proceed
              (regulatory requirement under DPDP / RBI). Captured for audit.

          consent_purpose: Specific purpose for which consent is taken (min 20 chars).
              Stored in the session and returned as a consent receipt.

          documents: Identities to verify and return in the response.

          prefill_mobile: Pre-verified mobile to skip the signup OTP step (only applies with user_flow=signup).

          redirect_url: Where to redirect the user after consent. Must be a valid http/https URL.

          state: Opaque value echoed back to your redirect_url unchanged.

          user_flow: Use "signin" for users with an existing DigiLocker account, "signup" for account-on-the-fly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/kyc/digilocker/session",
            body=await async_maybe_transform(
                {
                    "consent": consent,
                    "consent_purpose": consent_purpose,
                    "documents": documents,
                    "prefill_mobile": prefill_mobile,
                    "redirect_url": redirect_url,
                    "state": state,
                    "user_flow": user_flow,
                },
                kyc_start_digilocker_session_params.KycStartDigilockerSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycStartDigilockerSessionResponse,
        )

    async def get_digilocker_result(
        self,
        session_id: str,
        *,
        fetch_documents: List[Literal["pan", "aadhaar", "driving_licence"]] | Omit = omit,
        include_documents: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycGetDigilockerResultResponse:
        """
        Return everything available for a DigiLocker session in a single call.
        Each section is independent: if one is unavailable (e.g. the investor
        didn't consent to it), it's reported under `errors` and the rest of the
        response still succeeds.

        - `identity` — verified identity, when requested via `documents` (free).
        - `documents` — list of the investor's documents (free). Set
          `include_documents: false` to skip.
        - `fetched` — for each document in `fetch_documents`, the parsed document data.

        **Credits:** 0.25 per call, regardless of how many documents are
        fetched or whether identity is returned.

        Args:
          fetch_documents: Documents to additionally fetch + parse from the locker.
              Default: [] (no document fetch, no fetch billing).

          include_documents: Include the issued-documents list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/v1/kyc/digilocker/result/{session_id}", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "fetch_documents": fetch_documents,
                    "include_documents": include_documents,
                },
                kyc_get_digilocker_result_params.KycGetDigilockerResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycGetDigilockerResultResponse,
        )

    async def check_pan_status(
        self,
        *,
        pan_no: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KycCheckPanStatusResponse:
        """
        Query KYC registration status for a PAN number across all five SEBI-registered KRAs
        (CVL, NDML, CAMS, Karvy, KFin) via the CVL KRA portal.

        Raw portal status strings are normalized into clean enums (see `kyc_status`).

        **`kyc_compliant`** is `true` only when `kyc_status` is `validated` or `registered`.
        Use this for quick onboarding gate decisions.

        **`remarks`** on a KRA object is only actionable when `status` is `on_hold` —
        it contains the reason (e.g. `"APPLICANT PHOTO MISMATCH"`). For `validated` KRAs,
        remarks like `"FATCA NOT APPLICABLE"` can be safely ignored.

        **Note:** This endpoint may take up to 60 seconds. Set your client timeout accordingly.

        **Credits:** 0.25 per successful lookup. Failed lookups are not billed.

        Args:
          pan_no: PAN number to look up (10 characters, uppercase)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/kyc/pan/status",
            body=await async_maybe_transform(
                {
                    "pan_no": pan_no,
                },
                kyc_check_pan_status_params.KycCheckPanStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KycCheckPanStatusResponse,
        )


class KycResourceWithRawResponse:
    def __init__(self, kyc: KycResource) -> None:
        self._kyc = kyc

        self.lookup_digilocker_account = to_raw_response_wrapper(
            kyc.lookup_digilocker_account,
        )
        self.start_digilocker_session = to_raw_response_wrapper(
            kyc.start_digilocker_session,
        )
        self.get_digilocker_result = to_raw_response_wrapper(
            kyc.get_digilocker_result,
        )
        self.check_pan_status = to_raw_response_wrapper(
            kyc.check_pan_status,
        )


class AsyncKycResourceWithRawResponse:
    def __init__(self, kyc: AsyncKycResource) -> None:
        self._kyc = kyc

        self.lookup_digilocker_account = async_to_raw_response_wrapper(
            kyc.lookup_digilocker_account,
        )
        self.start_digilocker_session = async_to_raw_response_wrapper(
            kyc.start_digilocker_session,
        )
        self.get_digilocker_result = async_to_raw_response_wrapper(
            kyc.get_digilocker_result,
        )
        self.check_pan_status = async_to_raw_response_wrapper(
            kyc.check_pan_status,
        )


class KycResourceWithStreamingResponse:
    def __init__(self, kyc: KycResource) -> None:
        self._kyc = kyc

        self.lookup_digilocker_account = to_streamed_response_wrapper(
            kyc.lookup_digilocker_account,
        )
        self.start_digilocker_session = to_streamed_response_wrapper(
            kyc.start_digilocker_session,
        )
        self.get_digilocker_result = to_streamed_response_wrapper(
            kyc.get_digilocker_result,
        )
        self.check_pan_status = to_streamed_response_wrapper(
            kyc.check_pan_status,
        )


class AsyncKycResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKycResource) -> None:
        self._kyc = kyc

        self.lookup_digilocker_account = async_to_streamed_response_wrapper(
            kyc.lookup_digilocker_account,
        )
        self.start_digilocker_session = async_to_streamed_response_wrapper(
            kyc.start_digilocker_session,
        )
        self.get_digilocker_result = async_to_streamed_response_wrapper(
            kyc.get_digilocker_result,
        )
        self.check_pan_status = async_to_streamed_response_wrapper(
            kyc.check_pan_status,
        )
