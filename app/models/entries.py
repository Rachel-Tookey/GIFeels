from sqlalchemy import Column, String, Integer, ForeignKey, Date
from app import db


class Entries(db.Model):

    id = Column('id', Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    entry_date = Column('entry_date', Date)

    emotion = Column('emotion', String(50))

    giphy_url = Column('giphy_url', String(250))

    choice = Column('choice', String(50))

    content = Column('response', String(500))

    diary_entry = Column('diary_entry', String(500), nullable=True)
