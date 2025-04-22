from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

from .equipment_table import Equipment

class RecipeHasEquipment(Base):
    __tablename__ = 'RecipeTable_has_EquipmentTable'

    # Attributs de la classe (champ de la table)
    fk_RecipeId     = Column(Integer, ForeignKey('RecipeTable.recipeId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), primary_key = True, nullable = False)
    fk_EquipmentId  = Column(Integer, ForeignKey('EquipmentTable.equipmentId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), primary_key = True, nullable = False)

    recipe = relationship("Recipe", back_populates = "equipments", uselist = True)
    equipment = relationship("Equipment", back_populates = "recipes", uselist = True)

    def __eq__(self, other):
        if not isinstance(other, RecipeHasEquipment):
            return False
        return self.fk_RecipeId == other.fk_RecipeId and self.fk_EquipmentId == other.fk_EquipmentId
    
    def __hash__(self):
        return hash((self.fk_RecipeId, self.fk_EquipmentId))
    
    def __str__(self):
        return f"RecipeHasEquipment(fk_RecipeId={self.fk_RecipeId}, fk_EquipmentId={self.fk_EquipmentId})"