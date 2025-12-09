import json
import enum
from datetime import datetime

from flask_login import UserMixin

from app._init_ import db, create_app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import relationship


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(Base):
    __tablename__ = "category"
    name = Column(String(150), nullable=False)
    components = relationship('Component', backref="category", lazy=True)


class Brand(Base):
    __tablename__ = "brand"
    name = Column(String(150), nullable=False)
    components = relationship('Component', backref="brand", lazy=True)


class Component(Base):
    __tablename__ = "component"
    name = Column(String(150), nullable=False)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    brand_id = Column(Integer, ForeignKey(Brand.id), nullable=False)


class UserRole(enum.Enum):
    ADMIN = 1
    USER = 2


class User(Base, UserMixin):
    __tablename__ = "user"
    name = Column(String(150), nullable=False)
    username = Column(String(100), nullable=False,unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(300))
    active = Column(Boolean, default=True)
    joined = Column(DateTime, default=datetime.now)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

# if __name__ == "__main__":
#     app = create_app()
#     with app.app_context():
#         db.create_all()
#         c1 = Category(name="Moto")
#         c2 = Category(name="Oto")
#         db.session.add_all([c1, c2])
#
#         b1 = Brand(name="Honda")
#         b2 = Brand(name="Yamaha")
#         b3 = Brand(name="Toyota")
#         b4 = Brand(name="Mercedes")
#         db.session.add_all([b1, b2,b3,b4])
#
#
#         with open("data/component.json", encoding="utf-8") as f:
#             components = json.load(f)
#
#             for c in components:
#                 comp = Component(**c)
#                 db.session.add(comp)
#
#         db.session.commit()
