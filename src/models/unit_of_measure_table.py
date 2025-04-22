from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class UnitOfMeasure(Base):
    __tablename__ = 'UnitOfMeasureTable'

    # Attributs de la classe (champ de la table)
    unitOfMeasureId     = Column(Integer, primary_key = True, autoincrement = True)
    unitOfMeasureSymbol = Column(String(45), unique = True, nullable = False)

    ingredients = relationship("Ingredient", back_populates = "unitOfMeasure", cascade = "all, delete-orphan", uselist = True)

    def __eq__(self, other):
        if not isinstance(other, UnitOfMeasure):
            return False
        return self.unitOfMeasureId == other.unitOfMeasureId and self.unitOfMeasureSymbol == other.unitOfMeasureSymbol
    
    def __hash__(self):
        return hash((self.unitOfMeasureId, self.unitOfMeasureSymbol))
    
    def __str__(self):
        return f"UnitOfMeasure(unitOfMeasureId={self.unitOfMeasureId}, unitOfMeasureSymbol='{self.unitOfMeasureSymbol}')"