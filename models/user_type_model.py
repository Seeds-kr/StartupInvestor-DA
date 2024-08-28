from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserType(Base):
    __tablename__ = 'user_type'

    # Primary Key
    user_type_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Columns
    type = Column(String(255), nullable=False)

    # Relationship with User
    users = relationship("User", back_populates="user_type")

    # Constructor
    def __init__(self, type):
        self.type = type
