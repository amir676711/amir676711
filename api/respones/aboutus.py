
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AboutUsRespones(BaseModel):
    id : int
    Title : str
    Text : str
    PictureUrlaboute : str
