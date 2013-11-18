#!/usr/bin/env python
#coding=utf-8
import six
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, DateTime, Boolean, Text, Float
from sqlalchemy.orm import relationship, backref, object_mapper
from sqlalchemy import func, or_, not_
import session as Session


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

    @classmethod
    def get_by_id(cls, id, session=None, columns=None, lock_mode=None):
        if not session:
            session = Session.get_session()
        if hasattr(cls, 'id'):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.id == id)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_by_name(cls, name, session=None, columns=None, lock_mode=None):
        if not session:
            session = Session.get_session()
        if hasattr(cls, 'name'):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.name == name)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_by_title(cls, title, session=None, columns=None, lock_mode=None):
        if not session:
            session = Session.get_session()
        if hasattr(cls, 'title'):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.title == title)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_all(cls,
                session=None,
                columns=None,
                offset=None,
                limit=None,
                order_by=None,
                lock_mode=None):
        if not session:
            session = Session.get_session()
        if columns:
            if isinstance(columns, (tuple, list)):
                query = session.query(*columns)
            else:
                query = session.query(columns)
                if isinstance(columns, str):
                    query = query.select_from(cls)
        else:
            query = session.query(cls)
        if order_by is not None:
            if isinstance(order_by, (tuple, list)):
                query = query.order_by(*order_by)
            else:
                query = query.order_by(order_by)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.all()

    @classmethod
    def count_all(cls, session=None, lock_mode=None):
        if not session:
            session = Session.get_session()
        query = session.query(func.count('*')).select_from(cls)
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.scalar()

    @classmethod
    def id_exist(cls, id, session=None, lock_mode=None):
        if not session:
            session = Session.get_session()

        if hasattr(cls, 'id'):
            query = session.query(func.count('*')).select_from(cls).filter(cls.id == id)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            return query.scalar() > 0
        return False

    @classmethod
    def name_exist(cls, name, session=None, lock_mode=None):
        if not session:
            session = Session.get_session()

        if hasattr(cls, 'name'):
            query = session.query(func.count('*')).select_from(cls).filter(cls.name == name)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            return query.scalar() > 0
        return False

    @classmethod
    def set_attr(cls, id, attr, value, session=None):
        if not session:
            session = Session.get_session()

        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update({
                attr: value
            })
            session.commit()

    @classmethod
    def set_attrs(cls, id, attrs, session=None):
        if not session:
            session = Session.get_session()
        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update(attrs)
            session.commit()


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
