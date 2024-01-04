from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,UUID,DateTime,String
from sqlalchemy.orm import relationship
import uuid
from .database import Base
from .Types import BinaryUUID
import typing
import types


class product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True, index=True)
    Name = Column(String(30))
    Minimal_Description = Column(String(3000))
    Picture_Url = Column(String(3000))

class project(Base):
    __tablename__ = "project"
    id = Column(Integer,primary_key=True, index=True)
    Title = Column(String(30))
    Text = Column(String(3000))
    PictureUrlproject = Column(String(3000))


class aboutus(Base):
    __tablename__ = "aboutus"
    id = Column(Integer,primary_key=True, index=True)
    Title = Column(String(30))
    Text = Column(String(3000))
    PictureUrlaboute = Column(String(3000))

class contactus(Base):
    __tablename__ = "contactus"
    id = Column(Integer,primary_key=True, index=True)
    Name = Column(String(30))
    Family = Column(String(30))
    Email = Column(String(300))
    Description = Column(String(3000))
    CreateAt = Column(DateTime)


class catalog(Base):
    __tablename__ = "catalog"
    id = Column(Integer,primary_key=True, index=True)
    File = Column(String(300))

class socialicon(Base):
    __tablename__ = "socialicon"
    id = Column(Integer,primary_key=True, index=True)
    Picture = Column(String(300))
    LinkAddress = Column(String(3000))

class companycustomers(Base):
    __tablename__ = "companycustomers"
    id = Column(Integer,primary_key=True, index=True)
    LogoPicture = Column(String(300))

# class home(Base):
#     __tablename__ = "home"
#     id = Column('id',primary_key=True, index=True)
#     # Title = Column(String(30))
#     Slide = Column(String(3000))
#     DescriptionCompany = Column(String(3000))
#     TitleOfDescriptionCompany = Column(String(300))



    