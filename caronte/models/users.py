from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    accounts = relationship('Account', back_populates='user')
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
