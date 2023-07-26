from sqlalchemy import create_engine,MetaData
<<<<<<< HEAD
=======



>>>>>>> b0e5be158b5d4564c8fa80fe72a9d60f42e22019

engine = create_engine("mysql+pymysql://root@localhost:3309/test")

meta = MetaData()
conn = engine.connect()
