# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transaction import Transaction
from .linked_holder import LinkedHolder

__all__ = [
    "UnifiedResponse",
    "DematAccount",
    "DematAccountAdditionalInfo",
    "DematAccountHoldings",
    "DematAccountHoldingsAif",
    "DematAccountHoldingsAifAdditionalInfo",
    "DematAccountHoldingsCorporateBond",
    "DematAccountHoldingsCorporateBondAdditionalInfo",
    "DematAccountHoldingsDematMutualFund",
    "DematAccountHoldingsDematMutualFundAdditionalInfo",
    "DematAccountHoldingsEquity",
    "DematAccountHoldingsEquityAdditionalInfo",
    "DematAccountHoldingsGovernmentSecurity",
    "DematAccountHoldingsGovernmentSecurityAdditionalInfo",
    "Insurance",
    "InsuranceLifeInsurancePolicy",
    "Investor",
    "Meta",
    "MetaStatementPeriod",
    "MutualFund",
    "MutualFundAdditionalInfo",
    "MutualFundScheme",
    "MutualFundSchemeAdditionalInfo",
    "MutualFundSchemeGain",
    "Np",
    "NpFund",
    "NpFundAdditionalInfo",
    "Summary",
    "SummaryAccounts",
    "SummaryAccountsDemat",
    "SummaryAccountsInsurance",
    "SummaryAccountsMutualFunds",
    "SummaryAccountsNps",
]


class DematAccountAdditionalInfo(BaseModel):
    """Additional information specific to the demat account type"""

    bo_status: Optional[str] = None
    """Beneficiary Owner status (CDSL)"""

    bo_sub_status: Optional[str] = None
    """Beneficiary Owner sub-status (CDSL)"""

    bo_type: Optional[str] = None
    """Beneficiary Owner type (CDSL)"""

    bsda: Optional[str] = None
    """Basic Services Demat Account status (CDSL)"""

    email: Optional[str] = None
    """Email associated with the demat account (CDSL)"""

    linked_pans: Optional[List[str]] = None
    """List of linked PAN numbers (NSDL)"""

    nominee: Optional[str] = None
    """Nominee details (CDSL)"""

    status: Optional[str] = None
    """Account status (CDSL)"""


class DematAccountHoldingsAifAdditionalInfo(BaseModel):
    """Additional information specific to the AIF"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period (beta)"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period (beta)"""


class DematAccountHoldingsAif(BaseModel):
    additional_info: Optional[DematAccountHoldingsAifAdditionalInfo] = None
    """Additional information specific to the AIF"""

    isin: Optional[str] = None
    """ISIN code of the AIF"""

    name: Optional[str] = None
    """Name of the AIF"""

    transactions: Optional[List[Transaction]] = None
    """List of transactions for this holding (beta)"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class DematAccountHoldingsCorporateBondAdditionalInfo(BaseModel):
    """Additional information specific to the corporate bond"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period (beta)"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period (beta)"""


class DematAccountHoldingsCorporateBond(BaseModel):
    additional_info: Optional[DematAccountHoldingsCorporateBondAdditionalInfo] = None
    """Additional information specific to the corporate bond"""

    isin: Optional[str] = None
    """ISIN code of the corporate bond"""

    name: Optional[str] = None
    """Name of the corporate bond"""

    transactions: Optional[List[Transaction]] = None
    """List of transactions for this holding (beta)"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class DematAccountHoldingsDematMutualFundAdditionalInfo(BaseModel):
    """Additional information specific to the mutual fund"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period (beta)"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period (beta)"""


class DematAccountHoldingsDematMutualFund(BaseModel):
    additional_info: Optional[DematAccountHoldingsDematMutualFundAdditionalInfo] = None
    """Additional information specific to the mutual fund"""

    isin: Optional[str] = None
    """ISIN code of the mutual fund"""

    name: Optional[str] = None
    """Name of the mutual fund"""

    transactions: Optional[List[Transaction]] = None
    """List of transactions for this holding (beta)"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class DematAccountHoldingsEquityAdditionalInfo(BaseModel):
    """Additional information specific to the equity"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period (beta)"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period (beta)"""


class DematAccountHoldingsEquity(BaseModel):
    additional_info: Optional[DematAccountHoldingsEquityAdditionalInfo] = None
    """Additional information specific to the equity"""

    isin: Optional[str] = None
    """ISIN code of the equity"""

    name: Optional[str] = None
    """Name of the equity"""

    transactions: Optional[List[Transaction]] = None
    """List of transactions for this holding (beta)"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class DematAccountHoldingsGovernmentSecurityAdditionalInfo(BaseModel):
    """Additional information specific to the government security"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period (beta)"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period (beta)"""


