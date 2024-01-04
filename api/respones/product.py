from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ProductRespones(BaseModel):
    Name : str
    Minimal_Description : str
    Picture_Url : str
