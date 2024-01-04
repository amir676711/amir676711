from sqlalchemy.orm import Session
from database import models
from api.requests.product import CreateProductRequest,EditproductRequest
from datetime import datetime


def get_Allcontact(db: Session):
    return db.query(models.contactus).all()

def get_contact_ByID(db:Session,id:int):
    return db.query(models.contactus).filter(models.contactus.id==id).first()

def create_contact(db:Session,Name:str,Family:str,Email:str,Description:str):
    new_contact = models.contactus(Name=Name,Family=Family,Description=Description,CreateAt=datetime.now())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

# def delete_contact(db:Session,id=int):
#     try:
#         product = db.query(models.product).filter(models.product.id==id).first()
#         db.delete(product)
#         db.commit()
#     except:
#         return False
#     return True

