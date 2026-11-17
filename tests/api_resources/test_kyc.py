# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import (
    KycCheckPanStatusResponse,
    KycGetDigilockerResultResponse,
    KycStartDigilockerSessionResponse,
    KycLookupDigilockerAccountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKyc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_digilocker_account(self, client: CasParser) -> None:
        kyc = client.kyc.lookup_digilocker_account()
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_digilocker_account_with_all_params(self, client: CasParser) -> None:
        kyc = client.kyc.lookup_digilocker_account(
            aadhaar_number="123456789012",
            mobile="9876543210",
            reference_id="reference_id",
        )
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_digilocker_account(self, client: CasParser) -> None:
        response = client.kyc.with_raw_response.lookup_digilocker_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_digilocker_account(self, client: CasParser) -> None:
        with client.kyc.with_streaming_response.lookup_digilocker_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_digilocker_session(self, client: CasParser) -> None:
        kyc = client.kyc.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        )
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_digilocker_session_with_all_params(self, client: CasParser) -> None:
        kyc = client.kyc.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            documents=["aadhaar"],
            prefill_mobile="9999999999",
            redirect_url="https://yourapp.com/digilocker/callback",
            state="investor_42",
            user_flow="signin",
        )
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_digilocker_session(self, client: CasParser) -> None:
        response = client.kyc.with_raw_response.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_digilocker_session(self, client: CasParser) -> None:
        with client.kyc.with_streaming_response.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_digilocker_result(self, client: CasParser) -> None:
        kyc = client.kyc.get_digilocker_result(
            "session_id",
        )
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_digilocker_result_with_all_params(self, client: CasParser) -> None:
        kyc = client.kyc.get_digilocker_result(
            "session_id",
            fetch_documents=["pan"],
            include_documents=True,
        )
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_digilocker_result(self, client: CasParser) -> None:
        response = client.kyc.with_raw_response.get_digilocker_result(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_digilocker_result(self, client: CasParser) -> None:
        with client.kyc.with_streaming_response.get_digilocker_result(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_digilocker_result(self, client: CasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.kyc.with_raw_response.get_digilocker_result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_pan_status(self, client: CasParser) -> None:
        kyc = client.kyc.check_pan_status(
            pan_no="ABCDE1234F",
        )
        assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_pan_status(self, client: CasParser) -> None:
        response = client.kyc.with_raw_response.check_pan_status(
            pan_no="ABCDE1234F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_pan_status(self, client: CasParser) -> None:
        with client.kyc.with_streaming_response.check_pan_status(
            pan_no="ABCDE1234F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKyc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_digilocker_account(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.lookup_digilocker_account()
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_digilocker_account_with_all_params(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.lookup_digilocker_account(
            aadhaar_number="123456789012",
            mobile="9876543210",
            reference_id="reference_id",
        )
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_digilocker_account(self, async_client: AsyncCasParser) -> None:
        response = await async_client.kyc.with_raw_response.lookup_digilocker_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_digilocker_account(self, async_client: AsyncCasParser) -> None:
        async with async_client.kyc.with_streaming_response.lookup_digilocker_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KycLookupDigilockerAccountResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_digilocker_session(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        )
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_digilocker_session_with_all_params(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            documents=["aadhaar"],
            prefill_mobile="9999999999",
            redirect_url="https://yourapp.com/digilocker/callback",
            state="investor_42",
            user_flow="signin",
        )
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_digilocker_session(self, async_client: AsyncCasParser) -> None:
        response = await async_client.kyc.with_raw_response.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_digilocker_session(self, async_client: AsyncCasParser) -> None:
        async with async_client.kyc.with_streaming_response.start_digilocker_session(
            consent=True,
            consent_purpose="KYC for loan account opening",
            redirect_url="https://yourapp.com/digilocker/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KycStartDigilockerSessionResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_digilocker_result(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.get_digilocker_result(
            "session_id",
        )
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_digilocker_result_with_all_params(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.get_digilocker_result(
            "session_id",
            fetch_documents=["pan"],
            include_documents=True,
        )
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_digilocker_result(self, async_client: AsyncCasParser) -> None:
        response = await async_client.kyc.with_raw_response.get_digilocker_result(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_digilocker_result(self, async_client: AsyncCasParser) -> None:
        async with async_client.kyc.with_streaming_response.get_digilocker_result(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KycGetDigilockerResultResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_digilocker_result(self, async_client: AsyncCasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.kyc.with_raw_response.get_digilocker_result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_pan_status(self, async_client: AsyncCasParser) -> None:
        kyc = await async_client.kyc.check_pan_status(
            pan_no="ABCDE1234F",
        )
        assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_pan_status(self, async_client: AsyncCasParser) -> None:
        response = await async_client.kyc.with_raw_response.check_pan_status(
            pan_no="ABCDE1234F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_pan_status(self, async_client: AsyncCasParser) -> None:
        async with async_client.kyc.with_streaming_response.check_pan_status(
            pan_no="ABCDE1234F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KycCheckPanStatusResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True
