from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List

# get db dependency
from configurations.sqlalchemy_config import get_db
# schema
from schema import inventory
# services
from services.inventory import InventoryService

router = APIRouter(
    prefix="/inventories",
    tags=["INVENTORY"],
    responses={
        200:{'description':'Ok'},
        201:{'description':'created'},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"},
        409: {"description": "Conflict"}
    }  
)

# POST INV
@router.post('',
summary="Add an inventory",
response_model=inventory.Inventory,
response_description = "The added inventory",
status_code = 201
)
async def post_inventory(
    payload: inventory.InventoryPost,
    db: Session = Depends(get_db)
):
    return InventoryService.add_inventory(payload, db)

# GET
@router.get('',
summary="Get all inventories",
response_model=List[inventory.Inventory],
response_description = "A list of inventories",
status_code = 200
)
async def get_inventories(
    db: Session = Depends(get_db)
):
    return InventoryService.get_all_inventories(db)

# GET -> /:id
@router.get('/{inventory_id}',
summary="Get an inventory by ID",
response_model=inventory.Inventory,
response_description = "The inventory",
status_code = 200
)
async def inventory_byID(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return InventoryService.get_inventory_byID(inventory_id, db)

@router.put('/{inventory_id}',
summary="update an inventory by ID",
response_model=inventory.Inventory,
response_description = "The updated inventory",
status_code = 200
)
async def update(
    inventory_id: int,
    payload: inventory.InventoryPut,
    db: Session = Depends(get_db)
):
    return InventoryService.update_inventory(inventory_id, payload, db)
