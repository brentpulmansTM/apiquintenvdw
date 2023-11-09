from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Star_wars(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    faction_id = Column(Integer)
    lightsaber_Wielder = Column(Boolean, default=True)
    age = Column(Integer)
    species = Column(String)
    addition = Column(String)


class Star_wars(Base):
    __tablename__ = "faction"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

