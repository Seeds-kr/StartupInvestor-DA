from sqlalchemy import Column, String, BigInteger, Date, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = 'company'

    # Primary Key
    company_id = Column(BigInteger, primary_key=True, autoincrement=True)

    # One-to-One relationship with User (foreign key to user table)
    ceo_user_id = Column(BigInteger, ForeignKey('user.user_id'), nullable=False)
    user = relationship("User", back_populates="company", uselist=False)

    # Columns
    name = Column(String(255), nullable=False, unique=True)
    address = Column(String(255), nullable=False, unique=True)
    founded_at = Column(Date, nullable=False)
    amount = Column(BigInteger, nullable=False)

    # Many-to-One relationship with SeriesCategory (foreign key to latest_series_category table)
    latest_series_category_id = Column(BigInteger, ForeignKey('series_category.series_category_id'), nullable=False)
    latest_series_category = relationship("SeriesCategory", foreign_keys=[latest_series_category_id])

    is_possible_invest = Column(Boolean, nullable=False, default=True)
    company_url = Column(String(255), nullable=False)
    modified_at = Column(Date, nullable=False)
    introduction = Column(Text, nullable=False)

    # Many-to-One relationship with SeriesCategory for goal series (nullable)
    goal_series_category_id = Column(BigInteger, ForeignKey('series_category.series_category_id'), nullable=True)
    goal_series_category = relationship("SeriesCategory", foreign_keys=[goal_series_category_id])

    goal_amount_minimum = Column(BigInteger, nullable=True)
    goal_amount_maximum = Column(BigInteger, nullable=True)
    product_name = Column(String(255), nullable=True)
    product_description = Column(Text, nullable=True)
    product_image_url = Column(String(255), nullable=True)
    product_introduce_url = Column(String(255), nullable=True)
    new_headline = Column(String(255), nullable=True)
    new_url = Column(String(255), nullable=True)
    new_upload_at = Column(Date, nullable=True)
    news_company = Column(String(255), nullable=True)

    # Constructor
    def __init__(self, user, name, address, founded_at, amount,
                 latest_series_category, company_url, introduction,
                 goal_series_category=None, goal_amount_minimum=None, goal_amount_maximum=None,
                 product_name=None, product_description=None, product_image_url=None, product_introduce_url=None,
                 newHeadline=None, newUrl=None, newUploadAt=None, newsCompany=None):
        self.user = user
        self.name = name
        self.address = address
        self.founded_at = founded_at
        self.amount = amount
        self.latest_series_category = latest_series_category
        self.is_possible_invest = True
        self.company_url = company_url
        self.introduction = introduction
        self.modified_at = Date.today()
        self.goal_series_category = goal_series_category
        self.goal_amount_minimum = goal_amount_minimum
        self.goal_amount_maximum = goal_amount_maximum
        self.product_name = product_name
        self.product_description = product_description
        self.product_image_url = product_image_url
        self.product_introduce_url = product_introduce_url
        self.new_headline = newHeadline
        self.new_url = newUrl
        self.new_upload_at = newUploadAt
        self.news_company = newsCompany
