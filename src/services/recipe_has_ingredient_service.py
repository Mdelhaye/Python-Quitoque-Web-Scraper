from src.models.recipe_has_ingredient_table import RecipeHasIngredient
from .base_service import BaseService

class RecipeHasIngredientService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_insert(RecipeHasIngredient.__table__, recipe_has_ingredient))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_insert_multiple(RecipeHasIngredient.__table__, recipe_has_ingredients))
    
    @classmethod
    def to_sql_select(cls, recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_select(RecipeHasIngredient.__table__, recipe_has_ingredient))
    
    @classmethod
    def to_sql_select_multiple(cls, recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_select(RecipeHasIngredient.__table__, recipe_has_ingredients))