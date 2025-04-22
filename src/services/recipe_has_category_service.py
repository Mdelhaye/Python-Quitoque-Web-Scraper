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
        return super().run_query(super().to_sql_select_multiple(RecipeHasCategory.__table__, recipe_has_categories))
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, recipe_has_category: RecipeHasCategory) -> None:
        """
        Génère la requête SQL d'insertion pour un objet RecipeHasCategory s'il n'existe pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_category = cls.to_sql_select(recipe_has_category)
        if not existing_recipe_has_category:
            cls.to_sql_insert(RecipeHasCategory.__table__, recipe_has_category)
    
    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, recipe_has_categories: list) -> None:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasCategory s'ils n'existent pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_categories = cls.to_sql_select_multiple(recipe_has_categories)
        existing_recipe_has_categories = [RecipeHasCategory(**row._mapping) for row in existing_recipe_has_categories]

        recipe_has_categories_to_insert = []
        for recipe_has_category in recipe_has_categories:
            if cls.check_in_list(recipe_has_category, existing_recipe_has_categories) is False:
                recipe_has_categories_to_insert.append(recipe_has_category)
        
        cls.to_sql_insert_multiple(recipe_has_categories_to_insert) if len(recipe_has_categories_to_insert) else None

    @classmethod
    def check_in_list(cls, recipe_has_category: RecipeHasCategory, recipe_has_categories: list) -> bool:
        """
        Vérifie si un objet RecipeHasCategory existe déjà dans une liste d'objets RecipeHasCategory.
        """
        for rhc in recipe_has_categories:
            if  rhc.fk_RecipeId   == recipe_has_category.fk_RecipeId and \
                rhc.fk_CategoryId == recipe_has_category.fk_CategoryId:
                    return True
        return False