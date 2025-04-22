import sys
import os

# Ajoutes le dossier 'src' au sys.path pour que Python puisse l'importer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recipe_table import NutriscoreEnum, Recipe
# from models.recipe_review_table import RecipeReview
from models.category_table import Category
from models.recipe_has_category_table import RecipeHasCategory
from models.equipment_table import Equipment
from models.recipe_has_equipment_table import RecipeHasEquipment
# from models.unit_of_measure_table import UnitOfMeasure
from models.ingredient_table import Ingredient
from models.recipe_has_ingredient_table import RecipeHasIngredient

from services.recipe_service import RecipeService
# from services.recipe_review_service import RecipeReviewService
from services.category_service import CategoryService
from services.recipe_has_category_service import RecipeHasCategoryService
from services.equipment_service import EquipmentService
from services.recipe_has_equipment_service import RecipeHasEquipmentService
from services.unit_of_measure_service import UnitOfMeasureService
from services.ingredient_service import IngredientService
from services.recipe_has_ingredient_service import RecipeHasIngredientService

from database.connection import Session

from scraper.recipe_list_scraper import RecipeListScraper
from scraper.recipe_scraper import RecipeScraper
from scraper.category_scraper import CategoryScraper
from scraper.equipment_scraper import EquipmentScraper
from scraper.ingredient_scraper import IngredientScraper

def main():
    recipe_list_scraper   = RecipeListScraper("https://www.quitoque.fr")

    recipe_list_endpoints = []
    for i in range (1, 2):
        recipe_list_soups = recipe_list_scraper.make_request(f"/recettes?page={i}")
        for a in recipe_list_soups:
            recipe_list_endpoints.append(a["href"])

    recipe_table_list = [RecipeScraper("https://www.quitoque.fr").make_request(endpoint) for endpoint in recipe_list_endpoints]

    recipe_with_categories = [
        {
            "recipe": recipe.parse_recipe(),
            "categories": CategoryScraper(recipe).parse_categories(),
            "equipments": EquipmentScraper(recipe).parse_equipments(),
            "ingredients_qty_unit": IngredientScraper(recipe).parse_ingredients(),
        } for recipe in recipe_table_list
    ]

    recipes = []
    categories = []
    equipments = []
    ingredients = []
    units = []
    
    for item in recipe_with_categories:
        recipes.append(item["recipe"])
        for category in item["categories"]:
            categories.append(category)
        for equipment in item["equipments"]:
            equipments.append(equipment)
        for ingredient in item["ingredients_qty_unit"][0]:
            ingredients.append(ingredient)
        for unit in item["ingredients_qty_unit"] [2]:
            units.append(unit)

    recipes     = list(set(recipes))
    categories  = list(set(categories))
    equipments  = list(set(equipments))
    ingredients = list(set(ingredients))
    units       = list(set(units))

    recipes_dict     = RecipeService.to_sql_insert_multiple_if_not_exists(recipes)
    categories_dict  = CategoryService.to_sql_insert_multiple_if_not_exists(categories)
    equipments_dict  = EquipmentService.to_sql_insert_multiple_if_not_exists(equipments)
    units_dict       = UnitOfMeasureService.to_sql_insert_multiple_if_not_exists(units)

    ingredients_with_units = []
    for item in recipe_with_categories:
        for i in range(len(item["ingredients_qty_unit"][0])):
            ingredient = item["ingredients_qty_unit"][0][i]
            unit       = item["ingredients_qty_unit"][2][i]
            ingredient.fk_UnitOfMeasureId = units_dict.get(unit.unitOfMeasureSymbol if unit.unitOfMeasureSymbol != None else 'x')
            ingredients_with_units.append(ingredient)

    ingredients_with_units = list(set(ingredients_with_units))

    ingredients_dict = IngredientService.to_sql_insert_multiple_if_not_exists(ingredients_with_units)

    recipe_with_category_ids = [
        RecipeHasCategory(
            fk_RecipeId = recipes_dict.get(item["recipe"].title),
            fk_CategoryId = categories_dict.get(category.categoryName),
        ) for item in recipe_with_categories for category in item["categories"]
    ]

    recipe_with_equipment_ids = [
        RecipeHasEquipment(
            fk_RecipeId = recipes_dict.get(item["recipe"].title),
            fk_EquipmentId = equipments_dict.get(equipment.equipmentName),
        ) for item in recipe_with_categories for equipment in item["equipments"]
    ]

    recipe_with_ingredient_ids = [
         RecipeHasIngredient(
            fk_RecipeId = recipes_dict.get(item["recipe"].title),
            fk_IngredientId = ingredients_dict.get(item["ingredients_qty_unit"][0][i].ingredientName),
            quantity = item["ingredients_qty_unit"][1][i],
         ) for item in recipe_with_categories for i in range(len(item["ingredients_qty_unit"][0])) 
    ]

    RecipeHasCategoryService.to_sql_insert_multiple_if_not_exists(recipe_with_category_ids)
    RecipeHasEquipmentService.to_sql_insert_multiple_if_not_exists(recipe_with_equipment_ids)
    RecipeHasIngredientService.to_sql_insert_multiple_if_not_exists(recipe_with_ingredient_ids)
       
if __name__ == "__main__":
    main()