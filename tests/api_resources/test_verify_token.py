# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import VerifyTokenVerifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifyToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: CasParser) -> None:
        verify_token = client.verify_token.verify()
        assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: CasParser) -> None:
        response = client.verify_token.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_token = response.parse()
        assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: CasParser) -> None:
        with client.verify_token.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_token = response.parse()
            assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifyToken:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncCasParser) -> None:
        verify_token = await async_client.verify_token.verify()
        assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCasParser) -> None:
        response = await async_client.verify_token.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_token = await response.parse()
        assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCasParser) -> None:
        async with async_client.verify_token.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_token = await response.parse()
            assert_matches_type(VerifyTokenVerifyResponse, verify_token, path=["response"])

        assert cast(Any, response.is_closed) is True
