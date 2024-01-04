from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database.crud import product
from database import models
from sqlalchemy.orm import Session
from database.crud import product
from api.requests.product import CreateProductRequest,EditeCreateProductRequest
# from api.respones.product import ProductRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/contactus")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def create_product(req :CreateProductRequest,db: Session = Depends(get_db)):
    if len(req.Name) < 1:
            raise HTTPException(status_code=400,detail=" نام محصول را وارد کنید")
    if len(req.Description) < 1:
            raise HTTPException(status_code=400,detail=" توضیحات را وارد کنید")
    if len(req.Family) < 1:
            raise HTTPException(status_code=400,detail=" نام خانوادگی را وارد کنید")
    if len(req.Email) < 1:
            raise HTTPException(status_code=400,detail=" ایمیل را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    product=product.create_product(db=db,Name=req.Name,Family=req.Family,Email=req.Email,Description=req.Description)
    return BaseMessage(message=".درخواست باموفقیت ثبت شد.همکااران ما به زودی با شما تماس خواهند گرفت")

