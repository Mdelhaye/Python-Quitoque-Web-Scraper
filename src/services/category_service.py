from src.models.category_table import Category
from src.utils.sql_helpers import generate_insert_query, generate_insert_multiple_secure_query

class CategoryService:
    @staticmethod
    def to_sql_insert(category: Category) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Category.
        """
        sql, params = generate_insert_query(category)
        return sql, params
    
    @staticmethod
    def to_sql_insert_multiple_secure(categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Category.
        """
        query = generate_insert_multiple_secure_query(categories)
        return query