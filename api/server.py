from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from mangum import Mangum
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)
database = client["mydatabase"]
collection = database["mycollection"]

@app.get("/hello")
async def read_root():
    document = await collection.find_one()
    return {"message": "Hello World", "document": document}

handler = Mangum(app)
