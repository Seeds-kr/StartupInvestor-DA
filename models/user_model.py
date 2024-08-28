from sqlalchemy import Column, String, BigInteger, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    # Primary Key
    user_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Many-to-One relationship with UserType
    user_type_id = Column(BigInteger, ForeignKey('user_type.user_type_id'), nullable=False)
    user_type = relationship("UserType", back_populates="users")

    # Columns
    personal_type = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(BigInteger, nullable=False)
    is_on_alarm = Column(Boolean, nullable=False)
    profile_img_data = Column(LargeBinary, nullable=True)

    # One-to-One relationship with Company
    company = relationship("Company", back_populates="user", uselist=False)

    # Constructor
    def __init__(self, user_type, personal_type, username, password, email, phone_number, is_on_alarm,
                 profile_img_data=None):
        self.user_type = user_type
        self.personal_type = personal_type
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.is_on_alarm = is_on_alarm
        self.profile_img_data = profile_img_data
