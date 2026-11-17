# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

import datetime
from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "KycGetDigilockerResultResponse",
    "Consent",
    "Document",
    "FetchedAadhaarUnionMember0",
    "FetchedDrivingLicenceUnionMember0Category",
    "FetchedDrivingLicenceUnionMember0SignatureCertificate",
    "FetchedDrivingLicenceUnionMember0Signature",
    "FetchedDrivingLicenceUnionMember0",
    "FetchedPanUnionMember0SignatureCertificate",
    "FetchedPanUnionMember0Signature",
    "FetchedPanUnionMember0",
    "Fetched",
    "IdentityUnionMember0Verified",
    "IdentityUnionMember0",
]


class Consent(BaseModel):
    """
    Consent receipt captured at session start. Carried through the flow for
    audit (DPDP / RBI compliance).
    """

    consented_at: Optional[datetime.datetime] = None
    """ISO 8601 timestamp (UTC) when consent was captured."""

    purpose: Optional[str] = None
    """The consent_purpose provided at /session."""


class Document(BaseModel):
    """Metadata for a single issued document in the user's DigiLocker."""

    date: Optional[datetime.date] = None
    """Last modified date in DigiLocker, normalized to ISO 8601."""

    doctype: Optional[str] = None
    """5-character DigiLocker document type code"""

    issuer: Optional[str] = None

    issuerid: Optional[str] = None

    mime: Optional[List[str]] = None

    name: Optional[str] = None
    """Document name"""

    type: Optional[str] = None

    uri: Optional[str] = None
    """Unique DigiLocker identifier for the document"""


class FetchedAadhaarUnionMember0(BaseModel):
    """
    e-Aadhaar (Aadhaar Paperless Offline eKYC) data parsed from DigiLocker XML.
    Any field may be null if not present in the source XML.
    """

    address: Optional[str] = None
    """Full address assembled from the Aadhaar address fields"""

    care_of: Optional[str] = None
    """Care-of / guardian field"""

    dob: Optional[str] = None
    """Date of birth (as returned by DigiLocker, typically DD-MM-YYYY)"""

    gender: Optional[str] = None
    """Gender (M, F, or T)"""

    masked_aadhaar: Optional[str] = None
    """Masked Aadhaar number (only last 4 digits visible)"""

    name: Optional[str] = None
    """Full name as on Aadhaar"""

    photo_base64: Optional[str] = None
    """Base64-encoded photograph from the Aadhaar XML"""

    session_id: Optional[str] = None
    """DigiLocker/UIDAI reference id for this eKYC document"""


class FetchedDrivingLicenceUnionMember0Category(BaseModel):
    abbreviation: Optional[str] = None

    code: Optional[str] = None

    description: Optional[str] = None

    issue_date: Optional[datetime.date] = None


class FetchedDrivingLicenceUnionMember0SignatureCertificate(BaseModel):
    issuer: Optional[str] = None

    serial_number: Optional[str] = None

    subject: Optional[str] = None

    valid_from: Optional[datetime.datetime] = None

    valid_until: Optional[datetime.datetime] = None


class FetchedDrivingLicenceUnionMember0Signature(BaseModel):
    """
    Signature provenance for a fetched document. Reports whether a signed
    XML block with an X.509 certificate is present, plus the signing
    certificate's details. Note: this is provenance reporting, not full
    XML-DSIG cryptographic verification (the trust model is direct-from-source
    retrieval, consistent with the industry).
    """

    certificate: Optional[FetchedDrivingLicenceUnionMember0SignatureCertificate] = None

    signature_present: Optional[bool] = None


class FetchedDrivingLicenceUnionMember0(BaseModel):
    """
    Driving licence data parsed from DigiLocker XML (returned under
    `fetched.driving_licence`). Any field may be null if absent in the
    source XML.
    """

    categories: Optional[List[FetchedDrivingLicenceUnionMember0Category]] = None
    """Vehicle classes the holder is licensed for."""

    dl_number: Optional[str] = None

    dob: Optional[str] = None
    """Date of birth, normalized to ISO 8601."""

    expiry_date: Optional[datetime.date] = None

    father_name: Optional[str] = None

    gender: Optional[str] = None

    issue_date: Optional[datetime.date] = None

    issued_at: Optional[str] = None

    name: Optional[str] = None

    permanent_address: Optional[str] = None

    present_address: Optional[str] = None

    signature: Optional[FetchedDrivingLicenceUnionMember0Signature] = None
    """
    Signature provenance for a fetched document. Reports whether a signed
    XML block with an X.509 certificate is present, plus the signing
    certificate's details. Note: this is provenance reporting, not full
    XML-DSIG cryptographic verification (the trust model is direct-from-source
    retrieval, consistent with the industry).
    """

    status: Optional[str] = None

    valid_from: Optional[datetime.date] = None


