import enum
from core.db import Base
from core.db.mixins import DefaultMixin

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, JSON, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid


class ShelfStatuses(enum.Enum):
    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    DELETED = 'DELETED'


class ShelfType(enum.Enum):
    INN = 'INN'
    OUT = 'OUT'
    TRASH = 'TRASH'
    LOSTFOUND = 'LOSTFOUND'
    STORE = 'STORE'


class StorageType(DefaultMixin, Base):
    __tablename__ = "storage_type"
    storage_type_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False, unique=True)
    code = Column(String(50), nullable=False, unique=True, index=True)


class Shelves(DefaultMixin, Base):
    __tablename__ = "shelf"
    title = Column(String, nullable=False, unique=True)
    barcode = Column(String, nullable=False, unique=True, index=True)
    status = Column(Enum(ShelfStatuses), default=ShelfStatuses.ACTIVE, nullable=False)
    type = Column(Enum(ShelfType), default=ShelfType.STORE, nullable=False)
    storage_tags = Column(ARRAY(String(50)))
    vars = Column(JSON, default={}, nullable=True)
