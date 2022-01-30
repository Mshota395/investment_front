from sqlalchemy.orm import Session
from sqlalchemy.util.langhelpers import repr_tuple_names
from . import models, schemas


"""
データベースの読み込み
"""

#事業部工場名の取得
def get_div_factorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.div_factory).offset(skip).limit(limit).all()


# #事業部名の取得
# def get_divs(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Div).offset(skip).limit(limit).all()

# #部門名の取得
# def get_div_cats(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Div_cat).offset(skip).limit(limit).all()

# #工場名の取得
# def get_factorys(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Factory).offset(skip).limit(limit).all()

# #投資項目の取得
# def get_investmentitems(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Investment_Plan).offset(skip).limit(limit).all()


"""
データベースへの登録
"""
# 事業部工場名の登録
def create_div_factorys(db:Session, div_factory : schemas.Div_factory):
    db_div_factory = models.div_factory(
        div_name = div_factory.div_name,
        div_cat_name = div_factory.div_cat_name,
        factory_name = div_factory.factory_name
        )
    db.add(db_div_factory)
    db.commit()
    db.refresh(db_div_factory)
    return db_div_factory



# # 事業部名の登録
# def create_divs(db:Session, div : schemas.Div):
#     db_div = models.Div(div_name = div.div_name)
#     db.add(db_div)
#     db.commit()
#     db.refresh(db_div)
#     return db_div

# # 部門名の登録
# def create_div_cats(db:Session, div_cat : schemas.Div_cat):
#     db_div_cat = models.Div_cat(
#         div_id = div_cat.div_id,
#         div_cat_name = div_cat.div_cat_name
#         )
#     db.add(db_div_cat)
#     db.commit()
#     db.refresh(db_div_cat)
#     return db_div_cat

# # 工場名の登録
# def create_factorys(db:Session, factory : schemas.Factory):
#     db_factory = models.Factory(
#         div_id = factory.div_id,
#         div_cat_id = factory.div_cat_id,
#         factory_name = factory.factory_name
#         )
#     db.add(db_factory)
#     db.commit()
#     db.refresh(db_factory)
#     return db_factory

# 投資項目の登録
def create_investmentitems(db:Session, investmentitem : schemas.Investmentitem):
    db_investmentitem = models.Investmentitem(
        div_id = investmentitem.div_id,
        div_cat_id = investmentitem.div_cat_id,
        factory_id = investmentitem.factory_id,
        investment_name = investmentitem.itemname,
        item_amount = investmentitem.item_amount,
        acceptance_month_plan = investmentitem.acceptance_month_plan
        )
    db.add(db_investmentitem)
    db.commit()
    db.refresh(db_investmentitem)
    return db_investmentitem