class DematAccountHoldingsGovernmentSecurity(BaseModel):
    additional_info: Optional[DematAccountHoldingsGovernmentSecurityAdditionalInfo] = None
    """Additional information specific to the government security"""

    isin: Optional[str] = None
    """ISIN code of the government security"""

    name: Optional[str] = None
    """Name of the government security"""

    transactions: Optional[List[Transaction]] = None
    """List of transactions for this holding (beta)"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class DematAccountHoldings(BaseModel):
    aifs: Optional[List[DematAccountHoldingsAif]] = None

    corporate_bonds: Optional[List[DematAccountHoldingsCorporateBond]] = None

    demat_mutual_funds: Optional[List[DematAccountHoldingsDematMutualFund]] = None

    equities: Optional[List[DematAccountHoldingsEquity]] = None

    government_securities: Optional[List[DematAccountHoldingsGovernmentSecurity]] = None


class DematAccount(BaseModel):
    additional_info: Optional[DematAccountAdditionalInfo] = None
    """Additional information specific to the demat account type"""

    bo_id: Optional[str] = None
    """Beneficiary Owner ID (primarily for CDSL)"""

    client_id: Optional[str] = None
    """Client ID"""

    demat_type: Optional[Literal["NSDL", "CDSL"]] = None
    """Type of demat account"""

    dp_id: Optional[str] = None
    """Depository Participant ID"""

    dp_name: Optional[str] = None
    """Depository Participant name"""

    holdings: Optional[DematAccountHoldings] = None

    linked_holders: Optional[List[LinkedHolder]] = None
    """List of account holders linked to this demat account"""

    value: Optional[float] = None
    """Total value of the demat account"""


class InsuranceLifeInsurancePolicy(BaseModel):
    additional_info: Optional[object] = None
    """Additional information specific to the policy"""

    life_assured: Optional[str] = None
    """Name of the life assured"""

    policy_name: Optional[str] = None
    """Name of the insurance policy"""

    policy_number: Optional[str] = None
    """Insurance policy number"""

    premium_amount: Optional[float] = None
    """Premium amount"""

    premium_frequency: Optional[str] = None
    """Frequency of premium payment (e.g., Annual, Monthly)"""

    provider: Optional[str] = None
    """Insurance company name"""

    status: Optional[str] = None
    """Status of the policy (e.g., Active, Lapsed)"""

    sum_assured: Optional[float] = None
    """Sum assured amount"""


class Insurance(BaseModel):
    life_insurance_policies: Optional[List[InsuranceLifeInsurancePolicy]] = None


class Investor(BaseModel):
    address: Optional[str] = None
    """Address of the investor"""

    cas_id: Optional[str] = None
    """CAS ID of the investor (only for NSDL and CDSL)"""

    email: Optional[str] = None
    """Email address of the investor"""

    mobile: Optional[str] = None
    """Mobile number of the investor"""

    name: Optional[str] = None
    """Name of the investor"""

    pan: Optional[str] = None
    """PAN (Permanent Account Number) of the investor"""

    pincode: Optional[str] = None
    """Postal code of the investor's address"""


class MetaStatementPeriod(BaseModel):
    from_: Optional[date] = FieldInfo(alias="from", default=None)
    """Start date of the statement period"""

    to: Optional[date] = None
    """End date of the statement period"""


class Meta(BaseModel):
    cas_type: Optional[Literal["NSDL", "CDSL", "CAMS_KFINTECH"]] = None
    """Type of CAS detected and processed"""

    generated_at: Optional[datetime] = None
    """Timestamp when the response was generated"""

    statement_period: Optional[MetaStatementPeriod] = None


class MutualFundAdditionalInfo(BaseModel):
    """Additional folio information"""

    kyc: Optional[str] = None
    """KYC status of the folio"""

    pan: Optional[str] = None
    """PAN associated with the folio"""

    pankyc: Optional[str] = None
    """PAN KYC status"""


class MutualFundSchemeAdditionalInfo(BaseModel):
    """Additional information specific to the scheme"""

    advisor: Optional[str] = None
    """Financial advisor name (CAMS/KFintech)"""

    amfi: Optional[str] = None
    """AMFI code for the scheme (CAMS/KFintech)"""

    close_units: Optional[float] = None
    """Closing balance units for the statement period"""

    open_units: Optional[float] = None
    """Opening balance units for the statement period"""

    rta_code: Optional[str] = None
    """RTA code for the scheme (CAMS/KFintech)"""


