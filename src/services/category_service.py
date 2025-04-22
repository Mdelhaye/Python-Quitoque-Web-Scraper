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
        return super().run_query(super().to_sql_select_multiple(Category.__table__, categories))
    
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
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, category: Category) -> str:
        """
        Génère la requête SQL d'insertion pour un objet Category s'il n'existe pas déjà. S'il existe, retourne son ID.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_category = cls.to_sql_select(category)
        if existing_category:
            return existing_category.categoryId
        
        return cls.to_sql_insert(Category.__table__, category)
    
    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, categories: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Category s'ils n'existent pas déjà. S'ils existent, retourne leurs IDs.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_categories       = cls.to_sql_select_multiple(categories)
        existing_categories_dict  = cls.to_id_dict([Category(**row._mapping) for row in existing_categories])
        existing_categories_names = existing_categories_dict.keys()

        categories_to_insert     = [category for category in categories if category.categoryName not in existing_categories_names]
        inserted_categories_dict = cls.to_sql_insert_multiple_return_ids(categories_to_insert) if len(categories_to_insert) > 1 else {}

        return {**existing_categories_dict, **inserted_categories_dict}