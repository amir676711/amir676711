from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database.crud import project
from database import models
from sqlalchemy.orm import Session
from database.crud import project
from api.requests.socialicon import CreateSocialiconRequest,EditeSocialiconRequest
from api.respones.socialicon import socialiconRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/socialicon")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all",status_code=200,response_model=list[socialiconRespones])
def GetAllsocialicon(db:Session=Depends(get_db)):
    socialicon=socialicon.GetAllsocialicon(db)
    response=[]
    for item in socialicon:
            response.append(socialiconRespones(
            Picture=item.Picture,
            LinkAddress=item.LinkAddress
        ))
    return response

@router.get("/{id}",status_code=200,response_model=list[socialiconRespones])
def get_socialicon_BYID(id:int,db:Session=Depends(get_db)):
    socialiconid=socialiconid.get_socialicon_BYID(db,id)

    response=[]
    for item in project:
            response.append(socialiconRespones(
            id=item.id,
            Picture=item.Picture,
            LinkAddress=item.LinkAddress
        ))
    return response

@router.post("/",status_code=201,response_model=BaseMessage)
def create_project(req :CreateSocialiconRequest,db: Session = Depends(get_db)):
    if len(req.Picture) < 1:
            raise HTTPException(status_code=400,detail="عکس ایکون رسانه را وارد کنید")
    if len(req.LinkAddress) < 1:
            raise HTTPException(status_code=400,detail=" لینک ایکون رسانه را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    socialiconcreate=socialicon.create_socialicon(db=db,Picture=req.Picture,LinkAddress=req.LinkAddress)
    return BaseMessage(message="ایکون رسانه اجتماعی باموفقیت ثبت شد")

@router.patch("/",status_code=201,response_model=BaseMessage)
def Editproject(req :EditeSocialiconRequest,db: Session = Depends(get_db)):
    if len(req.Picture) < 1:
            raise HTTPException(status_code=400,detail="عکس ایکون رسانه را وارد کنید")
    if len(req.LinkAddress) < 1:
            raise HTTPException(status_code=400,detail=" لینک ایکون رسانه را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
        
    editsocial=socialicon.get_socialicon_BYID(db,req.id)
    if editproject is None:
        raise HTTPException(status_code=404,detail="پروژه مورد نظر یافت نشد")
    editsocial.Picture=req.Picture
    editsocial.LinkAddress=req.LinkAddress
    db.commit()

    return BaseMessage(message="ایکون رسانه اجتماعی باموفقیت ویرایش شد")


@router.delete("/{id}",response_model=BaseMessage)
def Deletesocialicon(id:int,db:Session=Depends(get_db)):
    delete_socialicon=socialicon.delete_socialicon(db,id)
    if delete_socialicon is None :
        raise HTTPException(status_code=404,detail="ایکون رسانه نظر یافت نشد")
    if not socialicon.delete_socialicon(db,id) :
        raise HTTPException(status_code=400,detail="در حذف ایکون رسانه خطا رخ داده است")
    return BaseMessage(message="ایکون رسانه مورد نظر با موفقیت حذف شد")

