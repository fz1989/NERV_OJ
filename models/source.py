from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Source(Base):
    __table__ = 'sources'

    id = Column(Integer, primary_key = True)
    username = Column(String(20))
    source_code = Column(Text)
    length = Column(Integer)
    submit_time =  Column(DateTime)
    submit_ip = Column(String(20))
    lang = Column(Integer)
    share = Column(Boolean)
    judge_time = Column(DateTime)
    memory_usage = Column(Integer)
    time_usage = Column(Integer)
    result = Column(String)
