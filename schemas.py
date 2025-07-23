from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: Optional[str] = Field(None, title="Street", description="Street name of the address.")
    number: Optional[str] = Field(None, title="Number", description="Building or house number.")
    neighborhood: Optional[str] = Field(None, title="Neighborhood", description="District or neighborhood name.")
    city: Optional[str] = Field(None, title="City", description="City or municipality name.")
    state: Optional[str] = Field(None, title="State", description="State abbreviation (e.g., SP, RJ).")
    postal_code: Optional[str] = Field(None, title="Postal Code", description="ZIP/postal code (CEP).")


class Issuer(BaseModel):
    cnpj: Optional[str] = Field(None, title="CNPJ", description="CNPJ of the issuer.")
    corporate_name: Optional[str] = Field(None, title="Corporate Name", description="Full legal name of the issuer.")
    trade_name: Optional[str] = Field(None, title="Trade Name", description="Trade or fantasy name.")
    state_registration: Optional[str] = Field(None, title="State Registration", description="State tax registration number.")
    municipal_registration: Optional[str] = Field(None, title="Municipal Registration", description="Municipal tax registration number.")
    address: Optional[Address] = Field(None, title="Issuer Address", description="Address details of the issuer.")


class Recipient(BaseModel):
    cnpj_or_cpf: Optional[str] = Field(None, title="CNPJ or CPF", description="Recipient's CNPJ or CPF.")
    corporate_name: Optional[str] = Field(None, title="Corporate Name", description="Full legal name of the recipient.")
    state_registration: Optional[str] = Field(None, title="State Registration", description="State registration of the recipient.")
    address: Optional[Address] = Field(None, title="Recipient Address", description="Address details of the recipient.")


class Tax(BaseModel):
    tax_status: Optional[str] = Field(None, title="Tax Status", description="Tax situation code or description.")
    rate: Optional[float] = Field(None, title="Rate", description="Applied tax rate (%).")
    amount: Optional[float] = Field(None, title="Amount", description="Calculated tax amount.")


class ProductTaxes(BaseModel):
    icms: Optional[Tax] = Field(None, title="ICMS", description="ICMS tax information.")
    ipi: Optional[Tax] = Field(None, title="IPI", description="IPI tax information.")
    pis: Optional[Tax] = Field(None, title="PIS", description="PIS tax information.")
    cofins: Optional[Tax] = Field(None, title="COFINS", description="COFINS tax information.")


class Product(BaseModel):
    item_number: Optional[int] = Field(None, title="Item Number", description="Sequential number of the item in the invoice.")
    code: Optional[str] = Field(None, title="Product Code", description="Internal or external product code.")
    description: Optional[str] = Field(None, title="Product Description", description="Name or description of the product.")
    ncm: Optional[str] = Field(None, title="NCM", description="NCM code (Mercosur Common Nomenclature).")
    cfop: Optional[str] = Field(None, title="CFOP", description="CFOP code indicating the operation type.")
    unit: Optional[str] = Field(None, title="Unit", description="Unit of measure (e.g., kg, pcs).")
    quantity: Optional[float] = Field(None, title="Quantity", description="Quantity sold or moved.")
    unit_price: Optional[float] = Field(None, title="Unit Price", description="Unit price of the product.")
    total_price: Optional[float] = Field(None, title="Total Price", description="Total price for the item.")
    taxes: Optional[ProductTaxes] = Field(None, title="Product Taxes", description="Taxes applied to the product.")


class Totals(BaseModel):
    total_products: Optional[float] = Field(None, title="Total Products", description="Sum of all product values.")
    total_freight: Optional[float] = Field(None, title="Total Freight", description="Total freight amount.")
    total_insurance: Optional[float] = Field(None, title="Total Insurance", description="Total insurance cost.")
    total_discount: Optional[float] = Field(None, title="Total Discount", description="Total discount applied.")
    total_ipi: Optional[float] = Field(None, title="Total IPI", description="Total IPI tax.")
    total_icms: Optional[float] = Field(None, title="Total ICMS", description="Total ICMS tax.")
    total_pis: Optional[float] = Field(None, title="Total PIS", description="Total PIS tax.")
    total_cofins: Optional[float] = Field(None, title="Total COFINS", description="Total COFINS tax.")
    total_invoice: Optional[float] = Field(None, title="Total Invoice", description="Final total amount of the invoice.")


