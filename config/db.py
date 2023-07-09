from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine("mysql+pymysql://root@localhost:3309/test")

SessionLocal = sessionmaker(autocommit= False, autoflush=False,bind=engine)

Base = declarative_base()


meta = MetaData()
conn = engine.connect()