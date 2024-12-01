# A model class for Category items
# See https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel, validator
from typing import Optional

class Category(BaseModel):
    id: Optional[int] = 0 # default for new product
    name: str
    description: str