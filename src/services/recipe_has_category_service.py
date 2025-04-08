from src.models.recipe_has_category_table import RecipeHasCategory
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class RecipeHasCategoryService:
    @staticmethod
    def to_sql_insert(recipe_has_category: RecipeHasCategory) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasCategory.
        """
        sql, params = generate_insert_query(recipe_has_category)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(recipe_has_categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasCategory.
        """
        query = generate_insert_multiple_secure_query(recipe_has_categories)
        return query