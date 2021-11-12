from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker

SQLALCHEMY_DATABSE_URI = "sqlite:///./blog.db"

engine = create_engine(SQLALCHEMY_DATABSE_URI, connect_args = {'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()