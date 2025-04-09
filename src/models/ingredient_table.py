from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base
from .unit_of_measure_table import UnitOfMeasure

class Ingredient(Base):
    __tablename__ = 'IngredientTable'

    # Attributs de la classe (champ de la table)
    ingredientId   = Column(Integer, primary_key = True, autoincrement = True)
    ingredientName = Column(String(45), unique = True, nullable = False)
    fk_UnitOfMeasureId = Column(Integer, ForeignKey('UnitOfMeasureTable.unitOfMeasureId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), nullable = False)
    
    __table_args__ = (
        UniqueConstraint('ingredientName', 'fk_UnitOfMeasureId', name='unique'),
    )

    recipes = relationship("RecipeHasIngredient", back_populates = "ingredient", cascade = "all, delete-orphan", uselist = True)
    unitOfMeasure = relationship("UnitOfMeasure", back_populates = "ingredients", uselist = False)