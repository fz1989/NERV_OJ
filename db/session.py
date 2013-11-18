#!/usr/bin/env python
#coding=utf-8
import sys
sys.path.insert(0, '../')
import six
from sqlalchemy import *
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
from config.config import *

_ENGINE = None
_MAKER = None


def clean_up():
    global _MAKER, _ENGINE
    if _MAKER:
        _MAKER.close_all()
        _MAKER = None
    if _ENGINE:
        _ENGINE.dispose()
        _ENGINE = None


def get_session():
    global _MAKER
    maker = _MAKER
    if maker is None:
        engine = get_engine()
        maker = get_maker(engine)
    _MAKER = maker

    session = maker()
    return session


def get_maker(engine):
    return sqlalchemy.orm.sessionmaker(bind=engine)


def get_engine():
    global _ENGINE
    engine = _ENGINE
    if engine is None:
        engine = create_engine(DATA_BASE_URI, echo=True)
    _ENGINE = engine
    return engine
