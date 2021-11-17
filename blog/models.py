from sqlalchemy import Column, Integer, String
from .BlogDB import Base


class Blog(Base):
    __tablename__ = 'blog_posts'
    post_id = Column(Integer, primary_key=True, index=True)
    post_title = Column(String)
    post_body = Column(String)
