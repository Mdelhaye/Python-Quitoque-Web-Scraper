from src.models.recipe_has_category_table import RecipeHasCategory
from .base_service import BaseService

class RecipeHasCategoryService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_category: RecipeHasCategory) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasCategory.
        """
        sql, params = super().to_sql_insert(recipe_has_category)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, recipe_has_categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasCategory.
        """
        sql, params = super().to_sql_insert_multiple_secure(recipe_has_categories)
        return sql, params