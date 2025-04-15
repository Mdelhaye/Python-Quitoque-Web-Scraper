from src.models.recipe_has_category_table import RecipeHasCategory
from .base_service import BaseService

class RecipeHasCategoryService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_category: RecipeHasCategory) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasCategory.
        """
        return super().run_query(super().to_sql_insert(RecipeHasCategory.__table__, recipe_has_category))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipe_has_categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasCategory.
        """
        return super().run_query(super().to_sql_insert_multiple(RecipeHasCategory.__table__, recipe_has_categories))
    
    @classmethod
    def to_sql_select(cls, recipe_has_category: RecipeHasCategory) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet RecipeHasCategory.
        """
        return super().run_query(super().to_sql_select(RecipeHasCategory.__table__, recipe_has_category))
    
    @classmethod
    def to_sql_select_multiple(cls, recipe_has_categories: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets RecipeHasCategory.
        """
        return super().run_query(super().to_sql_select(RecipeHasCategory.__table__, recipe_has_categories))