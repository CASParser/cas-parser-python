# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types.cdsl import (
    FetchVerifyOtpResponse,
    FetchRequestOtpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFetch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_otp(self, client: CasParser) -> None:
        fetch = client.cdsl.fetch.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        )
        assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_otp(self, client: CasParser) -> None:
        response = client.cdsl.fetch.with_raw_response.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = response.parse()
        assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_otp(self, client: CasParser) -> None:
        with client.cdsl.fetch.with_streaming_response.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = response.parse()
            assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_otp(self, client: CasParser) -> None:
        fetch = client.cdsl.fetch.verify_otp(
            session_id="session_id",
            otp="123456",
        )
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_otp_with_all_params(self, client: CasParser) -> None:
        fetch = client.cdsl.fetch.verify_otp(
            session_id="session_id",
            otp="123456",
            num_periods=6,
        )
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_otp(self, client: CasParser) -> None:
        response = client.cdsl.fetch.with_raw_response.verify_otp(
            session_id="session_id",
            otp="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = response.parse()
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_otp(self, client: CasParser) -> None:
        with client.cdsl.fetch.with_streaming_response.verify_otp(
            session_id="session_id",
            otp="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = response.parse()
            assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify_otp(self, client: CasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.cdsl.fetch.with_raw_response.verify_otp(
                session_id="",
                otp="123456",
            )


class TestAsyncFetch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_otp(self, async_client: AsyncCasParser) -> None:
        fetch = await async_client.cdsl.fetch.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        )
        assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_otp(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cdsl.fetch.with_raw_response.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = await response.parse()
        assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_otp(self, async_client: AsyncCasParser) -> None:
        async with async_client.cdsl.fetch.with_streaming_response.request_otp(
            bo_id="1234567890123456",
            dob="1990-01-15",
            pan="ABCDE1234F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = await response.parse()
            assert_matches_type(FetchRequestOtpResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_otp(self, async_client: AsyncCasParser) -> None:
        fetch = await async_client.cdsl.fetch.verify_otp(
            session_id="session_id",
            otp="123456",
        )
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_otp_with_all_params(self, async_client: AsyncCasParser) -> None:
        fetch = await async_client.cdsl.fetch.verify_otp(
            session_id="session_id",
            otp="123456",
            num_periods=6,
        )
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_otp(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cdsl.fetch.with_raw_response.verify_otp(
            session_id="session_id",
            otp="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = await response.parse()
        assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_otp(self, async_client: AsyncCasParser) -> None:
        async with async_client.cdsl.fetch.with_streaming_response.verify_otp(
            session_id="session_id",
            otp="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = await response.parse()
            assert_matches_type(FetchVerifyOtpResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify_otp(self, async_client: AsyncCasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.cdsl.fetch.with_raw_response.verify_otp(
                session_id="",
                otp="123456",
            )
