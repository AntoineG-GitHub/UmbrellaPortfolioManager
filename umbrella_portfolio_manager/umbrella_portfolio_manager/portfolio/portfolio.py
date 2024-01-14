from typing import List
from pydantic import BaseModel

class Portfolio(BaseModel):
    owner: str