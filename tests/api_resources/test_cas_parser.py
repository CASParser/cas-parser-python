# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import (
    UnifiedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCasParser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cams_kfintech(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.cams_kfintech()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cams_kfintech_with_all_params(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.cams_kfintech(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cams_kfintech(self, client: CasParser) -> None:
        response = client.cas_parser.with_raw_response.cams_kfintech()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cams_kfintech(self, client: CasParser) -> None:
        with client.cas_parser.with_streaming_response.cams_kfintech() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cdsl(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.cdsl()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cdsl_with_all_params(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.cdsl(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cdsl(self, client: CasParser) -> None:
        response = client.cas_parser.with_raw_response.cdsl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cdsl(self, client: CasParser) -> None:
        with client.cas_parser.with_streaming_response.cdsl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_nsdl(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.nsdl()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_nsdl_with_all_params(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.nsdl(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_nsdl(self, client: CasParser) -> None:
        response = client.cas_parser.with_raw_response.nsdl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_nsdl(self, client: CasParser) -> None:
        with client.cas_parser.with_streaming_response.nsdl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_smart_parse(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.smart_parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_smart_parse_with_all_params(self, client: CasParser) -> None:
        cas_parser = client.cas_parser.smart_parse(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_smart_parse(self, client: CasParser) -> None:
        response = client.cas_parser.with_raw_response.smart_parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_smart_parse(self, client: CasParser) -> None:
        with client.cas_parser.with_streaming_response.smart_parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCasParser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cams_kfintech(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.cams_kfintech()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cams_kfintech_with_all_params(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.cams_kfintech(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cams_kfintech(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cas_parser.with_raw_response.cams_kfintech()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = await response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cams_kfintech(self, async_client: AsyncCasParser) -> None:
        async with async_client.cas_parser.with_streaming_response.cams_kfintech() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = await response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cdsl(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.cdsl()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cdsl_with_all_params(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.cdsl(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cdsl(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cas_parser.with_raw_response.cdsl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = await response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cdsl(self, async_client: AsyncCasParser) -> None:
        async with async_client.cas_parser.with_streaming_response.cdsl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = await response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_nsdl(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.nsdl()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_nsdl_with_all_params(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.nsdl(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_nsdl(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cas_parser.with_raw_response.nsdl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = await response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_nsdl(self, async_client: AsyncCasParser) -> None:
        async with async_client.cas_parser.with_streaming_response.nsdl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = await response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_smart_parse(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.smart_parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_smart_parse_with_all_params(self, async_client: AsyncCasParser) -> None:
        cas_parser = await async_client.cas_parser.smart_parse(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_smart_parse(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cas_parser.with_raw_response.smart_parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cas_parser = await response.parse()
        assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_smart_parse(self, async_client: AsyncCasParser) -> None:
        async with async_client.cas_parser.with_streaming_response.smart_parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cas_parser = await response.parse()
            assert_matches_type(UnifiedResponse, cas_parser, path=["response"])

        assert cast(Any, response.is_closed) is True
