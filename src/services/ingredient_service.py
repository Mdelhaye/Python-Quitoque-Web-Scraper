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
        return super().run_query(super().to_sql_select(Ingredient.__table__, ingredients))
    
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