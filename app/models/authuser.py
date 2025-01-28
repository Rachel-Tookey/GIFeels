from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from app import db


class AuthUser(db.Model):

    id = Column('id', Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    auth0_id = Column('auth0_id', String(100), unique=True, nullable=False)

    name = Column('name', String(100), nullable=False)

    accept_tos = Column('accept_tos', Boolean, nullable=False)

