from src.models.ingredient_table import Ingredient
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class IngredientService:
    @staticmethod
    def to_sql_insert(ingredient: Ingredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Ingredient.
        """
        sql, params = generate_insert_query(ingredient)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Ingredient.
        """
        query = generate_insert_multiple_secure_query(ingredients)
        return query