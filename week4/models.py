from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), unique=False)
    phone       = Column(String(120), unique=False)
    email       = Column(String(120), unique=True)
    birth       = Column(String(10), unique=False)
    gender      = Column(String(10), unique=False)
    hobby       = Column(String(120), unique=False)
    carNo       = Column(String(120), unique=False)
    description = Column(String(200), unique=False)

    def __init__(self, name=None, phone=None, email=None, birth=None, gender=None, hobby=None, carNo=None, description=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth = birth
        self.gender = gender
        self.hobby = hobby
        self.carNo = carNo
        self.description = description
        
    def __repr__(self):
        return '<User %r>' % (self.name)