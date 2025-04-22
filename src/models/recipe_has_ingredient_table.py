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

    def __eq__(self, other):
        if not isinstance(other, RecipeHasIngredient):
            return False
        return self.fk_RecipeId == other.fk_RecipeId and self.fk_IngredientId == other.fk_IngredientId
    
    def __hash__(self):
        return hash((self.fk_RecipeId, self.fk_IngredientId))
    
    def __str__(self):
        return f"RecipeHasIngredient(fk_RecipeId={self.fk_RecipeId}, fk_IngredientId={self.fk_IngredientId}, quantity={self.quantity})"