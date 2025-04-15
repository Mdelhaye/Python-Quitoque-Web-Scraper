from src.models.recipe_table import Recipe, NutriscoreEnum
from .base_service import BaseService

class RecipeService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe: Recipe) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        return super().run_query(super().to_sql_insert(Recipe.__table__, recipe))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipes: list) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Recipe.
        """
        return super().run_query(super().to_sql_insert_multiple(Recipe.__table__, recipes))
    
    @classmethod
    def to_sql_select(cls, recipe: Recipe) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet Recipe.
        """
        return super().run_query(super().to_sql_select(Recipe.__table__, recipe))
    
    @classmethod
    def to_sql_select_multiple(cls, recipes: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets Recipe.
        """
        return super().run_query(super().to_sql_select(Recipe.__table__, recipes))
    
    @classmethod
    def to_id_dict(cls, recipes: list) -> dict:
        """
        Convertit un objet Recipe en dictionnaire.
        """
        return super().to_id_dict([recipe.title for recipe in recipes], [recipe.recipeId for recipe in recipes])
    
    @classmethod
    def to_sql_insert_multiple_return_ids(cls, recipes: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Recipe et retourne les IDs insérés.
        """
        cls.to_sql_insert_multiple(recipes)
        rows = cls.to_sql_select_multiple(recipes)
        return cls.to_id_dict([Recipe(**row._mapping) for row in rows])
