from src.models.recipe_review_table import RecipeReview
from .base_service import BaseService

class RecipeReviewService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_review: RecipeReview) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeReview.
        """
        sql, params = super().to_sql_insert(recipe_review)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, recipe_reviews: list) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeReview.
        """
        sql, params = super().to_sql_insert_multiple_secure(recipe_reviews)
        return sql, params