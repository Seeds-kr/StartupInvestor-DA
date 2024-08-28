from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 데이터베이스 정보 가져오기
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# MySQL 데이터베이스 URI 설정
DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# 엔진 생성
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
