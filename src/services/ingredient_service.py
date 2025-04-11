from src.models.ingredient_table import Ingredient
from .base_service import BaseService

class IngredientService(BaseService):
    @classmethod
    def to_sql_insert(cls, ingredient: Ingredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Ingredient.
        """
        sql, params = super().to_sql_insert(ingredient)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Ingredient.
        """
        sql, params = super().to_sql_insert_multiple_secure(ingredients)
        return sql, params