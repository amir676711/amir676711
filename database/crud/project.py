from sqlalchemy.orm import Session
from database import models
from api.requests.project import CreateProjectRequest,EditeProjectRequest
from datetime import datetime


def get_Allprojects(db: Session):
    return db.query(models.project).all()

def get_project(db:Session,id:int):
    return db.query(models.product).filter(models.product.id==id).first()

def create_project(db:Session,Text:str,Title:str,Picture_Urlproject:str):
    new_project = models.product(Text=Text,Name=Name,Picture_Urlproject=Picture_Urlproject)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def delete_project(db:Session,id=int):
    try:
        project = db.query(models.project).filter(models.project.id==id).first()
        db.delete(project)
        db.commit()
    except:
        return False
    return True

