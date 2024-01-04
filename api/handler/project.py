from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database.crud import project
from database import models
from sqlalchemy.orm import Session
from database.crud import project
from api.requests.project import CreateProjectRequest,EditeProjectRequest
from api.respones.project import projectRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/project")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all",status_code=200,response_model=list[projectRespones])
def GetAllprojects(db:Session=Depends(get_db)):
    project=project.get_Allprojects(db)
    response=[]
    for item in project:
            response.append(ProductRespones(
            id=item.id,
            Title=item.Title,
            Text=item.Text,
            Picture_Urlprojec=item.Picture_Urlproject
        ))
    return response

@router.get("/{id}",status_code=200,response_model=list[projectRespones])
def get_product(id:int,db:Session=Depends(get_db)):
    project=project.get_project(db,id)

    response=[]
    for item in project:
            response.append(projectRespones(
            id=item.id,
            Title=item.Title,
            Text=item.Text,
            Picture_Urlproject=item.Picture_Urlproject
        ))
    return response

@router.post("/",status_code=201,response_model=BaseMessage)
def create_project(req :CreateProjectRequest,db: Session = Depends(get_db)):
    if len(req.Title) < 1:
            raise HTTPException(status_code=400,detail=" عنوان پروژه را وارد کنید")
    if len(req.Text) < 1:
            raise HTTPException(status_code=400,detail=" توضیحات را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    project=project.create_project(db=db,Title=req.Title,Text=req.Text,Picture_Urlproject=req.Picture_Urlproject)
    return BaseMessage(message="پروژه باموفقیت ثبت شد")

@router.patch("/",status_code=201,response_model=BaseMessage)
def Editproject(req :EditeProjectRequest,db: Session = Depends(get_db)):
    if len(req.Title) < 1:
        raise HTTPException(status_code=400,detail=" عنوان را وارد کنید")
    if len(req.Text) < 1:
        raise HTTPException(status_code=400,detail=" توضیحات پروژه را وارد کنید")
    if req is None:
        raise HTTPException(status_code=400,detail=" پروژه را وارد کنید")
        
    editproject=project.get_project(db,req.id)
    if editproject is None:
        raise HTTPException(status_code=404,detail="پروژه مورد نظر یافت نشد")
    editproject.Title=req.Title
    editproject.Text=req.Text
    editproject.Picture_Urlproject=req.Picture_Urlproject
    db.commit()

    return BaseMessage(message="پروژه باموفقیت ویرایش شد")


@router.delete("/{id}",response_model=BaseMessage)
def Deleteproject(id:int,db:Session=Depends(get_db)):
    delete_project=project.get_project(db,id)
    if delete_project is None :
        raise HTTPException(status_code=404,detail="پروژه مورد نظر یافت نشد")
    if not product.delete_product(db,id) :
        raise HTTPException(status_code=400,detail="در حذف پروژه خطا رخ داده است")
    return BaseMessage(message="پروژه مورد نظر با موفقیت حذف شد")

