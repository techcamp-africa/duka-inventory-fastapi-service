from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy config
from configurations.sqlalchemy_config import engine, Base

# models
from models.inventory import Inventory
# create all tables
Base.metadata.create_all(bind=engine)
# drop all tables
# Base.metadata.drop_all(bind=engine)

# routes
from routes import (inventory)

app = FastAPI(
    title='Duka-Inventory Service',
    version='0.0.1',
    description='endpoints for Duka ',
    redoc_url='/',
)

# setup the origins
origins = ["http://localhost","http://localhost:3000","http://127.0.0.1", ]

# add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inventory.router)