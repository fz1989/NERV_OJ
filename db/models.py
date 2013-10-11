from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(10), unique = True, nullable = False)
    password = Column(String(128), nullable = False)
    email = Column(String(100), unique = True, nullable = False)
    school = Column(String(100))
    reg_time = Column(DateTime)
    last_sign_in = Column(DateTime)
    last_ip = Column(String(20))
    submit = Column(Integer)
    solved = Column(Integer)
    share_code = Column(Boolean)
    group_id = Column(Text)

class Contest(Base):
    __table__ = 'contests'

    id = Column(Integer, primary_key = True)
    title = Column(Text)
    description =  Column(Text)
    private =  Column(Integer)
    start_time =  Column(DateTime)
    end_time =  Column(DateTime)
    enabled =  Column(Boolean)

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