class MutualFundSchemeGain(BaseModel):
    absolute: Optional[float] = None
    """Absolute gain or loss"""

    percentage: Optional[float] = None
    """Percentage gain or loss"""


class MutualFundScheme(BaseModel):
    additional_info: Optional[MutualFundSchemeAdditionalInfo] = None
    """Additional information specific to the scheme"""

    cost: Optional[float] = None
    """Cost of investment"""

    gain: Optional[MutualFundSchemeGain] = None

    isin: Optional[str] = None
    """ISIN code of the scheme"""

    name: Optional[str] = None
    """Scheme name"""

    nav: Optional[float] = None
    """Net Asset Value per unit"""

    nominees: Optional[List[str]] = None
    """List of nominees"""

    transactions: Optional[List[Transaction]] = None

    type: Optional[Literal["Equity", "Debt", "Hybrid", "Other"]] = None
    """Type of mutual fund scheme"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class MutualFund(BaseModel):
    additional_info: Optional[MutualFundAdditionalInfo] = None
    """Additional folio information"""

    amc: Optional[str] = None
    """Asset Management Company name"""

    folio_number: Optional[str] = None
    """Folio number"""

    linked_holders: Optional[List[LinkedHolder]] = None
    """List of account holders linked to this mutual fund folio"""

    registrar: Optional[str] = None
    """Registrar and Transfer Agent name"""

    schemes: Optional[List[MutualFundScheme]] = None

    value: Optional[float] = None
    """Total value of the folio"""


class NpFundAdditionalInfo(BaseModel):
    """Additional information specific to the NPS fund"""

    manager: Optional[str] = None
    """Fund manager name"""

    tier: Optional[Literal[1, 2]] = None
    """NPS tier (Tier I or Tier II)"""


class NpFund(BaseModel):
    additional_info: Optional[NpFundAdditionalInfo] = None
    """Additional information specific to the NPS fund"""

    cost: Optional[float] = None
    """Cost of investment"""

    name: Optional[str] = None
    """Name of the NPS fund"""

    nav: Optional[float] = None
    """Net Asset Value per unit"""

    units: Optional[float] = None
    """Number of units held"""

    value: Optional[float] = None
    """Current market value of the holding"""


class Np(BaseModel):
    additional_info: Optional[object] = None
    """Additional information specific to the NPS account"""

    cra: Optional[str] = None
    """Central Record Keeping Agency name"""

    funds: Optional[List[NpFund]] = None

    linked_holders: Optional[List[LinkedHolder]] = None
    """List of account holders linked to this NPS account"""

    pran: Optional[str] = None
    """Permanent Retirement Account Number (PRAN)"""

    value: Optional[float] = None
    """Total value of the NPS account"""


class SummaryAccountsDemat(BaseModel):
    count: Optional[int] = None
    """Number of demat accounts"""

    total_value: Optional[float] = None
    """Total value of demat accounts"""


class SummaryAccountsInsurance(BaseModel):
    count: Optional[int] = None
    """Number of insurance policies"""

    total_value: Optional[float] = None
    """Total value of insurance policies"""


class SummaryAccountsMutualFunds(BaseModel):
    count: Optional[int] = None
    """Number of mutual fund folios"""

    total_value: Optional[float] = None
    """Total value of mutual funds"""


class SummaryAccountsNps(BaseModel):
    count: Optional[int] = None
    """Number of NPS accounts"""

    total_value: Optional[float] = None
    """Total value of NPS accounts"""


class SummaryAccounts(BaseModel):
    demat: Optional[SummaryAccountsDemat] = None

    insurance: Optional[SummaryAccountsInsurance] = None

    mutual_funds: Optional[SummaryAccountsMutualFunds] = None

    nps: Optional[SummaryAccountsNps] = None


class Summary(BaseModel):
    accounts: Optional[SummaryAccounts] = None

    total_value: Optional[float] = None
    """Total portfolio value across all accounts"""


class UnifiedResponse(BaseModel):
    demat_accounts: Optional[List[DematAccount]] = None

    insurance: Optional[Insurance] = None

    investor: Optional[Investor] = None

    meta: Optional[Meta] = None

    mutual_funds: Optional[List[MutualFund]] = None

    nps: Optional[List[Np]] = None
    """List of NPS accounts"""

    summary: Optional[Summary] = None
