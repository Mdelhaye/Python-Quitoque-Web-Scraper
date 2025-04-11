from src.models.category_table import Category
from .base_service import BaseService

class CategoryService(BaseService):
    @classmethod
    def to_sql_insert(cls, category: Category) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Category.
        """
        sql, params = super().to_sql_insert(category)
        return sql, params
    
    @classmethod
    def to_sql_insert_multiple_secure(cls, categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Category.
        """
        sql, params = super().to_sql_insert_multiple_secure(categories)
        return sql, params