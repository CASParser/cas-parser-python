# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import log_create_params, log_get_summary_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.log_create_response import LogCreateResponse
from ..types.log_get_summary_response import LogGetSummaryResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogCreateResponse:
        """
        Retrieve detailed API usage logs for your account.

        Returns a list of API calls with timestamps, features used, status codes, and
        credits consumed. Useful for monitoring usage patterns and debugging.

        Args:
          end_time: End time filter (ISO 8601). Defaults to now.

          limit: Maximum number of logs to return

          start_time: Start time filter (ISO 8601). Defaults to 30 days ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/logs",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "limit": limit,
                    "start_time": start_time,
                },
                log_create_params.LogCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogCreateResponse,
        )

    def get_summary(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogGetSummaryResponse:
        """
        Get aggregated usage statistics grouped by feature.

        Useful for understanding which API features are being used most and tracking
        usage trends.

        Args:
          end_time: End time filter (ISO 8601). Defaults to now.

          start_time: Start time filter (ISO 8601). Defaults to start of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/logs/summary",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                },
                log_get_summary_params.LogGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogGetSummaryResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CASParser/cas-parser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CASParser/cas-parser-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogCreateResponse:
        """
        Retrieve detailed API usage logs for your account.

        Returns a list of API calls with timestamps, features used, status codes, and
        credits consumed. Useful for monitoring usage patterns and debugging.

        Args:
          end_time: End time filter (ISO 8601). Defaults to now.

          limit: Maximum number of logs to return

          start_time: Start time filter (ISO 8601). Defaults to 30 days ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/logs",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "limit": limit,
                    "start_time": start_time,
                },
                log_create_params.LogCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogCreateResponse,
        )

    async def get_summary(
        self,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogGetSummaryResponse:
        """
        Get aggregated usage statistics grouped by feature.

        Useful for understanding which API features are being used most and tracking
        usage trends.

        Args:
          end_time: End time filter (ISO 8601). Defaults to now.

          start_time: Start time filter (ISO 8601). Defaults to start of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/logs/summary",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                },
                log_get_summary_params.LogGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogGetSummaryResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.create = to_raw_response_wrapper(
            logs.create,
        )
        self.get_summary = to_raw_response_wrapper(
            logs.get_summary,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.create = async_to_raw_response_wrapper(
            logs.create,
        )
        self.get_summary = async_to_raw_response_wrapper(
            logs.get_summary,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.create = to_streamed_response_wrapper(
            logs.create,
        )
        self.get_summary = to_streamed_response_wrapper(
            logs.get_summary,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.create = async_to_streamed_response_wrapper(
            logs.create,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            logs.get_summary,
        )
