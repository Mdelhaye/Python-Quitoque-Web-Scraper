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
        return super().run_query(super().to_sql_select(RecipeHasEquipment.__table__, recipe_has_equipments))