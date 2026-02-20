from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:zaqmlp@localhost:5432/EndToEnd"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)