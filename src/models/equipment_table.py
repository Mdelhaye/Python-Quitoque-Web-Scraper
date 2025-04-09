from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Equipment(Base):
    __tablename__ = 'EquipmentTable'

    # Attributs de la classe (champ de la table)
    equipmentId   = Column(Integer, primary_key = True, autoincrement = True)
    equipmentName = Column(String(45), unique = True, nullable = False)

    recipes = relationship("RecipeHasEquipment", back_populates = "equipment", cascade = "all, delete-orphan", uselist = True)