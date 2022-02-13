
# データベース側の構造の作成
from sqlalchemy import Column, ForeignKey, ForeignKey, Integer, String, DateTime, Float
from .database import Base


class Div_factory(Base):
    """
    工場名の登録
    """
    __tablename__ = "div_factory"
    # div_id = Column(Integer, ForeignKey('div.div_id', ondelete='SET NULL'), nullable=False)
    # div_cat_id = Column(Integer, ForeignKey('div_cat.div_cat_id', ondelete='SET NULL'), nullable=False)
    factory_id = Column(Integer, primary_key=True, index = True)
    factory_name = Column(String, unique=False, index = True)
    div_name = Column(String, unique=False, index = True)
    div_cat_name = Column(String, unique=False, index = False, nullable=True)


# class Div(Base):
#     """
#     事業部の登録
#     """
#     __tablename__ = "div"
#     div_id = Column(Integer, primary_key=True, index = True)
#     div_name = Column(String, unique=False, index = True)

# class Div_cat(Base):
#     """
#     部門の登録
#     """
#     __tablename__ = "div_cat"
#     div_id = Column(Integer, ForeignKey('div.div_id', ondelete='SET NULL'), nullable=False)
#     div_cat_id = Column(Integer, primary_key=True, index = True)
#     div_cat_name = Column(String, unique=False, index = True)

# class Factory(Base):
#     """
#     工場名の登録
#     """
#     __tablename__ = "factory"
#     div_id = Column(Integer, ForeignKey('div.div_id', ondelete='SET NULL'), nullable=False)
#     div_cat_id = Column(Integer, ForeignKey('div_cat.div_cat_id', ondelete='SET NULL'), nullable=False)
#     factory_id = Column(Integer, primary_key=True, index = True)
#     factory_name = Column(String, unique=False, index = True)
    

class Investmentitem(Base):
    """
    投資項目の登録
    """
    __tablename__ = "investmentsitem"
    # div_id = Column(Integer, ForeignKey('div.div_id', ondelete='SET NULL'), nullable=False)
    # div_cat_id = Column(Integer, ForeignKey('div_cat.div_cat_id', ondelete='SET NULL'), nullable=False)
    factory_id = Column(Integer, ForeignKey('div_factory.factory_id', ondelete='SET NULL'), nullable=False)
    investment_id = Column(Integer, primary_key=True, index = True)
    investment_name = Column(String, unique=True, index = True)
    item_amount = Column(Float, unique=False, index=True)
    acceptance_month_plan = Column(DateTime, unique=False, index=True)
 