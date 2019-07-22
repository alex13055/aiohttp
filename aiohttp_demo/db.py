from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String, Table, Date, ForeignKey, Sequence

Base = declarative_base()

class Tab_news(Base):
    __tablename__ = 'news'
    id = Column(Integer, Sequence('id'), primary_key=True)
    title = Column(String(50))
    date = Column(Date) # do ISO
    body = Column(String(20))
    deleted = Column(String(20))

    def __repr__(self):
        return "<Tab_news(id='%s', title='%s', date='%s', body = '%s', deleted = '%s')>" % (
                                self.id, self.title, self.date, self.body, self.deleted)


class Tab_comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, Sequence('id'), primary_key=True)
    news_id = Column(String(50), ForeignKey('news_id', ondelete = 'CASCADE'))
    date = Column(Date) # do ISO
    comment = Column(String(20))

    def __repr__(self):
        return "<Tab_comments(id='%s', news_id='%s', date='%s', comment = '%s')>" % (
                                self.id, self.news_id, self.date, self.comment)



