# Credits

Types:

```python
from cas_parser.types import CreditCheckResponse
```

Methods:

- <code title="post /v1/credits">client.credits.<a href="./src/cas_parser/resources/credits.py">check</a>() -> <a href="./src/cas_parser/types/credit_check_response.py">CreditCheckResponse</a></code>

# Logs

Types:

```python
from cas_parser.types import LogCreateResponse, LogGetSummaryResponse
```

Methods:

- <code title="post /v1/usage">client.logs.<a href="./src/cas_parser/resources/logs.py">create</a>(\*\*<a href="src/cas_parser/types/log_create_params.py">params</a>) -> <a href="./src/cas_parser/types/log_create_response.py">LogCreateResponse</a></code>
- <code title="post /v1/usage/summary">client.logs.<a href="./src/cas_parser/resources/logs.py">get_summary</a>(\*\*<a href="src/cas_parser/types/log_get_summary_params.py">params</a>) -> <a href="./src/cas_parser/types/log_get_summary_response.py">LogGetSummaryResponse</a></code>

# AccessToken

Types:

```python
from cas_parser.types import AccessTokenCreateResponse
```

Methods:

- <code title="post /v1/token">client.access_token.<a href="./src/cas_parser/resources/access_token.py">create</a>(\*\*<a href="src/cas_parser/types/access_token_create_params.py">params</a>) -> <a href="./src/cas_parser/types/access_token_create_response.py">AccessTokenCreateResponse</a></code>

# VerifyToken

Types:

```python
from cas_parser.types import VerifyTokenVerifyResponse
```

Methods:

- <code title="post /v1/token/verify">client.verify_token.<a href="./src/cas_parser/resources/verify_token.py">verify</a>() -> <a href="./src/cas_parser/types/verify_token_verify_response.py">VerifyTokenVerifyResponse</a></code>

# CamsKfintech

Types:

```python
from cas_parser.types import LinkedHolder, Transaction, UnifiedResponse
```

Methods:

- <code title="post /v4/cams_kfintech/parse">client.cams_kfintech.<a href="./src/cas_parser/resources/cams_kfintech.py">parse</a>(\*\*<a href="src/cas_parser/types/cams_kfintech_parse_params.py">params</a>) -> <a href="./src/cas_parser/types/unified_response.py">UnifiedResponse</a></code>

# Cdsl

Methods:

- <code title="post /v4/cdsl/parse">client.cdsl.<a href="./src/cas_parser/resources/cdsl/cdsl.py">parse_pdf</a>(\*\*<a href="src/cas_parser/types/cdsl_parse_pdf_params.py">params</a>) -> <a href="./src/cas_parser/types/unified_response.py">UnifiedResponse</a></code>

## Fetch

Types:

```python
from cas_parser.types.cdsl import FetchRequestOtpResponse, FetchVerifyOtpResponse
```

Methods:

- <code title="post /v4/cdsl/fetch">client.cdsl.fetch.<a href="./src/cas_parser/resources/cdsl/fetch.py">request_otp</a>(\*\*<a href="src/cas_parser/types/cdsl/fetch_request_otp_params.py">params</a>) -> <a href="./src/cas_parser/types/cdsl/fetch_request_otp_response.py">FetchRequestOtpResponse</a></code>
- <code title="post /v4/cdsl/fetch/{session_id}/verify">client.cdsl.fetch.<a href="./src/cas_parser/resources/cdsl/fetch.py">verify_otp</a>(session_id, \*\*<a href="src/cas_parser/types/cdsl/fetch_verify_otp_params.py">params</a>) -> <a href="./src/cas_parser/types/cdsl/fetch_verify_otp_response.py">FetchVerifyOtpResponse</a></code>

# ContractNote

Types:

```python
from cas_parser.types import ContractNoteParseResponse
```

Methods:

- <code title="post /v4/contract_note/parse">client.contract_note.<a href="./src/cas_parser/resources/contract_note.py">parse</a>(\*\*<a href="src/cas_parser/types/contract_note_parse_params.py">params</a>) -> <a href="./src/cas_parser/types/contract_note_parse_response.py">ContractNoteParseResponse</a></code>

# Inbox

Types:

