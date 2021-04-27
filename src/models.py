import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email=Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name_user=Column(String(250), nullable=False)
    image=Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey(User.id) )
    comments = Column(String(250), nullable=False)
    like= Column(Integer, nullable=False)
    post = Column(String(250), nullable=False)
    creation_date=Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ ='Comment'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey(User.id) )
    post_id=Column(Integer, ForeignKey(Post.id) )
    comment =Column(String(250), nullable=False)
    creation_date =Column(String(250), nullable=False)

class Save(Base):
    __tablename__ ='Save'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey(User.id) )
    post_id=Column(Integer, ForeignKey(Post.id) )
    save_date =Column(String(250), nullable=False)



    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')