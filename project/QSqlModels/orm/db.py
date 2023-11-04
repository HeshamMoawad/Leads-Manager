from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , relationship



engine = create_engine('sqlite:///Data\database.db',echo=True)
session = sessionmaker(engine)()
BaseModel = declarative_base()

