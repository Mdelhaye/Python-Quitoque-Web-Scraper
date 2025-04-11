from src.models.recipe_has_equipment_table import RecipeHasEquipment
from .base_service import BaseService

class RecipeHasEquipmentService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_equipment: RecipeHasEquipment) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasEquipment.
        """
        sql, params = super().to_sql_insert(recipe_has_equipment)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, recipe_has_equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasEquipment.
        """
        sql, params = super().to_sql_insert_multiple_secure(recipe_has_equipments)
        return sql, params