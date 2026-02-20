# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import ContractNoteParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContractNote:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse(self, client: CasParser) -> None:
        contract_note = client.contract_note.parse()
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse_with_all_params(self, client: CasParser) -> None:
        contract_note = client.contract_note.parse(
            broker_type="zerodha",
            password="FAXAK2545F",
            pdf_file="JVBERi0xLjQKMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwo...",
            pdf_url="https://example.com/contract_note.pdf",
        )
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_parse(self, client: CasParser) -> None:
        response = client.contract_note.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract_note = response.parse()
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_parse(self, client: CasParser) -> None:
        with client.contract_note.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract_note = response.parse()
            assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContractNote:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse(self, async_client: AsyncCasParser) -> None:
        contract_note = await async_client.contract_note.parse()
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse_with_all_params(self, async_client: AsyncCasParser) -> None:
        contract_note = await async_client.contract_note.parse(
            broker_type="zerodha",
            password="FAXAK2545F",
            pdf_file="JVBERi0xLjQKMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwo...",
            pdf_url="https://example.com/contract_note.pdf",
        )
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncCasParser) -> None:
        response = await async_client.contract_note.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract_note = await response.parse()
        assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncCasParser) -> None:
        async with async_client.contract_note.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract_note = await response.parse()
            assert_matches_type(ContractNoteParseResponse, contract_note, path=["response"])

        assert cast(Any, response.is_closed) is True
