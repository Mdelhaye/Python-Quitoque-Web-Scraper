from src.models.recipe_has_ingredient_table import RecipeHasIngredient
from .base_service import BaseService

class RecipeHasIngredientService(BaseService):
    @classmethod
    def to_sql_insert(cls, recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_insert(RecipeHasIngredient.__table__, recipe_has_ingredient))
    
    @classmethod
    def to_sql_insert_multiple(cls, recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_insert_multiple(RecipeHasIngredient.__table__, recipe_has_ingredients))
    
    @classmethod
    def to_sql_select(cls, recipe_has_ingredient: RecipeHasIngredient) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_select(RecipeHasIngredient.__table__, recipe_has_ingredient))
    
    @classmethod
    def to_sql_select_multiple(cls, recipe_has_ingredients: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets RecipeHasIngredient.
        """
        return super().run_query(super().to_sql_select_multiple(RecipeHasIngredient.__table__, recipe_has_ingredients))
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, recipe_has_ingredient: RecipeHasIngredient) -> None:
        """
        Génère la requête SQL d'insertion pour un objet RecipeHasIngredient s'il n'existe pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_ingredient = cls.to_sql_select(recipe_has_ingredient)
        if existing_recipe_has_ingredient:
            cls.to_sql_insert(RecipeHasIngredient.__table__, recipe_has_ingredient)

    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, recipe_has_ingredients: list) -> None:
        """
        Génère la requête SQL d'insertion pour plusieurs objets RecipeHasIngredient s'ils n'existent pas déjà.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_recipe_has_ingredients = cls.to_sql_select_multiple(recipe_has_ingredients)
        existing_recipe_has_ingredients = [RecipeHasIngredient(**row._mapping) for row in existing_recipe_has_ingredients]

        recipe_has_ingredients_to_insert = []
        for recipe_has_ingredient in recipe_has_ingredients:
            if cls.check_in_list(recipe_has_ingredient, existing_recipe_has_ingredients) is False:
                recipe_has_ingredients_to_insert.append(recipe_has_ingredient)
            
        cls.to_sql_insert_multiple(recipe_has_ingredients_to_insert) if len(recipe_has_ingredients_to_insert) else None

    @classmethod
    def check_in_list(cls, recipe_has_ingredient: RecipeHasIngredient, recipe_has_ingredients: list) -> bool:
        """
        Vérifie si un objet RecipeHasIngredient existe déjà dans une liste d'objets RecipeHasIngredient.
        """
        for rhi in recipe_has_ingredients:
            if  rhi.fk_RecipeId == recipe_has_ingredient.fk_RecipeId and \
                rhi.fk_IngredientId == recipe_has_ingredient.fk_IngredientId:
                    return True
        return False