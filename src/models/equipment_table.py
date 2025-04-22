from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Equipment(Base):
    __tablename__ = 'EquipmentTable'

    # Attributs de la classe (champ de la table)
    equipmentId   = Column(Integer, primary_key = True, autoincrement = True)
    equipmentName = Column(String(45), unique = True, nullable = False)

    recipes = relationship("RecipeHasEquipment", back_populates = "equipment", cascade = "all, delete-orphan", uselist = True)

    def __eq__(self, other):
        if not isinstance(other, Equipment):
            return False
        return self.equipmentId == other.equipmentId and self.equipmentName == other.equipmentName
    
    def __hash__(self):
        return hash((self.equipmentId, self.equipmentName))
    
    def __str__(self):
        return f"Equipment(equipmentId={self.equipmentId}, equipmentName='{self.equipmentName}')"