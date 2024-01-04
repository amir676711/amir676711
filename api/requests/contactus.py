from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateContactRequest(BaseModel):
    Name : str
    Family : str
    Email : str
    Description : str

class EditeContactUsRequest(BaseModel):
    id : int
    Name : str
    Family : str
    Email : str
    Description : str
