from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON, Text, Float
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base

class Inventory(Model, Base):
    __tablename__ = 'inventories'
    public_id = Column(String, nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    isbn_no = Column(String, nullable=False)
    buying_price = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)
    status = Column(Integer, default=1 , nullable=False) #1 - visible
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)

    @classmethod
    def check_title_exists(cls, title: str, db:Session):
        if db.query(cls).filter(cls.title == title).first():
            return True
        return False

    @classmethod
    def fetch_inventory_byID(cls, inventory_id: int, db: Session):
        return db.query(cls).filter(cls.id == inventory_id).first()