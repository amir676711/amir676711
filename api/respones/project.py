from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class projectRespones(BaseModel):
    id : int
    Title : str
    Text : str
    Picture_Urlproject : str