from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Category(Base):
    __tablename__ = 'CategoryTable'

    # Attributs de la classe (champ de la table)
    categoryId      = Column(Integer, primary_key = True, autoincrement = True)
    categoryName    = Column(String(45), unique = True, nullable = False)

    recipes = relationship("RecipeHasCategory", back_populates = "category", cascade = "all, delete-orphan", uselist = True)

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.categoryId == other.categoryId and self.categoryName == other.categoryName
    
    def __hash__(self):
        return hash((self.categoryId, self.categoryName))
    
    def __str__(self):
        return f"Category(categoryId={self.categoryId}, categoryName='{self.categoryName}')"