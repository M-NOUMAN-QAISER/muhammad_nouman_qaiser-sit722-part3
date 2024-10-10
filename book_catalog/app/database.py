from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://assessmentpart3_k41e_user:hZML5OKBBltjNpvoDhrTUPbNmAz9U5XC@dpg-cs202fu8ii6s73d9njg0-a.oregon-postgres.render.com/assessmentpart3_k41e"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
