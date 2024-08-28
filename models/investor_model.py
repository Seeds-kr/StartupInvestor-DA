from sqlalchemy import Column, String, BigInteger, Date, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Investor(Base):
    __tablename__ = 'investor'

    # Primary Key
    investor_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # One-to-One relationship with User (foreign key to user table)
    ceo_user_id = Column(BigInteger, ForeignKey('user.user_id'), nullable=False)
    user = relationship("User", back_populates="investor", uselist=False)

    # Columns
    url = Column(String(255), nullable=True)
    founded_date = Column(Date, nullable=True)
    introduction = Column(Text, nullable=True)
    modified_at = Column(Date, nullable=True)
    invest_type = Column(String(255), nullable=True)
    total_amount = Column(BigInteger, nullable=True)
    total_invest_cnt = Column(Integer, nullable=True)

    # Constructor
    def __init__(self, user, url=None, founded_date=None, introduction=None,
                 modified_at=None, invest_type=None, total_amount=None, total_invest_cnt=None):
        self.user = user
        self.url = url
        self.founded_date = founded_date
        self.introduction = introduction
        self.modified_at = modified_at
        self.invest_type = invest_type
        self.total_amount = total_amount
        self.total_invest_cnt = total_invest_cnt