```python
from cas_parser.types import (
    InboxCheckConnectionStatusResponse,
    InboxConnectEmailResponse,
    InboxDisconnectEmailResponse,
    InboxListCasFilesResponse,
    InboxReadResponse,
)
```

Methods:

- <code title="post /v4/inbox/status">client.inbox.<a href="./src/cas_parser/resources/inbox.py">check_connection_status</a>() -> <a href="./src/cas_parser/types/inbox_check_connection_status_response.py">InboxCheckConnectionStatusResponse</a></code>
- <code title="post /v4/inbox/connect">client.inbox.<a href="./src/cas_parser/resources/inbox.py">connect_email</a>(\*\*<a href="src/cas_parser/types/inbox_connect_email_params.py">params</a>) -> <a href="./src/cas_parser/types/inbox_connect_email_response.py">InboxConnectEmailResponse</a></code>
- <code title="post /v4/inbox/disconnect">client.inbox.<a href="./src/cas_parser/resources/inbox.py">disconnect_email</a>() -> <a href="./src/cas_parser/types/inbox_disconnect_email_response.py">InboxDisconnectEmailResponse</a></code>
- <code title="post /v4/inbox/cas">client.inbox.<a href="./src/cas_parser/resources/inbox.py">list_cas_files</a>(\*\*<a href="src/cas_parser/types/inbox_list_cas_files_params.py">params</a>) -> <a href="./src/cas_parser/types/inbox_list_cas_files_response.py">InboxListCasFilesResponse</a></code>
- <code title="post /v4/inbox/read">client.inbox.<a href="./src/cas_parser/resources/inbox.py">read</a>(\*\*<a href="src/cas_parser/types/inbox_read_params.py">params</a>) -> <a href="./src/cas_parser/types/inbox_read_response.py">InboxReadResponse</a></code>

# Nsdl

Methods:

- <code title="post /v4/nsdl/parse">client.nsdl.<a href="./src/cas_parser/resources/nsdl.py">parse</a>(\*\*<a href="src/cas_parser/types/nsdl_parse_params.py">params</a>) -> <a href="./src/cas_parser/types/unified_response.py">UnifiedResponse</a></code>

# Smart

Methods:

- <code title="post /v4/smart/parse">client.smart.<a href="./src/cas_parser/resources/smart.py">parse_cas_pdf</a>(\*\*<a href="src/cas_parser/types/smart_parse_cas_pdf_params.py">params</a>) -> <a href="./src/cas_parser/types/unified_response.py">UnifiedResponse</a></code>

# InboundEmail

Types:

```python
from cas_parser.types import (
    InboundEmailCreateResponse,
    InboundEmailRetrieveResponse,
    InboundEmailListResponse,
    InboundEmailDeleteResponse,
    InboundEmailListFilesResponse,
)
```

Methods:

- <code title="post /v4/inbound-email">client.inbound_email.<a href="./src/cas_parser/resources/inbound_email.py">create</a>(\*\*<a href="src/cas_parser/types/inbound_email_create_params.py">params</a>) -> <a href="./src/cas_parser/types/inbound_email_create_response.py">InboundEmailCreateResponse</a></code>
- <code title="get /v4/inbound-email/{inbound_email_id}">client.inbound_email.<a href="./src/cas_parser/resources/inbound_email.py">retrieve</a>(inbound_email_id) -> <a href="./src/cas_parser/types/inbound_email_retrieve_response.py">InboundEmailRetrieveResponse</a></code>
- <code title="get /v4/inbound-email">client.inbound_email.<a href="./src/cas_parser/resources/inbound_email.py">list</a>(\*\*<a href="src/cas_parser/types/inbound_email_list_params.py">params</a>) -> <a href="./src/cas_parser/types/inbound_email_list_response.py">InboundEmailListResponse</a></code>
- <code title="delete /v4/inbound-email/{inbound_email_id}">client.inbound_email.<a href="./src/cas_parser/resources/inbound_email.py">delete</a>(inbound_email_id) -> <a href="./src/cas_parser/types/inbound_email_delete_response.py">InboundEmailDeleteResponse</a></code>
- <code title="get /v4/inbound-email/{inbound_email_id}/files">client.inbound_email.<a href="./src/cas_parser/resources/inbound_email.py">list_files</a>(inbound_email_id, \*\*<a href="src/cas_parser/types/inbound_email_list_files_params.py">params</a>) -> <a href="./src/cas_parser/types/inbound_email_list_files_response.py">InboundEmailListFilesResponse</a></code>

