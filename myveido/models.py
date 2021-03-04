from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import (Column, Date, Integer,
                    String, ForeignKey, DateTime,
                    Boolean, Table)
from sqlalchemy.orm import relationship
from myveido.settings import DYY

def db_dyy():
    """数据库DYY"""
    return create_engine(URL(**DYY))


def create_news_table(engine):
    """"""
    Base.metadata.create_all(engine)


Base = declarative_base()

'''dyy数据库'''
class Category(Base):
    __tablename__ = 'dyy_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class VideoType(Base):
    __tablename__ = 'dyy_videotype'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Star(Base):
    __tablename__ = 'dyy_star'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Director(Base):
    __tablename__ = 'dyy_director'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class VideoDetails(Base):
    __tablename__ = 'dyy_videodetails'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    thumb = Column(String(255))
    name = Column(String(255))
    alias = Column(String(255))
    time = Column(String(255))
    area = Column(String(255))
    language = Column(String(255))
    releasetime = Column(String(255))
    newtime = Column(String(255))
    television = Column(String(255))
    lianzaijs = Column(String(255))
    introduction = Column(String(255))
    heat = Column(String(255))
    score = Column(String(255))
    source = Column(String(255))
    status = Column(Integer)
    is_new = Column(Integer)

    director_id = Column(Integer, ForeignKey('dyy_director.id'))
    directors = relationship('Director', backref='videodetails_directors')

    category_id = Column(Integer, ForeignKey('dyy_category.id'))
    categorys = relationship('Category', backref='videodetails_categorys')

    videotypes = relationship(
                        "VideoType",
                        secondary="dyy_videodetails_videotypes",
                        backref="videodetails_videotype"
                    )

    stars = relationship(
                        "Star",
                        secondary="dyy_videodetails_stars",
                        backref="videodetails_star"
                    )

class VideodetailsVideotype(Base):
    __tablename__ = 'dyy_videodetails_videotypes'

    id = Column(Integer, primary_key=True)
    videodetails_id = Column(Integer, ForeignKey('dyy_videodetails.id'))
    videotype_id = Column(Integer, ForeignKey('dyy_videotype.id'))


class VideodetailsStar(Base):
    __tablename__ = 'dyy_videodetails_stars'

    id = Column(Integer, primary_key=True)
    videodetails_id = Column(Integer, ForeignKey('dyy_videodetails.id'))
    star_id = Column(Integer, ForeignKey('dyy_star.id'))



class VideoContent(Base):
    __tablename__ = 'dyy_videocontent'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    source = Column(String(255))
    url = Column(String(255))

    videodetails_id = Column(Integer, ForeignKey('dyy_videodetails.id'))
    videodetailes = relationship('VideoDetails', backref='videocontent_videodetailes')