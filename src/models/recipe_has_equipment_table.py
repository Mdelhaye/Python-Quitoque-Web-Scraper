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