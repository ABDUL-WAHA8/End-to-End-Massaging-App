from fastapi import Depends, FastAPI
from DB_models.db_users import DbUser, __init__
from Pydantic_models import users, __init__
from DB_models import __init__
from Dependencies import DbConnection
from passlib.context import CryptContext



def create_db():
    from DB_models.db_users import Base
    Base.metadata.create_all(bind=DbConnection.engine)

create_db()

def get_db():
    db = DbConnection.SessionLocal()
    try:
        yield db
    finally:
        db.close()



def hashing(password:str):
    pwd=CryptContext(schemes=["argon2"], deprecated="auto")
    return pwd.hash(password)

app = FastAPI()


@app.post("/register")
async def register_user(user: users.User, db = Depends(get_db)):
    hashed_password = hashing(user.password)
    db_user = DbUser(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": f"User {db_user.email} registered successfully"}
