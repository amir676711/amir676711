from pydantic import BaseModel

class CreateCatalogRequest(BaseModel):
    file : str
