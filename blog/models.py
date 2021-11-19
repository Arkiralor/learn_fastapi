from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
from .BlogDB import Base


class Blog(Base):
    __tablename__ = 'blog_posts'
    post_id = Column(Integer, primary_key=True, index=True)
    post_title = Column(String)
    post_body = Column(String)
    author_id = Column(Integer, ForeignKey('users.user_id'))

    author = relationship("User", back_populates="posts")


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    user_email = Column(String, unique=True)
    user_password = Column(String)

    posts = relationship("Blog", back_populates="author")
