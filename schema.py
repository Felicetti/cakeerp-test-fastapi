from mailbox import NotEmptyError
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class SchemaItemBase(BaseModel):
    title : str
    description : Optional[str] = None
    create_date : datetime = None 

class SchemaItemCreate(SchemaItemBase):
    pass

class SchemaItem(SchemaItemBase):
    id: int 

    class Config:
        orm_mode = True
