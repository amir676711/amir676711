from sqlalchemy.orm import Session
from database import models
from api.requests.aboutus import CreateAboutUsRequest
from datetime import datetime


def get_Allabouteus(db: Session):
    return db.query(models.aboutus).all()


def create_aboutus(db:Session,Text:str,Title:str,PictureUrlaboute:str):
    aboutUsC = models.aboutUs(Text=Text,Title=Title,PictureUrlaboute=PictureUrlaboute)
    db.add(aboutUsC)
    db.commit()
    db.refresh(aboutUsC)
    return aboutUsC

def delete_aboutus(db:Session,id=int):
    try:
        aboutUsDelete = db.query(models.aboutus).filter(models.aboutus.id==id).first()
        db.delete(aboutUsDelete)
        db.commit()
    except:
        return False
    return True

