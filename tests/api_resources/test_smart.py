# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import UnifiedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse_cas_pdf(self, client: CasParser) -> None:
        smart = client.smart.parse_cas_pdf()
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse_cas_pdf_with_all_params(self, client: CasParser) -> None:
        smart = client.smart.parse_cas_pdf(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_parse_cas_pdf(self, client: CasParser) -> None:
        response = client.smart.with_raw_response.parse_cas_pdf()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart = response.parse()
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_parse_cas_pdf(self, client: CasParser) -> None:
        with client.smart.with_streaming_response.parse_cas_pdf() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart = response.parse()
            assert_matches_type(UnifiedResponse, smart, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSmart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse_cas_pdf(self, async_client: AsyncCasParser) -> None:
        smart = await async_client.smart.parse_cas_pdf()
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse_cas_pdf_with_all_params(self, async_client: AsyncCasParser) -> None:
        smart = await async_client.smart.parse_cas_pdf(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_parse_cas_pdf(self, async_client: AsyncCasParser) -> None:
        response = await async_client.smart.with_raw_response.parse_cas_pdf()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart = await response.parse()
        assert_matches_type(UnifiedResponse, smart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_parse_cas_pdf(self, async_client: AsyncCasParser) -> None:
        async with async_client.smart.with_streaming_response.parse_cas_pdf() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart = await response.parse()
            assert_matches_type(UnifiedResponse, smart, path=["response"])

        assert cast(Any, response.is_closed) is True
