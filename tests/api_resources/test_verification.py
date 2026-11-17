# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import (
    VerificationVerifyMfdResponse,
    VerificationVerifySebiResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_mfd(self, client: CasParser) -> None:
        verification = client.verification.verify_mfd(
            arn="123456",
        )
        assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_mfd(self, client: CasParser) -> None:
        response = client.verification.with_raw_response.verify_mfd(
            arn="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_mfd(self, client: CasParser) -> None:
        with client.verification.with_streaming_response.verify_mfd(
            arn="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_sebi(self, client: CasParser) -> None:
        verification = client.verification.verify_sebi()
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_sebi_with_all_params(self, client: CasParser) -> None:
        verification = client.verification.verify_sebi(
            name="Motilal Oswal",
            registration_number="INP000000670",
            type="investment-adviser",
        )
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_sebi(self, client: CasParser) -> None:
        response = client.verification.with_raw_response.verify_sebi()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_sebi(self, client: CasParser) -> None:
        with client.verification.with_streaming_response.verify_sebi() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_mfd(self, async_client: AsyncCasParser) -> None:
        verification = await async_client.verification.verify_mfd(
            arn="123456",
        )
        assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_mfd(self, async_client: AsyncCasParser) -> None:
        response = await async_client.verification.with_raw_response.verify_mfd(
            arn="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_mfd(self, async_client: AsyncCasParser) -> None:
        async with async_client.verification.with_streaming_response.verify_mfd(
            arn="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationVerifyMfdResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_sebi(self, async_client: AsyncCasParser) -> None:
        verification = await async_client.verification.verify_sebi()
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_sebi_with_all_params(self, async_client: AsyncCasParser) -> None:
        verification = await async_client.verification.verify_sebi(
            name="Motilal Oswal",
            registration_number="INP000000670",
            type="investment-adviser",
        )
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_sebi(self, async_client: AsyncCasParser) -> None:
        response = await async_client.verification.with_raw_response.verify_sebi()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_sebi(self, async_client: AsyncCasParser) -> None:
        async with async_client.verification.with_streaming_response.verify_sebi() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationVerifySebiResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True
