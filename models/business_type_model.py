from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class BusinessType(Base):
    __tablename__ = 'business_type'

    # Primary Key
    business_type_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Columns
    main_category = Column(String(50), nullable=False)
    sub_category = Column(String(100), nullable=False)

    def __init__(self, main_category, sub_category):
        self.main_category = main_category
        self.sub_category = sub_category

# Database configuration example (to be customized)
DATABASE_URI = 'mysql+pymysql://user:password@localhost:3306/db_name'

# Create engine and session
engine = create_engine(DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database (this needs to be run once)
Base.metadata.create_all(engine)
