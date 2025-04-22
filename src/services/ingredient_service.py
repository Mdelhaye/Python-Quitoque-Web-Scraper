from src.models.ingredient_table import Ingredient
from .base_service import BaseService

class IngredientService(BaseService):
    @classmethod
    def to_sql_insert(cls, ingredient: Ingredient) -> str:
        """
        Génère la requête SQL d'insertion pour un seul objet Ingredient.
        """
        return super().run_query(super().to_sql_insert(Ingredient.__table__, ingredient))
    
    @classmethod
    def to_sql_insert_multiple(cls, ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Ingredient.
        """
        return super().run_query(super().to_sql_insert_multiple(Ingredient.__table__, ingredients))
    
    @classmethod
    def to_sql_select(cls, ingredient: Ingredient) -> str:
        """
        Génère la requête SQL de sélection pour un seul objet Ingredient.
        """
        return super().run_query(super().to_sql_select(Ingredient.__table__, ingredient))
    
    @classmethod
    def to_sql_select_multiple(cls, ingredients: list) -> str:
        """
        Génère la requête SQL de sélection pour plusieurs objets Ingredient.
        """
        return super().run_query(super().to_sql_select_multiple(Ingredient.__table__, ingredients))
    
    @classmethod
    def to_id_dict(cls, ingredients: list) -> dict:
        """
        Convertit un objet Ingredient en dictionnaire.
        """
        return super().to_id_dict([ingredient.ingredientName for ingredient in ingredients], [ingredient.ingredientId for ingredient in ingredients])
    
    @classmethod
    def to_sql_insert_multiple_return_ids(cls, ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Ingredient et retourne les IDs insérés.
        """
        cls.to_sql_insert_multiple(ingredients)
        rows = cls.to_sql_select_multiple(ingredients)
        return cls.to_id_dict([Ingredient(**row._mapping) for row in rows])
    
    @classmethod
    def to_sql_insert_if_not_exists(cls, ingredient: Ingredient) -> str:
        """
        Génère la requête SQL d'insertion pour un objet Ingredient s'il n'existe pas déjà. S'il existe, retourne son ID.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_ingredient = cls.to_sql_select(ingredient)
        if existing_ingredient:
            return existing_ingredient.ingredientId
        
        return cls.to_sql_insert(Ingredient.__table__, ingredient)
    
    @classmethod
    def to_sql_insert_multiple_if_not_exists(cls, ingredients: list) -> str:
        """
        Génère la requête SQL d'insertion pour plusieurs objets Ingredient s'ils n'existent pas déjà. S'ils existent, retourne leurs IDs.
        Cette méthode est utilisée pour éviter les doublons dans la base de données.
        """
        existing_ingredients       = cls.to_sql_select_multiple(ingredients)
        existing_ingredients_dict  = cls.to_id_dict([Ingredient(**row._mapping) for row in existing_ingredients])
        existing_ingredients_names = existing_ingredients_dict.keys()

        ingredients_to_insert     = [ingredient for ingredient in ingredients if ingredient.ingredientName not in existing_ingredients_names]
        inserted_ingredients_dict = cls.to_sql_insert_multiple_return_ids(ingredients_to_insert) if len(ingredients_to_insert) > 1 else {}

        return {**existing_ingredients_dict, **inserted_ingredients_dict}