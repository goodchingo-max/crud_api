from sqlalchemy.orm import Session
from . import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ItemModel).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.get(models.ItemModel, item_id)


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.ItemModel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, db_item: models.ItemModel, data: dict):
    for key, value in data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, db_item: models.ItemModel):
    db.delete(db_item)
    db.commit()

