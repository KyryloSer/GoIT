from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///D:\\GOIT\\modul_9\\personal_assistant.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()


