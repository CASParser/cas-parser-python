# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ContractNoteParseResponse",
    "Data",
    "DataBrokerInfo",
    "DataChargesSummary",
    "DataClientInfo",
    "DataContractNoteInfo",
    "DataDerivativesTransaction",
    "DataDetailedTrade",
    "DataEquityTransaction",
]


class DataBrokerInfo(BaseModel):
    broker_type: Optional[Literal["zerodha", "groww", "upstox", "icici", "unknown"]] = None
    """Auto-detected or specified broker type"""

    name: Optional[str] = None
    """Broker company name"""

    sebi_registration: Optional[str] = None
    """SEBI registration number of the broker"""


class DataChargesSummary(BaseModel):
    """Breakdown of various charges and fees"""

    cgst: Optional[float] = None
    """Central GST amount"""

    exchange_transaction_charges: Optional[float] = None
    """Exchange transaction charges"""

    igst: Optional[float] = None
    """Integrated GST amount"""

    net_amount_receivable_payable: Optional[float] = None
    """Final net amount receivable or payable"""

    pay_in_pay_out_obligation: Optional[float] = None
    """Net pay-in/pay-out obligation"""

    sebi_turnover_fees: Optional[float] = None
    """SEBI turnover fees"""

    securities_transaction_tax: Optional[float] = None
    """Securities Transaction Tax"""

    sgst: Optional[float] = None
    """State GST amount"""

    stamp_duty: Optional[float] = None
    """Stamp duty charges"""

    taxable_value_brokerage: Optional[float] = None
    """Taxable brokerage amount"""


class DataClientInfo(BaseModel):
    address: Optional[str] = None
    """Client address"""

    gst_state_code: Optional[str] = None
    """GST state code"""

    name: Optional[str] = None
    """Client name"""

    pan: Optional[str] = None
    """Client PAN number"""

    place_of_supply: Optional[str] = None
    """GST place of supply"""

    ucc: Optional[str] = None
    """Unique Client Code"""


class DataContractNoteInfo(BaseModel):
    contract_note_number: Optional[str] = None
    """Contract note reference number"""

    settlement_date: Optional[date] = None
    """Settlement date for the trades"""

    settlement_number: Optional[str] = None
    """Settlement reference number"""

    trade_date: Optional[date] = None
    """Date when trades were executed"""


class DataDerivativesTransaction(BaseModel):
    brokerage_per_unit: Optional[float] = None
    """Brokerage charged per unit"""

    buy_sell_bf_cf: Optional[str] = None
    """Transaction type (Buy/Sell/Bring Forward/Carry Forward)"""

    closing_rate_per_unit: Optional[float] = None
    """Closing rate per unit"""

    contract_description: Optional[str] = None
    """Derivatives contract description"""

    net_total: Optional[float] = None
    """Net total amount"""

    quantity: Optional[float] = None
    """Quantity traded"""

    wap_per_unit: Optional[float] = None
    """Weighted Average Price per unit"""


class DataDetailedTrade(BaseModel):
    brokerage: Optional[float] = None
    """Brokerage charged for this trade"""

    buy_sell: Optional[str] = None
    """Transaction type (B for Buy, S for Sell)"""

    closing_rate_per_unit: Optional[float] = None
    """Closing rate per unit"""

    exchange: Optional[str] = None
    """Exchange name"""

    net_rate_per_unit: Optional[float] = None
    """Net rate per unit"""

    net_total: Optional[float] = None
    """Net total for this trade"""

    order_number: Optional[str] = None
    """Order reference number"""

    order_time: Optional[str] = None
    """Time when order was placed"""

    quantity: Optional[float] = None
    """Quantity traded"""

    remarks: Optional[str] = None
    """Additional remarks or notes"""

    security_description: Optional[str] = None
    """Security name with exchange and ISIN"""

    trade_number: Optional[str] = None
    """Trade reference number"""

    trade_time: Optional[str] = None
    """Time when trade was executed"""


class DataEquityTransaction(BaseModel):
    buy_quantity: Optional[float] = None
    """Total quantity purchased"""

    buy_total_value: Optional[float] = None
    """Total value of buy transactions"""

    buy_wap: Optional[float] = None
    """Weighted Average Price for buy transactions"""

    isin: Optional[str] = None
    """ISIN code of the security"""

    net_obligation: Optional[float] = None
    """Net amount payable/receivable for this security"""

    security_name: Optional[str] = None
    """Name of the security"""

    security_symbol: Optional[str] = None
    """Trading symbol"""

    sell_quantity: Optional[float] = None
    """Total quantity sold"""

    sell_total_value: Optional[float] = None
    """Total value of sell transactions"""

    sell_wap: Optional[float] = None
    """Weighted Average Price for sell transactions"""


class Data(BaseModel):
    broker_info: Optional[DataBrokerInfo] = None

    charges_summary: Optional[DataChargesSummary] = None
    """Breakdown of various charges and fees"""

    client_info: Optional[DataClientInfo] = None

    contract_note_info: Optional[DataContractNoteInfo] = None

    derivatives_transactions: Optional[List[DataDerivativesTransaction]] = None
    """Summary of derivatives transactions"""

    detailed_trades: Optional[List[DataDetailedTrade]] = None
    """Detailed breakdown of all individual trades"""

    equity_transactions: Optional[List[DataEquityTransaction]] = None
    """Summary of equity transactions grouped by security"""


class ContractNoteParseResponse(BaseModel):
    data: Optional[Data] = None

    msg: Optional[str] = None

    status: Optional[str] = None
