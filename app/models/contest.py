from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contest(Base):
    __table__ = 'contests'

    id = Column(Integer, primary_key = True)
    title = Column(Text)
    description =  Column(Text)
    private =  Column(Integer)
    start_time =  Column(DateTime)
    end_time =  Column(DateTime)
    enabled =  Column(Boolean)
