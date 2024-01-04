from sqlalchemy.orm import Session
from database import models
from api.requests.project import CreateProjectRequest,EditeProjectRequest
from datetime import datetime


def get_Allsocialicon(db: Session):
    return db.query(models.socialicon).all()

def get_icon_BYID(db:Session,id:int):
    return db.query(models.socialicon).filter(models.socialicon.id==id).first()

def create_socialicon(db:Session,Text:str,Title:str,Picture_Urlproject:str):
    new_icon = models.socialicon(Picture=Picture,LinkAddress=LinkAddress)
    db.add(new_icon)
    db.commit()
    db.refresh(new_icon)
    return new_icon

def delete_socialicon(db:Session,id=int):
    try:
        icon = db.query(models.socialicon).filter(models.socialicon.id==id).first()
        db.delete(icon)
        db.commit()
    except:
        return False
    return True