# AgentAuth

Types:

```python
from cas_parser.types import AgentAuthPollResponse, AgentAuthApproveResponse
```

Methods:

- <code title="get /v1/agent-auth/token/{token}">client.agent_auth.<a href="./src/cas_parser/resources/agent_auth.py">poll</a>(token) -> <a href="./src/cas_parser/types/agent_auth_poll_response.py">AgentAuthPollResponse</a></code>
- <code title="post /v1/agent-auth/token/{token}/approve">client.agent_auth.<a href="./src/cas_parser/resources/agent_auth.py">approve</a>(token, \*\*<a href="src/cas_parser/types/agent_auth_approve_params.py">params</a>) -> <a href="./src/cas_parser/types/agent_auth_approve_response.py">AgentAuthApproveResponse</a></code>

# Kyc

Types:

```python
from cas_parser.types import KycLookupDigilockerAccountResponse, KycStartDigilockerSessionResponse, KycGetDigilockerResultResponse, KycCheckPanStatusResponse
```

Methods:

- <code title="post /v1/kyc/digilocker/account-lookup">client.kyc.<a href="./src/cas_parser/resources/kyc.py">lookup_digilocker_account</a>(\*\*<a href="src/cas_parser/types/kyc_lookup_digilocker_account_params.py">params</a>) -> <a href="./src/cas_parser/types/kyc_lookup_digilocker_account_response.py">KycLookupDigilockerAccountResponse</a></code>
- <code title="post /v1/kyc/digilocker/session">client.kyc.<a href="./src/cas_parser/resources/kyc.py">start_digilocker_session</a>(\*\*<a href="src/cas_parser/types/kyc_start_digilocker_session_params.py">params</a>) -> <a href="./src/cas_parser/types/kyc_start_digilocker_session_response.py">KycStartDigilockerSessionResponse</a></code>
- <code title="post /v1/kyc/digilocker/result/{session_id}">client.kyc.<a href="./src/cas_parser/resources/kyc.py">get_digilocker_result</a>(session_id, \*\*<a href="src/cas_parser/types/kyc_get_digilocker_result_params.py">params</a>) -> <a href="./src/cas_parser/types/kyc_get_digilocker_result_response.py">KycGetDigilockerResultResponse</a></code>
- <code title="post /v1/kyc/pan/status">client.kyc.<a href="./src/cas_parser/resources/kyc.py">check_pan_status</a>(\*\*<a href="src/cas_parser/types/kyc_check_pan_status_params.py">params</a>) -> <a href="./src/cas_parser/types/kyc_check_pan_status_response.py">KycCheckPanStatusResponse</a></code>

# Verification

Types:

```python
from cas_parser.types import VerificationVerifyMfdResponse, VerificationVerifySebiResponse
```

Methods:

- <code title="post /v1/verify/mfd">client.verification.<a href="./src/cas_parser/resources/verification.py">verify_mfd</a>(\*\*<a href="src/cas_parser/types/verification_verify_mfd_params.py">params</a>) -> <a href="./src/cas_parser/types/verification_verify_mfd_response.py">VerificationVerifyMfdResponse</a></code>
- <code title="post /v1/verify/sebi">client.verification.<a href="./src/cas_parser/resources/verification.py">verify_sebi</a>(\*\*<a href="src/cas_parser/types/verification_verify_sebi_params.py">params</a>) -> <a href="./src/cas_parser/types/verification_verify_sebi_response.py">VerificationVerifySebiResponse</a></code>

# CasGenerator

Types:

```python
from cas_parser.types import CasGeneratorGenerateCasResponse
```

Methods:

- <code title="post /v4/generate">client.cas_generator.<a href="./src/cas_parser/resources/cas_generator.py">generate_cas</a>(\*\*<a href="src/cas_parser/types/cas_generator_generate_cas_params.py">params</a>) -> <a href="./src/cas_parser/types/cas_generator_generate_cas_response.py">CasGeneratorGenerateCasResponse</a></code>
