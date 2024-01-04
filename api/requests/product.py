from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateProductRequest(BaseModel):
    Name : str
    Minimal_Description : str
    Picture_Url : str

class EditeCreateProductRequest(BaseModel):
    Name : str
    Minimal_Description : str
    Picture_Url : str