class FetchedPanUnionMember0SignatureCertificate(BaseModel):
    issuer: Optional[str] = None

    serial_number: Optional[str] = None

    subject: Optional[str] = None

    valid_from: Optional[datetime.datetime] = None

    valid_until: Optional[datetime.datetime] = None


class FetchedPanUnionMember0Signature(BaseModel):
    """
    Signature provenance for a fetched document. Reports whether a signed
    XML block with an X.509 certificate is present, plus the signing
    certificate's details. Note: this is provenance reporting, not full
    XML-DSIG cryptographic verification (the trust model is direct-from-source
    retrieval, consistent with the industry).
    """

    certificate: Optional[FetchedPanUnionMember0SignatureCertificate] = None

    signature_present: Optional[bool] = None


class FetchedPanUnionMember0(BaseModel):
    """
    PAN certificate data parsed from DigiLocker XML (returned as `parsed`
    when `parse=pan`). Any field may be null if absent in the source XML.
    """

    dob: Optional[str] = None
    """Date of birth (DD-MM-YYYY as returned)"""

    father_name: Optional[str] = None
    """Father/spouse name (the `swd` field; often empty)"""

    gender: Optional[str] = None

    name: Optional[str] = None
    """PAN holder name"""

    pan: Optional[str] = None
    """PAN number"""

    signature: Optional[FetchedPanUnionMember0Signature] = None
    """
    Signature provenance for a fetched document. Reports whether a signed
    XML block with an X.509 certificate is present, plus the signing
    certificate's details. Note: this is provenance reporting, not full
    XML-DSIG cryptographic verification (the trust model is direct-from-source
    retrieval, consistent with the industry).
    """

    status: Optional[str] = None
    """Certificate status (e.g. "A" = Active)"""

    verified_on: Optional[str] = None
    """Timestamp DigiLocker verified the record"""


class Fetched(BaseModel):
    """
    Parsed documents keyed by the `fetch_documents` value
    (pan/aadhaar/driving_licence). Value is null if the document
    was requested but unavailable. Each parsed object also
    includes a `signature` block.
    """

    aadhaar: Optional[FetchedAadhaarUnionMember0] = None

    driving_licence: Optional[FetchedDrivingLicenceUnionMember0] = None

    pan: Optional[FetchedPanUnionMember0] = None


class IdentityUnionMember0Verified(BaseModel):
    """Authenticated document identifiers (keys present only when verified)."""

    aadhaar: Optional[str] = None
    """Usually masked"""

    driving_licence: Optional[str] = None

    pan: Optional[str] = None


class IdentityUnionMember0(BaseModel):
    """
    The investor's verified identity. Only fields the investor shared are
    populated. `verified` contains the authenticated document identifiers
    (e.g. PAN, Aadhaar number).
    """

    address: Optional[str] = None

    care_of: Optional[str] = None

    digilocker_id: Optional[str] = None

    dob: Optional[str] = None

    email: Optional[str] = None

    gender: Optional[str] = None

    mobile: Optional[str] = None

    name: Optional[str] = None

    username: Optional[str] = None
    """DigiLocker preferred username"""

    verified: Optional[IdentityUnionMember0Verified] = None
    """Authenticated document identifiers (keys present only when verified)."""


class KycGetDigilockerResultResponse(BaseModel):
    consent: Optional[Consent] = None
    """
    Consent receipt captured at session start. Carried through the flow for
    audit (DPDP / RBI compliance).
    """

    consented_documents: Optional[List[str]] = None
    """Friendly names of documents the user consented to share."""

    documents: Optional[List[Document]] = None

    errors: Optional[Dict[str, str]] = None
    """Per-section error codes (omitted when there are none)."""

    fetched: Optional[Fetched] = None
    """
    Parsed documents keyed by the `fetch_documents` value
    (pan/aadhaar/driving_licence). Value is null if the document
    was requested but unavailable. Each parsed object also
    includes a `signature` block.
    """

    identity: Optional[IdentityUnionMember0] = None

    status: Optional[str] = None
