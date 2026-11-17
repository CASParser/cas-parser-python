# Checks each call added from the live API description against a stubbed transport (respx).
# For every call: one request with the description's method and path, every argument sent where the description
# puts it, and the documented response parsed into the method's return type with strict validation on.

from __future__ import annotations

import json
from typing import Any, Dict, cast

import httpx
import respx
import pytest

from cas_parser import CasParser, AsyncCasParser, types
from cas_parser._models import BaseModel

base_url = "http://stub.test"

CASES: list[Dict[str, Any]] = json.loads(
    '[{"id": "agent_auth.poll", "resource": "agent_auth", "method": "poll", "http": "GET", "path": "/v1/agent-auth/token/a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2", "args": ["a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"status": "pending"}, "response_type": "AgentAuthPollResponse"}, {"id": "agent_auth.approve", "resource": "agent_auth", "method": "approve", "http": "POST", "path": "/v1/agent-auth/token/a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2/approve", "args": ["a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2a3b4c5d6a7b8c9d0e1f2"], "kwargs": {"client_name": "Claude Code", "id_token": "id_token-value"}, "body": {"client_name": "Claude Code", "id_token": "id_token-value"}, "query": {}, "headers": {}, "response": {"email": "user@example.com", "status": "approved"}, "response_type": "AgentAuthApproveResponse"}, {"id": "kyc.lookup_digilocker_account", "resource": "kyc", "method": "lookup_digilocker_account", "http": "POST", "path": "/v1/kyc/digilocker/account-lookup", "args": [], "kwargs": {"aadhaar_number": "123456789012", "mobile": "9876543210", "reference_id": "reference_id-value"}, "body": {"aadhaar_number": "123456789012", "mobile": "9876543210", "reference_id": "reference_id-value"}, "query": {}, "headers": {}, "response": {"digilocker_id": "digilocker_id-value", "next_step": {"action": "start_session", "endpoint": "POST /v1/kyc/digilocker/session", "message": "message-value"}, "reference_id": "reference_id-value", "registered": true, "status": "success", "suggested_user_flow": "signin"}, "response_type": "KycLookupDigilockerAccountResponse"}, {"id": "kyc.start_digilocker_session", "resource": "kyc", "method": "start_digilocker_session", "http": "POST", "path": "/v1/kyc/digilocker/session", "args": [], "kwargs": {"consent": true, "consent_purpose": "KYC for loan account opening", "documents": ["aadhaar", "pan"], "prefill_mobile": "9999999999", "redirect_url": "https://yourapp.com/digilocker/callback", "state": "investor_42", "user_flow": "signin"}, "body": {"consent": true, "consent_purpose": "KYC for loan account opening", "documents": ["aadhaar", "pan"], "prefill_mobile": "9999999999", "redirect_url": "https://yourapp.com/digilocker/callback", "state": "investor_42", "user_flow": "signin"}, "query": {}, "headers": {}, "response": {"authorization_url": "authorization_url-value", "expires_in": 600, "session_id": "3f9a2c1e8b7d4e6fa1c2d3e4f5a6b7c8", "status": "success"}, "response_type": "KycStartDigilockerSessionResponse"}, {"id": "kyc.get_digilocker_result", "resource": "kyc", "method": "get_digilocker_result", "http": "POST", "path": "/v1/kyc/digilocker/result/session_id-value", "args": ["session_id-value"], "kwargs": {"fetch_documents": ["pan", "driving_licence"], "include_documents": true}, "body": {"fetch_documents": ["pan", "driving_licence"], "include_documents": true}, "query": {}, "headers": {}, "response": {"consent": {"consented_at": "2026-05-30T22:37:17+00:00", "purpose": "KYC for loan account opening"}, "consented_documents": ["pan", "driving_licence"], "documents": [{"date": "2024-09-19", "doctype": "PANCR", "issuer": "Income Tax Department", "issuerid": "in.gov.pan", "mime": ["application/pdf", "application/xml"], "name": "PAN Verification Record", "type": "file", "uri": "in.gov.pan-PANCR-xxxxxxxxxxxx"}], "errors": {}, "fetched": {"aadhaar": {"address": "12, MG Road, Indiranagar, Bengaluru, Karnataka, 560038, India", "care_of": "S/O Rajesh Sharma", "dob": "16-05-1990", "gender": "F", "masked_aadhaar": "XXXXXXXX1234", "name": "Anjali Sharma", "photo_base64": "photo_base64-value", "session_id": "session_id-value"}, "driving_licence": {"categories": [{"abbreviation": "abbreviation-value", "code": "code-value", "description": "description-value", "issue_date": "2026-01-15"}], "dl_number": "KA0120190008989", "dob": "1995-03-22", "expiry_date": "2026-01-15", "father_name": "Suresh Sharma", "gender": "M", "issue_date": "2026-01-15", "issued_at": "RTO, Bengaluru", "name": "Rahul Sharma", "permanent_address": "permanent_address-value", "present_address": "present_address-value", "signature": {"certificate": {"issuer": "issuer-value", "serial_number": "serial_number-value", "subject": "C=IN,O=DIGITAL INDIA CORPORATION,CN=DS DIGITAL INDIA CORPORATION", "valid_from": "2026-01-15T10:00:00+00:00", "valid_until": "2026-01-15T10:00:00+00:00"}, "signature_present": true}, "status": "A", "valid_from": "2026-01-15"}, "pan": {"dob": "22-03-1995", "father_name": null, "gender": "MALE", "name": "RAHUL SHARMA", "pan": "ABCPD1234E", "signature": {"certificate": {"issuer": "issuer-value", "serial_number": "serial_number-value", "subject": "C=IN,O=DIGITAL INDIA CORPORATION,CN=DS DIGITAL INDIA CORPORATION", "valid_from": "2026-01-15T10:00:00+00:00", "valid_until": "2026-01-15T10:00:00+00:00"}, "signature_present": true}, "status": "A", "verified_on": "31-05-2026 03:55:02"}}, "identity": {"address": "address-value", "care_of": "S/O Rajesh Sharma", "digilocker_id": "rahul22031995", "dob": "1990-05-16", "email": "anjali@example.com", "gender": "F", "mobile": "98XXXXXX10", "name": "Anjali Sharma", "username": "rahul22031995", "verified": {"aadhaar": "XXXXXXXX1234", "driving_licence": "KA01-20110012345", "pan": "ABCDE1234F"}}, "status": "success"}, "response_type": "KycGetDigilockerResultResponse"}, {"id": "kyc.check_pan_status", "resource": "kyc", "method": "check_pan_status", "http": "POST", "path": "/v1/kyc/pan/status", "args": [], "kwargs": {"pan_no": "ABCDE1234F"}, "body": {"pan_no": "ABCDE1234F"}, "query": {}, "headers": {}, "response": {"active_kra": "cvl", "kras": {"cams": {"kyc_mode": null, "last_updated_on": null, "raw_status": null, "registered_on": null, "remarks": null, "status": "not_checked"}, "cvl": {"kyc_mode": "normal", "last_updated_on": "2026-04-25", "raw_status": "ON HOLD - New KYC", "registered_on": "2026-04-24", "remarks": "APPLICANT PHOTO MISMATCH IN THE APPLICATION,FATCA NOT APPLICABLE", "status": "on_hold"}, "karvy": {"kyc_mode": null, "last_updated_on": null, "raw_status": null, "registered_on": null, "remarks": null, "status": "not_checked"}, "kfin": {"kyc_mode": null, "last_updated_on": null, "raw_status": null, "registered_on": null, "remarks": null, "status": "not_checked"}, "ndml": {"kyc_mode": null, "last_updated_on": null, "raw_status": null, "registered_on": null, "remarks": null, "status": "not_available"}}, "kyc_compliant": false, "kyc_mode": "normal", "kyc_status": "on_hold", "last_updated_on": "2026-04-25", "pan": "XYZPQ9876R", "registered_on": "2026-04-24", "status": "success"}, "response_type": "KycCheckPanStatusResponse"}, {"id": "verification.verify_mfd", "resource": "verification", "method": "verify_mfd", "http": "POST", "path": "/v1/verify/mfd", "args": [], "kwargs": {"arn": "123456"}, "body": {"arn": "123456"}, "query": {}, "headers": {}, "response": {"address": "MG Road, Bengaluru, Karnataka", "arn": "123456", "authority": "AMFI", "category": "mutual-fund-distributor", "category_label": "Mutual Fund Distributor (ARN)", "euin": "E123456", "is_perpetual": false, "kyd_compliant": true, "name": "Example Wealth Distributors LLP", "negative_list": null, "negative_list_hit": false, "pincode": "560001", "registration_status": "ACTIVE", "status": "success", "valid_from": "2024-04-01", "valid_till": "2027-03-31", "verified": true}, "response_type": "VerificationVerifyMfdResponse"}, {"id": "verification.verify_sebi", "resource": "verification", "method": "verify_sebi", "http": "POST", "path": "/v1/verify/sebi", "args": [], "kwargs": {"name": "Motilal Oswal", "registration_number": "INP000000670", "type": "portfolio-manager"}, "body": {"name": "Motilal Oswal", "registration_number": "INP000000670", "type": "portfolio-manager"}, "query": {}, "headers": {}, "response": {"address": "10th Floor, Motilal Oswal Tower, Prabhadevi, MUMBAI, MAHARASHTRA, 400025", "authority": "SEBI", "category": "portfolio-manager", "category_label": "Portfolio Manager (PMS)", "contact_person": null, "detected_by": "registration_number", "email": null, "is_perpetual": true, "name": "MOTILAL OSWAL ASSET MANAGEMENT COMPANY LIMITED", "registration_number": "INP000000670", "registration_status": "ACTIVE", "status": "success", "telephone": null, "valid_from": "2014-09-16", "valid_till": null, "verified": true}, "response_type": "VerificationVerifySebiResponse"}, {"id": "cas_generator.generate_cas", "resource": "cas_generator", "method": "generate_cas", "http": "POST", "path": "/v4/generate", "args": [], "kwargs": {"cas_authority": "cams", "email": "user@example.com", "from_date": "2023-01-01", "pan_no": "ABCDE1234F", "password": "Abcdefghi12$", "to_date": "2023-12-31"}, "body": {"cas_authority": "cams", "email": "user@example.com", "from_date": "2023-01-01", "pan_no": "ABCDE1234F", "password": "Abcdefghi12$", "to_date": "2023-12-31"}, "query": {}, "headers": {}, "response": {"msg": "CAS request submitted. Check email shortly.", "status": "success"}, "response_type": "CasGeneratorGenerateCasResponse"}, {"id": "inbox.read", "resource": "inbox", "method": "read", "http": "POST", "path": "/v4/inbox/read", "args": [], "kwargs": {"x_inbox_token": "x-inbox-token-value", "categories": ["credit"], "document_types": ["card_statement"], "end_date": "2026-10-31", "include_body": true, "senders": ["estatement@examplebank.in"], "sources": ["hdfc_credit_card", "axis_credit_card"], "start_date": "2026-08-01"}, "body": {"categories": ["credit"], "document_types": ["card_statement"], "end_date": "2026-10-31", "include_body": true, "senders": ["estatement@examplebank.in"], "sources": ["hdfc_credit_card", "axis_credit_card"], "start_date": "2026-08-01"}, "query": {}, "headers": {"x-inbox-token": "x-inbox-token-value"}, "response": {"count": 3, "failures": 0, "messages": [{"attachments": [{"attachment_url": "attachment_url-value", "content_type": "application/pdf", "filename": "hdfc_credit_card_20261012_a1b2c3d4e5f6.pdf", "original_filename": "Infinia_Statement_Oct2026.pdf", "size": 245000}], "body": {"html": "html-value", "text": "text-value"}, "category": "credit", "document_type": "card_statement", "institution": "HDFC Bank", "message_date": "2026-10-12", "message_id": "18d4a2b3c4d5e6f7", "sender_email": "emailstatements.cards@hdfcbank.net", "sender_verified": true, "source": "hdfc_credit_card", "subject": "Your HDFC Bank Credit Card Statement for October 2026"}], "status": "success", "truncated": false}, "response_type": "InboxReadResponse"}, {"id": "inbound_email.list_files", "resource": "inbound_email", "method": "list_files", "http": "GET", "path": "/v4/inbound-email/inbound_email_id-value/files", "args": ["inbound_email_id-value"], "kwargs": {"since": "2026-01-15T10:00:00+00:00", "limit": 1}, "body": {}, "query": {"since": "2026-01-15T10:00:00+00:00", "limit": "1"}, "headers": {}, "response": {"count": 1, "cursor": "2025-02-21T10:45:12.000123+00:00", "files": [{"cas_type": "cdsl", "expires_in": 86400, "filename": "cdsl_20250115_a1b2c3d4.pdf", "message_date": "2025-01-15", "message_id": "18d4a2b3c4d5e6f7", "original_filename": "CDSL_CAS_Statement.pdf", "sender_email": "eCAS@cdslstatement.com", "size": 245000, "url": "https://cdn.casparser.in/email-cas/user123/cdsl_20250115_a1b2c3d4.pdf", "received_at": "2025-02-21T10:45:12.000123+00:00"}], "status": "success"}, "response_type": "InboundEmailListFilesResponse"}]'
)


