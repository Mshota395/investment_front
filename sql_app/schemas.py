
from sqlalchemy.sql.sqltypes import Date
from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime

class DivCreate(BaseModel):
    """
    事業部の登録
    """
    div_name : str = Field(max_length = 100)


class Div(DivCreate):
    """
    事業部の参照
    """
    div_id : int

    class Config:
        orm_mode = True

class Div_catCreate(BaseModel):
    """
    部門の登録
    """
    div_id : int
    div_cat_name : str = Field(max_length = 100)

class Div_cat(Div_catCreate):
    """
    部門の参照
    """
    div_cat_id  : int

    class Config:
        orm_mode = True

class FactoryCreate(BaseModel):
    """
    工場名の登録
    """
    div_id : int
    div_cat_id : int
    factory_name : str = Field(max_length = 100)

class Factory(FactoryCreate):
    """
    工場名の登録
    """
    factory_id : int

    class Config:
        orm_mode = True


class InvestmentitemCreate(BaseModel):
    """
    投資の期初計画
    エクセルからデータを読み込む
    """
    div_id : int
    div_cat_id : int
    factory_id : int

    itemname : str = Field(max_length = 100)
    # relocation : int
    item_amount : float
    # delivery_time : int
    # sliding : int
    # approval_month_plan : int = Field(min_value = 1,max_value = 12)
    # order_month_plan : int = Field(min_value = 1,max_value = 12)
    acceptance_month_plan : datetime.datetime

class Investmentitem(BaseModel):
    """
    投資の期初計画
    エクセルからデータを読み込む
    """
    investment_id : int

    class Config:
        orm_mode = True

    
# class ActualCreate(BaseModel):
#     """
#     実績入力
#     """
#     factory_id : int
#     investment_id : int 
#     # 実績月
#     approval_month_act : int = Field(min_value = 1,max_value = 12)
#     order_month_act : int = Field(min_value = 1,max_value = 12)
#     acceptance_month_act : int = Field(min_value = 1,max_value = 12)
#     # 実績金額 
#     approval_amount_act : float
#     order_amount_act : float
#     acceptance_amount_act : float

# class Actual(ActualCreate):
#     """
#     実績入力
#     """
#     actuarl_id : int

#     class Config:
#         orm_mode = True

# class Change_planCreate(BaseModel):
#     factory_id : int
#     investment_id : int 
#     # 見直し後の月
#     approval_month_change : int = Field(min_value = 1,max_value = 12)
#     order_month_change : int = Field(min_value = 1,max_value = 12)
#     acceptance_month_change : int = Field(min_value = 1,max_value = 12)
#     # 変更金額 
#     approval_amount_change : float
#     order_amount_change : float
#     acceptance_amount_change : float
#     # 変更を行なった月
#     # changed_month : datetime.datetime.now()
#     # 来期ずれ込み
#     sliding_next : int

#     class Config:
#         orm_mode = True

# class Change_plan(Change_planCreate):
#     change_plan_id : int

#     class Config:
#         orm_mode = True

# class exchage_rate(BaseModel):
#     jpy : int = 1
#     usd : float
#     rmb : float
#     thb : float

#     class Config:
#         orm_mode = True