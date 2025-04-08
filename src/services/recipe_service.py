from src.models.recipe_table import Recipe
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class RecipeService:
    @staticmethod
    def to_sql_insert(recipe: Recipe) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        sql, params = generate_insert_query(recipe)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(recipes: list) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        query = generate_insert_multiple_secure_query(recipes)
        return query