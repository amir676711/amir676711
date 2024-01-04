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
from api.respones.product import ProductRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/product")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all",status_code=200,response_model=list[ProductRespones])
def GetAllProducts(db:Session=Depends(get_db)):
    product=product.get_Allproducts(db)
    response=[]
    for item in product:
            response.append(ProductRespones(
            id=item.id,
            Name=item.Name,
            Minimal_Description=item.Minimal_Description
        ))
    return response

@router.get("/{id}",status_code=200,response_model=list[ProductRespones])
def get_product(id:int,db:Session=Depends(get_db)):
    product=product.get_product(db,id)

    response=[]
    for item in product:
            response.append(ProductRespones(
            id=item.id,
            Name=item.Name,
            Minimal_Description=item.Minimal_Description
        ))
    return response

@router.post("/",status_code=201,response_model=BaseMessage)
def create_product(req :CreateProductRequest,db: Session = Depends(get_db)):
    if len(req.Title) < 1:
            raise HTTPException(status_code=400,detail=" نام محصول را وارد کنید")
    if len(req.Minimal_Description) < 1:
            raise HTTPException(status_code=400,detail=" توضیحات را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    product=product.create_product(db=db,Name=req.Name,Minimal_Description=req.Minimal_Description,Picture_Url=req.Picture_Url)
    return BaseMessage(message="محصول باموفقیت ثبت شد")

@router.patch("/",status_code=201,response_model=BaseMessage)
def EditproductRequest(req :EditeCreateProductRequest,db: Session = Depends(get_db)):
    if len(req.Name) < 1:
        raise HTTPException(status_code=400,detail=" نام را وارد کنید")
    if len(req.Minimal_Description) < 1:
        raise HTTPException(status_code=400,detail=" توضیحات محصول را وارد کنید")
    if req is None:
        raise HTTPException(status_code=400,detail=" عنوان را وارد کنید")
        
    editproduct=product.get_product(db,req.id)
    if editproduct is None:
        raise HTTPException(status_code=404,detail="محصول مورد نظر یافت نشد")
    editproduct.Name=req.Name
    editproduct.Minimal_Description=req.Minimal_Description
    editproduct.Picture_Url=req.Picture_Url
    db.commit()

    return BaseMessage(message="محصول باموفقیت ویرایش شد")


@router.delete("/{id}",response_model=BaseMessage)
def DeleteRole(id:int,db:Session=Depends(get_db)):
    delete_product=product.get_product(db,id)
    if delete_product is None :
        raise HTTPException(status_code=404,detail="محصول مورد نظر یافت نشد")
    if not product.delete_product(db,id) :
        raise HTTPException(status_code=400,detail="در حذف محصول خطا رخ داده است")
    return BaseMessage(message="محصول مورد نظر با موفقیت حذف شد")

