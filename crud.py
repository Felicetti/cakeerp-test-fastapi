from sqlalchemy.orm import Session

from models import Item
from schema import SchemaItemCreate

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offeset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: SchemaItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

def delete_item(db: Session, item_id: int):
    try:
        db.query(Item).filter(Item.id == item_id).delete()
        db.commit()
    except Exception as exeption:
        raise(exeption)
    return{"deleted status": "Sucess"}



