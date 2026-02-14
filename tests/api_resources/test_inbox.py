# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cas_parser import CasParser, AsyncCasParser
from tests.utils import assert_matches_type
from cas_parser.types import (
    InboxConnectEmailResponse,
    InboxListCasFilesResponse,
    InboxDisconnectEmailResponse,
    InboxCheckConnectionStatusResponse,
)
from cas_parser._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_connection_status(self, client: CasParser) -> None:
        inbox = client.inbox.check_connection_status(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_connection_status(self, client: CasParser) -> None:
        response = client.inbox.with_raw_response.check_connection_status(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_connection_status(self, client: CasParser) -> None:
        with client.inbox.with_streaming_response.check_connection_status(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_email(self, client: CasParser) -> None:
        inbox = client.inbox.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        )
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_email_with_all_params(self, client: CasParser) -> None:
        inbox = client.inbox.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
            state="abc123",
        )
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect_email(self, client: CasParser) -> None:
        response = client.inbox.with_raw_response.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect_email(self, client: CasParser) -> None:
        with client.inbox.with_streaming_response.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disconnect_email(self, client: CasParser) -> None:
        inbox = client.inbox.disconnect_email(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_disconnect_email(self, client: CasParser) -> None:
        response = client.inbox.with_raw_response.disconnect_email(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_disconnect_email(self, client: CasParser) -> None:
        with client.inbox.with_streaming_response.disconnect_email(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_cas_files(self, client: CasParser) -> None:
        inbox = client.inbox.list_cas_files(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_cas_files_with_all_params(self, client: CasParser) -> None:
        inbox = client.inbox.list_cas_files(
            x_inbox_token="x-inbox-token",
            cas_types=["cdsl", "nsdl"],
            end_date=parse_date("2025-12-31"),
            start_date=parse_date("2025-12-01"),
        )
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_cas_files(self, client: CasParser) -> None:
        response = client.inbox.with_raw_response.list_cas_files(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_cas_files(self, client: CasParser) -> None:
        with client.inbox.with_streaming_response.list_cas_files(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_connection_status(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.check_connection_status(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_connection_status(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbox.with_raw_response.check_connection_status(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_connection_status(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbox.with_streaming_response.check_connection_status(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxCheckConnectionStatusResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_email(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        )
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_email_with_all_params(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
            state="abc123",
        )
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect_email(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbox.with_raw_response.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect_email(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbox.with_streaming_response.connect_email(
            redirect_uri="https://yourapp.com/oauth-callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxConnectEmailResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disconnect_email(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.disconnect_email(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_disconnect_email(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbox.with_raw_response.disconnect_email(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect_email(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbox.with_streaming_response.disconnect_email(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxDisconnectEmailResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_cas_files(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.list_cas_files(
            x_inbox_token="x-inbox-token",
        )
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_cas_files_with_all_params(self, async_client: AsyncCasParser) -> None:
        inbox = await async_client.inbox.list_cas_files(
            x_inbox_token="x-inbox-token",
            cas_types=["cdsl", "nsdl"],
            end_date=parse_date("2025-12-31"),
            start_date=parse_date("2025-12-01"),
        )
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_cas_files(self, async_client: AsyncCasParser) -> None:
        response = await async_client.inbox.with_raw_response.list_cas_files(
            x_inbox_token="x-inbox-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_cas_files(self, async_client: AsyncCasParser) -> None:
        async with async_client.inbox.with_streaming_response.list_cas_files(
            x_inbox_token="x-inbox-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxListCasFilesResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True
