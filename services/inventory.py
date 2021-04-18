import uuid

from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

# schema
from schema import inventory
# models
from models.inventory import Inventory
# rabbitMQ sender
from rabbitmq.sender import send_log_to_queue

class InventoryService:

    @classmethod
    def add_inventory(cls, payload: inventory.InventoryPost, db: Session):
        """create a new inventory"""
        # check inventory title exists
    
        # if Inventory.check_title_exists(title=payload.title, db=db):
        #     raise HTTPException(status_code=409, detail="the inventory already exists")

        try:
            # add the inventory
            record = Inventory(
                public_id=str(uuid.uuid4()),
                title=payload.title.strip().title(),
                isbn_no=payload.isbn_no,
                buying_price=payload.buying_price,
                selling_price=payload.selling_price
            )
            created_record = record.create(db=db)
            send_log_to_queue('Successfully Save Inventory Record')
            return created_record
        except Exception as e:
            send_log_to_queue('Failed Save Inventory')
            raise HTTPException(status_code=500, detail='Server Error')


    @classmethod
    def get_all_inventories(cls, db: Session):
        """"return a list of all inventories"""
        send_log_to_queue('All Inventory Fetched')
        return Inventory.fetch_all(db=db)

    @classmethod
    def get_inventory_byID(cls, inventory_id: int, db: Session):
        """"get an inventory that matches the id"""
        if not Inventory.fetch_inventory_byID(inventory_id=inventory_id, db=db):
            raise HTTPException(status_code=400, detail="the inventory does not exists")
        
        send_log_to_queue(f'Inventory Fetched with ID {inventory_id}')

        return Inventory.fetch_inventory_byID(inventory_id=inventory_id, db=db)

    @classmethod
    def update_inventory(cls,inventory_id: int, payload: inventory.InventoryPut, db:Session):
        """update an inventory"""
        inv : inventory.Inventory = Inventory.fetch_inventory_byID(inventory_id=inventory_id, db=db)
        if payload.title is not None:
            inv.title = payload.title
        if payload.isbn_no is not None:
            inv.isbn_no = payload.isbn_no
        if payload.buying_price is not None:
            inv.buying_price = payload.buying_price
        if payload.selling_price is not None:
            inv.selling_price =payload.selling_price
        if payload.status is not None:
            inv.status = payload.status
        
        inv.updated_at = date.today()
        
        db.commit()
        db.refresh(inv)
        return inv