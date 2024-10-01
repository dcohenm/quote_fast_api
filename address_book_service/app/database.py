import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson import objectid
from pymongo import ASCENDING

#MONGO_DETAILS = "mongodb://localhost:27917"
#MONGO_DETAILS = "mongodb://host.docker.internal:27017"
MONGO_DETAILS = os.environ.get("MONGO_DETAILS", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.addressbook
address_collection = database.get_collection("addresses")

# Create an index on the 'cuit' field for faster lookups
# We'll do this in an async function that we can call when the app starts
async def create_index():
    await address_collection.create_index([("cuit", 1)], unique=True)

def address_helper(address) -> dict:
    return {
        "id": str(address["_id"]),
        "cuit": address["cuit"],
        "customerId": address["customerId"],
        "name": address["name"],
        "phone": address["phone"],
        "statusClient": address["statusClient"],
        "address": address["address"],
        "emails": address["emails"],
        "condicionVenta": address["condicionVenta"],
        "esCtaCte": address["esCtaCte"]
    }