from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Problem(Base):
    __table__ = 'problems'

    id = Column(Integer, primary_key = True)
    title = Column(Text)
    description = Column(Text)
    input = Column(Text)
    output = Column(Text)
    sample_input = Column(Text)
    sample_output = Column(Text)
    hint = Column(Text)
    source = Column(Text)
    time_limit = Column(Integer)
    memory_limit = Column(Integer)
    spj =  Column(Boolean)
    accepted = Column(Integer)
    submitted = Column(Integer)
    enabled = Column(Boolean)

