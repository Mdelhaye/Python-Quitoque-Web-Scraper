from src.models.equipment_table import Equipment
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class EquipmentService:
    @staticmethod
    def to_sql_insert(equipment: Equipment) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Equipment.
        """
        sql, params = generate_insert_query(equipment)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Equipment.
        """
        query = generate_insert_multiple_secure_query(equipments)
        return query