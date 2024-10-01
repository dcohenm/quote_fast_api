import logging
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from app.database import address_collection, address_helper
from app.schemas import AddressBook, AddressBookResponse, DeleteResponse

router = APIRouter()

@router.post("/addressBook", response_model=AddressBookResponse)
async def create_address_book(address_book: AddressBook = Body(...)):
    logging.info(f"Received address book: {address_book}")
    address_book_dict = jsonable_encoder(address_book)
    logging.info(f"Encoded address book: {address_book_dict}")
    new_address_book = await address_collection.insert_one(address_book_dict)
    created_address_book = await address_collection.find_one({"_id": new_address_book.inserted_id})
    logging.info(f"Created address book: {created_address_book}")
    return AddressBookResponse(code=0, return_=address_helper(created_address_book))

@router.post("/getAddressBook", response_model=AddressBookResponse)
async def get_address_book(cuit: str = Body(..., embed=True)):
    address_book = await address_collection.find_one({"cuit": cuit})
    if address_book:
        return AddressBookResponse(code=0, return_=address_helper(address_book))
    raise HTTPException(status_code=404, detail=f"Address book with CUIT {cuit} not found")

@router.delete("/addressBook/{cuit}", response_model=DeleteResponse)
async def delete_address_book(cuit: str):
    deltete_resul = await address_collection.delete_one({"cuit": cuit})

    if deltete_resul.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Address book with CUIT {cuit} not found")
    
    return DeleteResponse(message=f"Address book with CUIT {cuit} has been deleted")
