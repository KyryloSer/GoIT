from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime

from db.connect import Base


class NewsOne(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    created = Column(DateTime, default=datetime.now())
    link_news = Column(String(200), nullable=False)
    views = Column(String(10), nullable=False)
