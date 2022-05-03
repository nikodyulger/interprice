from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

user = os.environ['DB_USER']
password =  os.environ['DB_PASSWORD']
port = os.environ['DB_PORT']
db_name = os.environp['DB_NAME']
host = os.environ['RDS_HOST']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

engine = create_engine( SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()