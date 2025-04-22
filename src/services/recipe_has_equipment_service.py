from src.models.recipe_has_equipment_table import RecipeHasEquipment
from .base_service import BaseService

class RecipeHasEquipmentService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_equipment: RecipeHasEquipment) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasEquipment.
        """
        return super().run_query(super().to_sql_insert(RecipeHasEquipment.__table__, recipe_has_equipment))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipe_has_equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasEquipment.
        """
        return super().run_query(super().to_sql_insert_multiple(RecipeHasEquipment.__table__, recipe_has_equipments))
    
    @classmethod
    def to_sql_select(cls, recipe_has_equipment: RecipeHasEquipment) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet RecipeHasEquipment.
        """
        return super().run_query(super().to_sql_select(RecipeHasEquipment.__table__, recipe_has_equipment))
    
    @classmethod
    def to_sql_select_multiple(cls, recipe_has_equipments: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets RecipeHasEquipment.
        """
        return super().run_query(super().to_sql_select_multiple(RecipeHasEquipment.__table__, recipe_has_equipments))
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, recipe_has_equipment: RecipeHasEquipment) -> None:
        """
        Génère la requête SQL d'insertion pour un objet RecipeHasEquipment s'il n'existe pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_equipment = cls.to_sql_select(recipe_has_equipment)
        if existing_recipe_has_equipment:
            cls.to_sql_insert(RecipeHasEquipment.__table__, recipe_has_equipment)

    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, recipe_has_equipments: list) -> None:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasEquipment s'ils n'existent pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_equipments = cls.to_sql_select_multiple(recipe_has_equipments)
        existing_recipe_has_equipments = [RecipeHasEquipment(**row._mapping) for row in existing_recipe_has_equipments]

        recipe_has_equipments_to_insert = []
        for recipe_has_equipment in recipe_has_equipments:
            if cls.check_in_list(recipe_has_equipment, existing_recipe_has_equipments) is False:
                recipe_has_equipments_to_insert.append(recipe_has_equipment)
        
        cls.to_sql_insert_multiple(recipe_has_equipments_to_insert) if len(recipe_has_equipments_to_insert) else None

    @classmethod
    def check_in_list(cls, recipe_has_equipment: RecipeHasEquipment, recipe_has_equipments: list) -> bool:
        """
        Vérifie si un objet RecipeHasEquipment existe déjà dans une liste d'objets RecipeHasEquipment.
        """
        for rhe in recipe_has_equipments:
            if  rhe.fk_EquipmentId == recipe_has_equipment.fk_EquipmentId and \
                rhe.fk_RecipeId    == recipe_has_equipment.fk_RecipeId:
                    return True
        return False