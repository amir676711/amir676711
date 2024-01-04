from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database.crud import aboutus
from database import models
from sqlalchemy.orm import Session
from database.crud import product
from api.requests.aboutus import CreateAboutUsRequest,EditeAboutUsRequest
from api.respones.aboutus import AboutUsRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/aboutus")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all",status_code=200,response_model=list[AboutUsRespones])
def GetAboutus(db:Session=Depends(get_db)):
    getAboutus=aboutus.get_Allabouteus(db)
    response=[]
    for item in getAboutus:
            response.append(AboutUsRespones(
            id=item.id,
            Title=item.Title,
            Text=item.Text
        ))
    return response


@router.post("/",status_code=201,response_model=BaseMessage)
def create_aboutUS(req :CreateAboutUsRequest,db: Session = Depends(get_db)):
    if len(req.Title) < 1:
            raise HTTPException(status_code=400,detail=" عنوان را وارد کنید")
    if len(req.Text) < 1:
            raise HTTPException(status_code=400,detail=" توضیحات را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    createaboutus=aboutus.create_aboutus(db=db,Title=req.Title,Text=req.Text,PictureUrlaboute=req.PictureUrlaboute)
    return BaseMessage(message="محتوا باموفقیت ثبت شد")

@router.patch("/",status_code=201,response_model=BaseMessage)
def EditAboutUsRequest(req :EditeAboutUsRequest,db: Session = Depends(get_db)):
    if len(req.Text) < 1:
        raise HTTPException(status_code=400,detail=" توضیحات را وارد کنید")
    if len(req.Title) < 1:
        raise HTTPException(status_code=400,detail=" عنوان محصول را وارد کنید")
    if req is None:
        raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
        
    editaboutus=aboutus.get_Allabouteus(db,req.id)
    if editaboutus is None:
        raise HTTPException(status_code=404,detail="محتوا مورد نظر یافت نشد")
    editaboutus.Title=req.Title
    editaboutus.Text=req.Text
    editaboutus.PictureUrlaboute=req.PictureUrlaboute
    db.commit()

    return BaseMessage(message="محتوا باموفقیت ویرایش شد")


@router.delete("/{id}",response_model=BaseMessage)
def DeleteَAboutUs(id:int,db:Session=Depends(get_db)):
    delete_aboutUS=aboutus.get_Allabouteus(db)
    if delete_aboutUS is None :
        raise HTTPException(status_code=404,detail=" محتوا نظر یافت نشد")
    if not delete_aboutUS.delete_aboutUS(db) :
        raise HTTPException(status_code=400,detail="در حذف محتوا خطا رخ داده است")
    return BaseMessage(message="محنوا مورد نظر با موفقیت حذف شد")

