from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Category(Base):
    __tablename__ = 'CategoryTable'

    # Attributs de la classe (champ de la table)
    categoryId      = Column(Integer, primary_key = True, autoincrement = True)
    categoryName    = Column(String(255), unique = True, nullable = False)

    recipes = relationship("RecipeHasCategory", back_populates = "category", cascade = "all, delete-orphan", uselist = True)