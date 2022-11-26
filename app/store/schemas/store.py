from pydantic import BaseModel, Field, Json
from app.store.models.store import Types, Statuses
from typing import Optional
from uuid import UUID


class StoreListResponce(BaseModel):
    store_id: UUID
    external_id: str
    title: str
    email: str
    status: Statuses
    type = Types
    vars = Optional[Json]

    class Config:
        orm_mode = True


class StoreCreate(BaseModel):
    title: str = Field(..., description="Title")
    external_id: str = Field(..., description="External ID")
    email: str = Field(..., description="Email")
    type: Optional[Types] = Field(..., description="Store type")

