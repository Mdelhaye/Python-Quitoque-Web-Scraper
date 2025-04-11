from src.models.equipment_table import Equipment
from .base_service import BaseService

class EquipmentService(BaseService):
    @classmethod
    def to_sql_insert(cls, equipment: Equipment) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Equipment.
        """
        sql, params = super().to_sql_insert(equipment)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Equipment.
        """
        sql, params = super().to_sql_insert_multiple_secure(equipments)
        return sql, params