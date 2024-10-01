from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Address(BaseModel):
    state: str
    city: str
    zipCode: str
    line_1: str
    line_2: Optional[str] = None
    line_3: Optional[str] = None
    line_4: Optional[str] = None

class AddressBook(BaseModel):
    cuit: str = Field(..., alias="cuit")
    customerId: str
    name: str
    phone: str
    statusClient: Optional[str] = None
    address: Address
    emails: List[EmailStr]
    condicionVenta: str
    esCtaCte: str

class DeleteResponse(BaseModel):
    message: str

class AddressBookResponse(BaseModel):
    code: int
    return_: AddressBook = Field(..., alias="return")

    class Config:
        allow_population_by_field_name = True



