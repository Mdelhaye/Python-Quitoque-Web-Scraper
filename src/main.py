import sys
import os

# Ajoutes le dossier 'src' au sys.path pour que Python puisse l'importer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recipe_table import NutriscoreEnum, Recipe
# from models.recipe_review_table import RecipeReview
from models.category_table import Category
from models.recipe_has_category_table import RecipeHasCategory
# from models.equipment_table import Equipment
# from models.recipe_has_equipment_table import RecipeHasEquipment
# from models.unit_of_measure_table import UnitOfMeasure
# from models.ingredient_table import Ingredient
# from models.recipe_has_ingredient_table import RecipeHasIngredient

from services.recipe_service import RecipeService
# from services.recipe_review_service import RecipeReviewService
from services.category_service import CategoryService
from services.recipe_has_category_service import RecipeHasCategoryService
# from services.equipment_service import EquipmentService
# from services.recipe_has_equipment_service import RecipeHasEquipmentService
# from services.unit_of_measure_service import UnitOfMeasureService
# from services.ingredient_service import IngredientService
# from services.recipe_has_ingredient_service import RecipeHasIngredientService

from database.connection import Session

from scraper.recipe_list_scraper import RecipeListScraper
from scraper.recipe_scraper import RecipeScraper
from scraper.category_scraper import CategoryScraper

def main():
    recipe_list_scraper   = RecipeListScraper("https://www.quitoque.fr")

    recipe_list_endpoints = []
    for i in range (1, 48):
        print (f"Scraping page {i}...")
        recipe_list_soups = recipe_list_scraper.make_request(f"/recettes?page={i}")
        for a in recipe_list_soups:
            recipe_list_endpoints.append(a["href"])

    print(f"Scraping {len(recipe_list_endpoints)} recipes...")
    recipe_table_list = [RecipeScraper("https://www.quitoque.fr").make_request(endpoint) for endpoint in recipe_list_endpoints]

    print(f"Created {len(recipe_table_list)} recipes.")
    recipe_with_categories = [
        {
            "recipe": recipe.parse_recipe(),
            "categories": CategoryScraper(recipe).parse_categories(),
        } for recipe in recipe_table_list
    ]

    recipes = []
    categories = []
    categories_names = []
    
    for item in recipe_with_categories:
        recipes.append(item["recipe"])
        for category in item["categories"]:
            if category.categoryName not in categories_names:
                categories_names.append(category.categoryName)
                categories.append(category)
    
    recipes_dict = RecipeService.to_sql_insert_multiple_return_ids(recipes)
    categories_dict = CategoryService.to_sql_insert_multiple_return_ids(categories)

    recipe_with_category_ids = [
        RecipeHasCategory(
            fk_RecipeId = recipes_dict.get(item["recipe"].title),
            fk_CategoryId = categories_dict.get(category.categoryName),
        ) for item in recipe_with_categories for category in item["categories"]
    ]

    RecipeHasCategoryService.to_sql_insert_multiple(recipe_with_category_ids)
       
if __name__ == "__main__":
    main()