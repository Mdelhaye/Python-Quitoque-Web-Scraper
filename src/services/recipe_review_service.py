from src.models.recipe_review_table import RecipeReview
from .base_service import BaseService

class RecipeReviewService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_review: RecipeReview) -> str:
        """
        Generates the SQL insert query for a single object RecipeReview.
        """
        return super().run_query(super().to_sql_insert(RecipeReview.__table__, recipe_review))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipe_reviews: list) -> str:
        """
        Generates the SQL insert query for multiple objects RecipeReview.
        """
        return super().run_query(super().to_sql_insert_multiple(RecipeReview.__table__, recipe_reviews))
    
    @classmethod
    def to_sql_select(cls, recipe_review: RecipeReview) -> str:
        """
        Generates the SQL select query for a single object RecipeReview.
        """
        return super().run_query(super().to_sql_select(RecipeReview.__table__, recipe_review))
    
    @classmethod
    def to_sql_select_multiple(cls, recipe_reviews: list) -> str:
        """
        Generates the SQL select query for multiple objects RecipeReview.
        """
        return super().run_query(super().to_sql_select_multiple(RecipeReview.__table__, recipe_reviews))