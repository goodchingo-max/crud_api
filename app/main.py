from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mahsulotlar CRUD API")


def get_item_or_404(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    return db_item


@app.post("/items/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)


@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(db_item=Depends(get_item_or_404)):
    return db_item


@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def replace_item(
    item: schemas.ItemCreate,
    db_item=Depends(get_item_or_404),
    db: Session = Depends(get_db),
):
    return crud.update_item(db, db_item, item.model_dump())


@app.patch("/items/{item_id}", response_model=schemas.ItemResponse)
def patch_item(
    item: schemas.ItemUpdate,
    db_item=Depends(get_item_or_404),
    db: Session = Depends(get_db),
):
    return crud.update_item(db, db_item, item.model_dump(exclude_unset=True))


@app.delete("/items/{item_id}", status_code=204)
def delete_item(db_item=Depends(get_item_or_404), db: Session = Depends(get_db)):
    crud.delete_item(db, db_item)

