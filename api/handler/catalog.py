from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database.crud import catalog
from database import models
from sqlalchemy.orm import Session
from database.crud import product
from api.requests.catalog import CreateCatalogRequest
from api.respones.catalog import catalogRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/catalog")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all",status_code=200,response_model=list[catalogRespones])
def Getcatalogs(db:Session=Depends(get_db)):
    catalog=catalog.get_cataloges(db)
    return catalog

@router.get("/{id}",status_code=200,response_model=list[catalogRespones])
def get_catalog_ByID(id:int,db:Session=Depends(get_db)):
    catalog=catalog.get_catalog_ByID(db,id)

    response=[]
    for item in catalog:
            response.append(catalogRespones(
                file = item.file
        ))
    return response

@router.post("/",status_code=201,response_model=BaseMessage)
def create_product(req :CreateCatalogRequest,db: Session = Depends(get_db)):
    if len(req.file) < 1:
            raise HTTPException(status_code=400,detail=" قایل را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    catalog=catalog.catalog(db=db,file=req.file)
    return BaseMessage(message="فایل باموفقیت ثبت شد")


@router.delete("/{id}",response_model=BaseMessage)
def Deletecataloge(id:int,db:Session=Depends(get_db)):
    delete_catalogge=catalog.delete_cataloge(db,id)
    if delete_catalogge is None :
        raise HTTPException(status_code=404,detail="فایل مورد نظر یافت نشد")
    if not catalog.delete_cataloge(db,id) :
        raise HTTPException(status_code=400,detail="در حذف فایل خطا رخ داده است")
    return BaseMessage(message="فایل مورد نظر با موفقیت حذف شد")

