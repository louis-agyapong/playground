"""
Pydantic is a Pythonic model validation library.
You declare the shape of your data and the library will validate it.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    User model.
    """

    id: int
    name: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


external_data = {
    "id": 1,
    "name": "Kweku Frimpong",
    "email": "kweku.frimpong@mail.com",
    "phone": "123456789",
    "website": "https://kwekufrinpong.com",
    "company": "Kweku Frimpong Inc.",
    "created_at": "2020-01-01T00:00:00Z",
    "updated_at": "2020-01-01T00:00:00Z",
    "deleted_at": None,
}

user = User(**external_data)
print(user)
print(user.dict())
print(user.json())
print(user.id)
print(user.name)
print(user.email)
