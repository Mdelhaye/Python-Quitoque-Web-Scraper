from src.models.recipe_table import Recipe
from .base_service import BaseService

class RecipeService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe: Recipe) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        sql, params = super().to_sql_insert(recipe)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, recipes: list) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        sql, params = super().to_sql_insert_multiple_secure(recipes)
        return sql, params