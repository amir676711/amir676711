from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateSocialiconRequest(BaseModel):
    Picture : str
    LinkAddress : str

class EditeSocialiconRequest(BaseModel):
    id : int
    Picture : str
    LinkAddress : str