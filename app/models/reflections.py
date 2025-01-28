from sqlalchemy import Column, String, Integer, ForeignKey, Date
from app import db


class Reflections(db.Model):

    id = Column('id', Integer, primary_key=True)

    entry_id = Column(Integer, ForeignKey('entries.id', ondelete='CASCADE'), nullable=False)

    reflection_date = Column('reflection_date', Date, nullable=False)

    content = Column('content', String(500), nullable=False)
