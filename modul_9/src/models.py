from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Date
from sqlalchemy.orm import relationship

from src.db import Base


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    date_birth = Column('date_birth', Date, nullable=True)
    adress = relationship('Adress', back_populates='person')

class Adress(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column('email', String(100), nullable=False)
    phone = Column('phone', String(100), nullable=False)
    address = Column('address', String(120), nullable=True)
    added_at = Column('added_at', Date, nullable=False)
    person_id = Column('person_id', ForeignKey('persons.id'))
    person = relationship('Person', back_populates='adress')