def _check_request(route: respx.Route, case: Dict[str, Any]) -> None:
    assert route.call_count == 1
    request = cast(httpx.Request, route.calls[0].request)  # pyright: ignore[reportUnknownMemberType]
    assert request.method == case["http"]
    assert request.url.path == case["path"]
    if case["body"]:
        sent = json.loads(request.content or b"{}")
        for key, expected in case["body"].items():
            assert sent.get(key) == expected, key
    for key, expected in case["query"].items():
        assert str(request.url.params.get(key)).lower() == expected.lower(), key
    for key, expected in case["headers"].items():
        assert request.headers.get(key) == expected, key


def _check_response(result: Any, case: Dict[str, Any]) -> None:
    expected = case["response"]
    if isinstance(result, BaseModel):
        # every field of the documented response came back, under its wire name
        assert set(result.to_dict(use_api_names=True).keys()) == set(expected.keys())
    elif isinstance(expected, str):
        # a string response comes back as the response body's text, as the existing string methods do
        assert result == json.dumps(expected)
    else:
        # a list or map response is returned as parsed
        assert result == expected
    expected_type = getattr(types, case["response_type"])
    if isinstance(expected_type, type):
        assert isinstance(result, expected_type)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
def test_added_call_sync(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(200, json=case["response"])
    )
    client = CasParser(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = method(*case["args"], **case["kwargs"])
    _check_request(route, case)
    _check_response(result, case)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
async def test_added_call_async(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(200, json=case["response"])
    )
    client = AsyncCasParser(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = await method(*case["args"], **case["kwargs"])
    _check_request(route, case)
    _check_response(result, case)
