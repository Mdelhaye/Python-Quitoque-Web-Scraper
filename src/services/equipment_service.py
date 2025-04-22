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
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, equipment: Equipment) -> str:
        """
        Génère la requête SQL d'insertion pour un objet Equipment s'il n'existe pas déjà. S'il existe, retourne son ID.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_equipment = cls.to_sql_select(equipment)
        if existing_equipment:
            return existing_equipment.equipmentId
        
        return cls.to_sql_insert(Equipment.__table__, equipment)
    
    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Equipment s'ils n'existent pas déjà. S'ils existent, retourne leurs IDs.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_equipments       = cls.to_sql_select_multiple(equipments)
        existing_equipments_dict  = cls.to_id_dict([Equipment(**row._mapping) for row in existing_equipments])
        existing_equipments_names = existing_equipments_dict.keys()

        equipments_to_insert     = [equipment for equipment in equipments if equipment.equipmentName not in existing_equipments_names]
        inserted_equipments_dict = cls.to_sql_insert_multiple_return_ids(equipments_to_insert) if len(equipments_to_insert) > 1 else {}

        return {**existing_equipments_dict, **inserted_equipments_dict}