

from typing import Any, Optional
from pydantic import BaseModel

class CustomResponse(BaseModel):
    status: int
    message: Optional[str]
    data: Any