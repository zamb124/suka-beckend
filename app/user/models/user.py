from sqlalchemy import Column, Unicode, BigInteger, Boolean
from core.db.mixins.main_mixins import DefaultMixin
from core.db import Base


class User(Base, DefaultMixin):
    __tablename__ = "users"

    password = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    nickname = Column(Unicode(255), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
