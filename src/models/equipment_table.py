from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
# from .unit_of_measure_table import UnitOfMeasure

class Equipment(Base):
    __tablename__ = 'EquipmentTable'

    # Attributs de la classe (champ de la table)
    equipmentId   = Column(Integer, primary_key = True, autoincrement = True)
    equipmentName = Column(String(45), unique = True, nullable = False)
    # fk_UnitOfMeasureId = Column(Integer, ForeignKey('UnitOfMeasureTable.unitOfMeasureId', ondelete = 'CASCADE', onupdate = 'NO ACTION'), nullable = False)

    recipes = relationship("RecipeHasEquipment", back_populates = "equipment", cascade = "all, delete-orphan", uselist = True)
    # unitOfMeasure = relationship("UnitOfMeasure", back_populates = "equipments", uselist = False)