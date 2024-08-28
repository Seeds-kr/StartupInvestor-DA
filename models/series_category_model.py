from sqlalchemy import Column, String, BigInteger, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()


# Enum for SeriesCategoryConst
class SeriesCategoryConst(PyEnum):
    CATEGORY_A = "CATEGORY_A"
    CATEGORY_B = "CATEGORY_B"
    # Add more categories as per your domain needs


class SeriesCategory(Base):
    __tablename__ = 'series_category'

    # Primary Key
    series_category_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Enum Column
    category = Column(Enum(SeriesCategoryConst), nullable=False)

    # Constructor
    def __init__(self, category):
        self.category = category
