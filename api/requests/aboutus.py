from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateAboutUsRequest(BaseModel):
    Title : str
    Text : str
    PictureUrlaboute : str

class EditeAboutUsRequest(BaseModel):
    id : int
    Title : str
    Text : str
    PictureUrlaboute : str
