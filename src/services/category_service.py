from src.models.category_table import Category
from .base_service import BaseService

class CategoryService(BaseService):
    @classmethod
    def to_sql_insert(cls, category: Category) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Category.
        """
        return super().run_query(super().to_sql_insert(Category.__table__, category))
    
    @classmethod
    def to_sql_insert_multiple(cls, categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Category.
        """
        return super().run_query(super().to_sql_insert_multiple(Category.__table__, categories))
    
    @classmethod
    def to_sql_select(cls, category: Category) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet Category.
        """
        return super().run_query(super().to_sql_select(Category.__table__, category))
    
    @classmethod
    def to_sql_select_multiple(cls, categories: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets Category.
        """
        return super().run_query(super().to_sql_select(Category.__table__, categories))
    
    @classmethod
    def to_id_dict(cls, categories: list) -> dict:
        """
        Convertit un objet Category en dictionnaire.
        """
        return super().to_id_dict([category.categoryName for category in categories], [category.categoryId for category in categories])
    
    @classmethod
    def to_sql_insert_multiple_return_ids(cls, categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Category et retourne les IDs insérés.
        """
        cls.to_sql_insert_multiple(categories)
        rows = cls.to_sql_select_multiple(categories)
        return cls.to_id_dict([Category(**row._mapping) for row in rows])