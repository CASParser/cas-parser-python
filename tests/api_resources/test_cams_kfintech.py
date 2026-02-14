# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import UnifiedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCamsKfintech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_parse(self, client: CasParser) -> None:
        cams_kfintech = client.cams_kfintech.parse()
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_parse_with_all_params(self, client: CasParser) -> None:
        cams_kfintech = client.cams_kfintech.parse(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_parse(self, client: CasParser) -> None:
        response = client.cams_kfintech.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cams_kfintech = response.parse()
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_parse(self, client: CasParser) -> None:
        with client.cams_kfintech.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cams_kfintech = response.parse()
            assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCamsKfintech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_parse(self, async_client: AsyncCasParser) -> None:
        cams_kfintech = await async_client.cams_kfintech.parse()
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_parse_with_all_params(self, async_client: AsyncCasParser) -> None:
        cams_kfintech = await async_client.cams_kfintech.parse(
            password="password",
            pdf_file="pdf_file",
            pdf_url="https://example.com",
        )
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncCasParser) -> None:
        response = await async_client.cams_kfintech.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cams_kfintech = await response.parse()
        assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncCasParser) -> None:
        async with async_client.cams_kfintech.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cams_kfintech = await response.parse()
            assert_matches_type(UnifiedResponse, cams_kfintech, path=["response"])

        assert cast(Any, response.is_closed) is True
