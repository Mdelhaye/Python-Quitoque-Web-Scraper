from src.models.recipe_has_equipment_table import RecipeHasEquipment
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class RecipeHasEquipmentService:
    @staticmethod
    def to_sql_insert(recipe_has_equipment: RecipeHasEquipment) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasEquipment.
        """
        sql, params = generate_insert_query(recipe_has_equipment)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(recipe_has_equipments: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasEquipment.
        """
        query = generate_insert_multiple_secure_query(recipe_has_equipments)
        return query