import enum
from core.db import Base
from core.db.mixins import DefaultMixin
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, JSON, Sequence, BigInteger
from sqlalchemy.dialects.postgresql import UUID
import uuid



class StoreStatus(enum.Enum):
    DISABLED = 'disabled'
    ACTIVE = 'active'
    CLOSED = 'closed'


class StoreType(enum.Enum):
    DARKSTORE = 'DARKSTORE'
    SHOP = 'SHOP'
    DC = 'DC'

    def __len__(self):
        pass

class Stores(Base, DefaultMixin):
    __tablename__ = "store"
    #lsn_seq = Sequence(f"{__tablename__}_lsn_seq", metadata=Base.metadata, start=1)

    external_id = Column(String, nullable=False, unique=True, index=True)
    title = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    status = Column(Enum(StoreStatus), default=StoreStatus.DISABLED, nullable=False)
    type = Column(Enum(StoreType), default=StoreType.DARKSTORE, nullable=False)
    vars = Column(JSON, default={}, nullable=True)
