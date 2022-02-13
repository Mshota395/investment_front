import datetime
from typing import List

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

from . import models, schemas, crud
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# async def index():
#     return {"message": "success"}



# 一覧の取得
@app.get("/div_factorys", response_model = List[schemas.Div_factory])
async def read_div_factory(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
    div_factorys = crud.get_div_factorys(db, skip=skip, limit=limit)
    return div_factorys

# @app.get("/divs", response_model = List[schemas.Div])
# async def read_div(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
#     divs = crud.get_divs(db, skip=skip, limit=limit)
#     return divs

# @app.get("/div_cats", response_model = List[schemas.Div_cat])
# async def read_div_cat(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
#     div_cats = crud.get_div_cats(db, skip=skip, limit=limit)
#     return div_cats

# @app.get("/factorys", response_model = List[schemas.Factory])
# async def read_factory(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
#     factorys = crud.get_factorys(db, skip=skip, limit=limit)
#     return factorys

@app.get("/investmentitems", response_model = List[schemas.Investmentitem])
async def read_investmentitem(skip: int = 0, limit : int = 100, db : Session = Depends(get_db)):
    investmentitems = crud.get_investmentitems(db, skip=skip, limit=limit)
    return investmentitems



# Create
@app.post("/div_factorys", response_model=schemas.Div_factory)
async def create_Div_Factory(div_factory: schemas.Div_factoryCreate, db: Session = Depends(get_db)):
    return crud.create_div_factorys(db=db, div_factory=div_factory)

# @app.post("/divs", response_model=schemas.Div)
# async def create_div(div: schemas.DivCreate, db: Session = Depends(get_db)):
#     return crud.create_divs(db=db, div=div)

# @app.post("/div_cats", response_model=schemas.Div_cat)
# async def create_div_cat(div_cat: schemas.Div_catCreate, db: Session = Depends(get_db)):
#     return crud.create_div_cats(db=db, div_cat=div_cat)

# @app.post("/factorys", response_model=schemas.Factory)
# async def create_Factory(factory: schemas.FactoryCreate, db: Session = Depends(get_db)):
#     return crud.create_factorys(db=db, factory=factory)

@app.post("/investmentitems", response_model=schemas.Investmentitem)
async def create_investmentitem(investmentitem: schemas.InvestmentitemCreate, db: Session = Depends(get_db)):
    return crud.create_investmentitems(db=db, investmentitem=investmentitem)

# update
@app.put("/div_update", response_model = schemas.Div_factory)
async def div_update(div_factory : schemas.Div_factory, db: Session = Depends(get_db)):
    return crud.update_div_factorys(db = db, div_factory=div_factory, factory_id=div_factory.factory_id)