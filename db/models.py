#!/usr/bin/env python
#coding=utf-8
import six
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, DateTime, Boolean, Text, Float
from sqlalchemy.orm import relationship, backref, object_mapper
import session as Session
Base = declarative_base()
from sqlalchemy import DDL
from sqlalchemy import event
from base import OJBase
# this copy from https://github.com/openstack/nova/
# and the classmethod copy from http://www.keakon.net/


class User(Base, OJBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    school = Column(String(100))
    reg_time = Column(DateTime)
    last_sign_in = Column(DateTime)
    last_ip = Column(String(20))
    submit = Column(Integer)
    solved = Column(Integer)
    share_code = Column(Boolean)
    group_id = Column(Text)
    source_code = relationship("Source", backref="user")


class Contest(Base, OJBase):
    __tablename__ = 'contest'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    private = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    enabled = Column(Boolean)
    contest_problem = relationship("Contest_Problem", backref="contest")


class Problem(Base, OJBase):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True)
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
    spj = Column(Boolean)
    accepted = Column(Integer)
    submitted = Column(Integer)
    enabled = Column(Boolean)
    source_code = relationship("Source", backref="problem")
    contest_problem = relationship("Contest_Problem", backref="problem")


class Source(Base, OJBase):
    __tablename__ = 'source'

    id = Column(Integer, primary_key=True)
    source_code = Column(Text)
    length = Column(Integer)
    submit_time = Column(DateTime)
    submit_ip = Column(String(20))
    lang = Column(Integer)
    share = Column(Boolean)
    judge_time = Column(DateTime)
    memory_usage = Column(Integer)
    time_usage = Column(Integer)
    result = Column(String(20))
    contest_id = Column(Integer)

    user_id = Column(Integer,
                     ForeignKey("user.id",
                                ondelete='CASCADE',
                                onupdate='CASCADE'))
    problem_id = Column(Integer,
                        ForeignKey("problem.id",
                                   ondelete='CASCADE',
                                   onupdate='CASCADE'))


class Contest_Problem(Base, OJBase):
    __tablename__ = "contest_problem"

    title = Column(Text)
    num = Column(Integer)
    id = Column(Integer, primary_key=True)
    contest_id = Column(Integer,
                        ForeignKey("contest.id",
                                   ondelete='CASCADE',
                                   onupdate='CASCADE'))
    problem_id = Column(Integer,
                        ForeignKey("problem.id",
                                   ondelete='CASCADE',
                                   onupdate='CASCADE'))


event.listen(Problem.__table__,
             "after_create",
             DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 1001;"))
