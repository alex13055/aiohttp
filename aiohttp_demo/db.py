from sqlalchemy import MetaData, Column, Integer, String, Table, Date, ForeignKey


metadata = MetaData()

news = Table('news', metadata,
    Column('id', Integer, primary_key = True),
    Column('title', String(20), nullable = False),
    Column('date', Date), # do ISO
    Column('body', String(20), nullable = False),
    Column('deleted', String(20), nullable = False)
)

comments = Table('comments', metadata,
    Column('id', Integer, primary_key = True),
    Column('news_id', Integer, ForeignKey('news_id', ondelete = 'CASCADE')),
    Column('date', Date), # do ISO
    Column('comment', String(20), nullable = False)
)




