from src.models.equipment_table import Equipment
from .base_service import BaseService

class EquipmentService(BaseService):
    @classmethod
    def to_sql_insert(cls, equipment: Equipment) -> str:
            """
            Génère la requête SQL d'insertion pour un seul objet Equipment.
            """
            return super().run_query(super().to_sql_insert(Equipment.__table__, equipment))

    @classmethod
    def to_sql_insert_multiple(cls, equipments: list) -> str:
            """
            Génère la requête SQL d'insertion pour plusieurs objets Equipment.
            """
            return super().run_query(super().to_sql_insert_multiple(Equipment.__table__, equipments))

    @classmethod
    def to_sql_select(cls, equipment: Equipment) -> str:
            """
            Génère la requête SQL de sélection pour un seul objet Equipment.
            """
            return super().run_query(super().to_sql_select(Equipment.__table__, equipment))

    @classmethod
    def to_sql_select_multiple(cls, equipments: list) -> str:
            """
            Génère la requête SQL de sélection pour plusieurs objets Equipment.
            """
            return super().run_query(super().to_sql_select_multiple(Equipment.__table__, equipments))

    @classmethod
    def to_id_dict(cls, equipments: list) -> dict:
            """
            Convertit un objet Equipment en dictionnaire.
            """
            return super().to_id_dict([equipment.equipmentName for equipment in equipments], [equipment.equipmentId for equipment in equipments])

    @classmethod
    def to_sql_insert_multiple_return_ids(cls, equipments: list) -> str:
            """
            Génère la requête SQL d'insertion pour plusieurs objets Equipment et retourne les IDs insérés.
            """
            cls.to_sql_insert_multiple(equipments)
            rows = cls.to_sql_select_multiple(equipments)
            return cls.to_id_dict([Equipment(**row._mapping) for row in rows])