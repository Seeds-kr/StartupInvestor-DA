from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+pymysql://root:mqkrwnsgk0903!@localhost:3306/startupinvestor'
engine = create_engine(DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 기본 베이스를 사용하여 테이블 생성
from models.user_model import Base as UserBase
from models.company_model import Base as CompanyBase
from models.series_category_model import Base as SeriesCategoryBase
from models.user_type_model import Base as UserTypeBase
from models.investor_model import Base as InvestorBase


# 모든 테이블 생성 (필요한 경우 한 번 실행)
def create_tables():
    UserBase.metadata.create_all(bind=engine)
    CompanyBase.metadata.create_all(bind=engine)
    SeriesCategoryBase.metadata.create_all(bind=engine)
    UserTypeBase.metadata.create_all(bind=engine)
    InvestorBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
