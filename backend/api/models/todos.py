from typing import Optional

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str = Field(index=True)
    description: str = Field(index=True)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "hello world",
                "description": "こんにちは、せかい。",
            }
        }


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TodoCreate(TodoBase):
    title: Optional[str] = ""
    description: Optional[str] = ""


class TodoRead(TodoBase):
    id: int


class TodoUpdate(TodoBase):
    title: Optional[str] = ""
    description: Optional[str] = ""
