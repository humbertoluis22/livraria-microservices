from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class ResponseData(BaseModel, Generic[T]):
    status: int
    message: str
    result: Optional[T]
    timestamp: int
