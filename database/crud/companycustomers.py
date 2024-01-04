from sqlalchemy.orm import Session
from database import models
from api.requests.product import CreateProductRequest,EditproductRequest
from datetime import datetime


def get_logo(db: Session):
    return db.query(models.companycustomers).all()

def get_logo_ByID(db:Session,id:int):
    return db.query(models.companycustomers).filter(models.companycustomers.id==id).first()

def create_logo(db:Session,LogoPicture:str):
    new_logo = models.companycustomers(LogoPicture=LogoPicture)
    db.add(new_logo)
    db.commit()
    db.refresh(new_logo)
    return new_logo

def delete_logo(db:Session,id=int):
    try:
        logod = db.query(models.companycustomers).filter(models.companycustomers.id==id).first()
        db.delete(logod)
        db.commit()
    except:
        return False
    return True

