# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import agent_auth_approve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_auth_poll_response import AgentAuthPollResponse
from ..types.agent_auth_approve_response import AgentAuthApproveResponse

__all__ = ["AgentAuthResource", "AsyncAgentAuthResource"]


class AgentAuthResource(SyncAPIResource):
    """
    Endpoints for coding agents to obtain API keys via a browser-based approval flow.

    **How it works:**
    1. Agent generates a random token locally (e.g. `openssl rand -hex 32`). No API call needed.
    2. Agent asks the user to open `https://app.casparser.in/agent-auth?token=<token>&client_name=<name>`
    3. User signs in via the browser and clicks Approve.
    4. Agent polls `GET /v1/agent-auth/token/{token}` every 5 seconds until the key is delivered.

    **Security:**
    - Token must be 16-128 characters (recommended: 64 hex chars / 256 bits)
    - Approved keys are delivered once (one-shot) and then deleted
    - Tokens expire after 10 minutes if not approved
    """

    @cached_property
    def with_raw_response(self) -> AgentAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AgentAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AgentAuthResourceWithStreamingResponse(self)

    def poll(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthPollResponse:
        """
        Agent polls this endpoint to check if the user has approved the authorization.

        Returns `{"status": "pending"}` while waiting for user approval.
        Returns `{"status": "approved", "api_key": "sk_...", "email": "..."}` once approved.

        **One-shot delivery:** the API key is returned exactly once. After delivery, the token is deleted
        and subsequent polls return `{"status": "pending"}`.

        **Recommended polling interval:** 5 seconds. Token expires after 10 minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return cast(
            AgentAuthPollResponse,
            self._get(
                path_template("/v1/agent-auth/token/{token}", token=token),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentAuthPollResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def approve(
        self,
        token: str,
        *,
        id_token: str,
        client_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthApproveResponse:
        """
        Called by the frontend after the user signs in.

        Verifies the identity token, creates or looks up the user's API key,
        and stores it against the token for the agent to poll via `GET /v1/agent-auth/token/{token}`.

        **This endpoint is called by the browser, not by agents directly.**

        Args:
          client_name: Name of the agent/application (stored in customer metadata for audit)

          id_token: Identity token obtained after the user signs in on the approval page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._post(
            path_template("/v1/agent-auth/token/{token}/approve", token=token),
            body=maybe_transform(
                {
                    "client_name": client_name,
                    "id_token": id_token,
                },
                agent_auth_approve_params.AgentAuthApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthApproveResponse,
        )


class AsyncAgentAuthResource(AsyncAPIResource):
    """
    Endpoints for coding agents to obtain API keys via a browser-based approval flow.

    **How it works:**
    1. Agent generates a random token locally (e.g. `openssl rand -hex 32`). No API call needed.
    2. Agent asks the user to open `https://app.casparser.in/agent-auth?token=<token>&client_name=<name>`
    3. User signs in via the browser and clicks Approve.
    4. Agent polls `GET /v1/agent-auth/token/{token}` every 5 seconds until the key is delivered.

    **Security:**
    - Token must be 16-128 characters (recommended: 64 hex chars / 256 bits)
    - Approved keys are delivered once (one-shot) and then deleted
    - Tokens expire after 10 minutes if not approved
    """

    @cached_property
    def with_raw_response(self) -> AsyncAgentAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncAgentAuthResourceWithStreamingResponse(self)

    async def poll(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthPollResponse:
        """
        Agent polls this endpoint to check if the user has approved the authorization.

        Returns `{"status": "pending"}` while waiting for user approval.
        Returns `{"status": "approved", "api_key": "sk_...", "email": "..."}` once approved.

        **One-shot delivery:** the API key is returned exactly once. After delivery, the token is deleted
        and subsequent polls return `{"status": "pending"}`.

        **Recommended polling interval:** 5 seconds. Token expires after 10 minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return cast(
            AgentAuthPollResponse,
            await self._get(
                path_template("/v1/agent-auth/token/{token}", token=token),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentAuthPollResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def approve(
        self,
        token: str,
        *,
        id_token: str,
        client_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthApproveResponse:
        """
        Called by the frontend after the user signs in.

        Verifies the identity token, creates or looks up the user's API key,
        and stores it against the token for the agent to poll via `GET /v1/agent-auth/token/{token}`.

        **This endpoint is called by the browser, not by agents directly.**

        Args:
          client_name: Name of the agent/application (stored in customer metadata for audit)

          id_token: Identity token obtained after the user signs in on the approval page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._post(
            path_template("/v1/agent-auth/token/{token}/approve", token=token),
            body=await async_maybe_transform(
                {
                    "client_name": client_name,
                    "id_token": id_token,
                },
                agent_auth_approve_params.AgentAuthApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthApproveResponse,
        )


class AgentAuthResourceWithRawResponse:
    def __init__(self, agent_auth: AgentAuthResource) -> None:
        self._agent_auth = agent_auth

        self.poll = to_raw_response_wrapper(
            agent_auth.poll,
        )
        self.approve = to_raw_response_wrapper(
            agent_auth.approve,
        )


class AsyncAgentAuthResourceWithRawResponse:
    def __init__(self, agent_auth: AsyncAgentAuthResource) -> None:
        self._agent_auth = agent_auth

        self.poll = async_to_raw_response_wrapper(
            agent_auth.poll,
        )
        self.approve = async_to_raw_response_wrapper(
            agent_auth.approve,
        )


class AgentAuthResourceWithStreamingResponse:
    def __init__(self, agent_auth: AgentAuthResource) -> None:
        self._agent_auth = agent_auth

        self.poll = to_streamed_response_wrapper(
            agent_auth.poll,
        )
        self.approve = to_streamed_response_wrapper(
            agent_auth.approve,
        )


class AsyncAgentAuthResourceWithStreamingResponse:
    def __init__(self, agent_auth: AsyncAgentAuthResource) -> None:
        self._agent_auth = agent_auth

        self.poll = async_to_streamed_response_wrapper(
            agent_auth.poll,
        )
        self.approve = async_to_streamed_response_wrapper(
            agent_auth.approve,
        )
