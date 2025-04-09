from sqlalchemy import Column, SmallInteger, Integer, String, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .base import Base

from enum import Enum as PyEnum

# Enum pour le Nutriscore
class NutriscoreEnum(PyEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    Unknow = "Unknow"

# Définition de la table RecipeTable
class Recipe(Base):
    __tablename__ = 'RecipeTable'
    
    # Attributs de la classe (champ de la table)
    recipeId    = Column(Integer, primary_key = True, autoincrement = True)
    title       = Column(String(255), unique = True, nullable = False)
    subTitle    = Column(String(255))
    url         = Column(String(255), unique = True, nullable = False)
    totalTime   = Column(SmallInteger())
    cookTime    = Column(SmallInteger())
    nutriscore  = Column(Enum('A', 'B', 'C', 'D', 'E', 'Unknow'), nullable = False)
    createdAt   = Column(TIMESTAMP, server_default = func.current_timestamp(), nullable = True)
    modifiedAt  = Column(TIMESTAMP, server_default = func.current_timestamp(), server_onupdate = func.current_timestamp(), nullable = True)

    reviews     = relationship("RecipeReview", back_populates = "recipe", cascade = "all, delete-orphan", uselist = True)
    categories  = relationship("RecipeHasCategory", back_populates = "recipe", cascade = "all, delete-orphan", uselist = True)
    equipments  = relationship("RecipeHasEquipment", back_populates = "recipe", cascade = "all, delete-orphan", uselist = True)