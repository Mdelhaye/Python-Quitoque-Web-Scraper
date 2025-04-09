from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class UnitOfMeasure(Base):
    __tablename__ = 'UnitOfMeasureTable'

    # Attributs de la classe (champ de la table)
    unitOfMeasureId     = Column(Integer, primary_key = True, autoincrement = True)
    unitOfMeasureSymbol = Column(String(45), unique = True, nullable = False)

    ingredients = relationship("Ingredient", back_populates = "unitOfMeasure", cascade = "all, delete-orphan", uselist = True)