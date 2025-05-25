from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_ = Column(String)
    level = Column(Integer)
    stats = Column(JSON)
    inventory = Column(JSON)
