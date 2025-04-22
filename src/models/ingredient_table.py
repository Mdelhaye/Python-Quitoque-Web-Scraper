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

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.ingredientId == other.ingredientId and self.ingredientName == other.ingredientName and self.fk_UnitOfMeasureId == other.fk_UnitOfMeasureId
    
    def __hash__(self):
        return hash((self.ingredientId, self.ingredientName, self.fk_UnitOfMeasureId))
    
    def __str__(self):
        return f"Ingredient(ingredientId={self.ingredientId}, ingredientName='{self.ingredientName}', fk_UnitOfMeasureId={self.fk_UnitOfMeasureId})"