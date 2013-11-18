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
# this copy from https://github.com/openstack/nova/blob/master/nova/openstack/common/db/sqlalchemy/models.py


class ModelBase(object):
    """Base class for models."""
    __table_initialized__ = False

    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}

    def save(self, session=None):
        """Save this object."""
        if not session:
            session = Session.get_session()
        # NOTE(boris-42): This part of code should be look like:
        #                       sesssion.add(self)
        #                       session.flush()
        #                 But there is a bug in sqlalchemy and eventlet that
        #                 raises NoneType exception if there is no running
        #                 transaction and rollback is called. As long as
        #                 sqlalchemy has this bug we have to create transaction
        #                 explicity.
        #with session.begin(subtransactions=True):
        session.add(self)
        try:
            session.flush()
            session.commit()
        except:
            session.rollback()

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __iter__(self):
        columns = dict(object_mapper(self).columns).keys()
        # NOTE(russellb): Allow models to specify other keys that can be looked
        # up, beyond the actual db columns.  An example would be the 'name'
        # property for an Instance.
        if hasattr(self, '_extra_keys'):
            columns.extend(self._extra_keys())
        self._i = iter(columns)
        return self

    def next(self):
        n = six.advance_iterator(self._i)
        return n, getattr(self, n)

    def update(self, values):
        """Make the model object behave like a dict."""
        for k, v in six.iteritems(values):
            setattr(self, k, v)

    def iteritems(self):
        """Make the model object behave like a dict.

        Includes attributes from joins.
        """
        local = dict(self)
        joined = dict([(k, v) for k, v in six.iteritems(self.__dict__)
                      if not k[0] == '_'])
        local.update(joined)
        return local.iteritems()


class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())


class SoftDeleteMixin(object):
    deleted_at = Column(DateTime)
    deleted = Column(Integer, default=0)

    def soft_delete(self, session=None):
        """Mark this object as deleted."""
        self.deleted = self.id
        self.deleted_at = datetime.now()
        self.save(session=session)


class OJBase(SoftDeleteMixin,
             TimestampMixin,
             ModelBase):
    metadata = None


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

    user_id = Column(Integer, ForeignKey("user.id"))
    problem_id = Column(Integer, ForeignKey("problem.id"))


class Contest_Problem(Base, OJBase):
    __tablename__ = "contest_problem"

    title = Column(Text)
    num = Column(Integer)
    id = Column(Integer, primary_key=True)
    contest_id = Column(Integer, ForeignKey("contest.id"))
    problem_id = Column(Integer, ForeignKey("problem.id"))

event.listen(Problem.__table__,
             "after_create",
             DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 1001;"))
