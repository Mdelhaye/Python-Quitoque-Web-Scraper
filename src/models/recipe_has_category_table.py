from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

from .category_table import Category

class RecipeHasCategory(Base):
    __tablename__ = 'RecipeTable_has_CategoryTable'

    # Attributs de la classe (champ de la table)
    fk_RecipeId   = Column(Integer, ForeignKey('RecipeTable.recipeId', ondelete = 'CASCADE', onupdate = 'NO ACTION'),primary_key = True, nullable = False)
    fk_CategoryId = Column(Integer, ForeignKey('CategoryTable.categoryId', ondelete = 'CASCADE', onupdate = 'NO ACTION'),primary_key = True, nullable = False)

    recipe = relationship("Recipe", back_populates = "categories", uselist = True)
    category = relationship("Category", back_populates = "recipes", uselist = True)

    def __eq__(self, other):
        if not isinstance(other, RecipeHasCategory):
            return False
        return self.fk_RecipeId == other.fk_RecipeId and self.fk_CategoryId == other.fk_CategoryId
    
    def __hash__(self):
        return hash((self.fk_RecipeId, self.fk_CategoryId))
    
    def __str__(self):
        return f"RecipeHasCategory(fk_RecipeId={self.fk_RecipeId}, fk_CategoryId={self.fk_CategoryId})"