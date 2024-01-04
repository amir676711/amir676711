from sqlalchemy.orm import Session
from database import models
from datetime import datetime


def get_Allproducts(db: Session):
    return db.query(models.product).all()

def get_product(db:Session,id:int):
    return db.query(models.product).filter(models.product.id==id).first()

def create_product(db:Session,text:str,Name:str,Picture_Url:str):
    new_product = models.product(text=text,Name=Title,Picture_Url=Picture_Url)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def delete_product(db:Session,id=int):
    try:
        product = db.query(models.product).filter(models.product.id==id).first()
        db.delete(product)
        db.commit()
    except:
        return False
    return True

