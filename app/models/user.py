# A model class for Product items
# See https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel, ValidationError, ValidationInfo, field_validator
from typing import Optional

class User(BaseModel):
    email: str
    password: str