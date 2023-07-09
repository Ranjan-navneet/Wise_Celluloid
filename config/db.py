from sqlalchemy import create_engine,MetaData




engine = create_engine("mysql+pymysql://root@localhost:3309/test")

meta = MetaData()
conn = engine.connect()
