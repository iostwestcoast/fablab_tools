from typing import Optional

from sqlmodel import Field, SQLModel


class Tools(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    room: int
    type: str
    