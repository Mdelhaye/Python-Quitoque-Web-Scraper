from src.models.recipe_has_ingredient_table import RecipeHasIngredient
from .base_service import BaseService

class RecipeHasIngredientService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasIngredient.
        """
        sql, params = super().to_sql_insert(recipe_has_ingredient)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasIngredient.
        """
        sql, params = super().to_sql_insert_multiple_secure(recipe_has_ingredients)
        return sql, params