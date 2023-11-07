from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , relationship
from sqlite3 import connect




con = connect("Data\database.db")


engine = create_engine('sqlite:///Data\database.db',echo=False)
session = sessionmaker(engine)()
BaseModel = declarative_base()

