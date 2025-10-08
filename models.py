from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(..., max_length=25, min_length=2, description='Имя пользователя')
