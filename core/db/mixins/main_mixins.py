from sqlalchemy import Column, DateTime, func, BigInteger, Sequence, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import declarative_mixin
from core.db import Base
import uuid


class DefaultMixin():

    @declared_attr
    def lsn_sec(cls):
        return Sequence(
            f"{cls.__tablename__}_seq",
            metadata=Base.metadata
        )
    @declared_attr
    def lsn(cls):
        return Column(
            BigInteger,
            Sequence(f'lsn_{cls.__tablename__}_seq'),
            onupdate=cls.lsn_sec.next_value(),
            nullable=False
        )

    @declared_attr
    def id(cls):
        return Column(
            UUID,
            default=uuid.uuid4,
            nullable=False,
            primary_key=True
        )

    @declared_attr
    def company_id(cls):
        return Column(
            UUID(as_uuid=True),
            nullable=False,
            index=True
        )

    @declared_attr
    def created_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            nullable=False
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )