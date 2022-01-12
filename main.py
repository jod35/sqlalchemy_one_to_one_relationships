from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


conn_str='sqlite:///'+ os.path.join(BASE_DIR,'data.db')

engine=create_engine(conn_str)

Base=declarative_base()


"""
    class Parent:
        id:int pk
        name: str


    class Child:
        id:int pk
        name:str
        parent_id:int fk (parent)
"""


class Parent(Base):
    __tablename__='parents'
    id=Column(Integer(),primary_key=True)
    name=Column(String(25),nullable=False)
    child=relationship('Child',back_populates='parent',uselist=False,cascade="all, delete")

    def __repr__(self):
        return f"<Parent {self.id}>"


class Child(Base):
    __tablename__='children'
    id=Column(Integer(),primary_key=True)
    name=Column(String(25),nullable=False)
    parent_id=Column(Integer(),ForeignKey('parents.id',ondelete="CASCADE"))
    parent=relationship('Parent',back_populates='child')


    def __repr__(self):
        return f"<Child {self.id}>"



Base.metadata.create_all(engine)
session=sessionmaker()(bind=engine)







