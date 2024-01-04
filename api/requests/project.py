from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateProjectRequest(BaseModel):
    Title : str
    Text : str
    Picture_Urlproject : str

class EditeProjectRequest(BaseModel):
    id : int
    Title : str
    Text : str
    Picture_Urlproject : str