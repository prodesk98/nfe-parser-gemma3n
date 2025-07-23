from typing import List, Optional, Literal
from pydantic import BaseModel


class Address(BaseModel):
    street: Optional[str]
    number: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]


class Issuer(BaseModel):
    cnpj: Optional[str]
    corporate_name: Optional[str]
    trade_name: Optional[str]
    state_registration: Optional[str]
    municipal_registration: Optional[str]
    address: Optional[Address]


class Recipient(BaseModel):
    cnpj_or_cpf: Optional[str]
    corporate_name: Optional[str]
    state_registration: Optional[str]
    address: Optional[Address]


class Tax(BaseModel):
    tax_status: Optional[str]
    rate: Optional[float]
    amount: Optional[float]


class ProductTaxes(BaseModel):
    icms: Optional[Tax]
    ipi: Optional[Tax]
    pis: Optional[Tax]
    cofins: Optional[Tax]


class Product(BaseModel):
    item_number: Optional[int]
    code: Optional[str]
    description: Optional[str]
    ncm: Optional[str]
    cfop: Optional[str]
    unit: Optional[str]
    quantity: Optional[float]
    unit_price: Optional[float]
    total_price: Optional[float]
    taxes: Optional[ProductTaxes]


class Totals(BaseModel):
    total_products: Optional[float]
    total_freight: Optional[float]
    total_insurance: Optional[float]
    total_discount: Optional[float]
    total_ipi: Optional[float]
    total_icms: Optional[float]
    total_pis: Optional[float]
    total_cofins: Optional[float]
    total_invoice: Optional[float]


class Carrier(BaseModel):
    cnpj: Optional[str]
    corporate_name: Optional[str]
    state_registration: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]


class Transportation(BaseModel):
    freight_mode: Optional[str]  # 0 to 9
    carrier: Optional[Carrier]
    vehicle_plate: Optional[str]
    vehicle_state: Optional[str]


class InvoiceInstallment(BaseModel):
    number: Optional[str]
    original_value: Optional[float]
    discount_value: Optional[float]
    net_value: Optional[float]


class Installment(BaseModel):
    number: Optional[str]
    due_date: Optional[str]
    value: Optional[float]


class Billing(BaseModel):
    invoice: Optional[InvoiceInstallment]
    installments: Optional[List[Installment]]


class AdditionalInfo(BaseModel):
    complementary_info: Optional[str]
    taxpayer_notes: Optional[str]


class InvoiceIdentification(BaseModel):
    number: Optional[str]
    series: Optional[str]
    issue_date: Optional[str]
    dispatch_or_entry_date: Optional[str]
    invoice_type: Optional[Literal["entry", "exit"]]
    issue_purpose: Optional[Literal["normal", "complementary", "adjustment", "return"]]
    operation_nature: Optional[str]
    model: Optional[str]  # 55|65
    access_key: Optional[str]
    version: Optional[str]


class NFe(BaseModel):
    identification: Optional[InvoiceIdentification] = None
    issuer: Optional[Issuer]                        = None
    recipient: Optional[Recipient]                  = None
    products: Optional[List[Product]]               = None
    totals: Optional[Totals]                        = None
    transportation: Optional[Transportation]        = None
    billing: Optional[Billing]                      = None
    additional_info: Optional[AdditionalInfo]       = None
