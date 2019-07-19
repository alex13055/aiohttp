from sqlalchemy import create_engine, MetaData

from db import news, comments
from settings import config

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind = engine, tables = [news, comments])
