from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class socialiconRespones(BaseModel):
    id : int
    Picture : str
    LinkAddress : str