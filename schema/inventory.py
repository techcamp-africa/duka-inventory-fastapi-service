from pydantic import BaseModel,Field
from typing import List, Optional, Any
from datetime import datetime

class InventoryBase(BaseModel):
    title: str
    isbn_no: str
    buying_price: float
    selling_price: float

class InventoryPost(InventoryBase):
    uid: str

class InventoryPut(BaseModel):
    title: Optional[str]
    isbn_no: Optional[str]
    buying_price: Optional[float]
    selling_price: Optional[float]
    status: Optional[int]

class Inventory(InventoryBase):
    id: int
    public_id: str
    uid: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
