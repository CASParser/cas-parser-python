# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, CasParserError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import cdsl, nsdl, inbox, smart, kfintech, cams_kfintech, contract_note
    from .resources.nsdl import NsdlResource, AsyncNsdlResource
    from .resources.inbox import InboxResource, AsyncInboxResource
    from .resources.smart import SmartResource, AsyncSmartResource
    from .resources.kfintech import KfintechResource, AsyncKfintechResource
    from .resources.cdsl.cdsl import CdslResource, AsyncCdslResource
    from .resources.cams_kfintech import CamsKfintechResource, AsyncCamsKfintechResource
    from .resources.contract_note import ContractNoteResource, AsyncContractNoteResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "CasParser",
    "AsyncCasParser",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://portfolio-parser.api.casparser.in",
    "environment_1": "https://client-apis.casparser.in",
    "environment_2": "http://localhost:5000",
}


class CasParser(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous CasParser client instance.

        This automatically infers the `api_key` argument from the `CAS_PARSER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CAS_PARSER_API_KEY")
        if api_key is None:
            raise CasParserError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CAS_PARSER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("CAS_PARSER_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CAS_PARSER_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def cams_kfintech(self) -> CamsKfintechResource:
        from .resources.cams_kfintech import CamsKfintechResource

        return CamsKfintechResource(self)

    @cached_property
    def cdsl(self) -> CdslResource:
        from .resources.cdsl import CdslResource

        return CdslResource(self)

    @cached_property
    def contract_note(self) -> ContractNoteResource:
        from .resources.contract_note import ContractNoteResource

        return ContractNoteResource(self)

    @cached_property
    def inbox(self) -> InboxResource:
        from .resources.inbox import InboxResource

        return InboxResource(self)

    @cached_property
    def kfintech(self) -> KfintechResource:
        from .resources.kfintech import KfintechResource

        return KfintechResource(self)

    @cached_property
    def nsdl(self) -> NsdlResource:
        from .resources.nsdl import NsdlResource

        return NsdlResource(self)

    @cached_property
    def smart(self) -> SmartResource:
        from .resources.smart import SmartResource

        return SmartResource(self)

    @cached_property
    def with_raw_response(self) -> CasParserWithRawResponse:
        return CasParserWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasParserWithStreamedResponse:
        return CasParserWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCasParser(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCasParser client instance.

        This automatically infers the `api_key` argument from the `CAS_PARSER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CAS_PARSER_API_KEY")
        if api_key is None:
            raise CasParserError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CAS_PARSER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("CAS_PARSER_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CAS_PARSER_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def cams_kfintech(self) -> AsyncCamsKfintechResource:
        from .resources.cams_kfintech import AsyncCamsKfintechResource

        return AsyncCamsKfintechResource(self)

    @cached_property
    def cdsl(self) -> AsyncCdslResource:
        from .resources.cdsl import AsyncCdslResource

        return AsyncCdslResource(self)

    @cached_property
    def contract_note(self) -> AsyncContractNoteResource:
        from .resources.contract_note import AsyncContractNoteResource

        return AsyncContractNoteResource(self)

    @cached_property
    def inbox(self) -> AsyncInboxResource:
        from .resources.inbox import AsyncInboxResource

        return AsyncInboxResource(self)

    @cached_property
    def kfintech(self) -> AsyncKfintechResource:
        from .resources.kfintech import AsyncKfintechResource

        return AsyncKfintechResource(self)

    @cached_property
    def nsdl(self) -> AsyncNsdlResource:
        from .resources.nsdl import AsyncNsdlResource

        return AsyncNsdlResource(self)

    @cached_property
    def smart(self) -> AsyncSmartResource:
        from .resources.smart import AsyncSmartResource

        return AsyncSmartResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCasParserWithRawResponse:
        return AsyncCasParserWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasParserWithStreamedResponse:
        return AsyncCasParserWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CasParserWithRawResponse:
    _client: CasParser

    def __init__(self, client: CasParser) -> None:
        self._client = client

    @cached_property
    def cams_kfintech(self) -> cams_kfintech.CamsKfintechResourceWithRawResponse:
        from .resources.cams_kfintech import CamsKfintechResourceWithRawResponse

        return CamsKfintechResourceWithRawResponse(self._client.cams_kfintech)

    @cached_property
    def cdsl(self) -> cdsl.CdslResourceWithRawResponse:
        from .resources.cdsl import CdslResourceWithRawResponse

        return CdslResourceWithRawResponse(self._client.cdsl)

    @cached_property
    def contract_note(self) -> contract_note.ContractNoteResourceWithRawResponse:
        from .resources.contract_note import ContractNoteResourceWithRawResponse

        return ContractNoteResourceWithRawResponse(self._client.contract_note)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithRawResponse:
        from .resources.inbox import InboxResourceWithRawResponse

        return InboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def kfintech(self) -> kfintech.KfintechResourceWithRawResponse:
        from .resources.kfintech import KfintechResourceWithRawResponse

        return KfintechResourceWithRawResponse(self._client.kfintech)

    @cached_property
    def nsdl(self) -> nsdl.NsdlResourceWithRawResponse:
        from .resources.nsdl import NsdlResourceWithRawResponse

        return NsdlResourceWithRawResponse(self._client.nsdl)

    @cached_property
    def smart(self) -> smart.SmartResourceWithRawResponse:
        from .resources.smart import SmartResourceWithRawResponse

        return SmartResourceWithRawResponse(self._client.smart)


class AsyncCasParserWithRawResponse:
    _client: AsyncCasParser

    def __init__(self, client: AsyncCasParser) -> None:
        self._client = client

    @cached_property
    def cams_kfintech(self) -> cams_kfintech.AsyncCamsKfintechResourceWithRawResponse:
        from .resources.cams_kfintech import AsyncCamsKfintechResourceWithRawResponse

        return AsyncCamsKfintechResourceWithRawResponse(self._client.cams_kfintech)

    @cached_property
    def cdsl(self) -> cdsl.AsyncCdslResourceWithRawResponse:
        from .resources.cdsl import AsyncCdslResourceWithRawResponse

        return AsyncCdslResourceWithRawResponse(self._client.cdsl)

    @cached_property
    def contract_note(self) -> contract_note.AsyncContractNoteResourceWithRawResponse:
        from .resources.contract_note import AsyncContractNoteResourceWithRawResponse

        return AsyncContractNoteResourceWithRawResponse(self._client.contract_note)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithRawResponse:
        from .resources.inbox import AsyncInboxResourceWithRawResponse

        return AsyncInboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def kfintech(self) -> kfintech.AsyncKfintechResourceWithRawResponse:
        from .resources.kfintech import AsyncKfintechResourceWithRawResponse

        return AsyncKfintechResourceWithRawResponse(self._client.kfintech)

    @cached_property
    def nsdl(self) -> nsdl.AsyncNsdlResourceWithRawResponse:
        from .resources.nsdl import AsyncNsdlResourceWithRawResponse

        return AsyncNsdlResourceWithRawResponse(self._client.nsdl)

    @cached_property
    def smart(self) -> smart.AsyncSmartResourceWithRawResponse:
        from .resources.smart import AsyncSmartResourceWithRawResponse

        return AsyncSmartResourceWithRawResponse(self._client.smart)


class CasParserWithStreamedResponse:
    _client: CasParser

    def __init__(self, client: CasParser) -> None:
        self._client = client

    @cached_property
    def cams_kfintech(self) -> cams_kfintech.CamsKfintechResourceWithStreamingResponse:
        from .resources.cams_kfintech import CamsKfintechResourceWithStreamingResponse

        return CamsKfintechResourceWithStreamingResponse(self._client.cams_kfintech)

    @cached_property
    def cdsl(self) -> cdsl.CdslResourceWithStreamingResponse:
        from .resources.cdsl import CdslResourceWithStreamingResponse

        return CdslResourceWithStreamingResponse(self._client.cdsl)

    @cached_property
    def contract_note(self) -> contract_note.ContractNoteResourceWithStreamingResponse:
        from .resources.contract_note import ContractNoteResourceWithStreamingResponse

        return ContractNoteResourceWithStreamingResponse(self._client.contract_note)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithStreamingResponse:
        from .resources.inbox import InboxResourceWithStreamingResponse

        return InboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def kfintech(self) -> kfintech.KfintechResourceWithStreamingResponse:
        from .resources.kfintech import KfintechResourceWithStreamingResponse

        return KfintechResourceWithStreamingResponse(self._client.kfintech)

    @cached_property
    def nsdl(self) -> nsdl.NsdlResourceWithStreamingResponse:
        from .resources.nsdl import NsdlResourceWithStreamingResponse

        return NsdlResourceWithStreamingResponse(self._client.nsdl)

    @cached_property
    def smart(self) -> smart.SmartResourceWithStreamingResponse:
        from .resources.smart import SmartResourceWithStreamingResponse

        return SmartResourceWithStreamingResponse(self._client.smart)


class AsyncCasParserWithStreamedResponse:
    _client: AsyncCasParser

    def __init__(self, client: AsyncCasParser) -> None:
        self._client = client

    @cached_property
    def cams_kfintech(self) -> cams_kfintech.AsyncCamsKfintechResourceWithStreamingResponse:
        from .resources.cams_kfintech import AsyncCamsKfintechResourceWithStreamingResponse

        return AsyncCamsKfintechResourceWithStreamingResponse(self._client.cams_kfintech)

    @cached_property
    def cdsl(self) -> cdsl.AsyncCdslResourceWithStreamingResponse:
        from .resources.cdsl import AsyncCdslResourceWithStreamingResponse

        return AsyncCdslResourceWithStreamingResponse(self._client.cdsl)

    @cached_property
    def contract_note(self) -> contract_note.AsyncContractNoteResourceWithStreamingResponse:
        from .resources.contract_note import AsyncContractNoteResourceWithStreamingResponse

        return AsyncContractNoteResourceWithStreamingResponse(self._client.contract_note)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithStreamingResponse:
        from .resources.inbox import AsyncInboxResourceWithStreamingResponse

        return AsyncInboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def kfintech(self) -> kfintech.AsyncKfintechResourceWithStreamingResponse:
        from .resources.kfintech import AsyncKfintechResourceWithStreamingResponse

        return AsyncKfintechResourceWithStreamingResponse(self._client.kfintech)

    @cached_property
    def nsdl(self) -> nsdl.AsyncNsdlResourceWithStreamingResponse:
        from .resources.nsdl import AsyncNsdlResourceWithStreamingResponse

        return AsyncNsdlResourceWithStreamingResponse(self._client.nsdl)

    @cached_property
    def smart(self) -> smart.AsyncSmartResourceWithStreamingResponse:
        from .resources.smart import AsyncSmartResourceWithStreamingResponse

        return AsyncSmartResourceWithStreamingResponse(self._client.smart)


Client = CasParser

AsyncClient = AsyncCasParser
