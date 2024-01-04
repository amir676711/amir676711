from sqlalchemy.orm import Session
from database import models
from api.requests.aboutus import CreateAboutUsRequest
from datetime import datetime


def get_cataloges(db: Session):
    return db.query(models.catalog).all()
def get_cataloge_BYID(db:Session,id:int):
    return db.query(models.catalog).filter(models.catalog.id==id).first()

def create_cataloge(db:Session,file:str):
    createfile = models.catalog(file=file)
    db.add(createfile)
    db.commit()
    db.refresh(createfile)
    return createfile

def delete_cataloge(db:Session,id:int):
    try:
        deletecatalog = db.query(models.catalog).filter(models.catalog.id==id).first()
        db.delete(deletecatalog)
        db.commit()
    except:
        return False
    return True

