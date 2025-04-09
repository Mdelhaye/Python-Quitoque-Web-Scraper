from src.models.recipe_has_ingredient_table import RecipeHasIngredient
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class RecipeHasIngredientService:
    @staticmethod
    def to_sql_insert(recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasIngredient.
        """
        sql, params = generate_insert_query(recipe_has_ingredient)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasIngredient.
        """
        query = generate_insert_multiple_secure_query(recipe_has_ingredients)
        return query