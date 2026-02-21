# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import KfintechGenerateCasResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKfintech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_cas(self, client: CasParser) -> None:
        kfintech = client.kfintech.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        )
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_cas_with_all_params(self, client: CasParser) -> None:
        kfintech = client.kfintech.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
            pan_no="ABCDE1234F",
        )
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_cas(self, client: CasParser) -> None:
        response = client.kfintech.with_raw_response.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kfintech = response.parse()
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_cas(self, client: CasParser) -> None:
        with client.kfintech.with_streaming_response.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kfintech = response.parse()
            assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKfintech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_cas(self, async_client: AsyncCasParser) -> None:
        kfintech = await async_client.kfintech.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        )
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_cas_with_all_params(self, async_client: AsyncCasParser) -> None:
        kfintech = await async_client.kfintech.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
            pan_no="ABCDE1234F",
        )
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_cas(self, async_client: AsyncCasParser) -> None:
        response = await async_client.kfintech.with_raw_response.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kfintech = await response.parse()
        assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_cas(self, async_client: AsyncCasParser) -> None:
        async with async_client.kfintech.with_streaming_response.generate_cas(
            email="user@example.com",
            from_date="2023-01-01",
            password="Abcdefghi12$",
            to_date="2023-12-31",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kfintech = await response.parse()
            assert_matches_type(KfintechGenerateCasResponse, kfintech, path=["response"])

        assert cast(Any, response.is_closed) is True
