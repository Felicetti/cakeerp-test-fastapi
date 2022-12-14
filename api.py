from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schema import SchemaItem, SchemaItemCreate
from database import get_db
from crud import get_item, get_items, create_item, delete_item

app = FastAPI()

@app.get ("/status")
def status():
    return{"message": "ok"}

@app.get("/items", response_model=List[SchemaItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)

    return items

@app.post("/items", response_model=List[SchemaItem])
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=SchemaItem)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item

@app.delete("/items/{item_id}", response_model=SchemaItem)
def delete_item_1(item_id: int, db: Session = Depends(get_db)):
     return delete_item(db=db, item_id=item_id)


    

