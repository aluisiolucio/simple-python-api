from sqlalchemy import Column, Date, Integer, String

from ext.database import Base


class People(Base):

    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=False)
    birthday = Column(Date, nullable=False)
