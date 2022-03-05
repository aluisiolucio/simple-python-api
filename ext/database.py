import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


def connection():
    host_port = os.getenv('HOST_PORT')
    password = os.getenv('PASS')
    user = os.getenv('DB_USERNAME')
    db_name = os.getenv('DB_NAME')

    DATABASE_URI = f"postgresql://{user}:{password}@{host_port}/{db_name}"
    engine = create_engine(os.getenv('DATABASE_URL'), echo=False)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()