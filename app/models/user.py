from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __table__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(10))
    password = Column(String(128))
    email = Column(String(100))
    school = Column(String(100))
    reg_time = Column(DateTime)
    last_sign_in = Column(DateTime)
    last_ip = Column(String(20))
    submit = Column(Integer)
    solved = Column(Integer)
    share_code = Column(Boolean)
    group_id = Column(Text)
