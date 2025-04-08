from src.models.recipe_review_table import RecipeReview
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class RecipeReviewService:
    @staticmethod
    def to_sql_insert(recipe_review: RecipeReview) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeReview.
        """
        sql, params = generate_insert_query(recipe_review)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(recipe_reviews: list) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeReview.
        """
        query = generate_insert_multiple_secure_query(recipe_reviews)
        return query