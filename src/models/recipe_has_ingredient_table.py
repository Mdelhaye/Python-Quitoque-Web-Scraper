from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

from .ingredient_table import Ingredient

class RecipeHasIngredient(Base):
    __tablename__ = 'RecipeTable_has_IngredientTable'

    # Attributs de la classe (champ de la table)
    fk_RecipeId     = Column(Integer, ForeignKey('RecipeTable.recipeId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), primary_key = True, nullable = False)
    fk_IngredientId = Column(Integer, ForeignKey('IngredientTable.ingredientId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), primary_key = True, nullable = False)
    quantity        = Column(DECIMAL, nullable = False)

    recipe = relationship("Recipe", back_populates = "ingredients", uselist = True)
    ingredient = relationship("Ingredient", back_populates = "recipes", uselist = True)