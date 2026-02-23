# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import (
    InboundEmailListResponse,
    InboundEmailCreateResponse,
    InboundEmailDeleteResponse,
    InboundEmailRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        )
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
            alias="john-portfolio",
            allowed_sources=["cdsl", "nsdl"],
            metadata={
                "plan": "premium",
                "source": "onboarding",
            },
            reference="user_12345",
        )
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: CasParser) -> None:
        response = client.inbound_email.with_raw_response.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = response.parse()
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: CasParser) -> None:
        with client.inbound_email.with_streaming_response.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = response.parse()
            assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.retrieve(
            "ie_a1b2c3d4e5f6",
        )
        assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: CasParser) -> None:
        response = client.inbound_email.with_raw_response.retrieve(
            "ie_a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = response.parse()
        assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: CasParser) -> None:
        with client.inbound_email.with_streaming_response.retrieve(
            "ie_a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = response.parse()
            assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: CasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_email_id` but received ''"):
            client.inbound_email.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.list()
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.list(
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: CasParser) -> None:
        response = client.inbound_email.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = response.parse()
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: CasParser) -> None:
        with client.inbound_email.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = response.parse()
            assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: CasParser) -> None:
        inbound_email = client.inbound_email.delete(
            "inbound_email_id",
        )
        assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: CasParser) -> None:
        response = client.inbound_email.with_raw_response.delete(
            "inbound_email_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = response.parse()
        assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: CasParser) -> None:
        with client.inbound_email.with_streaming_response.delete(
            "inbound_email_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = response.parse()
            assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: CasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_email_id` but received ''"):
            client.inbound_email.with_raw_response.delete(
                "",
            )


class TestAsyncInboundEmail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        )
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
            alias="john-portfolio",
            allowed_sources=["cdsl", "nsdl"],
            metadata={
                "plan": "premium",
                "source": "onboarding",
            },
            reference="user_12345",
        )
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbound_email.with_raw_response.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = await response.parse()
        assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbound_email.with_streaming_response.create(
            callback_url="https://api.yourapp.com/webhooks/cas-email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = await response.parse()
            assert_matches_type(InboundEmailCreateResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.retrieve(
            "ie_a1b2c3d4e5f6",
        )
        assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbound_email.with_raw_response.retrieve(
            "ie_a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = await response.parse()
        assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbound_email.with_streaming_response.retrieve(
            "ie_a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = await response.parse()
            assert_matches_type(InboundEmailRetrieveResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_email_id` but received ''"):
            await async_client.inbound_email.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.list()
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.list(
            limit=1,
            offset=0,
            status="active",
        )
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbound_email.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = await response.parse()
        assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbound_email.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = await response.parse()
            assert_matches_type(InboundEmailListResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCasParser) -> None:
        inbound_email = await async_client.inbound_email.delete(
            "inbound_email_id",
        )
        assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbound_email.with_raw_response.delete(
            "inbound_email_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_email = await response.parse()
        assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbound_email.with_streaming_response.delete(
            "inbound_email_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_email = await response.parse()
            assert_matches_type(InboundEmailDeleteResponse, inbound_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasParser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_email_id` but received ''"):
            await async_client.inbound_email.with_raw_response.delete(
                "",
            )