class Carrier(BaseModel):
    cnpj: Optional[str] = Field(None, title="Carrier CNPJ", description="CNPJ of the carrier.")
    corporate_name: Optional[str] = Field(None, title="Carrier Name", description="Legal name of the carrier.")
    state_registration: Optional[str] = Field(None, title="State Registration", description="Carrier's state registration.")
    address: Optional[str] = Field(None, title="Carrier Address", description="Address of the carrier.")
    city: Optional[str] = Field(None, title="Carrier City", description="City of the carrier.")
    state: Optional[str] = Field(None, title="Carrier State", description="State (UF) of the carrier.")


class Transportation(BaseModel):
    freight_mode: Optional[str] = Field(None, title="Freight Mode", description="Freight modality code (0 to 9).")
    carrier: Optional[Carrier] = Field(None, title="Carrier", description="Information about the transportation company.")
    vehicle_plate: Optional[str] = Field(None, title="Vehicle Plate", description="Vehicle license plate.")
    vehicle_state: Optional[str] = Field(None, title="Vehicle State", description="State where the vehicle is registered.")


class InvoiceInstallment(BaseModel):
    number: Optional[str] = Field(None, title="Invoice Number", description="Invoice number for payment.")
    original_value: Optional[float] = Field(None, title="Original Value", description="Original invoice amount.")
    discount_value: Optional[float] = Field(None, title="Discount Value", description="Discount applied to the invoice.")
    net_value: Optional[float] = Field(None, title="Net Value", description="Net payable amount.")


class Installment(BaseModel):
    number: Optional[str] = Field(None, title="Installment Number", description="Installment sequence number.")
    due_date: Optional[str] = Field(None, title="Due Date", description="Due date for the installment.")
    value: Optional[float] = Field(None, title="Installment Value", description="Amount of the installment.")


class Billing(BaseModel):
    invoice: Optional[InvoiceInstallment] = Field(None, title="Invoice Payment", description="Main invoice billing information.")
    installments: Optional[List[Installment]] = Field(None, title="Installments", description="List of payment installments.")


class AdditionalInfo(BaseModel):
    complementary_info: Optional[str] = Field(None, title="Complementary Info", description="Additional information from issuer.")
    taxpayer_notes: Optional[str] = Field(None, title="Taxpayer Notes", description="Notes from the taxpayer or client.")


class InvoiceIdentification(BaseModel):
    number: Optional[str] = Field(None, title="Invoice Number", description="Unique invoice number.")
    series: Optional[str] = Field(None, title="Series", description="Invoice series code.")
    issue_date: Optional[str] = Field(None, title="Issue Date", description="Date the invoice was issued.")
    dispatch_or_entry_date: Optional[str] = Field(None, title="Dispatch or Entry Date", description="Date of product dispatch or entry.")
    invoice_type: Optional[Literal["entry", "exit"]] = Field(None, title="Invoice Type", description="Defines whether the invoice is for an entry or an exit operation.")
    issue_purpose: Optional[Literal["normal", "complementary", "adjustment", "return"]] = Field(None, title="Purpose of Issue", description="Purpose of the invoice issuance.")
    operation_nature: Optional[str] = Field(None, title="Operation Nature", description="Nature or description of the operation.")
    model: Optional[str] = Field(None, title="Invoice Model", description="Invoice model (typically 55 or 65).")
    access_key: Optional[str] = Field(None, title="Access Key", description="44-digit access key of the NF-e.")
    version: Optional[str] = Field(None, title="Version", description="NF-e layout version.")


class NFe(BaseModel):
    identification: Optional[InvoiceIdentification] = Field(None, title="Identification", description="General information about the invoice.")
    issuer: Optional[Issuer] = Field(None, title="Issuer", description="Details of the company issuing the invoice.")
    recipient: Optional[Recipient] = Field(None, title="Recipient", description="Details of the invoice recipient.")
    products: Optional[List[Product]] = Field(None, title="Products", description="List of products or services in the invoice.")
    totals: Optional[Totals] = Field(None, title="Totals", description="Total amounts and taxes for the invoice.")
    transportation: Optional[Transportation] = Field(None, title="Transportation", description="Freight and carrier information.")
    billing: Optional[Billing] = Field(None, title="Billing", description="Billing and payment installments.")
    additional_info: Optional[AdditionalInfo] = Field(None, title="Additional Info", description="Observations and complementary data.")
